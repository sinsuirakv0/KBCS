# v15.7.4 → v16.0.0 · 最優先の変更候補 (10)

[一覧の目次](README.md)

### [`004cadbc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cadbc.md) → [`004edc54`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edc54.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc7e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7e0.md) · 呼出先 6件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004c9e38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`005229d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/005229d4.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c59230`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59230.md) · 呼出先 6件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004eccd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`0054586c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/0054586c.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      112,
      "DATA",
      [
        "storage",
        "00bed560",
        null,
        "undefined *"
      ]
    ],
    [
      180,
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
      112,
      "DATA",
      [
        "storage",
        "00c6a120",
        null,
        "undefined *"
      ]
    ],
    [
      180,
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


~~~diff
- 004cae0c ["INT_ADD", "register:40f0:8", ["const:4cae0c:8", "const:4:8"]]
+ 004edca4 ["INT_ADD", "register:40f0:8", ["const:4edca4:8", "const:4:8"]]
- 004cae18 ["INT_ADD", "register:40f0:8", ["const:4cae18:8", "const:4:8"]]
+ 004edcb0 ["INT_ADD", "register:40f0:8", ["const:4edcb0:8", "const:4:8"]]
- 004cae24 ["COPY", "register:4048:8", ["const:bed000:8"]]
- 004cae28 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 004edcbc ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 004edcc0 ["COPY", "tmp:0:8", ["const:120:8"]]
~~~


### [`004caf04`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004caf04.md) → [`004edd9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edd9c.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceE

根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc7f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7f0.md) · 呼出先 4件 [`004c9e38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00522a98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a98.md) [`00522a9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a9c.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c59240`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59240.md) · 呼出先 4件 [`004eccd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545930.md) [`00545934`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545934.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ],
    [
      96,
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
      40,
      "DATA",
      [
        "storage",
        "00c6a1b0",
        null,
        "undefined *"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "00c6a1d0",
        null,
        "pointer"
      ]
    ],
    [
      96,
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


~~~diff
- 004caf18 ["COPY", "register:4050:8", ["const:bed000:8"]]
- 004caf1c ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 004eddb0 ["COPY", "register:4050:8", ["const:c6a000:8"]]
+ 004eddb4 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 004caf3c ["INT_ADD", "register:40f0:8", ["const:4caf3c:8", "const:4:8"]]
+ 004eddd4 ["INT_ADD", "register:40f0:8", ["const:4eddd4:8", "const:4:8"]]
- 004caf68 ["INT_ADD", "register:40f0:8", ["const:4caf68:8", "const:4:8"]]
+ 004ede00 ["INT_ADD", "register:40f0:8", ["const:4ede00:8", "const:4:8"]]
~~~


### [`004cafdc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cafdc.md) → [`004ede74`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004ede74.md) _ZN5Botan5PKCS88copy_keyERKNS_11Private_KeyE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc800`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc800.md) · 呼出先 9件 [`004c9e38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00522a98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a98.md) [`00522a9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a9c.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c59250`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59250.md) · 呼出先 9件 [`004eccd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545930.md) [`00545934`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545934.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      52,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc670"
      ]
    ],
    [
      84,
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      148,
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
      52,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c590c0"
      ]
    ],
    [
      84,
      "DATA",
      [
        "storage",
        "00c6a1b0",
        null,
        "undefined *"
      ]
    ],
    [
      148,
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


~~~diff
- 004cb004 ["INT_ADD", "register:40f0:8", ["const:4cb004:8", "const:4:8"]]
+ 004ede9c ["INT_ADD", "register:40f0:8", ["const:4ede9c:8", "const:4:8"]]
- 004cb010 ["INT_ADD", "register:40f0:8", ["const:4cb010:8", "const:4:8"]]
- 004cb010 ["CALL", null, ["ram:bdc670:8"]]
+ 004edea8 ["INT_ADD", "register:40f0:8", ["const:4edea8:8", "const:4:8"]]
+ 004edea8 ["CALL", null, ["ram:c590c0:8"]]
- 004cb020 ["INT_ADD", "register:40f0:8", ["const:4cb020:8", "const:4:8"]]
+ 004edeb8 ["INT_ADD", "register:40f0:8", ["const:4edeb8:8", "const:4:8"]]
~~~


### [`004cb37c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb37c.md) → [`004ee214`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee214.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERNS_21RandomNumberGeneratorE

根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004c9e38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00522a98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a98.md) [`00522a9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a9c.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004eccd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545930.md) [`00545934`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545934.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ],
    [
      100,
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
      40,
      "DATA",
      [
        "storage",
        "00c6a1b0",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00c6a1d0",
        null,
        "pointer"
      ]
    ],
    [
      100,
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


~~~diff
- 004cb390 ["COPY", "register:4048:8", ["const:bed000:8"]]
- 004cb394 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 004ee228 ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 004ee22c ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 004cb3b8 ["INT_ADD", "register:40f0:8", ["const:4cb3b8:8", "const:4:8"]]
+ 004ee250 ["INT_ADD", "register:40f0:8", ["const:4ee250:8", "const:4:8"]]
- 004cb3e4 ["INT_ADD", "register:40f0:8", ["const:4cb3e4:8", "const:4:8"]]
+ 004ee27c ["INT_ADD", "register:40f0:8", ["const:4ee27c:8", "const:4:8"]]
~~~


### [`004cb45c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb45c.md) → [`004ee2f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee2f4.md) _ZN5Botan5PKCS88load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_21RandomNumberGeneratorENS1_8functionIFS7_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`004c9e38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc810.md) [`00bdc820`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc820.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004eccd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md) [`00c59270`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md)

変更の種類 call, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      288,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc820"
      ]
    ]
  ],
  "added": [
    [
      288,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59270"
      ]
    ]
  ]
}
~~~


~~~diff
- 004cb488 ["INT_ADD", "register:40f0:8", ["const:4cb488:8", "const:4:8"]]
+ 004ee320 ["INT_ADD", "register:40f0:8", ["const:4ee320:8", "const:4:8"]]
- 004cb4a4 ["INT_ADD", "register:40f0:8", ["const:4cb4a4:8", "const:4:8"]]
+ 004ee33c ["INT_ADD", "register:40f0:8", ["const:4ee33c:8", "const:4:8"]]
- 004cb4d4 ["INT_ADD", "register:40f0:8", ["const:4cb4d4:8", "const:4:8"]]
+ 004ee36c ["INT_ADD", "register:40f0:8", ["const:4ee36c:8", "const:4:8"]]
~~~


### [`004cb65c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb65c.md) → [`004ee4f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee4f4.md) _ZN5Botan5PKCS88load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_21RandomNumberGeneratorES9_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004c9e38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00522c18`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522c18.md) [`00522cdc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522cdc.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004eccd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545ab0.md) [`00545b74`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545b74.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      120,
      "DATA",
      [
        "storage",
        "00bed670",
        null,
        "pointer"
      ]
    ],
    [
      184,
      "READ",
      [
        "storage",
        "00bed680",
        null,
        "undefined *"
      ]
    ],
    [
      284,
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
      120,
      "DATA",
      [
        "storage",
        "00c6a230",
        null,
        "pointer"
      ]
    ],
    [
      184,
      "READ",
      [
        "storage",
        "00c6a240",
        null,
        "undefined *"
      ]
    ],
    [
      284,
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


~~~diff
- 004cb68c ["INT_ADD", "register:40f0:8", ["const:4cb68c:8", "const:4:8"]]
+ 004ee524 ["INT_ADD", "register:40f0:8", ["const:4ee524:8", "const:4:8"]]
- 004cb6b4 ["INT_ADD", "register:40f0:8", ["const:4cb6b4:8", "const:4:8"]]
+ 004ee54c ["INT_ADD", "register:40f0:8", ["const:4ee54c:8", "const:4:8"]]
- 004cb6c0 ["INT_ADD", "register:40f0:8", ["const:4cb6c0:8", "const:4:8"]]
+ 004ee558 ["INT_ADD", "register:40f0:8", ["const:4ee558:8", "const:4:8"]]
~~~


### [`004cb868`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb868.md) → [`004ee700`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee700.md) _ZN5Botan5PKCS88load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_21RandomNumberGeneratorE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004c9e38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00522a98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a98.md) [`00522a9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a9c.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc810.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004eccd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545930.md) [`00545934`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545934.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      56,
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      120,
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ],
    [
      120,
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
      56,
      "DATA",
      [
        "storage",
        "00c6a1b0",
        null,
        "undefined *"
      ]
    ],
    [
      120,
      "READ",
      [
        "storage",
        "00c6a1d0",
        null,
        "pointer"
      ]
    ],
    [
      120,
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


~~~diff
- 004cb890 ["INT_ADD", "register:40f0:8", ["const:4cb890:8", "const:4:8"]]
+ 004ee728 ["INT_ADD", "register:40f0:8", ["const:4ee728:8", "const:4:8"]]
- 004cb894 ["COPY", "register:4040:8", ["const:bed000:8"]]
- 004cb898 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 004ee72c ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 004ee730 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 004cb8b8 ["INT_ADD", "register:40f0:8", ["const:4cb8b8:8", "const:4:8"]]
+ 004ee750 ["INT_ADD", "register:40f0:8", ["const:4ee750:8", "const:4:8"]]
~~~


### [`004cb9bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb9bc.md) → [`004ee854`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee854.md) _ZNK5Botan12PK_Decryptor7decryptEPKhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc3a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc3a0.md) · 呼出先 6件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58df0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58df0.md) · 呼出先 6件 [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      132,
      "PARAM",
      [
        "storage",
        "00290a8a",
        null,
        "string"
      ]
    ],
    [
      188,
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      192,
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
      132,
      "PARAM",
      [
        "storage",
        "0029ffcc",
        null,
        "string"
      ]
    ],
    [
      188,
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      192,
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


~~~diff
- 004cb9fc ["INT_ADD", "register:40f0:8", ["const:4cb9fc:8", "const:4:8"]]
+ 004ee894 ["INT_ADD", "register:40f0:8", ["const:4ee894:8", "const:4:8"]]
- 004cba34 ["INT_ADD", "register:40f0:8", ["const:4cba34:8", "const:4:8"]]
+ 004ee8cc ["INT_ADD", "register:40f0:8", ["const:4ee8cc:8", "const:4:8"]]
- 004cba3c ["COPY", "register:4008:8", ["const:290000:8"]]
- 004cba40 ["COPY", "tmp:0:8", ["const:a8a:8"]]
+ 004ee8d4 ["COPY", "register:4008:8", ["const:29f000:8"]]
+ 004ee8d8 ["COPY", "tmp:0:8", ["const:fcc:8"]]
~~~


### [`004cbae4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cbae4.md) → [`004ee97c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee97c.md) _ZNK5Botan12PK_Decryptor17decrypt_or_randomEPKhmmRNS_21RandomNumberGeneratorES2_S2_m

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc830`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc830.md) · 呼出先 6件 [`00490630`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0051d614`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb800`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 1件 [`00c59280`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59280.md) · 呼出先 6件 [`004b34c8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58250`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      428,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      680,
      "PARAM",
      [
        "storage",
        "0029e4f5",
        null,
        "string"
      ]
    ],
    [
      688,
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
      428,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      680,
      "PARAM",
      [
        "storage",
        "002ae87a",
        null,
        "string"
      ]
    ],
    [
      688,
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


~~~diff
- 004cbb3c ["INT_ADD", "register:40f0:8", ["const:4cbb3c:8", "const:4:8"]]
+ 004ee9d4 ["INT_ADD", "register:40f0:8", ["const:4ee9d4:8", "const:4:8"]]
- 004cbb54 ["INT_ADD", "register:40f0:8", ["const:4cbb54:8", "const:4:8"]]
+ 004ee9ec ["INT_ADD", "register:40f0:8", ["const:4ee9ec:8", "const:4:8"]]
- 004cbb78 ["INT_ADD", "register:40f0:8", ["const:4cbb78:8", "const:4:8"]]
+ 004eea10 ["INT_ADD", "register:40f0:8", ["const:4eea10:8", "const:4:8"]]
~~~


### [`004cbe08`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cbe08.md) → [`004eeca0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004eeca0.md) _ZN5Botan16PK_Encryptor_EMEC2ERKNS_10Public_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorI

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc380`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc380.md) · 呼出先 7件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 1件 [`00c58dd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58dd0.md) · 呼出先 7件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "READ",
      [
        "storage",
        "00c1b218",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "DATA",
      [
        "storage",
        "00be9fb8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      232,
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
      40,
      "READ",
      [
        "storage",
        "00c9ac08",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "DATA",
      [
        "storage",
        "00c66b78",
        null,
        "undefined1[48]"
      ]
    ],
    [
      232,
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


~~~diff
- 004cbe24 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 004eecbc ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004cbe30 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:218:8"]]
+ 004eecc8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c08:8"]]
- 004cbe60 ["INT_ADD", "register:40f0:8", ["const:4cbe60:8", "const:4:8"]]
+ 004eecf8 ["INT_ADD", "register:40f0:8", ["const:4eecf8:8", "const:4:8"]]
~~~


### [`004cc1c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc1c4.md) → [`004ef05c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef05c.md) _ZN5Botan16PK_Decryptor_EMEC1ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocator

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc390`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc390.md) · 呼出先 7件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 1件 [`00c58de0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58de0.md) · 呼出先 7件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "READ",
      [
        "storage",
        "00c1b220",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "DATA",
      [
        "storage",
        "00be9fe8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      240,
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
      40,
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "DATA",
      [
        "storage",
        "00c66ba8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      240,
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


~~~diff
- 004cc1e0 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 004ef078 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004cc1ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:220:8"]]
+ 004ef084 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c10:8"]]
- 004cc21c ["INT_ADD", "register:40f0:8", ["const:4cc21c:8", "const:4:8"]]
+ 004ef0b4 ["INT_ADD", "register:40f0:8", ["const:4ef0b4:8", "const:4:8"]]
~~~


### [`004cc428`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc428.md) → [`004ef2c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef2c0.md) _ZN5Botan16PK_Decryptor_EMED0Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc3b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc3b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58e00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e00.md)

変更の種類 call, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc3b0"
      ]
    ]
  ],
  "added": [
    [
      16,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58e00"
      ]
    ]
  ]
}
~~~


~~~diff
- 004cc438 ["INT_ADD", "register:40f0:8", ["const:4cc438:8", "const:4:8"]]
- 004cc438 ["CALL", null, ["ram:bdc3b0:8"]]
+ 004ef2d0 ["INT_ADD", "register:40f0:8", ["const:4ef2d0:8", "const:4:8"]]
+ 004ef2d0 ["CALL", null, ["ram:c58e00:8"]]
~~~


### [`004cc45c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc45c.md) → [`004ef2f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef2f4.md) _ZN5Botan16PK_KEM_EncryptorC2ERKNS_10Public_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorI

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      220,
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      264,
      "PARAM",
      [
        "storage",
        "002a33e2",
        null,
        "string"
      ]
    ],
    [
      340,
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
      220,
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      264,
      "PARAM",
      [
        "storage",
        "002b3abc",
        null,
        "string"
      ]
    ],
    [
      340,
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


~~~diff
- 004cc4a8 ["INT_ADD", "register:40f0:8", ["const:4cc4a8:8", "const:4:8"]]
+ 004ef340 ["INT_ADD", "register:40f0:8", ["const:4ef340:8", "const:4:8"]]
- 004cc4c8 ["INT_ADD", "register:40f0:8", ["const:4cc4c8:8", "const:4:8"]]
+ 004ef360 ["INT_ADD", "register:40f0:8", ["const:4ef360:8", "const:4:8"]]
- 004cc4e0 ["INT_ADD", "register:40f0:8", ["const:4cc4e0:8", "const:4:8"]]
+ 004ef378 ["INT_ADD", "register:40f0:8", ["const:4ef378:8", "const:4:8"]]
~~~


### [`004cc6bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc6bc.md) → [`004ef554`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef554.md) _ZN5Botan16PK_KEM_DecryptorC1ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocator

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      228,
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      272,
      "PARAM",
      [
        "storage",
        "002a95b0",
        null,
        "string"
      ]
    ],
    [
      348,
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
      228,
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      272,
      "PARAM",
      [
        "storage",
        "002ba253",
        null,
        "string"
      ]
    ],
    [
      348,
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


~~~diff
- 004cc708 ["INT_ADD", "register:40f0:8", ["const:4cc708:8", "const:4:8"]]
+ 004ef5a0 ["INT_ADD", "register:40f0:8", ["const:4ef5a0:8", "const:4:8"]]
- 004cc728 ["INT_ADD", "register:40f0:8", ["const:4cc728:8", "const:4:8"]]
+ 004ef5c0 ["INT_ADD", "register:40f0:8", ["const:4ef5c0:8", "const:4:8"]]
- 004cc740 ["INT_ADD", "register:40f0:8", ["const:4cc740:8", "const:4:8"]]
+ 004ef5d8 ["INT_ADD", "register:40f0:8", ["const:4ef5d8:8", "const:4:8"]]
~~~


### [`004cc924`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc924.md) → [`004ef7bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef7bc.md) _ZN5Botan16PK_Key_AgreementC2ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocator

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      228,
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      272,
      "PARAM",
      [
        "storage",
        "00290a6a",
        null,
        "string"
      ]
    ],
    [
      348,
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
      228,
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      272,
      "PARAM",
      [
        "storage",
        "0029ffac",
        null,
        "string"
      ]
    ],
    [
      348,
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


~~~diff
- 004cc970 ["INT_ADD", "register:40f0:8", ["const:4cc970:8", "const:4:8"]]
+ 004ef808 ["INT_ADD", "register:40f0:8", ["const:4ef808:8", "const:4:8"]]
- 004cc990 ["INT_ADD", "register:40f0:8", ["const:4cc990:8", "const:4:8"]]
+ 004ef828 ["INT_ADD", "register:40f0:8", ["const:4ef828:8", "const:4:8"]]
- 004cc9a8 ["INT_ADD", "register:40f0:8", ["const:4cc9a8:8", "const:4:8"]]
+ 004ef840 ["INT_ADD", "register:40f0:8", ["const:4ef840:8", "const:4:8"]]
~~~


### [`004ccca0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004ccca0.md) → [`004efb38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efb38.md) _ZN5Botan9PK_SignerC1ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEENS

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc3e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc3e0.md) · 呼出先 7件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 1件 [`00c58e30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e30.md) · 呼出先 7件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      292,
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      336,
      "PARAM",
      [
        "storage",
        "002ada1f",
        null,
        "string"
      ]
    ],
    [
      412,
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
      292,
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      336,
      "PARAM",
      [
        "storage",
        "002bed45",
        null,
        "string"
      ]
    ],
    [
      412,
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


~~~diff
- 004cccf0 ["INT_ADD", "register:40f0:8", ["const:4cccf0:8", "const:4:8"]]
+ 004efb88 ["INT_ADD", "register:40f0:8", ["const:4efb88:8", "const:4:8"]]
- 004ccd10 ["INT_ADD", "register:40f0:8", ["const:4ccd10:8", "const:4:8"]]
+ 004efba8 ["INT_ADD", "register:40f0:8", ["const:4efba8:8", "const:4:8"]]
- 004ccd28 ["INT_ADD", "register:40f0:8", ["const:4ccd28:8", "const:4:8"]]
+ 004efbc0 ["INT_ADD", "register:40f0:8", ["const:4efbc0:8", "const:4:8"]]
~~~


### [`004ccf4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004ccf4c.md) → [`004efde4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efde4.md) _ZN5Botan9PK_Signer9signatureERNS_21RandomNumberGeneratorE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc400`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc400.md) · 呼出先 21件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0047c554`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00483ed8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512ca8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md)
- 新版 呼出元 1件 [`00c58e50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e50.md) · 呼出先 21件 [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0049f3ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004a6d70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      184,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      660,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      760,
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
      184,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      660,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      760,
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


~~~diff
- 004ccf8c ["INT_ADD", "register:40f0:8", ["const:4ccf8c:8", "const:4:8"]]
+ 004efe24 ["INT_ADD", "register:40f0:8", ["const:4efe24:8", "const:4:8"]]
- 004ccfac ["INT_ADD", "register:40f0:8", ["const:4ccfac:8", "const:4:8"]]
+ 004efe44 ["INT_ADD", "register:40f0:8", ["const:4efe44:8", "const:4:8"]]
- 004ccfc8 ["INT_ADD", "register:40f0:8", ["const:4ccfc8:8", "const:4:8"]]
+ 004efe60 ["INT_ADD", "register:40f0:8", ["const:4efe60:8", "const:4:8"]]
~~~


### [`004cd48c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd48c.md) → [`004f0324`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0324.md) _ZN5Botan11PK_VerifierC2ERKNS_10Public_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEENS_16Signature_FormatESC_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc3f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc3f0.md) · 呼出先 7件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 1件 [`00c58e40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e40.md) · 呼出先 7件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      264,
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      308,
      "PARAM",
      [
        "storage",
        "00291a66",
        null,
        "string"
      ]
    ],
    [
      384,
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
      264,
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      308,
      "PARAM",
      [
        "storage",
        "002a107f",
        null,
        "string"
      ]
    ],
    [
      384,
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


~~~diff
- 004cd4d8 ["INT_ADD", "register:40f0:8", ["const:4cd4d8:8", "const:4:8"]]
+ 004f0370 ["INT_ADD", "register:40f0:8", ["const:4f0370:8", "const:4:8"]]
- 004cd4f8 ["INT_ADD", "register:40f0:8", ["const:4cd4f8:8", "const:4:8"]]
+ 004f0390 ["INT_ADD", "register:40f0:8", ["const:4f0390:8", "const:4:8"]]
- 004cd510 ["INT_ADD", "register:40f0:8", ["const:4cd510:8", "const:4:8"]]
+ 004f03a8 ["INT_ADD", "register:40f0:8", ["const:4f03a8:8", "const:4:8"]]
~~~


### [`004cd70c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd70c.md) → [`004f05a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f05a4.md) _ZN5Botan11PK_Verifier16set_input_formatENS_16Signature_FormatE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      108,
      "PARAM",
      [
        "storage",
        "0028fb11",
        null,
        "string"
      ]
    ],
    [
      164,
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      168,
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
      108,
      "PARAM",
      [
        "storage",
        "0029ef51",
        null,
        "string"
      ]
    ],
    [
      164,
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      168,
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


~~~diff
- 004cd76c ["INT_ADD", "register:40f0:8", ["const:4cd76c:8", "const:4:8"]]
+ 004f0604 ["INT_ADD", "register:40f0:8", ["const:4f0604:8", "const:4:8"]]
- 004cd774 ["COPY", "register:4008:8", ["const:28f000:8"]]
- 004cd778 ["COPY", "tmp:0:8", ["const:b11:8"]]
+ 004f060c ["COPY", "register:4008:8", ["const:29e000:8"]]
+ 004f0610 ["COPY", "tmp:0:8", ["const:f51:8"]]
- 004cd780 ["INT_ADD", "register:40f0:8", ["const:4cd780:8", "const:4:8"]]
+ 004f0618 ["INT_ADD", "register:40f0:8", ["const:4f0618:8", "const:4:8"]]
~~~


### [`004cd86c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd86c.md) → [`004f0704`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0704.md) _ZN5Botan11PK_Verifier15check_signatureEPKhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc410`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc410.md) · 呼出先 16件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00490630`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`004cdca8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cdca8.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c58e60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e60.md) · 呼出先 16件 [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b34c8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`004f0b40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0b40.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      96,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb8f0"
      ]
    ],
    [
      276,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      320,
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
      96,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58340"
      ]
    ],
    [
      276,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      320,
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


~~~diff
- 004cd8b4 ["INT_ADD", "register:40f0:8", ["const:4cd8b4:8", "const:4:8"]]
+ 004f074c ["INT_ADD", "register:40f0:8", ["const:4f074c:8", "const:4:8"]]
- 004cd8cc ["INT_ADD", "register:40f0:8", ["const:4cd8cc:8", "const:4:8"]]
- 004cd8cc ["CALL", null, ["ram:bdb8f0:8"]]
+ 004f0764 ["INT_ADD", "register:40f0:8", ["const:4f0764:8", "const:4:8"]]
+ 004f0764 ["CALL", null, ["ram:c58340:8"]]
- 004cd8e0 ["INT_ADD", "register:40f0:8", ["const:4cd8e0:8", "const:4:8"]]
+ 004f0778 ["INT_ADD", "register:40f0:8", ["const:4f0778:8", "const:4:8"]]
~~~


### [`004cddd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cddd0.md) → [`004f0c68`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0c68.md) _ZN5Botan14if_work_factorEm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb5f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5f0.md) [`00bdc860`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc860.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58040.md) [`00c592b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592b0.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "002b2c08",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "002b27c0",
        null,
        "undefined8"
      ]
    ],
    [
      76,
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
      20,
      "READ",
      [
        "storage",
        "002c4318",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "002c3ea0",
        null,
        "undefined8"
      ]
    ],
    [
      76,
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


~~~diff
- 004cdde0 ["COPY", "register:4040:8", ["const:2b2000:8"]]
- 004cdde4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c08:8"]]
+ 004f0c78 ["COPY", "register:4040:8", ["const:2c4000:8"]]
+ 004f0c7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004cddf0 ["INT_ADD", "register:40f0:8", ["const:4cddf0:8", "const:4:8"]]
+ 004f0c88 ["INT_ADD", "register:40f0:8", ["const:4f0c88:8", "const:4:8"]]
- 004cde08 ["INT_ADD", "register:40f0:8", ["const:4cde08:8", "const:4:8"]]
+ 004f0ca0 ["INT_ADD", "register:40f0:8", ["const:4f0ca0:8", "const:4:8"]]
~~~


### [`004cde34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cde34.md) → [`004f0ccc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0ccc.md) _ZN5Botan14dl_work_factorEm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb5f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5f0.md) [`00bdc860`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc860.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58040.md) [`00c592b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592b0.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "002b2c08",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "002b27c0",
        null,
        "undefined8"
      ]
    ],
    [
      76,
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
      20,
      "READ",
      [
        "storage",
        "002c4318",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "002c3ea0",
        null,
        "undefined8"
      ]
    ],
    [
      76,
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


~~~diff
- 004cde44 ["COPY", "register:4040:8", ["const:2b2000:8"]]
- 004cde48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c08:8"]]
+ 004f0cdc ["COPY", "register:4040:8", ["const:2c4000:8"]]
+ 004f0ce0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004cde54 ["INT_ADD", "register:40f0:8", ["const:4cde54:8", "const:4:8"]]
+ 004f0cec ["INT_ADD", "register:40f0:8", ["const:4f0cec:8", "const:4:8"]]
- 004cde6c ["INT_ADD", "register:40f0:8", ["const:4cde6c:8", "const:4:8"]]
+ 004f0d04 ["INT_ADD", "register:40f0:8", ["const:4f0d04:8", "const:4:8"]]
~~~


### [`004cdf20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cdf20.md) → [`004f0db8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0db8.md) _ZN5Botan4X50910PEM_encodeERKNS_10Public_KeyE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc870`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc870.md) · 呼出先 4件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc640`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc640.md) [`00bdc780`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc780.md)
- 新版 呼出元 1件 [`00c592c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592c0.md) · 呼出先 4件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) [`00c591d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591d0.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      60,
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
      60,
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


~~~diff
- 004cdf44 ["INT_ADD", "register:40f0:8", ["const:4cdf44:8", "const:4:8"]]
+ 004f0ddc ["INT_ADD", "register:40f0:8", ["const:4f0ddc:8", "const:4:8"]]
- 004cdf4c ["COPY", "register:4048:8", ["const:2ae000:8"]]
- 004cdf50 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 004f0de4 ["COPY", "register:4048:8", ["const:2bf000:8"]]
+ 004f0de8 ["COPY", "tmp:0:8", ["const:dcc:8"]]
- 004cdf80 ["INT_ADD", "register:40f0:8", ["const:4cdf80:8", "const:4:8"]]
+ 004f0e18 ["INT_ADD", "register:40f0:8", ["const:4f0e18:8", "const:4:8"]]
~~~


### [`004ce004`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce004.md) → [`004f0e9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0e9c.md) _ZN5Botan4X5098load_keyERNS_10DataSourceE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc880`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc880.md) · 呼出先 20件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004828a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004828a4.md) [`004840c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/004840c4.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d3cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md)
- 新版 呼出元 1件 [`00c592d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592d0.md) · 呼出先 20件 [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004a573c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md) [`004a6f5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00540264`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      176,
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
      36,
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      176,
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


~~~diff
- 004ce01c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004f0eb4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004ce028 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
+ 004f0ec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:938:8"]]
- 004ce04c ["INT_ADD", "register:40f0:8", ["const:4ce04c:8", "const:4:8"]]
+ 004f0ee4 ["INT_ADD", "register:40f0:8", ["const:4f0ee4:8", "const:4:8"]]
~~~


### [`004ce670`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce670.md) → [`004f1508`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1508.md) _ZN5Botan4X5098load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc810.md) [`00bdc820`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc820.md) [`00bdc880`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc880.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md) [`00c59270`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md) [`00c592d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      60,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc820"
      ]
    ]
  ],
  "added": [
    [
      60,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59270"
      ]
    ]
  ]
}
~~~


~~~diff
- 004ce698 ["INT_ADD", "register:40f0:8", ["const:4ce698:8", "const:4:8"]]
+ 004f1530 ["INT_ADD", "register:40f0:8", ["const:4f1530:8", "const:4:8"]]
- 004ce6a0 ["INT_ADD", "register:40f0:8", ["const:4ce6a0:8", "const:4:8"]]
+ 004f1538 ["INT_ADD", "register:40f0:8", ["const:4f1538:8", "const:4:8"]]
- 004ce6ac ["INT_ADD", "register:40f0:8", ["const:4ce6ac:8", "const:4:8"]]
- 004ce6ac ["CALL", null, ["ram:bdc820:8"]]
+ 004f1544 ["INT_ADD", "register:40f0:8", ["const:4f1544:8", "const:4:8"]]
+ 004f1544 ["CALL", null, ["ram:c59270:8"]]
~~~


### [`004ce6fc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce6fc.md) → [`004f1594`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1594.md) _ZN5Botan4X5098load_keyERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc8a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8a0.md) · 呼出先 5件 [`00513e2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513e2c.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdc880`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc880.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00c592f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592f0.md) · 呼出先 5件 [`00536cc4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536cc4.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c592d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592d0.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      108,
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
      28,
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ],
    [
      108,
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


~~~diff
- 004ce714 ["COPY", "register:4040:8", ["const:c1a000:8"]]
- 004ce718 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 004f15ac ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004f15b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9e0:8"]]
- 004ce740 ["INT_ADD", "register:40f0:8", ["const:4ce740:8", "const:4:8"]]
+ 004f15d8 ["INT_ADD", "register:40f0:8", ["const:4f15d8:8", "const:4:8"]]
- 004ce74c ["INT_ADD", "register:40f0:8", ["const:4ce74c:8", "const:4:8"]]
+ 004f15e4 ["INT_ADD", "register:40f0:8", ["const:4f15e4:8", "const:4:8"]]
~~~


### [`004ce7d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce7d8.md) → [`004f1670`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1670.md) _ZN5Botan4X5098copy_keyERKNS_10Public_KeyE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdc670`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc670.md) [`00bdc870`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc870.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590c0.md) [`00c592c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592c0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      48,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc670"
      ]
    ],
    [
      100,
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
      48,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c590c0"
      ]
    ],
    [
      100,
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


~~~diff
- 004ce7fc ["INT_ADD", "register:40f0:8", ["const:4ce7fc:8", "const:4:8"]]
+ 004f1694 ["INT_ADD", "register:40f0:8", ["const:4f1694:8", "const:4:8"]]
- 004ce808 ["INT_ADD", "register:40f0:8", ["const:4ce808:8", "const:4:8"]]
- 004ce808 ["CALL", null, ["ram:bdc670:8"]]
+ 004f16a0 ["INT_ADD", "register:40f0:8", ["const:4f16a0:8", "const:4:8"]]
+ 004f16a0 ["CALL", null, ["ram:c590c0:8"]]
- 004ce818 ["INT_ADD", "register:40f0:8", ["const:4ce818:8", "const:4:8"]]
+ 004f16b0 ["INT_ADD", "register:40f0:8", ["const:4f16b0:8", "const:4:8"]]
~~~


### [`004cec60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cec60.md) → [`004f1af8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1af8.md) _ZN5Botan21RandomNumberGenerator8make_rngEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      64,
      "READ",
      [
        "storage",
        "002ada46",
        null,
        "string"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "002ada56",
        null,
        "string"
      ]
    ],
    [
      68,
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
      64,
      "READ",
      [
        "storage",
        "002bed6c",
        null,
        "string"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "002bed7c",
        null,
        "string"
      ]
    ],
    [
      68,
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


~~~diff
- 004cec84 ["INT_ADD", "register:40f0:8", ["const:4cec84:8", "const:4:8"]]
+ 004f1b1c ["INT_ADD", "register:40f0:8", ["const:4f1b1c:8", "const:4:8"]]
- 004cec90 ["INT_ADD", "register:40f0:8", ["const:4cec90:8", "const:4:8"]]
+ 004f1b28 ["INT_ADD", "register:40f0:8", ["const:4f1b28:8", "const:4:8"]]
- 004cec94 ["COPY", "register:4040:8", ["const:2ad000:8"]]
- 004cec98 ["COPY", "tmp:0:8", ["const:a46:8"]]
+ 004f1b2c ["COPY", "register:4040:8", ["const:2be000:8"]]
+ 004f1b30 ["COPY", "tmp:0:8", ["const:d6c:8"]]
~~~


### [`004ced48`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ced48.md) → [`004f1be0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1be0.md) _ZN5Botan14Serialized_RNGC1Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "READ",
      [
        "storage",
        "00c1b228",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "DATA",
      [
        "storage",
        "00bea010",
        null,
        "undefined1[104]"
      ]
    ],
    [
      108,
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
      36,
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "DATA",
      [
        "storage",
        "00c66bd0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      108,
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


~~~diff
- 004ced60 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004f1bf8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004ced6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
+ 004f1c04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
- 004ced98 ["INT_ADD", "register:40f0:8", ["const:4ced98:8", "const:4:8"]]
+ 004f1c30 ["INT_ADD", "register:40f0:8", ["const:4f1c30:8", "const:4:8"]]
~~~


### [`004cef80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cef80.md) → [`004f1e18`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1e18.md) _ZNK5Botan13RSA_PublicKey18estimated_strengthEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb5f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5f0.md) [`00bdc860`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc860.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58040.md) [`00c592b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592b0.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      32,
      "READ",
      [
        "storage",
        "002b2c08",
        null,
        "undefined8"
      ]
    ],
    [
      76,
      "READ",
      [
        "storage",
        "002b27c0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
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
      32,
      "READ",
      [
        "storage",
        "002c4318",
        null,
        "undefined8"
      ]
    ],
    [
      76,
      "READ",
      [
        "storage",
        "002c3ea0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
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


~~~diff
- 004cef94 ["INT_ADD", "register:40f0:8", ["const:4cef94:8", "const:4:8"]]
+ 004f1e2c ["INT_ADD", "register:40f0:8", ["const:4f1e2c:8", "const:4:8"]]
- 004cef9c ["COPY", "register:4040:8", ["const:2b2000:8"]]
- 004cefa0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c08:8"]]
+ 004f1e34 ["COPY", "register:4040:8", ["const:2c4000:8"]]
+ 004f1e38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004cefac ["INT_ADD", "register:40f0:8", ["const:4cefac:8", "const:4:8"]]
+ 004f1e44 ["INT_ADD", "register:40f0:8", ["const:4f1e44:8", "const:4:8"]]
~~~


### [`004ceff0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ceff0.md) → [`004f1e88`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1e88.md) _ZTv0_n40_NK5Botan13RSA_PublicKey18estimated_strengthEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb5f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5f0.md) [`00bdc860`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc860.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58040.md) [`00c592b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592b0.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      44,
      "READ",
      [
        "storage",
        "002b2c08",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "READ",
      [
        "storage",
        "002b27c0",
        null,
        "undefined8"
      ]
    ],
    [
      100,
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
      44,
      "READ",
      [
        "storage",
        "002c4318",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "READ",
      [
        "storage",
        "002c3ea0",
        null,
        "undefined8"
      ]
    ],
    [
      100,
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


~~~diff
- 004cf010 ["INT_ADD", "register:40f0:8", ["const:4cf010:8", "const:4:8"]]
+ 004f1ea8 ["INT_ADD", "register:40f0:8", ["const:4f1ea8:8", "const:4:8"]]
- 004cf018 ["COPY", "register:4040:8", ["const:2b2000:8"]]
- 004cf01c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c08:8"]]
+ 004f1eb0 ["COPY", "register:4040:8", ["const:2c4000:8"]]
+ 004f1eb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004cf028 ["INT_ADD", "register:40f0:8", ["const:4cf028:8", "const:4:8"]]
+ 004f1ec0 ["INT_ADD", "register:40f0:8", ["const:4f1ec0:8", "const:4:8"]]
~~~


### [`004cf06c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf06c.md) → [`004f1f04`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1f04.md) _ZNK5Botan13RSA_PublicKey20algorithm_identifierEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc8d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59320`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59320.md)

変更の種類 call, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      72,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc8d0"
      ]
    ]
  ],
  "added": [
    [
      72,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59320"
      ]
    ]
  ]
}
~~~


~~~diff
- 004cf0a4 ["INT_ADD", "register:40f0:8", ["const:4cf0a4:8", "const:4:8"]]
+ 004f1f3c ["INT_ADD", "register:40f0:8", ["const:4f1f3c:8", "const:4:8"]]
- 004cf0b4 ["INT_ADD", "register:40f0:8", ["const:4cf0b4:8", "const:4:8"]]
- 004cf0b4 ["CALL", null, ["ram:bdc8d0:8"]]
+ 004f1f4c ["INT_ADD", "register:40f0:8", ["const:4f1f4c:8", "const:4:8"]]
+ 004f1f4c ["CALL", null, ["ram:c59320:8"]]
- 004cf0c4 ["INT_ADD", "register:40f0:8", ["const:4cf0c4:8", "const:4:8"]]
+ 004f1f5c ["INT_ADD", "register:40f0:8", ["const:4f1f5c:8", "const:4:8"]]
~~~


### [`004cf11c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf11c.md) → [`004f1fb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1fb4.md) _ZTv0_n72_NK5Botan13RSA_PublicKey20algorithm_identifierEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc8d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59320`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59320.md)

変更の種類 call, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      84,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc8d0"
      ]
    ]
  ],
  "added": [
    [
      84,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59320"
      ]
    ]
  ]
}
~~~


~~~diff
- 004cf160 ["INT_ADD", "register:40f0:8", ["const:4cf160:8", "const:4:8"]]
+ 004f1ff8 ["INT_ADD", "register:40f0:8", ["const:4f1ff8:8", "const:4:8"]]
- 004cf170 ["INT_ADD", "register:40f0:8", ["const:4cf170:8", "const:4:8"]]
- 004cf170 ["CALL", null, ["ram:bdc8d0:8"]]
+ 004f2008 ["INT_ADD", "register:40f0:8", ["const:4f2008:8", "const:4:8"]]
+ 004f2008 ["CALL", null, ["ram:c59320:8"]]
- 004cf180 ["INT_ADD", "register:40f0:8", ["const:4cf180:8", "const:4:8"]]
+ 004f2018 ["INT_ADD", "register:40f0:8", ["const:4f2018:8", "const:4:8"]]
~~~


### [`004cf328`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf328.md) → [`004f21c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f21c0.md) _ZN5Botan13RSA_PublicKeyC2ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md) [`00bdb8c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8c0.md) [`00bdba30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba30.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58300`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md) [`00c58310`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58310.md) [`00c58480`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58480.md)

変更の種類 call, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      96,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba30"
      ]
    ],
    [
      212,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      280,
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
      96,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58480"
      ]
    ],
    [
      212,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      280,
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


~~~diff
- 004cf388 ["INT_ADD", "register:40f0:8", ["const:4cf388:8", "const:4:8"]]
- 004cf388 ["CALL", null, ["ram:bdba30:8"]]
+ 004f2220 ["INT_ADD", "register:40f0:8", ["const:4f2220:8", "const:4:8"]]
+ 004f2220 ["CALL", null, ["ram:c58480:8"]]
- 004cf39c ["INT_ADD", "register:40f0:8", ["const:4cf39c:8", "const:4:8"]]
+ 004f2234 ["INT_ADD", "register:40f0:8", ["const:4f2234:8", "const:4:8"]]
- 004cf3b0 ["INT_ADD", "register:40f0:8", ["const:4cf3b0:8", "const:4:8"]]
+ 004f2248 ["INT_ADD", "register:40f0:8", ["const:4f2248:8", "const:4:8"]]
~~~


### [`004cf634`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf634.md) → [`004f24cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f24cc.md) _ZNK5Botan14RSA_PrivateKey16private_key_bitsEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00512ca8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb860`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb860.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00535b40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c582b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      124,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      412,
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
      124,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      412,
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


~~~diff
- 004cf678 ["INT_ADD", "register:40f0:8", ["const:4cf678:8", "const:4:8"]]
+ 004f2510 ["INT_ADD", "register:40f0:8", ["const:4f2510:8", "const:4:8"]]
- 004cf684 ["INT_ADD", "register:40f0:8", ["const:4cf684:8", "const:4:8"]]
+ 004f251c ["INT_ADD", "register:40f0:8", ["const:4f251c:8", "const:4:8"]]
- 004cf698 ["INT_ADD", "register:40f0:8", ["const:4cf698:8", "const:4:8"]]
+ 004f2530 ["INT_ADD", "register:40f0:8", ["const:4f2530:8", "const:4:8"]]
~~~


### [`004cf854`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf854.md) → [`004f26ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f26ec.md) _ZN5Botan14RSA_PrivateKeyC2ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      268,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba40"
      ]
    ],
    [
      312,
      "READ",
      [
        "storage",
        "002a4529",
        null,
        "string"
      ]
    ],
    [
      312,
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
      268,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58490"
      ]
    ],
    [
      312,
      "READ",
      [
        "storage",
        "002b4d96",
        null,
        "string"
      ]
    ],
    [
      312,
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


~~~diff
- 004cf960 ["INT_ADD", "register:40f0:8", ["const:4cf960:8", "const:4:8"]]
- 004cf960 ["CALL", null, ["ram:bdba40:8"]]
+ 004f27f8 ["INT_ADD", "register:40f0:8", ["const:4f27f8:8", "const:4:8"]]
+ 004f27f8 ["CALL", null, ["ram:c58490:8"]]
- 004cf974 ["INT_ADD", "register:40f0:8", ["const:4cf974:8", "const:4:8"]]
+ 004f280c ["INT_ADD", "register:40f0:8", ["const:4f280c:8", "const:4:8"]]
- 004cf97c ["INT_ADD", "register:40f0:8", ["const:4cf97c:8", "const:4:8"]]
+ 004f2814 ["INT_ADD", "register:40f0:8", ["const:4f2814:8", "const:4:8"]]
~~~


### [`004cfc08`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cfc08.md) → [`004f2aa0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f2aa0.md) FUN_004f2aa0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      60,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      104,
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
      60,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      104,
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


~~~diff
- 004cfc24 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 004f2abc ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 004cfc44 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004f2adc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 004cfc54 ["INT_ADD", "register:40f0:8", ["const:4cfc54:8", "const:4:8"]]
+ 004f2aec ["INT_ADD", "register:40f0:8", ["const:4f2aec:8", "const:4:8"]]
~~~


### [`004cfcb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cfcb0.md) → [`004f2b48`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f2b48.md) _ZN5Botan14RSA_PrivateKeyC2ERKNS_6BigIntES3_S3_S3_S3_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00520804`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0054369c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md)

変更の種類 call, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      192,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      204,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      216,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ]
  ],
  "added": [
    [
      192,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      204,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      216,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ]
  ]
}
~~~


~~~diff
- 004cfd70 ["INT_ADD", "register:40f0:8", ["const:4cfd70:8", "const:4:8"]]
- 004cfd70 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004f2c08 ["INT_ADD", "register:40f0:8", ["const:4f2c08:8", "const:4:8"]]
+ 004f2c08 ["CALL", null, ["ram:c58740:8"]]
- 004cfd7c ["INT_ADD", "register:40f0:8", ["const:4cfd7c:8", "const:4:8"]]
- 004cfd7c ["CALL", null, ["ram:bdbcf0:8"]]
+ 004f2c14 ["INT_ADD", "register:40f0:8", ["const:4f2c14:8", "const:4:8"]]
+ 004f2c14 ["CALL", null, ["ram:c58740:8"]]
- 004cfd88 ["INT_ADD", "register:40f0:8", ["const:4cfd88:8", "const:4:8"]]
- 004cfd88 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004f2c20 ["INT_ADD", "register:40f0:8", ["const:4f2c20:8", "const:4:8"]]
+ 004f2c20 ["CALL", null, ["ram:c58740:8"]]
~~~


### [`004d04c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d0/004d04c0.md) → [`004f3358`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f3/004f3358.md) _ZN5Botan14RSA_PrivateKeyC1ERKNS_6BigIntES3_S3_S3_S3_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00520804`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0054369c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      48,
      "READ",
      [
        "storage",
        "00c1b1f0",
        null,
        "pointer"
      ]
    ],
    [
      108,
      "DATA",
      [
        "storage",
        "00bea2f8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      128,
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
      48,
      "READ",
      [
        "storage",
        "00c9abe0",
        null,
        "pointer"
      ]
    ],
    [
      108,
      "DATA",
      [
        "storage",
        "00c66eb8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      128,
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


~~~diff
- 004d04e4 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 004f337c ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004d04f0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1f0:8"]]
+ 004f3388 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:be0:8"]]
- 004d054c ["INT_ADD", "register:40f0:8", ["const:4d054c:8", "const:4:8"]]
- 004d054c ["CALL", null, ["ram:bdbcf0:8"]]
+ 004f33e4 ["INT_ADD", "register:40f0:8", ["const:4f33e4:8", "const:4:8"]]
+ 004f33e4 ["CALL", null, ["ram:c58740:8"]]
~~~


### [`004d0c9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d0/004d0c9c.md) → [`004f3b34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f3/004f3b34.md) _ZN5Botan14RSA_PrivateKeyC2ERNS_21RandomNumberGeneratorEmm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 17件 [`00483974`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 17件 [`004a680c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      400,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      564,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      816,
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
      400,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      564,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      816,
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


~~~diff
- 004d0dd8 ["INT_ADD", "register:40f0:8", ["const:4d0dd8:8", "const:4:8"]]
+ 004f3c70 ["INT_ADD", "register:40f0:8", ["const:4f3c70:8", "const:4:8"]]
- 004d0e28 ["COPY", "register:4048:8", ["const:bea000:8"]]
- 004d0e2c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004f3cc0 ["COPY", "register:4048:8", ["const:c67000:8"]]
+ 004f3cc4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:338:8"]]
- 004d0e3c ["INT_ADD", "register:40f0:8", ["const:4d0e3c:8", "const:4:8"]]
+ 004f3cd4 ["INT_ADD", "register:40f0:8", ["const:4f3cd4:8", "const:4:8"]]
~~~


### [`004d1904`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d1/004d1904.md) → [`004f479c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f4/004f479c.md) _ZNK5Botan14RSA_PrivateKey9check_keyERNS_21RandomNumberGeneratorEb

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc900`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc900.md) · 呼出先 13件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md)
- 新版 呼出元 1件 [`00c59350`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59350.md) · 呼出先 13件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      296,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      340,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      384,
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
      296,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      340,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      384,
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


~~~diff
- 004d1940 ["INT_ADD", "register:40f0:8", ["const:4d1940:8", "const:4:8"]]
+ 004f47d8 ["INT_ADD", "register:40f0:8", ["const:4f47d8:8", "const:4:8"]]
- 004d1954 ["INT_ADD", "register:40f0:8", ["const:4d1954:8", "const:4:8"]]
+ 004f47ec ["INT_ADD", "register:40f0:8", ["const:4f47ec:8", "const:4:8"]]
- 004d1978 ["INT_ADD", "register:40f0:8", ["const:4d1978:8", "const:4:8"]]
+ 004f4810 ["INT_ADD", "register:40f0:8", ["const:4f4810:8", "const:4:8"]]
~~~


### [`004d21d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d21d0.md) → [`004f5068`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5068.md) _ZNK5Botan13RSA_PublicKey20create_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorI

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc910`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc910.md) · 呼出先 6件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdc150`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc150.md)
- 新版 呼出元 1件 [`00c59360`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59360.md) · 呼出先 6件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58ba0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      144,
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      148,
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
      144,
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ],
    [
      148,
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


~~~diff
- 004d2238 ["INT_ADD", "register:40f0:8", ["const:4d2238:8", "const:4:8"]]
+ 004f50d0 ["INT_ADD", "register:40f0:8", ["const:4f50d0:8", "const:4:8"]]
- 004d2244 ["INT_ADD", "register:40f0:8", ["const:4d2244:8", "const:4:8"]]
+ 004f50dc ["INT_ADD", "register:40f0:8", ["const:4f50dc:8", "const:4:8"]]
- 004d2258 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004d2260 ["COPY", "register:4010:8", ["const:512990:8"]]
- 004d2264 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e0:8"]]
+ 004f50f0 ["COPY", "register:4008:8", ["const:c9a000:8"]]
+ 004f50f8 ["COPY", "register:4010:8", ["const:535828:8"]]
+ 004f50fc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ad0:8"]]
~~~


### [`004d2348`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2348.md) → [`004f51e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f51e0.md) _ZNK5Botan13RSA_PublicKey24create_kem_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9alloca

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc930.md) · 呼出先 8件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c59380`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59380.md) · 呼出先 8件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      132,
      "DATA",
      [
        "storage",
        "00be9f58",
        null,
        "undefined *"
      ]
    ],
    [
      180,
      "DATA",
      [
        "storage",
        "00becf28",
        null,
        "undefined *"
      ]
    ],
    [
      280,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc920"
      ]
    ]
  ],
  "added": [
    [
      132,
      "DATA",
      [
        "storage",
        "00c66b18",
        null,
        "undefined *"
      ]
    ],
    [
      180,
      "DATA",
      [
        "storage",
        "00c69ae8",
        null,
        "undefined *"
      ]
    ],
    [
      280,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59370"
      ]
    ]
  ]
}
~~~


~~~diff
- 004d23bc ["INT_ADD", "register:40f0:8", ["const:4d23bc:8", "const:4:8"]]
+ 004f5254 ["INT_ADD", "register:40f0:8", ["const:4f5254:8", "const:4:8"]]
- 004d23c4 ["COPY", "register:40c0:8", ["const:be9000:8"]]
- 004d23c8 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 004f525c ["COPY", "register:40c0:8", ["const:c66000:8"]]
+ 004f5260 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 004d23d4 ["INT_ADD", "register:40f0:8", ["const:4d23d4:8", "const:4:8"]]
+ 004f526c ["INT_ADD", "register:40f0:8", ["const:4f526c:8", "const:4:8"]]
~~~


### [`004d2528`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2528.md) → [`004f53c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f53c0.md) _ZNK5Botan13RSA_PublicKey22create_verification_opERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc940`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc940.md) · 呼出先 8件 [`004c8590`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8590.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c59390`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59390.md) · 呼出先 8件 [`004eb428`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb428.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      168,
      "DATA",
      [
        "storage",
        "00becf90",
        null,
        "undefined *"
      ]
    ],
    [
      268,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc920"
      ]
    ],
    [
      296,
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
      168,
      "DATA",
      [
        "storage",
        "00c69b50",
        null,
        "undefined *"
      ]
    ],
    [
      268,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59370"
      ]
    ],
    [
      296,
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


~~~diff
- 004d259c ["INT_ADD", "register:40f0:8", ["const:4d259c:8", "const:4:8"]]
+ 004f5434 ["INT_ADD", "register:40f0:8", ["const:4f5434:8", "const:4:8"]]
- 004d25a8 ["INT_ADD", "register:40f0:8", ["const:4d25a8:8", "const:4:8"]]
+ 004f5440 ["INT_ADD", "register:40f0:8", ["const:4f5440:8", "const:4:8"]]
- 004d25c0 ["INT_ADD", "register:40f0:8", ["const:4d25c0:8", "const:4:8"]]
+ 004f5458 ["INT_ADD", "register:40f0:8", ["const:4f5458:8", "const:4:8"]]
~~~


### [`004d26e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d26e0.md) → [`004f5578`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5578.md) _ZNK5Botan14RSA_PrivateKey20create_decryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocator

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdc150`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc150.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58ba0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      148,
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      152,
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      152,
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
      148,
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      152,
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ],
    [
      152,
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


~~~diff
- 004d274c ["INT_ADD", "register:40f0:8", ["const:4d274c:8", "const:4:8"]]
+ 004f55e4 ["INT_ADD", "register:40f0:8", ["const:4f55e4:8", "const:4:8"]]
- 004d2758 ["INT_ADD", "register:40f0:8", ["const:4d2758:8", "const:4:8"]]
+ 004f55f0 ["INT_ADD", "register:40f0:8", ["const:4f55f0:8", "const:4:8"]]
- 004d276c ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004d2774 ["COPY", "register:4010:8", ["const:512990:8"]]
- 004d2778 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e0:8"]]
+ 004f5604 ["COPY", "register:4008:8", ["const:c9a000:8"]]
+ 004f560c ["COPY", "register:4010:8", ["const:535828:8"]]
+ 004f5610 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ad0:8"]]
~~~


### [`004d2830`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2830.md) → [`004f56c8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f56c8.md) _ZNK5Botan14RSA_PrivateKey24create_kem_decryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9alloc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051483c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/0051483c.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005376d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00537/005376d4.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      140,
      "DATA",
      [
        "storage",
        "00be9f88",
        null,
        "undefined *"
      ]
    ],
    [
      184,
      "DATA",
      [
        "storage",
        "00bed1f0",
        null,
        "undefined *"
      ]
    ],
    [
      268,
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
      140,
      "DATA",
      [
        "storage",
        "00c66b48",
        null,
        "undefined *"
      ]
    ],
    [
      184,
      "DATA",
      [
        "storage",
        "00c69db0",
        null,
        "undefined *"
      ]
    ],
    [
      268,
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


~~~diff
- 004d28ac ["INT_ADD", "register:40f0:8", ["const:4d28ac:8", "const:4:8"]]
+ 004f5744 ["INT_ADD", "register:40f0:8", ["const:4f5744:8", "const:4:8"]]
- 004d28b4 ["COPY", "register:40c8:8", ["const:be9000:8"]]
- 004d28b8 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 004f574c ["COPY", "register:40c8:8", ["const:c66000:8"]]
+ 004f5750 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 004d28c4 ["INT_ADD", "register:40f0:8", ["const:4d28c4:8", "const:4:8"]]
+ 004f575c ["INT_ADD", "register:40f0:8", ["const:4f575c:8", "const:4:8"]]
~~~


### [`004d29f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d29f8.md) → [`004f5890`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5890.md) _ZNK5Botan14RSA_PrivateKey19create_signature_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorI

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`004c824c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c824c.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051483c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/0051483c.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004eb0e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb0e4.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005376d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00537/005376d4.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      164,
      "DATA",
      [
        "storage",
        "00bed258",
        null,
        "undefined *"
      ]
    ],
    [
      244,
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "byte[43]"
      ]
    ],
    [
      256,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc920"
      ]
    ]
  ],
  "added": [
    [
      164,
      "DATA",
      [
        "storage",
        "00c69e18",
        null,
        "undefined *"
      ]
    ],
    [
      244,
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "qword"
      ]
    ],
    [
      256,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59370"
      ]
    ]
  ]
}
~~~


~~~diff
- 004d2a70 ["INT_ADD", "register:40f0:8", ["const:4d2a70:8", "const:4:8"]]
+ 004f5908 ["INT_ADD", "register:40f0:8", ["const:4f5908:8", "const:4:8"]]
- 004d2a7c ["INT_ADD", "register:40f0:8", ["const:4d2a7c:8", "const:4:8"]]
+ 004f5914 ["INT_ADD", "register:40f0:8", ["const:4f5914:8", "const:4:8"]]
- 004d2a8c ["INT_ADD", "register:40f0:8", ["const:4d2a8c:8", "const:4:8"]]
+ 004f5924 ["INT_ADD", "register:40f0:8", ["const:4f5924:8", "const:4:8"]]
~~~


### [`004d2b8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2b8c.md) → [`004f5a24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5a24.md) _ZNK5Botan7SHA_16010copy_stateEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005132d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md) [`0051d3cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053616c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) [`00540264`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      80,
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
      40,
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      80,
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


~~~diff
- 004d2ba8 ["INT_ADD", "register:40f0:8", ["const:4d2ba8:8", "const:4:8"]]
+ 004f5a40 ["INT_ADD", "register:40f0:8", ["const:4f5a40:8", "const:4:8"]]
- 004d2bac ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004f5a44 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004d2bb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 004f5a4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
~~~


### [`004d3a84`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3a84.md) → [`004f691c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f691c.md) _ZN5Botan7SHA_1605clearEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      72,
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
      72,
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


~~~diff
- 004d3aa8 ["INT_ADD", "register:40f0:8", ["const:4d3aa8:8", "const:4:8"]]
+ 004f6940 ["INT_ADD", "register:40f0:8", ["const:4f6940:8", "const:4:8"]]
- 004d3ac0 ["INT_ADD", "register:40f0:8", ["const:4d3ac0:8", "const:4:8"]]
+ 004f6958 ["INT_ADD", "register:40f0:8", ["const:4f6958:8", "const:4:8"]]
- 004d3ac4 ["COPY", "register:4040:8", ["const:2b0000:8"]]
+ 004f695c ["COPY", "register:4040:8", ["const:2c2000:8"]]
~~~


### [`004d3aec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3aec.md) → [`004f6984`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6984.md) _ZNK5Botan7SHA_22410copy_stateEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005132d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md) [`0051d3cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053616c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) [`00540264`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      80,
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
      40,
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      80,
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


~~~diff
- 004d3b08 ["INT_ADD", "register:40f0:8", ["const:4d3b08:8", "const:4:8"]]
+ 004f69a0 ["INT_ADD", "register:40f0:8", ["const:4f69a0:8", "const:4:8"]]
- 004d3b0c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004f69a4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004d3b14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 004f69ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
~~~


### [`004d3ba0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3ba0.md) → [`004f6a38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6a38.md) _ZNK5Botan7SHA_25610copy_stateEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005132d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md) [`0051d3cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053616c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) [`00540264`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      80,
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
      40,
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      80,
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


~~~diff
- 004d3bbc ["INT_ADD", "register:40f0:8", ["const:4d3bbc:8", "const:4:8"]]
+ 004f6a54 ["INT_ADD", "register:40f0:8", ["const:4f6a54:8", "const:4:8"]]
- 004d3bc0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004f6a58 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004d3bc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 004f6a60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
~~~


### [`004d5b18`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5b18.md) → [`004f89b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f89b0.md) _ZN5Botan7SHA_2245clearEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      52,
      "READ",
      [
        "storage",
        "002b1b00",
        null,
        null
      ]
    ],
    [
      56,
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
      52,
      "READ",
      [
        "storage",
        "002c31d0",
        null,
        null
      ]
    ],
    [
      56,
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


~~~diff
- 004d5b3c ["INT_ADD", "register:40f0:8", ["const:4d5b3c:8", "const:4:8"]]
+ 004f89d4 ["INT_ADD", "register:40f0:8", ["const:4f89d4:8", "const:4:8"]]
- 004d5b40 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004d5b44 ["COPY", "register:4050:8", ["const:2b1000:8"]]
+ 004f89d8 ["COPY", "register:4048:8", ["const:2c3000:8"]]
+ 004f89dc ["COPY", "register:4050:8", ["const:2c2000:8"]]
- 004d5b4c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b00:8"]]
+ 004f89e4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1d0:8"]]
~~~


### [`004d5be0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5be0.md) → [`004f8a78`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8a78.md) _ZN5Botan7SHA_2565clearEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      52,
      "READ",
      [
        "storage",
        "002b1a50",
        null,
        null
      ]
    ],
    [
      56,
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
      52,
      "READ",
      [
        "storage",
        "002c3120",
        null,
        null
      ]
    ],
    [
      56,
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


~~~diff
- 004d5c04 ["INT_ADD", "register:40f0:8", ["const:4d5c04:8", "const:4:8"]]
+ 004f8a9c ["INT_ADD", "register:40f0:8", ["const:4f8a9c:8", "const:4:8"]]
- 004d5c08 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004d5c0c ["COPY", "register:4050:8", ["const:2b1000:8"]]
+ 004f8aa0 ["COPY", "register:4048:8", ["const:2c3000:8"]]
+ 004f8aa4 ["COPY", "register:4050:8", ["const:2c2000:8"]]
- 004d5c14 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a50:8"]]
+ 004f8aac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:120:8"]]
~~~


### [`004d5ed0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5ed0.md) → [`004f8d68`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8d68.md) _ZN5Botan10system_rngEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc960`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc960.md) · 呼出先 5件 [`004d5f58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5f58.md) [`004d6094`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6094.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00c593b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593b0.md) · 呼出先 5件 [`004f8df0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8df0.md) [`004f8f2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f2c.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c253d0",
        null,
        "undefined1"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c253c0",
        null,
        "undefined8"
      ]
    ],
    [
      52,
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
      20,
      "READ",
      [
        "storage",
        "00ca4e90",
        null,
        "undefined1"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00ca4e80",
        null,
        "undefined8"
      ]
    ],
    [
      52,
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


~~~diff
- 004d5edc ["COPY", "register:4040:8", ["const:c25000:8"]]
- 004d5ee0 ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 004f8d74 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 004f8d78 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 004d5eec ["COPY", "register:4000:8", ["const:c25000:8"]]
- 004d5ef0 ["COPY", "tmp:0:8", ["const:3c0:8"]]
+ 004f8d84 ["COPY", "register:4000:8", ["const:ca4000:8"]]
+ 004f8d88 ["COPY", "tmp:0:8", ["const:e80:8"]]
- 004d5f00 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 004d5f04 ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 004f8d98 ["COPY", "register:4000:8", ["const:ca4000:8"]]
+ 004f8d9c ["COPY", "tmp:0:8", ["const:e90:8"]]
~~~


### [`004d5f58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5f58.md) → [`004f8df0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8df0.md) FUN_004f8df0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004d5ed0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5ed0.md) [`0051308c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051308c.md) · 呼出先 7件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 2件 [`004f8d68`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8d68.md) [`00535f24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535f24.md) · 呼出先 7件 [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "PARAM",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "00c253c0",
        null,
        "undefined8"
      ]
    ],
    [
      60,
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
      40,
      "PARAM",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "00ca4e80",
        null,
        "undefined8"
      ]
    ],
    [
      60,
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


~~~diff
- 004d5f70 ["COPY", "register:40a0:8", ["const:c25000:8"]]
- 004d5f74 ["COPY", "tmp:0:8", ["const:3c0:8"]]
+ 004f8e08 ["COPY", "register:40a0:8", ["const:ca4000:8"]]
+ 004f8e0c ["COPY", "tmp:0:8", ["const:e80:8"]]
- 004d5f7c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 004d5f80 ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 004f8e14 ["COPY", "register:4000:8", ["const:2b8000:8"]]
+ 004f8e18 ["COPY", "tmp:0:8", ["const:ddd:8"]]
- 004d5f8c ["COPY", "register:4040:8", ["const:bed000:8"]]
- 004d5f90 ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 004f8e24 ["COPY", "register:4040:8", ["const:c69000:8"]]
+ 004f8e28 ["COPY", "tmp:0:8", ["const:ea0:8"]]
~~~


### [`004d60c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d60c4.md) → [`004f8f5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f5c.md) _ZNK5Botan14calendar_point9to_stringEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`0042e9d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`004365f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb150`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00451870`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00459490`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      104,
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      104,
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      132,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      104,
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      104,
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      132,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ]
  ]
}
~~~


~~~diff
- 004d60f8 ["INT_ADD", "register:40f0:8", ["const:4d60f8:8", "const:4:8"]]
+ 004f8f90 ["INT_ADD", "register:40f0:8", ["const:4f8f90:8", "const:4:8"]]
- 004d6120 ["INT_ADD", "register:40f0:8", ["const:4d6120:8", "const:4:8"]]
+ 004f8fb8 ["INT_ADD", "register:40f0:8", ["const:4f8fb8:8", "const:4:8"]]
- 004d6124 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004f8fbc ["COPY", "register:4008:8", ["const:c9a000:8"]]
~~~


### [`004d6338`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6338.md) → [`004f91d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f91d0.md) FUN_004f91d0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0048aad4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048aad4.md) [`0048ac0c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ac0c.md) · 呼出先 7件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 2件 [`004ad96c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad96c.md) [`004adaa4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adaa4.md) · 呼出先 7件 [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      296,
      "PARAM",
      [
        "storage",
        "002a5727",
        null,
        "string"
      ]
    ],
    [
      348,
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      352,
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
      296,
      "PARAM",
      [
        "storage",
        "002b6155",
        null,
        "string"
      ]
    ],
    [
      348,
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      352,
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


~~~diff
- 004d6390 ["INT_ADD", "register:40f0:8", ["const:4d6390:8", "const:4:8"]]
+ 004f9228 ["INT_ADD", "register:40f0:8", ["const:4f9228:8", "const:4:8"]]
- 004d63c0 ["INT_ADD", "register:40f0:8", ["const:4d63c0:8", "const:4:8"]]
+ 004f9258 ["INT_ADD", "register:40f0:8", ["const:4f9258:8", "const:4:8"]]
- 004d63cc ["INT_ADD", "register:40f0:8", ["const:4d63cc:8", "const:4:8"]]
+ 004f9264 ["INT_ADD", "register:40f0:8", ["const:4f9264:8", "const:4:8"]]
~~~


### [`004d6550`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6550.md) → [`004f93e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f93e8.md) _ZN5Botan7Charset9transcodeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_13Character_SetESA_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00483974`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004a680c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      580,
      "PARAM",
      [
        "storage",
        "0029e62c",
        null,
        "string"
      ]
    ],
    [
      632,
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      636,
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
      580,
      "PARAM",
      [
        "storage",
        "002ae9b1",
        null,
        "string"
      ]
    ],
    [
      632,
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      636,
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


~~~diff
- 004d6628 ["INT_ADD", "register:40f0:8", ["const:4d6628:8", "const:4:8"]]
+ 004f94c0 ["INT_ADD", "register:40f0:8", ["const:4f94c0:8", "const:4:8"]]
- 004d6638 ["INT_ADD", "register:40f0:8", ["const:4d6638:8", "const:4:8"]]
+ 004f94d0 ["INT_ADD", "register:40f0:8", ["const:4f94d0:8", "const:4:8"]]
- 004d6734 ["INT_ADD", "register:40f0:8", ["const:4d6734:8", "const:4:8"]]
+ 004f95cc ["INT_ADD", "register:40f0:8", ["const:4f95cc:8", "const:4:8"]]
~~~


### [`004d6c30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6c30.md) → [`004f9ac8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9ac8.md) _ZN5Botan17DataSource_MemoryC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc670`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc670.md) · 呼出先 1件 [`0051d4f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md)
- 新版 呼出元 1件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590c0.md) · 呼出先 1件 [`00540388`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540388.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      28,
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
      20,
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      28,
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


~~~diff
- 004d6c3c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004f9ad4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004d6c44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 004f9adc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9e0:8"]]
- 004d6c78 ["INT_ADD", "register:40f0:8", ["const:4d6c78:8", "const:4:8"]]
+ 004f9b10 ["INT_ADD", "register:40f0:8", ["const:4f9b10:8", "const:4:8"]]
~~~


### [`004d6c8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6c8c.md) → [`004f9b24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9b24.md) _ZN5Botan17DataSource_Stream4readEPhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      140,
      "PARAM",
      [
        "storage",
        "0029d514",
        null,
        "string"
      ]
    ],
    [
      196,
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      200,
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
      140,
      "PARAM",
      [
        "storage",
        "002ad79e",
        null,
        "string"
      ]
    ],
    [
      196,
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      200,
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


~~~diff
- 004d6cb4 ["INT_ADD", "register:40f0:8", ["const:4d6cb4:8", "const:4:8"]]
+ 004f9b4c ["INT_ADD", "register:40f0:8", ["const:4f9b4c:8", "const:4:8"]]
- 004d6d0c ["INT_ADD", "register:40f0:8", ["const:4d6d0c:8", "const:4:8"]]
+ 004f9ba4 ["INT_ADD", "register:40f0:8", ["const:4f9ba4:8", "const:4:8"]]
- 004d6d14 ["COPY", "register:4008:8", ["const:29d000:8"]]
- 004d6d18 ["COPY", "tmp:0:8", ["const:514:8"]]
+ 004f9bac ["COPY", "register:4008:8", ["const:2ad000:8"]]
+ 004f9bb0 ["COPY", "tmp:0:8", ["const:79e:8"]]
~~~


### [`004d6e20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6e20.md) → [`004f9cb8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9cb8.md) _ZNK5Botan17DataSource_Stream4peekEPhmm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00490630`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`004b34c8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      160,
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      372,
      "PARAM",
      [
        "storage",
        "0029e50d",
        null,
        "string"
      ]
    ],
    [
      424,
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
      160,
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      372,
      "PARAM",
      [
        "storage",
        "002ae892",
        null,
        "string"
      ]
    ],
    [
      424,
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


~~~diff
- 004d6e7c ["INT_ADD", "register:40f0:8", ["const:4d6e7c:8", "const:4:8"]]
+ 004f9d14 ["INT_ADD", "register:40f0:8", ["const:4f9d14:8", "const:4:8"]]
- 004d6e8c ["INT_ADD", "register:40f0:8", ["const:4d6e8c:8", "const:4:8"]]
+ 004f9d24 ["INT_ADD", "register:40f0:8", ["const:4f9d24:8", "const:4:8"]]
- 004d6ebc ["COPY", "register:4048:8", ["const:bea000:8"]]
- 004d6ec0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004f9d54 ["COPY", "register:4048:8", ["const:c67000:8"]]
+ 004f9d58 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:338:8"]]
~~~


### [`004d717c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d717c.md) → [`004fa014`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa014.md) _ZN5Botan17DataSource_StreamC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc810.md) · 呼出先 9件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004d7338`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7338.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c59260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md) · 呼出先 9件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004fa1d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa1d0.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "READ",
      [
        "storage",
        "00c1b238",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[80]"
      ]
    ],
    [
      228,
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
      36,
      "READ",
      [
        "storage",
        "00c9ac28",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "00c66fd8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      228,
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


~~~diff
- 004d7194 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004fa02c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004d71a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:238:8"]]
+ 004fa038 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c28:8"]]
- 004d71e4 ["INT_ADD", "register:40f0:8", ["const:4d71e4:8", "const:4:8"]]
+ 004fa07c ["INT_ADD", "register:40f0:8", ["const:4fa07c:8", "const:4:8"]]
~~~


### [`004d7338`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7338.md) → [`004fa1d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa1d0.md) FUN_004fa1d0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004d717c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d717c.md) · 呼出先 4件 [`00bdb390`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb450`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdc0b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0b0.md) [`00bdc0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0c0.md)
- 新版 呼出元 1件 [`004fa014`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa014.md) · 呼出先 4件 [`00c57de0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57ea0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c58b00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b00.md) [`00c58b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b10.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "READ",
      [
        "storage",
        "00c1b240",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "00c1b248",
        null,
        "pointer"
      ]
    ],
    [
      60,
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
      36,
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      60,
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


~~~diff
- 004d7350 ["COPY", "register:40c8:8", ["const:c1b000:8"]]
- 004d7354 ["COPY", "register:40c0:8", ["const:c1b000:8"]]
+ 004fa1e8 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
+ 004fa1ec ["COPY", "register:40c0:8", ["const:c9a000:8"]]
- 004d735c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:240:8"]]
+ 004fa1f4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:c30:8"]]
- 004d7360 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:248:8"]]
+ 004fa1f8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c38:8"]]
~~~


### [`004d7450`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7450.md) → [`004fa2e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa2e8.md) _ZN5Botan17DataSource_StreamC2ERNSt6__ndk113basic_istreamIcNS1_11char_traitsIcEEEERKNS1_12basic_stringIcS4_NS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "READ",
      [
        "storage",
        "00c1b238",
        null,
        "pointer"
      ]
    ],
    [
      32,
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
      24,
      "READ",
      [
        "storage",
        "00c9ac28",
        null,
        "pointer"
      ]
    ],
    [
      32,
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


~~~diff
- 004d745c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004fa2f4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004d7468 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:238:8"]]
+ 004fa300 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c28:8"]]
- 004d7494 ["INT_ADD", "register:40f0:8", ["const:4d7494:8", "const:4:8"]]
+ 004fa32c ["INT_ADD", "register:40f0:8", ["const:4fa32c:8", "const:4:8"]]
~~~


### [`004d74f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d74f8.md) → [`004fa390`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa390.md) _ZN5Botan17DataSource_StreamD0Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc820`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc820.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c59270`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md)

変更の種類 call, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc820"
      ]
    ]
  ],
  "added": [
    [
      16,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59270"
      ]
    ]
  ]
}
~~~


~~~diff
- 004d7508 ["INT_ADD", "register:40f0:8", ["const:4d7508:8", "const:4:8"]]
- 004d7508 ["CALL", null, ["ram:bdc820:8"]]
+ 004fa3a0 ["INT_ADD", "register:40f0:8", ["const:4fa3a0:8", "const:4:8"]]
+ 004fa3a0 ["CALL", null, ["ram:c59270:8"]]
~~~


### [`004d751c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d751c.md) → [`004fa3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa3b4.md) _ZN5Botan9ExceptionC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb970`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb970.md) · 呼出先 1件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00c583c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583c0.md) · 呼出先 1件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      28,
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
      20,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      28,
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


~~~diff
- 004d7528 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004fa3c0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004d7530 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 004fa3c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 004d7560 ["INT_ADD", "register:40f0:8", ["const:4d7560:8", "const:4:8"]]
+ 004fa3f8 ["INT_ADD", "register:40f0:8", ["const:4fa3f8:8", "const:4:8"]]
~~~


### [`004d7584`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7584.md) → [`004fa41c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa41c.md) _ZN5Botan9ExceptionC1EPKcRKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md) · 呼出先 8件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00c58380`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md) · 呼出先 8件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      44,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ],
    [
      196,
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
      44,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ],
    [
      196,
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


~~~diff
- 004d75a4 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 004fa43c ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004d75b0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fe0:8"]]
+ 004fa448 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9d0:8"]]
- 004d75d0 ["INT_ADD", "register:40f0:8", ["const:4d75d0:8", "const:4:8"]]
+ 004fa468 ["INT_ADD", "register:40f0:8", ["const:4fa468:8", "const:4:8"]]
~~~


### [`004d7760`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7760.md) → [`004fa5f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa5f8.md) _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb820`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb820.md) · 呼出先 1件 [`00bdb930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)
- 新版 呼出元 1件 [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58270.md) · 呼出先 1件 [`00c58380`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      28,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb930"
      ]
    ],
    [
      36,
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
      20,
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      28,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58380"
      ]
    ],
    [
      36,
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


~~~diff
- 004d7770 ["COPY", "register:4008:8", ["const:296000:8"]]
- 004d7774 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 004fa608 ["COPY", "register:4008:8", ["const:2a6000:8"]]
+ 004fa60c ["COPY", "tmp:0:8", ["const:372:8"]]
- 004d777c ["INT_ADD", "register:40f0:8", ["const:4d777c:8", "const:4:8"]]
- 004d777c ["CALL", null, ["ram:bdb930:8"]]
- 004d7780 ["COPY", "register:4040:8", ["const:c1a000:8"]]
- 004d7784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
+ 004fa614 ["INT_ADD", "register:40f0:8", ["const:4fa614:8", "const:4:8"]]
+ 004fa614 ["CALL", null, ["ram:c58380:8"]]
+ 004fa618 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004fa61c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:960:8"]]
~~~


### [`004d779c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d779c.md) → [`004fa634`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa634.md) _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      280,
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      292,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb930"
      ]
    ],
    [
      332,
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
      280,
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      292,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58380"
      ]
    ],
    [
      332,
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


~~~diff
- 004d7838 ["INT_ADD", "register:40f0:8", ["const:4d7838:8", "const:4:8"]]
+ 004fa6d0 ["INT_ADD", "register:40f0:8", ["const:4fa6d0:8", "const:4:8"]]
- 004d7860 ["INT_ADD", "register:40f0:8", ["const:4d7860:8", "const:4:8"]]
+ 004fa6f8 ["INT_ADD", "register:40f0:8", ["const:4fa6f8:8", "const:4:8"]]
- 004d7894 ["INT_ADD", "register:40f0:8", ["const:4d7894:8", "const:4:8"]]
+ 004fa72c ["INT_ADD", "register:40f0:8", ["const:4fa72c:8", "const:4:8"]]
~~~


### [`004d7984`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7984.md) → [`004fa81c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa81c.md) _ZN5Botan12Lookup_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbf00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf00.md) · 呼出先 6件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00c58950`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58950.md) · 呼出先 6件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      32,
      "PARAM",
      [
        "storage",
        "002ae8f3",
        null,
        "string"
      ]
    ],
    [
      64,
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        null
      ]
    ],
    [
      184,
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
      32,
      "PARAM",
      [
        "storage",
        "002bfdd7",
        null,
        "string"
      ]
    ],
    [
      64,
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        null
      ]
    ],
    [
      184,
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


~~~diff
- 004d79a0 ["COPY", "register:4000:8", ["const:2ae000:8"]]
- 004d79a4 ["COPY", "tmp:0:8", ["const:8f3:8"]]
+ 004fa838 ["COPY", "register:4000:8", ["const:2bf000:8"]]
+ 004fa83c ["COPY", "tmp:0:8", ["const:dd7:8"]]
- 004d79bc ["INT_ADD", "register:40f0:8", ["const:4d79bc:8", "const:4:8"]]
+ 004fa854 ["INT_ADD", "register:40f0:8", ["const:4fa854:8", "const:4:8"]]
- 004d79c0 ["COPY", "register:4008:8", ["const:291000:8"]]
- 004d79c4 ["COPY", "tmp:0:8", ["const:8e1:8"]]
+ 004fa858 ["COPY", "register:4008:8", ["const:2a0000:8"]]
+ 004fa85c ["COPY", "tmp:0:8", ["const:efa:8"]]
~~~


### [`004d7c34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7c34.md) → [`004faacc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004faacc.md) _ZN5Botan14Internal_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bdbcb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcb0.md) [`00bdc9d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc9d0.md) · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 2件 [`00c58700`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58700.md) [`00c59420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59420.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      32,
      "PARAM",
      [
        "storage",
        "002a0638",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      72,
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
      32,
      "PARAM",
      [
        "storage",
        "002b0bf2",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      72,
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


~~~diff
- 004d7c50 ["COPY", "register:4000:8", ["const:2a0000:8"]]
- 004d7c54 ["COPY", "tmp:0:8", ["const:638:8"]]
+ 004faae8 ["COPY", "register:4000:8", ["const:2b0000:8"]]
+ 004faaec ["COPY", "tmp:0:8", ["const:bf2:8"]]
- 004d7c64 ["INT_ADD", "register:40f0:8", ["const:4d7c64:8", "const:4:8"]]
+ 004faafc ["INT_ADD", "register:40f0:8", ["const:4faafc:8", "const:4:8"]]
- 004d7c68 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004fab00 ["COPY", "register:4040:8", ["const:c9a000:8"]]
~~~


### [`004d7d1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7d1c.md) → [`004fabb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fabb4.md) _ZN5Botan18Invalid_Key_LengthC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbf30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf30.md) · 呼出先 8件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c58980`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58980.md) · 呼出先 8件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      212,
      "READ",
      [
        "storage",
        "00294810",
        null,
        "string"
      ]
    ],
    [
      216,
      "READ",
      [
        "storage",
        "0029481f",
        null,
        "string"
      ]
    ],
    [
      308,
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
      212,
      "READ",
      [
        "storage",
        "002a4126",
        null,
        "string"
      ]
    ],
    [
      216,
      "READ",
      [
        "storage",
        "002a4135",
        null,
        "string"
      ]
    ],
    [
      308,
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


~~~diff
- 004d7db4 ["INT_ADD", "register:40f0:8", ["const:4d7db4:8", "const:4:8"]]
+ 004fac4c ["INT_ADD", "register:40f0:8", ["const:4fac4c:8", "const:4:8"]]
- 004d7de0 ["INT_ADD", "register:40f0:8", ["const:4d7de0:8", "const:4:8"]]
+ 004fac78 ["INT_ADD", "register:40f0:8", ["const:4fac78:8", "const:4:8"]]
- 004d7de4 ["COPY", "register:4040:8", ["const:294000:8"]]
- 004d7de8 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 004fac7c ["COPY", "register:4040:8", ["const:2a4000:8"]]
+ 004fac80 ["COPY", "tmp:0:8", ["const:126:8"]]
~~~


### [`004d7f90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7f90.md) → [`004fae28`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fae28.md) _ZN5Botan17Invalid_IV_LengthC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbf40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf40.md) · 呼出先 7件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00c58990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58990.md) · 呼出先 7件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      56,
      "PARAM",
      [
        "storage",
        "002a4550",
        null,
        "string"
      ]
    ],
    [
      100,
      "PARAM",
      [
        "storage",
        "0029e55f",
        null,
        "string"
      ]
    ],
    [
      196,
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
      56,
      "PARAM",
      [
        "storage",
        "002b4dbd",
        null,
        "string"
      ]
    ],
    [
      100,
      "PARAM",
      [
        "storage",
        "002ae8e4",
        null,
        "string"
      ]
    ],
    [
      196,
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


~~~diff
- 004d7fc0 ["INT_ADD", "register:40f0:8", ["const:4d7fc0:8", "const:4:8"]]
+ 004fae58 ["INT_ADD", "register:40f0:8", ["const:4fae58:8", "const:4:8"]]
- 004d7fc4 ["COPY", "register:4010:8", ["const:2a4000:8"]]
- 004d7fc8 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 004fae5c ["COPY", "register:4010:8", ["const:2b4000:8"]]
+ 004fae60 ["COPY", "tmp:0:8", ["const:dbd:8"]]
- 004d7fd4 ["INT_ADD", "register:40f0:8", ["const:4d7fd4:8", "const:4:8"]]
+ 004fae6c ["INT_ADD", "register:40f0:8", ["const:4fae6c:8", "const:4:8"]]
~~~


### [`004d81b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d81b0.md) → [`004fb048`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb048.md) _ZN5Botan11Key_Not_SetC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb7f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7f0.md) · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`00c58240`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58240.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      32,
      "PARAM",
      [
        "storage",
        "00299c6b",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      72,
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
      32,
      "PARAM",
      [
        "storage",
        "002a9b44",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      72,
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


~~~diff
- 004d81cc ["COPY", "register:4000:8", ["const:299000:8"]]
- 004d81d0 ["COPY", "tmp:0:8", ["const:c6b:8"]]
+ 004fb064 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 004fb068 ["COPY", "tmp:0:8", ["const:b44:8"]]
- 004d81e0 ["INT_ADD", "register:40f0:8", ["const:4d81e0:8", "const:4:8"]]
+ 004fb078 ["INT_ADD", "register:40f0:8", ["const:4fb078:8", "const:4:8"]]
- 004d81e4 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004fb07c ["COPY", "register:4040:8", ["const:c9a000:8"]]
~~~


### [`004d82b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d82b8.md) → [`004fb150`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb150.md) _ZN5Botan16Policy_ViolationC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      32,
      "PARAM",
      [
        "storage",
        "002a95ff",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      72,
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
      32,
      "PARAM",
      [
        "storage",
        "002ba2a2",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      72,
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


~~~diff
- 004d82d4 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 004d82d8 ["COPY", "tmp:0:8", ["const:5ff:8"]]
+ 004fb16c ["COPY", "register:4000:8", ["const:2ba000:8"]]
+ 004fb170 ["COPY", "tmp:0:8", ["const:2a2:8"]]
- 004d82e8 ["INT_ADD", "register:40f0:8", ["const:4d82e8:8", "const:4:8"]]
+ 004fb180 ["INT_ADD", "register:40f0:8", ["const:4fb180:8", "const:4:8"]]
- 004d82ec ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004fb184 ["COPY", "register:4040:8", ["const:c9a000:8"]]
~~~


### [`004d83c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d83c0.md) → [`004fb258`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb258.md) _ZN5Botan13PRNG_UnseededC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd130`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd130.md) · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`00c59b80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b80.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      32,
      "PARAM",
      [
        "storage",
        "002afaef",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      72,
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
      32,
      "PARAM",
      [
        "storage",
        "002c1113",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      72,
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


~~~diff
- 004d83dc ["COPY", "register:4000:8", ["const:2af000:8"]]
- 004d83e0 ["COPY", "tmp:0:8", ["const:aef:8"]]
+ 004fb274 ["COPY", "register:4000:8", ["const:2c1000:8"]]
+ 004fb278 ["COPY", "tmp:0:8", ["const:113:8"]]
- 004d83f0 ["INT_ADD", "register:40f0:8", ["const:4d83f0:8", "const:4:8"]]
+ 004fb288 ["INT_ADD", "register:40f0:8", ["const:4fb288:8", "const:4:8"]]
- 004d83f4 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004fb28c ["COPY", "register:4040:8", ["const:c9a000:8"]]
~~~


### [`004d84c8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d84c8.md) → [`004fb360`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb360.md) _ZN5Botan19Algorithm_Not_FoundC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc150`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc150.md) · 呼出先 5件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`00c58ba0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md) · 呼出先 5件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      32,
      "PARAM",
      [
        "storage",
        "002a1617",
        null,
        "string"
      ]
    ],
    [
      56,
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      96,
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
      32,
      "PARAM",
      [
        "storage",
        "002b1c63",
        null,
        "string"
      ]
    ],
    [
      56,
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ],
    [
      96,
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


~~~diff
- 004d84e4 ["COPY", "register:4000:8", ["const:2a1000:8"]]
- 004d84e8 ["COPY", "tmp:0:8", ["const:617:8"]]
+ 004fb37c ["COPY", "register:4000:8", ["const:2b1000:8"]]
+ 004fb380 ["COPY", "tmp:0:8", ["const:c63:8"]]
- 004d84f8 ["INT_ADD", "register:40f0:8", ["const:4d84f8:8", "const:4:8"]]
+ 004fb390 ["INT_ADD", "register:40f0:8", ["const:4fb390:8", "const:4:8"]]
- 004d84fc ["COPY", "register:4008:8", ["const:2a5000:8"]]
- 004d8500 ["COPY", "tmp:0:8", ["const:41f:8"]]
+ 004fb394 ["COPY", "register:4008:8", ["const:2b5000:8"]]
+ 004fb398 ["COPY", "tmp:0:8", ["const:e4d:8"]]
~~~


### [`004d8628`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8628.md) → [`004fb4c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb4c0.md) _ZN5Botan17No_Provider_FoundC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      32,
      "PARAM",
      [
        "storage",
        "00295a6a",
        null,
        "string"
      ]
    ],
    [
      56,
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      96,
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
      32,
      "PARAM",
      [
        "storage",
        "002a54a3",
        null,
        "string"
      ]
    ],
    [
      56,
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ],
    [
      96,
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


~~~diff
- 004d8644 ["COPY", "register:4000:8", ["const:295000:8"]]
- 004d8648 ["COPY", "tmp:0:8", ["const:a6a:8"]]
+ 004fb4dc ["COPY", "register:4000:8", ["const:2a5000:8"]]
+ 004fb4e0 ["COPY", "tmp:0:8", ["const:4a3:8"]]
- 004d8658 ["INT_ADD", "register:40f0:8", ["const:4d8658:8", "const:4:8"]]
+ 004fb4f0 ["INT_ADD", "register:40f0:8", ["const:4fb4f0:8", "const:4:8"]]
- 004d865c ["COPY", "register:4008:8", ["const:2a5000:8"]]
- 004d8660 ["COPY", "tmp:0:8", ["const:41f:8"]]
+ 004fb4f4 ["COPY", "register:4008:8", ["const:2b5000:8"]]
+ 004fb4f8 ["COPY", "tmp:0:8", ["const:e4d:8"]]
~~~


### [`004d8768`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8768.md) → [`004fb600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb600.md) _ZN5Botan18Provider_Not_FoundC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc920`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc920.md) · 呼出先 6件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00c59370`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59370.md) · 呼出先 6件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "PARAM",
      [
        "storage",
        "0029284e",
        null,
        "string"
      ]
    ],
    [
      64,
      "PARAM",
      [
        "storage",
        "0029c676",
        null,
        "string"
      ]
    ],
    [
      160,
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
      40,
      "PARAM",
      [
        "storage",
        "002a1f5e",
        null,
        "string"
      ]
    ],
    [
      64,
      "PARAM",
      [
        "storage",
        "002ac80f",
        null,
        "string"
      ]
    ],
    [
      160,
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


~~~diff
- 004d878c ["COPY", "register:4000:8", ["const:292000:8"]]
- 004d8790 ["COPY", "tmp:0:8", ["const:84e:8"]]
+ 004fb624 ["COPY", "register:4000:8", ["const:2a1000:8"]]
+ 004fb628 ["COPY", "tmp:0:8", ["const:f5e:8"]]
- 004d87a0 ["INT_ADD", "register:40f0:8", ["const:4d87a0:8", "const:4:8"]]
+ 004fb638 ["INT_ADD", "register:40f0:8", ["const:4fb638:8", "const:4:8"]]
- 004d87a4 ["COPY", "register:4008:8", ["const:29c000:8"]]
- 004d87a8 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 004fb63c ["COPY", "register:4008:8", ["const:2ac000:8"]]
+ 004fb640 ["COPY", "tmp:0:8", ["const:80f:8"]]
~~~


### [`004d8930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8930.md) → [`004fb7c8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb7c8.md) _ZN5Botan22Invalid_Algorithm_NameC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc450`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc450.md) · 呼出先 4件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)
- 新版 呼出元 1件 [`00c58ea0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ea0.md) · 呼出先 4件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "0029f575",
        null,
        "string"
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      64,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb930"
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002af988",
        null,
        "string"
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      64,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58380"
      ]
    ]
  ]
}
~~~


~~~diff
- 004d8948 ["COPY", "register:4000:8", ["const:29f000:8"]]
- 004d894c ["COPY", "tmp:0:8", ["const:575:8"]]
+ 004fb7e0 ["COPY", "register:4000:8", ["const:2af000:8"]]
+ 004fb7e4 ["COPY", "tmp:0:8", ["const:988:8"]]
- 004d895c ["INT_ADD", "register:40f0:8", ["const:4d895c:8", "const:4:8"]]
+ 004fb7f4 ["INT_ADD", "register:40f0:8", ["const:4fb7f4:8", "const:4:8"]]
- 004d8960 ["COPY", "register:4008:8", ["const:296000:8"]]
- 004d8964 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 004fb7f8 ["COPY", "register:4008:8", ["const:2a6000:8"]]
+ 004fb7fc ["COPY", "tmp:0:8", ["const:372:8"]]
~~~


### [`004d89f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d89f4.md) → [`004fb88c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb88c.md) _ZN5Botan14Encoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb9e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9e0.md) · 呼出先 4件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)
- 新版 呼出元 1件 [`00c58430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58430.md) · 呼出先 4件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "00298e11",
        null,
        "string"
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      64,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb930"
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8bcf",
        null,
        "string"
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      64,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58380"
      ]
    ]
  ]
}
~~~


~~~diff
- 004d8a0c ["COPY", "register:4000:8", ["const:298000:8"]]
- 004d8a10 ["COPY", "tmp:0:8", ["const:e11:8"]]
+ 004fb8a4 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 004fb8a8 ["COPY", "tmp:0:8", ["const:bcf:8"]]
- 004d8a20 ["INT_ADD", "register:40f0:8", ["const:4d8a20:8", "const:4:8"]]
+ 004fb8b8 ["INT_ADD", "register:40f0:8", ["const:4fb8b8:8", "const:4:8"]]
- 004d8a24 ["COPY", "register:4008:8", ["const:296000:8"]]
- 004d8a28 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 004fb8bc ["COPY", "register:4008:8", ["const:2a6000:8"]]
+ 004fb8c0 ["COPY", "tmp:0:8", ["const:372:8"]]
~~~


### [`004d8ab8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8ab8.md) → [`004fb950`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb950.md) _ZN5Botan14Decoding_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcfa0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcfa0.md) · 呼出先 5件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)
- 新版 呼出元 1件 [`00c599f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599f0.md) · 呼出先 5件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      32,
      "PARAM",
      [
        "storage",
        "002ae900",
        null,
        "string"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "00292868",
        null,
        "string"
      ]
    ],
    [
      136,
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
      32,
      "PARAM",
      [
        "storage",
        "002bfde4",
        null,
        "string"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "002a1f78",
        null,
        "string"
      ]
    ],
    [
      136,
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


~~~diff
- 004d8ad4 ["COPY", "register:4000:8", ["const:2ae000:8"]]
- 004d8ad8 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 004fb96c ["COPY", "register:4000:8", ["const:2bf000:8"]]
+ 004fb970 ["COPY", "tmp:0:8", ["const:de4:8"]]
- 004d8aec ["INT_ADD", "register:40f0:8", ["const:4d8aec:8", "const:4:8"]]
+ 004fb984 ["INT_ADD", "register:40f0:8", ["const:4fb984:8", "const:4:8"]]
- 004d8af0 ["COPY", "register:4008:8", ["const:292000:8"]]
- 004d8af4 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 004fb988 ["COPY", "register:4008:8", ["const:2a1000:8"]]
+ 004fb98c ["COPY", "tmp:0:8", ["const:f78:8"]]
~~~


### [`004d8c5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8c5c.md) → [`004fbaf4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbaf4.md) _ZN5Botan17Integrity_FailureC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      32,
      "PARAM",
      [
        "storage",
        "00296a7b",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      72,
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
      32,
      "PARAM",
      [
        "storage",
        "002a65b0",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      72,
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


~~~diff
- 004d8c78 ["COPY", "register:4000:8", ["const:296000:8"]]
- 004d8c7c ["COPY", "tmp:0:8", ["const:a7b:8"]]
+ 004fbb10 ["COPY", "register:4000:8", ["const:2a6000:8"]]
+ 004fbb14 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 004d8c8c ["INT_ADD", "register:40f0:8", ["const:4d8c8c:8", "const:4:8"]]
+ 004fbb24 ["INT_ADD", "register:40f0:8", ["const:4fbb24:8", "const:4:8"]]
- 004d8c90 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004fbb28 ["COPY", "register:4040:8", ["const:c9a000:8"]]
~~~


### [`004d8d44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8d44.md) → [`004fbbdc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbbdc.md) _ZN5Botan11Invalid_OIDC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb990.md) · 呼出先 4件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)
- 新版 呼出元 1件 [`00c583e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583e0.md) · 呼出先 4件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9612",
        null,
        "string"
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "002ae900",
        null,
        "string"
      ]
    ],
    [
      72,
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
      28,
      "PARAM",
      [
        "storage",
        "002ba2b5",
        null,
        "string"
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "002bfde4",
        null,
        "string"
      ]
    ],
    [
      72,
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


~~~diff
- 004d8d5c ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 004d8d60 ["COPY", "tmp:0:8", ["const:612:8"]]
+ 004fbbf4 ["COPY", "register:4000:8", ["const:2ba000:8"]]
+ 004fbbf8 ["COPY", "tmp:0:8", ["const:2b5:8"]]
- 004d8d70 ["INT_ADD", "register:40f0:8", ["const:4d8d70:8", "const:4:8"]]
+ 004fbc08 ["INT_ADD", "register:40f0:8", ["const:4fbc08:8", "const:4:8"]]
- 004d8d74 ["COPY", "register:4000:8", ["const:2ae000:8"]]
- 004d8d78 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 004fbc0c ["COPY", "register:4000:8", ["const:2bf000:8"]]
+ 004fbc10 ["COPY", "tmp:0:8", ["const:de4:8"]]
~~~


### [`004d8e54`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8e54.md) → [`004fbcec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbcec.md) _ZN5Botan15Stream_IO_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb960`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb960.md) · 呼出先 4件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`00c583b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583b0.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      32,
      "PARAM",
      [
        "storage",
        "002a455b",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      72,
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
      32,
      "PARAM",
      [
        "storage",
        "002b4dc8",
        null,
        "string"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      72,
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


~~~diff
- 004d8e70 ["COPY", "register:4000:8", ["const:2a4000:8"]]
- 004d8e74 ["COPY", "tmp:0:8", ["const:55b:8"]]
+ 004fbd08 ["COPY", "register:4000:8", ["const:2b4000:8"]]
+ 004fbd0c ["COPY", "tmp:0:8", ["const:dc8:8"]]
- 004d8e84 ["INT_ADD", "register:40f0:8", ["const:4d8e84:8", "const:4:8"]]
+ 004fbd1c ["INT_ADD", "register:40f0:8", ["const:4fbd1c:8", "const:4:8"]]
- 004d8e88 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004fbd20 ["COPY", "register:4040:8", ["const:c9a000:8"]]
~~~


### [`004d8f3c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8f3c.md) → [`004fbdd4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbdd4.md) _ZN5Botan17Self_Test_FailureC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdc9d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc9d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c59420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a163c",
        null,
        "string"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "00c1b2c0",
        null,
        "pointer"
      ]
    ],
    [
      88,
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
      28,
      "PARAM",
      [
        "storage",
        "002b1c88",
        null,
        "string"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "00c9acb0",
        null,
        "pointer"
      ]
    ],
    [
      88,
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


~~~diff
- 004d8f54 ["COPY", "register:4000:8", ["const:2a1000:8"]]
- 004d8f58 ["COPY", "tmp:0:8", ["const:63c:8"]]
+ 004fbdec ["COPY", "register:4000:8", ["const:2b1000:8"]]
+ 004fbdf0 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 004d8f68 ["INT_ADD", "register:40f0:8", ["const:4d8f68:8", "const:4:8"]]
+ 004fbe00 ["INT_ADD", "register:40f0:8", ["const:4fbe00:8", "const:4:8"]]
- 004d8f74 ["INT_ADD", "register:40f0:8", ["const:4d8f74:8", "const:4:8"]]
+ 004fbe0c ["INT_ADD", "register:40f0:8", ["const:4fbe0c:8", "const:4:8"]]
~~~


### [`004d8fe8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8fe8.md) → [`004fbe80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbe80.md) _ZN5Botan15Not_ImplementedC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc690`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc690.md) · 呼出先 1件 [`00bdb930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)
- 新版 呼出元 1件 [`00c590e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590e0.md) · 呼出先 1件 [`00c58380`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "PARAM",
      [
        "storage",
        "0029f58e",
        null,
        "string"
      ]
    ],
    [
      28,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb930"
      ]
    ],
    [
      36,
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
      20,
      "PARAM",
      [
        "storage",
        "002af9a1",
        null,
        "string"
      ]
    ],
    [
      28,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58380"
      ]
    ],
    [
      36,
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


~~~diff
- 004d8ff8 ["COPY", "register:4008:8", ["const:29f000:8"]]
- 004d8ffc ["COPY", "tmp:0:8", ["const:58e:8"]]
+ 004fbe90 ["COPY", "register:4008:8", ["const:2af000:8"]]
+ 004fbe94 ["COPY", "tmp:0:8", ["const:9a1:8"]]
- 004d9004 ["INT_ADD", "register:40f0:8", ["const:4d9004:8", "const:4:8"]]
- 004d9004 ["CALL", null, ["ram:bdb930:8"]]
- 004d9008 ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 004d900c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c8:8"]]
+ 004fbe9c ["INT_ADD", "register:40f0:8", ["const:4fbe9c:8", "const:4:8"]]
+ 004fbe9c ["CALL", null, ["ram:c58380:8"]]
+ 004fbea0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004fbea4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb8:8"]]
~~~


### [`004d9024`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9024.md) → [`004fbebc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbebc.md) _ZN5Botan19get_files_recursiveERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc9e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc9e0.md) · 呼出先 20件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00436e9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00517044`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517044.md) [`005171dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/005171dc.md)
- 新版 呼出元 1件 [`00c59430`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59430.md) · 呼出先 20件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459d34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00539edc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539edc.md) [`0053a074`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a074.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      548,
      "DATA",
      [
        "storage",
        "00bed388",
        null,
        "undefined *"
      ]
    ],
    [
      564,
      "READ",
      [
        "storage",
        "00c1b2d0",
        null,
        "pointer"
      ]
    ],
    [
      568,
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
      548,
      "DATA",
      [
        "storage",
        "00c69f48",
        null,
        "undefined *"
      ]
    ],
    [
      564,
      "READ",
      [
        "storage",
        "00c9acc0",
        null,
        "pointer"
      ]
    ],
    [
      568,
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


~~~diff
- 004d9080 ["INT_ADD", "register:40f0:8", ["const:4d9080:8", "const:4:8"]]
+ 004fbf18 ["INT_ADD", "register:40f0:8", ["const:4fbf18:8", "const:4:8"]]
- 004d90ec ["INT_ADD", "register:40f0:8", ["const:4d90ec:8", "const:4:8"]]
+ 004fbf84 ["INT_ADD", "register:40f0:8", ["const:4fbf84:8", "const:4:8"]]
- 004d9104 ["INT_ADD", "register:40f0:8", ["const:4d9104:8", "const:4:8"]]
+ 004fbf9c ["INT_ADD", "register:40f0:8", ["const:4fbf9c:8", "const:4:8"]]
~~~


### [`004d989c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d989c.md) → [`004fc734`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc734.md) _ZN5Botan15allocate_memoryEmm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdca20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdca20.md) · 呼出先 5件 [`00bbad34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbbe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbe0.md) [`00bdbbf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbf0.md)
- 新版 呼出元 1件 [`00c59470`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59470.md) · 呼出先 5件 [`00c3777c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58630`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58630.md) [`00c58640`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58640.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      44,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      60,
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
      44,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      60,
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


~~~diff
- 004d98a8 ["INT_ADD", "register:40f0:8", ["const:4d98a8:8", "const:4:8"]]
+ 004fc740 ["INT_ADD", "register:40f0:8", ["const:4fc740:8", "const:4:8"]]
- 004d98c0 ["INT_ADD", "register:40f0:8", ["const:4d98c0:8", "const:4:8"]]
+ 004fc758 ["INT_ADD", "register:40f0:8", ["const:4fc758:8", "const:4:8"]]
- 004d98c8 ["INT_ADD", "register:40f0:8", ["const:4d98c8:8", "const:4:8"]]
- 004d98c8 ["CALL", null, ["ram:bdbbf0:8"]]
- 004d98cc ["COPY", "register:4008:8", ["const:c1a000:8"]]
- 004d98d0 ["COPY", "register:4010:8", ["const:c1b000:8"]]
+ 004fc760 ["INT_ADD", "register:40f0:8", ["const:4fc760:8", "const:4:8"]]
+ 004fc760 ["CALL", null, ["ram:c58640:8"]]
+ 004fc764 ["COPY", "register:4008:8", ["const:c9a000:8"]]
+ 004fc768 ["COPY", "register:4010:8", ["const:c9a000:8"]]
~~~


### [`004d98e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d98e4.md) → [`004fc77c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc77c.md) _ZN5Botan17deallocate_memoryEPvmm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdca30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdca30.md) · 呼出先 2件 [`00bdb810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00c59480`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59480.md) · 呼出先 2件 [`00c58260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
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
      28,
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


~~~diff
- 004d98f8 ["COPY", "register:4040:8", ["const:bea000:8"]]
+ 004fc790 ["COPY", "register:4040:8", ["const:c67000:8"]]
- 004d9900 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:778:8"]]
+ 004fc798 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
- 004d9908 ["INT_ADD", "register:40f0:8", ["const:4d9908:8", "const:4:8"]]
+ 004fc7a0 ["INT_ADD", "register:40f0:8", ["const:4fc7a0:8", "const:4:8"]]
~~~


### [`004d9940`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9940.md) → [`004fc7d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc7d8.md) _ZN5Botan2OS25run_cpu_instruction_probeENSt6__ndk18functionIFivEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00436e9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`004d9b40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9b40.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00459d34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`004fc9d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc9d8.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      60,
      "DATA",
      [
        "storage",
        "004d9b40",
        null,
        null
      ]
    ],
    [
      96,
      "PARAM",
      [
        "storage",
        "00c253d8",
        null,
        null
      ]
    ],
    [
      236,
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
      60,
      "DATA",
      [
        "storage",
        "004fc9d8",
        null,
        null
      ]
    ],
    [
      96,
      "PARAM",
      [
        "storage",
        "00ca4e98",
        null,
        null
      ]
    ],
    [
      236,
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


~~~diff
- 004d9974 ["COPY", "register:4040:8", ["const:4d9b40:8"]]
+ 004fc80c ["COPY", "register:4040:8", ["const:4fc9d8:8"]]
- 004d9980 ["INT_ADD", "register:40f0:8", ["const:4d9980:8", "const:4:8"]]
+ 004fc818 ["INT_ADD", "register:40f0:8", ["const:4fc818:8", "const:4:8"]]
- 004d9994 ["INT_ADD", "register:40f0:8", ["const:4d9994:8", "const:4:8"]]
+ 004fc82c ["INT_ADD", "register:40f0:8", ["const:4fc82c:8", "const:4:8"]]
~~~


### [`004d9b58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9b58.md) → [`004fc9f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc9f0.md) _ZN5Botan9to_uint16ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      100,
      "PARAM",
      [
        "storage",
        "0029391c",
        null,
        "string"
      ]
    ],
    [
      156,
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      160,
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
      100,
      "PARAM",
      [
        "storage",
        "002a3115",
        null,
        "string"
      ]
    ],
    [
      156,
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      160,
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


~~~diff
- 004d9b78 ["INT_ADD", "register:40f0:8", ["const:4d9b78:8", "const:4:8"]]
+ 004fca10 ["INT_ADD", "register:40f0:8", ["const:4fca10:8", "const:4:8"]]
- 004d9bb0 ["INT_ADD", "register:40f0:8", ["const:4d9bb0:8", "const:4:8"]]
+ 004fca48 ["INT_ADD", "register:40f0:8", ["const:4fca48:8", "const:4:8"]]
- 004d9bb8 ["COPY", "register:4008:8", ["const:293000:8"]]
- 004d9bbc ["COPY", "tmp:0:8", ["const:91c:8"]]
+ 004fca50 ["COPY", "register:4008:8", ["const:2a3000:8"]]
+ 004fca54 ["COPY", "tmp:0:8", ["const:115:8"]]
~~~


### [`004d9c58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9c58.md) → [`004fcaf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fcaf0.md) _ZN5Botan18timespec_to_u32bitERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      456,
      "PARAM",
      [
        "storage",
        "002a4567",
        null,
        "string"
      ]
    ],
    [
      512,
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      516,
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
      456,
      "PARAM",
      [
        "storage",
        "002b4dd4",
        null,
        "string"
      ]
    ],
    [
      512,
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      516,
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


~~~diff
- 004d9cfc ["INT_ADD", "register:40f0:8", ["const:4d9cfc:8", "const:4:8"]]
+ 004fcb94 ["INT_ADD", "register:40f0:8", ["const:4fcb94:8", "const:4:8"]]
- 004d9d1c ["INT_ADD", "register:40f0:8", ["const:4d9d1c:8", "const:4:8"]]
+ 004fcbb4 ["INT_ADD", "register:40f0:8", ["const:4fcbb4:8", "const:4:8"]]
- 004d9d6c ["INT_ADD", "register:40f0:8", ["const:4d9d6c:8", "const:4:8"]]
+ 004fcc04 ["INT_ADD", "register:40f0:8", ["const:4fcc04:8", "const:4:8"]]
~~~


### [`004d9ed0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9ed0.md) → [`004fcd68`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fcd68.md) _ZN5Botan13split_on_predERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFbcEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc160`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc160.md) · 呼出先 11件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00436e9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051dea4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c58bb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bb0.md) · 呼出先 11件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459d34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00540d3c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      528,
      "PARAM",
      [
        "storage",
        "0029d552",
        null,
        "string"
      ]
    ],
    [
      584,
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      588,
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
      528,
      "PARAM",
      [
        "storage",
        "002ad7dc",
        null,
        "string"
      ]
    ],
    [
      584,
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      588,
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


~~~diff
- 004d9f48 ["INT_ADD", "register:40f0:8", ["const:4d9f48:8", "const:4:8"]]
+ 004fcde0 ["INT_ADD", "register:40f0:8", ["const:4fcde0:8", "const:4:8"]]
- 004d9f90 ["INT_ADD", "register:40f0:8", ["const:4d9f90:8", "const:4:8"]]
+ 004fce28 ["INT_ADD", "register:40f0:8", ["const:4fce28:8", "const:4:8"]]
- 004d9fe0 ["INT_ADD", "register:40f0:8", ["const:4d9fe0:8", "const:4:8"]]
+ 004fce78 ["INT_ADD", "register:40f0:8", ["const:4fce78:8", "const:4:8"]]
~~~


### [`004da474`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004da474.md) → [`004fd30c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd30c.md) _ZN5Botan14string_to_ipv4ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcab0.md) · 呼出先 11件 [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00524c94`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c94.md) [`00524c98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c98.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c59500`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59500.md) · 呼出先 11件 [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00547b2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md) [`00547b30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      56,
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "00bed710",
        null,
        "pointer"
      ]
    ],
    [
      116,
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
      56,
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "00c6a2d0",
        null,
        "pointer"
      ]
    ],
    [
      116,
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


~~~diff
- 004da494 ["COPY", "register:4048:8", ["const:bed000:8"]]
- 004da498 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 004fd32c ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 004fd330 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 004da4c0 ["INT_ADD", "register:40f0:8", ["const:4da4c0:8", "const:4:8"]]
+ 004fd358 ["INT_ADD", "register:40f0:8", ["const:4fd358:8", "const:4:8"]]
- 004da4ec ["INT_ADD", "register:40f0:8", ["const:4da4ec:8", "const:4:8"]]
+ 004fd384 ["INT_ADD", "register:40f0:8", ["const:4fd384:8", "const:4:8"]]
~~~


### [`004daaa4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004daaa4.md) → [`004fd93c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd93c.md) _ZN5Botan19host_wildcard_matchERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcad0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcad0.md) · 呼出先 15件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`0041f280`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f280.md) [`0041f354`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md)
- 新版 呼出元 1件 [`00c59520`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59520.md) · 呼出先 15件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440ac0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440ac0.md) [`00441d80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441d80.md) [`00441e54`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      1144,
      "PARAM",
      [
        "storage",
        "002a6859",
        null,
        null
      ]
    ],
    [
      1228,
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      1356,
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
      1144,
      "PARAM",
      [
        "storage",
        "002b734a",
        null,
        null
      ]
    ],
    [
      1228,
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      1356,
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


~~~diff
- 004dab4c ["INT_ADD", "register:40f0:8", ["const:4dab4c:8", "const:4:8"]]
+ 004fd9e4 ["INT_ADD", "register:40f0:8", ["const:4fd9e4:8", "const:4:8"]]
- 004dae24 ["INT_ADD", "register:40f0:8", ["const:4dae24:8", "const:4:8"]]
+ 004fdcbc ["INT_ADD", "register:40f0:8", ["const:4fdcbc:8", "const:4:8"]]
- 004dae64 ["INT_ADD", "register:40f0:8", ["const:4dae64:8", "const:4:8"]]
+ 004fdcfc ["INT_ADD", "register:40f0:8", ["const:4fdcfc:8", "const:4:8"]]
~~~


### [`004db550`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004db550.md) → [`004fe3e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fe3e8.md) _ZN5Botan8read_cfgERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 23件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041fddc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00471da4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471da4.md) [`00483974`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00512990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)
- 新版 呼出元 0件  · 呼出先 23件 [`0043b724`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00494c3c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494c3c.md) [`004a680c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      184,
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      236,
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      268,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      184,
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      236,
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      268,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ]
  ]
}
~~~


~~~diff
- 004db5e4 ["COPY", "register:40b0:8", ["const:c1a000:8"]]
+ 004fe47c ["COPY", "register:40b0:8", ["const:c9a000:8"]]
- 004db608 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:e40:8"]]
+ 004fe4a0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:830:8"]]
- 004db634 ["INT_ADD", "register:40f0:8", ["const:4db634:8", "const:4:8"]]
+ 004fe4cc ["INT_ADD", "register:40f0:8", ["const:4fe4cc:8", "const:4:8"]]
~~~


### [`004dbc40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbc40.md) → [`004fead8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fead8.md) _ZN5Botan18short_version_cstrEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      4,
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
      4,
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


~~~diff
- 004dbc40 ["COPY", "register:4000:8", ["const:29f000:8"]]
- 004dbc44 ["COPY", "tmp:0:8", ["const:5c9:8"]]
+ 004fead8 ["COPY", "register:4000:8", ["const:2af000:8"]]
+ 004feadc ["COPY", "tmp:0:8", ["const:9dc:8"]]
~~~


### [`004dbc4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbc4c.md) → [`004feae4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feae4.md) _ZN5Botan12version_cstrEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      4,
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
      4,
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


~~~diff
- 004dbc4c ["COPY", "register:4000:8", ["const:2ab000:8"]]
- 004dbc50 ["COPY", "tmp:0:8", ["const:66b:8"]]
+ 004feae4 ["COPY", "register:4000:8", ["const:2bc000:8"]]
+ 004feae8 ["COPY", "tmp:0:8", ["const:58e:8"]]
~~~


### [`004dbc58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbc58.md) → [`004feaf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feaf0.md) _ZN5Botan14version_stringEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004feb18",
      "incomplete_value": true,
      "site": "004feb24",
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
                "const:a70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004dbc80",
      "incomplete_value": true,
      "site": "004dbc8c",
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
                "const:420:8"
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
      "definition_site": "004feb14",
      "incomplete_value": true,
      "site": "004feb28",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004dbc7c",
      "incomplete_value": true,
      "site": "004dbc90",
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
      "definition_site": "004feb14",
      "incomplete_value": true,
      "site": "004feb28",
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
      "definition_site": "004dbc7c",
      "incomplete_value": true,
      "site": "004dbc90",
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
    "ordinal": 6,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "READ",
      [
        "storage",
        "002ab6ab",
        null,
        "string"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "002ab6bb",
        null,
        "string"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "002b1420",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      36,
      "READ",
      [
        "storage",
        "002bc5ce",
        null,
        "string"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "002bc5de",
        null,
        "string"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "002c2a70",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 004dbc6c ["INT_ADD", "register:40f0:8", ["const:4dbc6c:8", "const:4:8"]]
+ 004feb04 ["INT_ADD", "register:40f0:8", ["const:4feb04:8", "const:4:8"]]
- 004dbc70 ["COPY", "register:4040:8", ["const:2ab000:8"]]
- 004dbc74 ["COPY", "tmp:0:8", ["const:66b:8"]]
+ 004feb08 ["COPY", "register:4040:8", ["const:2bc000:8"]]
+ 004feb0c ["COPY", "tmp:0:8", ["const:58e:8"]]
- 004dbc78 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004feb10 ["COPY", "register:4048:8", ["const:2c2000:8"]]
~~~


