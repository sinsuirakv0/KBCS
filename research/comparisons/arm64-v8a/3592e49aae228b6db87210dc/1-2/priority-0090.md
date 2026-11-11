# v16.0.0 → v16.0.1 · 最優先の変更候補 (90)

[一覧の目次](README.md)

### [`00bca0bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0bc.md) → [`00bca4e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4e4.md) _ZN8firebase4auth4Auth7GetAuthEPNS_3AppEPNS_10InitResultE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a5c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5c0.md) · 呼出先 8件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ad30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md) [`00c5b1e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md)
- 新版 呼出元 1件 [`00c5a9c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a9c0.md) · 呼出先 8件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b130`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md) [`00c5b5e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bca530",
      "incomplete_value": true,
      "site": "00bca530",
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
      "definition_site": "00bca108",
      "incomplete_value": true,
      "site": "00bca108",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca510",
      "incomplete_value": true,
      "site": "00bca514",
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
      "definition_site": "00bca0e8",
      "incomplete_value": true,
      "site": "00bca0ec",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca5d8",
      "incomplete_value": false,
      "site": "00bca5e4",
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
            "const:34e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca1b0",
      "incomplete_value": false,
      "site": "00bca1bc",
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
            "const:30e:8"
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
      28,
      "READ",
      [
        "storage",
        "00c9b5a0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "01126320",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126320",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9b9a0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "01126720",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126720",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bca0d8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5a0:8"]]
+ 00bca500 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9a0:8"]]
- 00bca0ec ["INT_ADD", "register:40f0:8", ["const:bca0ec:8", "const:4:8"]]
+ 00bca514 ["INT_ADD", "register:40f0:8", ["const:bca514:8", "const:4:8"]]
- 00bca0f8 ["INT_ADD", "register:40f0:8", ["const:bca0f8:8", "const:4:8"]]
+ 00bca520 ["INT_ADD", "register:40f0:8", ["const:bca520:8", "const:4:8"]]
~~~


### [`00bca368`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca368.md) → [`00bca790`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca790.md) _ZN8firebase4auth4AuthC1EPNS_3AppEPv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d690`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d690.md) · 呼出先 10件 [`00bcb984`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb984.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a7f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7f0.md)
- 新版 呼出元 1件 [`00c5da90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da90.md) · 呼出先 10件 [`00bcbdac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbdac.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5abf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abf0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca7e0",
      "incomplete_value": false,
      "site": "00bca7e4",
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
            "const:512:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca3b8",
      "incomplete_value": false,
      "site": "00bca3bc",
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
            "const:4d2:8"
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
      "definition_site": "00bca804",
      "incomplete_value": false,
      "site": "00bca810",
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
            "const:10f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca3dc",
      "incomplete_value": false,
      "site": "00bca3e8",
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
            "const:cf:8"
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
      "definition_site": "00bca868",
      "incomplete_value": false,
      "site": "00bca870",
      "value": [
        "leaf",
        "const:bcbdac:8"
      ]
    },
    "old": {
      "definition_site": "00bca440",
      "incomplete_value": false,
      "site": "00bca448",
      "value": [
        "leaf",
        "const:bcb984:8"
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      80,
      "PARAM",
      [
        "storage",
        "002af4d2",
        null,
        "string"
      ]
    ],
    [
      116,
      "PARAM",
      [
        "storage",
        "002bc0cf",
        null,
        null
      ]
    ],
    [
      216,
      "PARAM",
      [
        "storage",
        "00bcb984",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      80,
      "PARAM",
      [
        "storage",
        "002af512",
        null,
        "string"
      ]
    ],
    [
      116,
      "PARAM",
      [
        "storage",
        "002bc10f",
        null,
        null
      ]
    ],
    [
      216,
      "PARAM",
      [
        "storage",
        "00bcbdac",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bca39c ["INT_ADD", "register:40f0:8", ["const:bca39c:8", "const:4:8"]]
+ 00bca7c4 ["INT_ADD", "register:40f0:8", ["const:bca7c4:8", "const:4:8"]]
- 00bca3a4 ["INT_ADD", "register:40f0:8", ["const:bca3a4:8", "const:4:8"]]
+ 00bca7cc ["INT_ADD", "register:40f0:8", ["const:bca7cc:8", "const:4:8"]]
- 00bca3b8 ["COPY", "tmp:0:8", ["const:4d2:8"]]
+ 00bca7e0 ["COPY", "tmp:0:8", ["const:512:8"]]
~~~


### [`00bca614`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca614.md) → [`00bcaa3c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcaa3c.md) _ZN8firebase4auth4Auth14DeleteInternalEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d630`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d630.md) · 呼出先 14件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7f0.md) [`00c5a810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)
- 新版 呼出元 1件 [`00c5da30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da30.md) · 呼出先 14件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abf0.md) [`00c5ac10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcaad0",
      "incomplete_value": true,
      "site": "00bcaad4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00bca6a8",
      "incomplete_value": true,
      "site": "00bca6ac",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcaa5c",
      "incomplete_value": true,
      "site": "00bcaa60",
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
      "definition_site": "00bca634",
      "incomplete_value": true,
      "site": "00bca638",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcab48",
      "incomplete_value": false,
      "site": "00bcab50",
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
            "const:c16:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca720",
      "incomplete_value": false,
      "site": "00bca728",
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
            "const:b49:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
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
        "00c9b5a0",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "READ",
      [
        "storage",
        "01126320",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      136,
      "READ",
      [
        "storage",
        "00c9b5a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9b9a0",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "READ",
      [
        "storage",
        "01126720",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      136,
      "READ",
      [
        "storage",
        "00c9b9a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bca628 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5a0:8"]]
+ 00bcaa50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a0:8"]]
- 00bca638 ["INT_ADD", "register:40f0:8", ["const:bca638:8", "const:4:8"]]
+ 00bcaa60 ["INT_ADD", "register:40f0:8", ["const:bcaa60:8", "const:4:8"]]
- 00bca64c ["INT_ADD", "register:40f0:8", ["const:bca64c:8", "const:4:8"]]
+ 00bcaa74 ["INT_ADD", "register:40f0:8", ["const:bcaa74:8", "const:4:8"]]
~~~


### [`00bca9d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca9d4.md) → [`00bcadfc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcadfc.md) _ZN8firebase4auth4Auth3appEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d680`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d680.md) · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5da80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da80.md) · 呼出先 1件 [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcae18",
      "incomplete_value": false,
      "site": "00bcae1c",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca9f0",
      "incomplete_value": false,
      "site": "00bca9f4",
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
            "const:6c8:8"
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
        "002b16c8",
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
        "002b1708",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bca9f0 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00bcae18 ["COPY", "tmp:0:8", ["const:708:8"]]
- 00bca9f4 ["INT_ADD", "register:40f0:8", ["const:bca9f4:8", "const:4:8"]]
+ 00bcae1c ["INT_ADD", "register:40f0:8", ["const:bcae1c:8", "const:4:8"]]
~~~


### [`00bcaa0c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaa0c.md) → [`00bcae34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcae34.md) _ZN8firebase4auth4Auth20AddAuthStateListenerEPNS0_17AuthStateListenerE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5d6f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5daf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5daf0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcafac",
      "incomplete_value": false,
      "site": "00bcafb0",
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
            "const:c6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcab84",
      "incomplete_value": false,
      "site": "00bcab88",
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
            "const:c2c:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      376,
      "PARAM",
      [
        "storage",
        "002b8c2c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      376,
      "PARAM",
      [
        "storage",
        "002b8c6c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcaa48 ["INT_ADD", "register:40f0:8", ["const:bcaa48:8", "const:4:8"]]
+ 00bcae70 ["INT_ADD", "register:40f0:8", ["const:bcae70:8", "const:4:8"]]
- 00bcaacc ["INT_ADD", "register:40f0:8", ["const:bcaacc:8", "const:4:8"]]
+ 00bcaef4 ["INT_ADD", "register:40f0:8", ["const:bcaef4:8", "const:4:8"]]
- 00bcab54 ["INT_ADD", "register:40f0:8", ["const:bcab54:8", "const:4:8"]]
+ 00bcaf7c ["INT_ADD", "register:40f0:8", ["const:bcaf7c:8", "const:4:8"]]
~~~


### [`00bcabdc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcabdc.md) → [`00bcb004`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb004.md) _ZN8firebase4auth4Auth18AddIdTokenListenerEPNS0_15IdTokenListenerE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5d5e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5e0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5d9e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9e0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcb104",
      "incomplete_value": true,
      "site": "00bcb104",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "00bcacdc",
      "incomplete_value": true,
      "site": "00bcacdc",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00bcb170",
      "incomplete_value": true,
      "site": "00bcb170",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcad48",
      "incomplete_value": true,
      "site": "00bcad48",
      "value": [
        "LOAD",
        "8",
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
                "const:10:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcb184",
      "incomplete_value": true,
      "site": "00bcb188",
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
            "const:c6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcad5c",
      "incomplete_value": false,
      "site": "00bcad60",
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
            "const:c2c:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      384,
      "PARAM",
      [
        "storage",
        "002b8c2c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      384,
      "PARAM",
      [
        "storage",
        "002b8c6c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcac04 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
+ 00bcb02c ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
- 00bcac18 ["INT_ADD", "register:40f0:8", ["const:bcac18:8", "const:4:8"]]
+ 00bcb040 ["INT_ADD", "register:40f0:8", ["const:bcb040:8", "const:4:8"]]
- 00bcac9c ["INT_ADD", "register:40f0:8", ["const:bcac9c:8", "const:4:8"]]
+ 00bcb0c4 ["INT_ADD", "register:40f0:8", ["const:bcb0c4:8", "const:4:8"]]
~~~


### [`00bcadb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcadb4.md) → [`00bcb1dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb1dc.md) _ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d670`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d670.md) · 呼出先 2件 [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5da70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da70.md) · 呼出先 2件 [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcb244",
      "incomplete_value": true,
      "site": "00bcb244",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "00bcae1c",
      "incomplete_value": true,
      "site": "00bcae1c",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcb290",
      "incomplete_value": true,
      "site": "00bcb294",
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
              [
                "live",
                "register:4058:8"
              ]
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bcae6c",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcb2a8",
      "incomplete_value": true,
      "site": "00bcb2a8",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "00bcae80",
      "incomplete_value": true,
      "site": "00bcae80",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 0
  }
]
~~~


~~~diff
- 00bcadc8 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
+ 00bcb1f0 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00bcaddc ["INT_ADD", "register:40f0:8", ["const:bcaddc:8", "const:4:8"]]
+ 00bcb204 ["INT_ADD", "register:40f0:8", ["const:bcb204:8", "const:4:8"]]
- 00bcadec ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
+ 00bcb214 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
~~~


### [`00bcaec8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaec8.md) → [`00bcb2f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb2f0.md) _ZN8firebase4auth4Auth21RemoveIdTokenListenerEPNS0_15IdTokenListenerE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d660`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d660.md) · 呼出先 3件 [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5d600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d600.md)
- 新版 呼出元 1件 [`00c5da60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da60.md) · 呼出先 3件 [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5da00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 4件, `call_argument_candidate` 1件, `store_destination` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcb2f8",
      "incomplete_value": true,
      "site": "00bcb2f8",
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
                "const:ffffffffffffffc0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcaed0",
      "incomplete_value": true,
      "site": "00bcaed0",
      "value": [
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
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcb2f8",
      "incomplete_value": true,
      "site": "00bcb2f8",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcaed0",
      "incomplete_value": true,
      "site": "00bcaed0",
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
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcb2fc",
      "incomplete_value": true,
      "site": "00bcb2fc",
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
                "const:ffffffffffffffc0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcaed4",
      "incomplete_value": true,
      "site": "00bcaed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


~~~diff
- 00bcaee0 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
+ 00bcb308 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 00bcaefc ["INT_ADD", "register:40f0:8", ["const:bcaefc:8", "const:4:8"]]
+ 00bcb324 ["INT_ADD", "register:40f0:8", ["const:bcb324:8", "const:4:8"]]
- 00bcafa0 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
+ 00bcb3c8 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
~~~


### [`00bcb024`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb024.md) → [`00bcb44c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb44c.md) _ZN8firebase4auth17AuthStateListenerD1Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5d670`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d670.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5da70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcb46c",
      "incomplete_value": true,
      "site": "00bcb46c",
      "value": [
        "live",
        "register:4000:8"
      ]
    },
    "old": {
      "definition_site": "00bcb044",
      "incomplete_value": true,
      "site": "00bcb044",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcb46c",
      "incomplete_value": true,
      "site": "00bcb46c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb044",
      "incomplete_value": true,
      "site": "00bcb044",
      "value": [
        "live",
        "register:4040:8"
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
      16,
      "READ",
      [
        "storage",
        "00c9b5b8",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c914d8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "00c9b9b8",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c918d8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcb034 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b8:8"]]
+ 00bcb45c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00bcb050 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00bcb478 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00bcb05c ["INT_ADD", "register:40f0:8", ["const:bcb05c:8", "const:4:8"]]
+ 00bcb484 ["INT_ADD", "register:40f0:8", ["const:bcb484:8", "const:4:8"]]
~~~


### [`00bcb098`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb098.md) → [`00bcb4c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb4c0.md) FUN_00bcb4c0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

~~~diff
- 00bcb0a0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bcb4c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
~~~


### [`00bcb0b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb0b4.md) → [`00bcb4dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb4dc.md) _ZN8firebase4auth15IdTokenListenerD1Ev

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5d660`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d660.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5da60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da60.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_value

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcb4fc",
      "incomplete_value": true,
      "site": "00bcb4fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb0d4",
      "incomplete_value": true,
      "site": "00bcb0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      16,
      "READ",
      [
        "storage",
        "00c9b5b0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c91500",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "00c9b9b0",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c91900",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcb0c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 00bcb4ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b0:8"]]
- 00bcb0ec ["INT_ADD", "register:40f0:8", ["const:bcb0ec:8", "const:4:8"]]
+ 00bcb514 ["INT_ADD", "register:40f0:8", ["const:bcb514:8", "const:4:8"]]
~~~


### [`00bcb12c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb12c.md) → [`00bcb554`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb554.md) _ZN8firebase4auth24NotifyAuthStateListenersEPNS0_8AuthDataE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d610.md) · 呼出先 6件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ad30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md)
- 新版 呼出元 1件 [`00c5da10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da10.md) · 呼出先 6件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b130`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcb560",
      "incomplete_value": true,
      "site": "00bcb560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
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
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb138",
      "incomplete_value": true,
      "site": "00bcb138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcb560",
      "incomplete_value": true,
      "site": "00bcb560",
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
      "definition_site": "00bcb138",
      "incomplete_value": true,
      "site": "00bcb138",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcb57c",
      "incomplete_value": true,
      "site": "00bcb57c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
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
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb154",
      "incomplete_value": true,
      "site": "00bcb154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      80,
      "PARAM",
      [
        "storage",
        "002bd3ea",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      80,
      "PARAM",
      [
        "storage",
        "002bd42a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcb158 ["INT_ADD", "register:40f0:8", ["const:bcb158:8", "const:4:8"]]
+ 00bcb580 ["INT_ADD", "register:40f0:8", ["const:bcb580:8", "const:4:8"]]
- 00bcb168 ["INT_ADD", "register:40f0:8", ["const:bcb168:8", "const:4:8"]]
+ 00bcb590 ["INT_ADD", "register:40f0:8", ["const:bcb590:8", "const:4:8"]]
- 00bcb17c ["COPY", "tmp:0:8", ["const:3ea:8"]]
+ 00bcb5a4 ["COPY", "tmp:0:8", ["const:42a:8"]]
~~~


### [`00bcb294`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb294.md) → [`00bcb6bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb6bc.md) _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEEC2ERKS7_

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d700`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d700.md) · 呼出先 3件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`00c5db00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db00.md) · 呼出先 3件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

~~~diff
- 00bcb2b8 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00bcb6e0 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00bcb2c4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bcb6ec ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bcb2cc ["INT_ADD", "register:40f0:8", ["const:bcb2cc:8", "const:4:8"]]
+ 00bcb6f4 ["INT_ADD", "register:40f0:8", ["const:bcb6f4:8", "const:4:8"]]
~~~


### [`00bcb354`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb354.md) → [`00bcb77c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb77c.md) _ZN8firebase4auth22NotifyIdTokenListenersEPNS0_8AuthDataE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d5f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5f0.md) · 呼出先 6件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ad30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md)
- 新版 呼出元 1件 [`00c5d9f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9f0.md) · 呼出先 6件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b130`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcb7cc",
      "incomplete_value": false,
      "site": "00bcb7d0",
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
            "const:1e9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb3a4",
      "incomplete_value": false,
      "site": "00bcb3a8",
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
            "const:10d:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      80,
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      80,
      "PARAM",
      [
        "storage",
        "002a61e9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcb380 ["INT_ADD", "register:40f0:8", ["const:bcb380:8", "const:4:8"]]
+ 00bcb7a8 ["INT_ADD", "register:40f0:8", ["const:bcb7a8:8", "const:4:8"]]
- 00bcb390 ["INT_ADD", "register:40f0:8", ["const:bcb390:8", "const:4:8"]]
+ 00bcb7b8 ["INT_ADD", "register:40f0:8", ["const:bcb7b8:8", "const:4:8"]]
- 00bcb3a4 ["COPY", "tmp:0:8", ["const:10d:8"]]
+ 00bcb7cc ["COPY", "tmp:0:8", ["const:1e9:8"]]
~~~


### [`00bcb4bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb4bc.md) → [`00bcb8e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb8e4.md) _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEEC2ERKS7_

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d6e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6e0.md) · 呼出先 3件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dae0.md) · 呼出先 3件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

~~~diff
- 00bcb4e0 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00bcb908 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00bcb4ec ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00bcb914 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bcb4f4 ["INT_ADD", "register:40f0:8", ["const:bcb4f4:8", "const:4:8"]]
+ 00bcb91c ["INT_ADD", "register:40f0:8", ["const:bcb91c:8", "const:4:8"]]
~~~


### [`00bcb60c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb60c.md) → [`00bcba34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcba34.md) _ZNK8firebase4auth4Auth32SendPasswordResetEmailLastResultEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcba50",
      "incomplete_value": true,
      "site": "00bcba54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              [
                "live",
                "register:4000:8"
              ]
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
      "definition_site": "00bcb628",
      "incomplete_value": true,
      "site": "00bcb62c",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


~~~diff
- 00bcb62c ["INT_ADD", "register:40f0:8", ["const:bcb62c:8", "const:4:8"]]
+ 00bcba54 ["INT_ADD", "register:40f0:8", ["const:bcba54:8", "const:4:8"]]
- 00bcb638 ["INT_ADD", "register:40f0:8", ["const:bcb638:8", "const:4:8"]]
+ 00bcba60 ["INT_ADD", "register:40f0:8", ["const:bcba60:8", "const:4:8"]]
- 00bcb644 ["INT_ADD", "register:40f0:8", ["const:bcb644:8", "const:4:8"]]
+ 00bcba6c ["INT_ADD", "register:40f0:8", ["const:bcba6c:8", "const:4:8"]]
~~~


### [`00bcb69c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb69c.md) → [`00bcbac4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbac4.md) _ZNK8firebase4auth4Auth31SignInWithCustomTokenLastResultEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00bcb6bc ["INT_ADD", "register:40f0:8", ["const:bcb6bc:8", "const:4:8"]]
+ 00bcbae4 ["INT_ADD", "register:40f0:8", ["const:bcbae4:8", "const:4:8"]]
- 00bcb6c8 ["INT_ADD", "register:40f0:8", ["const:bcb6c8:8", "const:4:8"]]
+ 00bcbaf0 ["INT_ADD", "register:40f0:8", ["const:bcbaf0:8", "const:4:8"]]
- 00bcb6d4 ["INT_ADD", "register:40f0:8", ["const:bcb6d4:8", "const:4:8"]]
+ 00bcbafc ["INT_ADD", "register:40f0:8", ["const:bcbafc:8", "const:4:8"]]
~~~


### [`00bcb7bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb7bc.md) → [`00bcbbe4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbbe4.md) _ZNK8firebase4auth4Auth27SignInAnonymouslyLastResultEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bcb800",
      "incomplete_value": true,
      "site": "00bcb804",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


~~~diff
- 00bcb7dc ["INT_ADD", "register:40f0:8", ["const:bcb7dc:8", "const:4:8"]]
+ 00bcbc04 ["INT_ADD", "register:40f0:8", ["const:bcbc04:8", "const:4:8"]]
- 00bcb7e8 ["INT_ADD", "register:40f0:8", ["const:bcb7e8:8", "const:4:8"]]
+ 00bcbc10 ["INT_ADD", "register:40f0:8", ["const:bcbc10:8", "const:4:8"]]
- 00bcb7f4 ["INT_ADD", "register:40f0:8", ["const:bcb7f4:8", "const:4:8"]]
+ 00bcbc1c ["INT_ADD", "register:40f0:8", ["const:bcbc1c:8", "const:4:8"]]
~~~


### [`00bcb84c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb84c.md) → [`00bcbc74`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbc74.md) _ZNK8firebase4auth4Auth36SignInWithEmailAndPasswordLastResultEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00bcb86c ["INT_ADD", "register:40f0:8", ["const:bcb86c:8", "const:4:8"]]
+ 00bcbc94 ["INT_ADD", "register:40f0:8", ["const:bcbc94:8", "const:4:8"]]
- 00bcb878 ["INT_ADD", "register:40f0:8", ["const:bcb878:8", "const:4:8"]]
+ 00bcbca0 ["INT_ADD", "register:40f0:8", ["const:bcbca0:8", "const:4:8"]]
- 00bcb884 ["INT_ADD", "register:40f0:8", ["const:bcb884:8", "const:4:8"]]
+ 00bcbcac ["INT_ADD", "register:40f0:8", ["const:bcbcac:8", "const:4:8"]]
~~~


### [`00bcb8dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb8dc.md) → [`00bcbd04`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbd04.md) _ZNK8firebase4auth4Auth40CreateUserWithEmailAndPasswordLastResultEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bcb8f8",
      "incomplete_value": true,
      "site": "00bcb8fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              [
                "live",
                "register:4000:8"
              ]
            ]
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
    "new": null,
    "old": {
      "definition_site": "00bcb920",
      "incomplete_value": true,
      "site": "00bcb924",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


~~~diff
- 00bcb8fc ["INT_ADD", "register:40f0:8", ["const:bcb8fc:8", "const:4:8"]]
+ 00bcbd24 ["INT_ADD", "register:40f0:8", ["const:bcbd24:8", "const:4:8"]]
- 00bcb908 ["INT_ADD", "register:40f0:8", ["const:bcb908:8", "const:4:8"]]
+ 00bcbd30 ["INT_ADD", "register:40f0:8", ["const:bcbd30:8", "const:4:8"]]
- 00bcb914 ["INT_ADD", "register:40f0:8", ["const:bcb914:8", "const:4:8"]]
+ 00bcbd3c ["INT_ADD", "register:40f0:8", ["const:bcbd3c:8", "const:4:8"]]
~~~


### [`00bcb984`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb984.md) → [`00bcbdac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbdac.md) FUN_00bcbdac

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bca368`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca368.md) · 呼出先 2件 [`00c5a9e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5d630`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d630.md)
- 新版 呼出元 1件 [`00bca790`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca790.md) · 呼出先 2件 [`00c5ade0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) [`00c5da30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcbdc4",
      "incomplete_value": false,
      "site": "00bcbdd0",
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
            "const:c5c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb99c",
      "incomplete_value": false,
      "site": "00bcb9a8",
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
            "const:b8f:8"
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
      24,
      "PARAM",
      [
        "storage",
        "002a3b8f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      24,
      "PARAM",
      [
        "storage",
        "002a3c5c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcb99c ["COPY", "tmp:0:8", ["const:b8f:8"]]
+ 00bcbdc4 ["COPY", "tmp:0:8", ["const:c5c:8"]]
- 00bcb9a8 ["INT_ADD", "register:40f0:8", ["const:bcb9a8:8", "const:4:8"]]
+ 00bcbdd0 ["INT_ADD", "register:40f0:8", ["const:bcbdd0:8", "const:4:8"]]
~~~


### [`00bcb9bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9bc.md) → [`00bcbde4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbde4.md) _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d6c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6c0.md) · 呼出先 2件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5d6c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6c0.md)
- 新版 呼出元 1件 [`00c5dac0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dac0.md) · 呼出先 2件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5dac0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dac0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcbdf8",
      "incomplete_value": true,
      "site": "00bcbe00",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4008:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  }
]
~~~


~~~diff
- 00bcb9bc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bcbde4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcb9d8 ["INT_ADD", "register:40f0:8", ["const:bcb9d8:8", "const:4:8"]]
+ 00bcbe00 ["INT_ADD", "register:40f0:8", ["const:bcbe00:8", "const:4:8"]]
- 00bcb9e4 ["INT_ADD", "register:40f0:8", ["const:bcb9e4:8", "const:4:8"]]
+ 00bcbe0c ["INT_ADD", "register:40f0:8", ["const:bcbe0c:8", "const:4:8"]]
~~~


### [`00bcb9fc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9fc.md) → [`00bcbe24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbe24.md) _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d6f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6f0.md) · 呼出先 5件 [`00b3fe98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`00c5daf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5daf0.md) · 呼出先 5件 [`00b402c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcbe78",
      "incomplete_value": true,
      "site": "00bcbe78",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:102:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcba50",
      "incomplete_value": true,
      "site": "00bcba50",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              [
                "live",
                "register:4040:8"
              ],
              "INT_SRIGHT"
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
      "definition_site": "00bcbe8c",
      "incomplete_value": false,
      "site": "00bcbe90",
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
            "const:67b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcba64",
      "incomplete_value": false,
      "site": "00bcba68",
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
            "const:5ae:8"
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
      104,
      "PARAM",
      [
        "storage",
        "002a85ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      104,
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcba2c ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00bcbe54 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00bcba44 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bcbe6c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bcba54 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00bcbe7c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
~~~


### [`00bcbaf4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbaf4.md) → [`00bcbf1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbf1c.md) _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d710`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d710.md) · 呼出先 5件 [`00b3fe98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`00c5db10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db10.md) · 呼出先 5件 [`00b402c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcbf2c",
      "incomplete_value": true,
      "site": "00bcbf2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbb04",
      "incomplete_value": true,
      "site": "00bcbb04",
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
                "const:ffffffffffffffb0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:40:8"
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
      "definition_site": "00bcbf2c",
      "incomplete_value": true,
      "site": "00bcbf2c",
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
      "definition_site": "00bcbb04",
      "incomplete_value": true,
      "site": "00bcbb04",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcbfb0",
      "incomplete_value": true,
      "site": "00bcbfb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "INT_SLESS",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "INT_SBORROW",
            "1",
            [
              [
                "live",
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbb88",
      "incomplete_value": true,
      "site": "00bcbb88",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "live",
            "register:100:1"
          ],
          [
            "live",
            "register:103:1"
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
      104,
      "PARAM",
      [
        "storage",
        "002a85ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      104,
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcbb24 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00bcbf4c ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00bcbb3c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bcbf64 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bcbb4c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00bcbf74 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
~~~


### [`00bcbbec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbbec.md) → [`00bcc014`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc014.md) _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d6d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6d0.md) · 呼出先 5件 [`00b3fe98`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`00c5dad0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dad0.md) · 呼出先 5件 [`00b402c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc0a4",
      "incomplete_value": true,
      "site": "00bcc0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              [
                "live",
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:3:4"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbc7c",
      "incomplete_value": true,
      "site": "00bcbc7c",
      "value": [
        "live",
        "register:40c0:8"
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcc0a4",
      "incomplete_value": true,
      "site": "00bcc0a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:40b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbc7c",
      "incomplete_value": true,
      "site": "00bcbc7c",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc0a8",
      "incomplete_value": true,
      "site": "00bcc0a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "INT_SLESS",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "INT_SBORROW",
            "1",
            [
              [
                "live",
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbc80",
      "incomplete_value": true,
      "site": "00bcbc80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "live",
            "register:100:1"
          ],
          [
            "live",
            "register:103:1"
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
      104,
      "PARAM",
      [
        "storage",
        "002a85ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      104,
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcbc1c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00bcc044 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00bcbc44 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00bcc06c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00bcbc54 ["COPY", "tmp:0:8", ["const:5ae:8"]]
+ 00bcc07c ["COPY", "tmp:0:8", ["const:67b:8"]]
~~~


### [`00bcbce4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbce4.md) → [`00bcc10c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc10c.md) _INIT_290

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bca0a8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0a8.md) [`00bca0b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0b0.md) [`00bca0b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0b4.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bca4d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4d0.md) [`00bca4d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4d8.md) [`00bca4dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4dc.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 7件, `store_value` 4件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc138",
      "incomplete_value": false,
      "site": "00bcc138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbd10",
      "incomplete_value": false,
      "site": "00bcbd10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcc138",
      "incomplete_value": false,
      "site": "00bcc138",
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
            "const:10a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbd10",
      "incomplete_value": false,
      "site": "00bcbd10",
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
            "const:ca:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc138",
      "incomplete_value": false,
      "site": "00bcc138",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:6e8:8"
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
      "definition_site": "00bcbd10",
      "incomplete_value": false,
      "site": "00bcbd10",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:2e8:8"
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
    "ordinal": 5,
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
        "011262e8",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011262e8",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "002bc0ca",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "002bc10a",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcbd00 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00bcc128 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 00bcbd04 ["COPY", "tmp:0:8", ["const:ca:8"]]
+ 00bcc12c ["COPY", "tmp:0:8", ["const:10a:8"]]
- 00bcbd08 ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 00bcc130 ["COPY", "tmp:0:8", ["const:4d0:8"]]
~~~


### [`00bcbd8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbd8c.md) → [`00bcc1b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc1b4.md) _ZN8firebase4auth23GetCredentialFutureImplEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d750`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d750.md) · 呼出先 1件 [`00c5b930`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b930.md)
- 新版 呼出元 1件 [`00c5db50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db50.md) · 呼出先 1件 [`00c5bd30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd30.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      4,
      "PARAM",
      [
        "storage",
        "0030f023",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      4,
      "PARAM",
      [
        "storage",
        "0030f063",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcbd90 ["COPY", "tmp:0:8", ["const:23:8"]]
+ 00bcc1b8 ["COPY", "tmp:0:8", ["const:63:8"]]
~~~


### [`00bcbda8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbda8.md) → [`00bcc1d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc1d0.md) _ZN8firebase4auth14ClearUserInfosEPNS0_8AuthDataE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d5a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5a0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5d9a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9a0.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00bcbe04 ["INT_ADD", "register:40f0:8", ["const:bcbe04:8", "const:4:8"]]
+ 00bcc22c ["INT_ADD", "register:40f0:8", ["const:bcc22c:8", "const:4:8"]]
~~~


### [`00bcbee4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbee4.md) → [`00bcc30c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc30c.md) _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc338",
      "incomplete_value": true,
      "site": "00bcc338",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbf10",
      "incomplete_value": true,
      "site": "00bcbf10",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc320",
      "incomplete_value": true,
      "site": "00bcc320",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcbef8",
      "incomplete_value": true,
      "site": "00bcbef8",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc32c",
      "incomplete_value": false,
      "site": "00bcc330",
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
            "const:23c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbf04",
      "incomplete_value": false,
      "site": "00bcbf08",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcbef4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
+ 00bcc31c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00bcbf04 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00bcc32c ["COPY", "tmp:0:8", ["const:23c:8"]]
- 00bcbf08 ["INT_ADD", "register:40f0:8", ["const:bcbf08:8", "const:4:8"]]
+ 00bcc330 ["INT_ADD", "register:40f0:8", ["const:bcc330:8", "const:4:8"]]
~~~


### [`00bcbf24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf24.md) → [`00bcc34c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc34c.md) _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc378",
      "incomplete_value": true,
      "site": "00bcc378",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbf50",
      "incomplete_value": true,
      "site": "00bcbf50",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc360",
      "incomplete_value": true,
      "site": "00bcc360",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcbf38",
      "incomplete_value": true,
      "site": "00bcbf38",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc368",
      "incomplete_value": false,
      "site": "00bcc370",
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
            "const:23c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbf40",
      "incomplete_value": false,
      "site": "00bcbf48",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcbf34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
+ 00bcc35c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00bcbf40 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00bcc368 ["COPY", "tmp:0:8", ["const:23c:8"]]
- 00bcbf48 ["INT_ADD", "register:40f0:8", ["const:bcbf48:8", "const:4:8"]]
+ 00bcc370 ["INT_ADD", "register:40f0:8", ["const:bcc370:8", "const:4:8"]]
~~~


### [`00bcbf64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf64.md) → [`00bcc38c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc38c.md) _ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc3bc",
      "incomplete_value": true,
      "site": "00bcc3bc",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbf94",
      "incomplete_value": true,
      "site": "00bcbf94",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc3a0",
      "incomplete_value": true,
      "site": "00bcc3a0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcbf78",
      "incomplete_value": true,
      "site": "00bcbf78",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc3ac",
      "incomplete_value": false,
      "site": "00bcc3b4",
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
            "const:23c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbf84",
      "incomplete_value": false,
      "site": "00bcbf8c",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcbf74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
+ 00bcc39c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00bcbf78 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bcc3a0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcbf84 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00bcc3ac ["COPY", "tmp:0:8", ["const:23c:8"]]
~~~


### [`00bcbfa8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbfa8.md) → [`00bcc3d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc3d0.md) _ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc400",
      "incomplete_value": true,
      "site": "00bcc400",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbfd8",
      "incomplete_value": true,
      "site": "00bcbfd8",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc3e4",
      "incomplete_value": true,
      "site": "00bcc3e4",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcbfbc",
      "incomplete_value": true,
      "site": "00bcbfbc",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc3ec",
      "incomplete_value": false,
      "site": "00bcc3f8",
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
            "const:23c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbfc4",
      "incomplete_value": false,
      "site": "00bcbfd0",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcbfb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
+ 00bcc3e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00bcbfc4 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00bcc3ec ["COPY", "tmp:0:8", ["const:23c:8"]]
- 00bcbfd0 ["INT_ADD", "register:40f0:8", ["const:bcbfd0:8", "const:4:8"]]
+ 00bcc3f8 ["INT_ADD", "register:40f0:8", ["const:bcc3f8:8", "const:4:8"]]
~~~


### [`00bcbfec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbfec.md) → [`00bcc414`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc414.md) _ZN8firebase4auth4auth8GetClassEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00bcbff0",
      "incomplete_value": true,
      "site": "00bcbff4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:328:8"
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
      4,
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      4,
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcbff0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:328:8"]]
+ 00bcc418 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:728:8"]]
~~~


### [`00bcbff8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbff8.md) → [`00bcc420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc420.md) _ZN8firebase4auth4auth15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc478",
      "incomplete_value": true,
      "site": "00bcc478",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc050",
      "incomplete_value": true,
      "site": "00bcc050",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc454",
      "incomplete_value": true,
      "site": "00bcc460",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "old": {
      "definition_site": "00bcc02c",
      "incomplete_value": true,
      "site": "00bcc038",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:328:8"
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
      "definition_site": "00bcc468",
      "incomplete_value": true,
      "site": "00bcc46c",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
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
        "01126330",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126330",
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
        "01126730",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc00c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:330:8"]]
+ 00bcc434 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:730:8"]]
- 00bcc018 ["BRANCH", null, ["local:b4:8"]]
+ 00bcc440 ["BRANCH", null, ["local:b3:8"]]
- 00bcc02c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:328:8"]]
+ 00bcc454 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
~~~


### [`00bcc064`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc064.md) → [`00bcc48c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc48c.md) _ZN8firebase4auth4auth12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc4c8",
      "incomplete_value": true,
      "site": "00bcc4c8",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc0a0",
      "incomplete_value": true,
      "site": "00bcc0a0",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc4e8",
      "incomplete_value": true,
      "site": "00bcc4e8",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc0c0",
      "incomplete_value": true,
      "site": "00bcc0c0",
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
            "const:328:8"
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
      "definition_site": "00bcc4a4",
      "incomplete_value": true,
      "site": "00bcc4a4",
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
      "definition_site": "00bcc07c",
      "incomplete_value": true,
      "site": "00bcc07c",
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
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126330",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126330",
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
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc078 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
+ 00bcc4a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00bcc084 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:330:8"]]
+ 00bcc4ac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:730:8"]]
- 00bcc09c ["INT_ADD", "register:40f0:8", ["const:bcc09c:8", "const:4:8"]]
+ 00bcc4c4 ["INT_ADD", "register:40f0:8", ["const:bcc4c4:8", "const:4:8"]]
~~~


### [`00bcc0d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc0d4.md) → [`00bcc4fc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc4fc.md) _ZN8firebase4auth4auth14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc500",
      "incomplete_value": true,
      "site": "00bcc500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc0d8",
      "incomplete_value": true,
      "site": "00bcc0d8",
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
                "const:ffffffffffffffe0:8"
              ]
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
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc500",
      "incomplete_value": true,
      "site": "00bcc500",
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
                "const:10:8"
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
      "definition_site": "00bcc0d8",
      "incomplete_value": true,
      "site": "00bcc0d8",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc53c",
      "incomplete_value": true,
      "site": "00bcc53c",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc114",
      "incomplete_value": true,
      "site": "00bcc114",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
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
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126328",
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
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc0e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
+ 00bcc510 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00bcc0f0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bcc518 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc0f8 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00bcc520 ["COPY", "tmp:0:8", ["const:23c:8"]]
~~~


### [`00bcc144`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc144.md) → [`00bcc56c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc56c.md) _ZN8firebase4auth4auth11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc588",
      "incomplete_value": false,
      "site": "00bcc58c",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc160",
      "incomplete_value": false,
      "site": "00bcc164",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bcc598",
      "incomplete_value": true,
      "site": "00bcc5a4",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc170",
      "incomplete_value": true,
      "site": "00bcc17c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc160 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bcc588 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bcc164 ["INT_ADD", "register:40f0:8", ["const:bcc164:8", "const:4:8"]]
+ 00bcc58c ["INT_ADD", "register:40f0:8", ["const:bcc58c:8", "const:4:8"]]
- 00bcc16c ["COPY", "tmp:0:8", ["const:338:8"]]
+ 00bcc594 ["COPY", "tmp:0:8", ["const:738:8"]]
~~~


### [`00bcc180`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc180.md) → [`00bcc5a8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc5a8.md) _ZN8firebase4auth4auth13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc5e8",
      "incomplete_value": true,
      "site": "00bcc5e8",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc1c0",
      "incomplete_value": true,
      "site": "00bcc1c0",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc5c4",
      "incomplete_value": true,
      "site": "00bcc5c4",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc19c",
      "incomplete_value": true,
      "site": "00bcc19c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "live",
            "register:4008:8"
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
    "new": null,
    "old": {
      "definition_site": "00bcc1a4",
      "incomplete_value": false,
      "site": "00bcc1b8",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
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
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126328",
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
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc194 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
+ 00bcc5bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00bcc1a4 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00bcc5cc ["COPY", "tmp:0:8", ["const:23c:8"]]
- 00bcc1b8 ["INT_ADD", "register:40f0:8", ["const:bcc1b8:8", "const:4:8"]]
+ 00bcc5e0 ["INT_ADD", "register:40f0:8", ["const:bcc5e0:8", "const:4:8"]]
~~~


### [`00bcc1f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc1f0.md) → [`00bcc618`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc618.md) _ZN8firebase4auth4auth10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc634",
      "incomplete_value": false,
      "site": "00bcc638",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc20c",
      "incomplete_value": false,
      "site": "00bcc210",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bcc644",
      "incomplete_value": true,
      "site": "00bcc650",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "011263c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "011267c8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc20c ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bcc634 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bcc210 ["INT_ADD", "register:40f0:8", ["const:bcc210:8", "const:4:8"]]
+ 00bcc638 ["INT_ADD", "register:40f0:8", ["const:bcc638:8", "const:4:8"]]
- 00bcc218 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 00bcc640 ["COPY", "tmp:0:8", ["const:7c8:8"]]
~~~


### [`00bcc22c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc22c.md) → [`00bcc654`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc654.md) _ZN8firebase4auth17signinmethodquery19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc680",
      "incomplete_value": true,
      "site": "00bcc680",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc258",
      "incomplete_value": true,
      "site": "00bcc258",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc668",
      "incomplete_value": true,
      "site": "00bcc668",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc240",
      "incomplete_value": true,
      "site": "00bcc240",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc674",
      "incomplete_value": false,
      "site": "00bcc678",
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
            "const:cc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc24c",
      "incomplete_value": false,
      "site": "00bcc250",
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
            "const:bf5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc23c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d0:8"]]
+ 00bcc664 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bcc24c ["COPY", "tmp:0:8", ["const:bf5:8"]]
+ 00bcc674 ["COPY", "tmp:0:8", ["const:cc2:8"]]
- 00bcc250 ["INT_ADD", "register:40f0:8", ["const:bcc250:8", "const:4:8"]]
+ 00bcc678 ["INT_ADD", "register:40f0:8", ["const:bcc678:8", "const:4:8"]]
~~~


### [`00bcc26c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc26c.md) → [`00bcc694`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc694.md) _ZN8firebase4auth17signinmethodquery19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc6c0",
      "incomplete_value": true,
      "site": "00bcc6c0",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc298",
      "incomplete_value": true,
      "site": "00bcc298",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc6a8",
      "incomplete_value": true,
      "site": "00bcc6a8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc280",
      "incomplete_value": true,
      "site": "00bcc280",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc6b0",
      "incomplete_value": false,
      "site": "00bcc6b8",
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
            "const:cc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc288",
      "incomplete_value": false,
      "site": "00bcc290",
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
            "const:bf5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc27c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d0:8"]]
+ 00bcc6a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bcc288 ["COPY", "tmp:0:8", ["const:bf5:8"]]
+ 00bcc6b0 ["COPY", "tmp:0:8", ["const:cc2:8"]]
- 00bcc290 ["INT_ADD", "register:40f0:8", ["const:bcc290:8", "const:4:8"]]
+ 00bcc6b8 ["INT_ADD", "register:40f0:8", ["const:bcc6b8:8", "const:4:8"]]
~~~


### [`00bcc2ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2ac.md) → [`00bcc6d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc6d4.md) _ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc704",
      "incomplete_value": true,
      "site": "00bcc704",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc2dc",
      "incomplete_value": true,
      "site": "00bcc2dc",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc6e8",
      "incomplete_value": true,
      "site": "00bcc6e8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc2c0",
      "incomplete_value": true,
      "site": "00bcc2c0",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc6f4",
      "incomplete_value": false,
      "site": "00bcc6fc",
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
            "const:cc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc2cc",
      "incomplete_value": false,
      "site": "00bcc2d4",
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
            "const:bf5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc2bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d0:8"]]
+ 00bcc6e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bcc2cc ["COPY", "tmp:0:8", ["const:bf5:8"]]
+ 00bcc6f4 ["COPY", "tmp:0:8", ["const:cc2:8"]]
- 00bcc2d4 ["INT_ADD", "register:40f0:8", ["const:bcc2d4:8", "const:4:8"]]
+ 00bcc6fc ["INT_ADD", "register:40f0:8", ["const:bcc6fc:8", "const:4:8"]]
~~~


### [`00bcc2f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2f0.md) → [`00bcc718`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc718.md) _ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc748",
      "incomplete_value": true,
      "site": "00bcc748",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc320",
      "incomplete_value": true,
      "site": "00bcc320",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc72c",
      "incomplete_value": true,
      "site": "00bcc72c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc304",
      "incomplete_value": true,
      "site": "00bcc304",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "live",
            "register:4040:8"
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
    "new": null,
    "old": {
      "definition_site": "00bcc30c",
      "incomplete_value": false,
      "site": "00bcc318",
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
            "const:bf5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc300 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d0:8"]]
+ 00bcc728 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bcc30c ["COPY", "tmp:0:8", ["const:bf5:8"]]
+ 00bcc734 ["COPY", "tmp:0:8", ["const:cc2:8"]]
- 00bcc318 ["INT_ADD", "register:40f0:8", ["const:bcc318:8", "const:4:8"]]
+ 00bcc740 ["INT_ADD", "register:40f0:8", ["const:bcc740:8", "const:4:8"]]
~~~


### [`00bcc340`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc340.md) → [`00bcc768`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc768.md) _ZN8firebase4auth17signinmethodquery15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc7c0",
      "incomplete_value": true,
      "site": "00bcc7c0",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc398",
      "incomplete_value": true,
      "site": "00bcc398",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc79c",
      "incomplete_value": true,
      "site": "00bcc7a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "old": {
      "definition_site": "00bcc374",
      "incomplete_value": true,
      "site": "00bcc380",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:3d0:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "011263d8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "011263d8",
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
        "011267d8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc354 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3d8:8"]]
+ 00bcc77c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7d8:8"]]
- 00bcc360 ["BRANCH", null, ["local:b3:8"]]
+ 00bcc788 ["BRANCH", null, ["local:b4:8"]]
- 00bcc374 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3d0:8"]]
+ 00bcc79c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7d0:8"]]
~~~


### [`00bcc3ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc3ac.md) → [`00bcc7d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc7d4.md) _ZN8firebase4auth17signinmethodquery12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc810",
      "incomplete_value": true,
      "site": "00bcc810",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc3e8",
      "incomplete_value": true,
      "site": "00bcc3e8",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc830",
      "incomplete_value": true,
      "site": "00bcc830",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc408",
      "incomplete_value": true,
      "site": "00bcc408",
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
            "const:3d0:8"
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
      "definition_site": "00bcc7ec",
      "incomplete_value": true,
      "site": "00bcc7ec",
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
      "definition_site": "00bcc3c4",
      "incomplete_value": true,
      "site": "00bcc3c4",
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
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "011263d8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "011263d8",
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
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc3c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d0:8"]]
+ 00bcc7e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00bcc3c4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bcc7ec ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bcc3cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3d8:8"]]
+ 00bcc7f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7d8:8"]]
~~~


### [`00bcc41c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc41c.md) → [`00bcc844`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc844.md) _ZN8firebase4auth17signinmethodquery14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc884",
      "incomplete_value": true,
      "site": "00bcc884",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc45c",
      "incomplete_value": true,
      "site": "00bcc45c",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc860",
      "incomplete_value": true,
      "site": "00bcc860",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc438",
      "incomplete_value": true,
      "site": "00bcc438",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc868",
      "incomplete_value": false,
      "site": "00bcc87c",
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
            "const:cc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc440",
      "incomplete_value": false,
      "site": "00bcc454",
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
            "const:bf5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
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
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011263d0",
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
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc430 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d0:8"]]
+ 00bcc858 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00bcc440 ["COPY", "tmp:0:8", ["const:bf5:8"]]
+ 00bcc868 ["COPY", "tmp:0:8", ["const:cc2:8"]]
- 00bcc454 ["INT_ADD", "register:40f0:8", ["const:bcc454:8", "const:4:8"]]
+ 00bcc87c ["INT_ADD", "register:40f0:8", ["const:bcc87c:8", "const:4:8"]]
~~~


### [`00bcc48c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc48c.md) → [`00bcc8b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc8b4.md) _ZN8firebase4auth17signinmethodquery11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc8d0",
      "incomplete_value": false,
      "site": "00bcc8d4",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc4a8",
      "incomplete_value": false,
      "site": "00bcc4ac",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bcc8e0",
      "incomplete_value": true,
      "site": "00bcc8ec",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc4b8",
      "incomplete_value": true,
      "site": "00bcc4c4",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "011263e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "011267e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc4a8 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bcc8d0 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bcc4ac ["INT_ADD", "register:40f0:8", ["const:bcc4ac:8", "const:4:8"]]
+ 00bcc8d4 ["INT_ADD", "register:40f0:8", ["const:bcc8d4:8", "const:4:8"]]
- 00bcc4b4 ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 00bcc8dc ["COPY", "tmp:0:8", ["const:7e0:8"]]
~~~


### [`00bcc4c8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc4c8.md) → [`00bcc8f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc8f0.md) _ZN8firebase4auth17signinmethodquery13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc930",
      "incomplete_value": true,
      "site": "00bcc930",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc508",
      "incomplete_value": true,
      "site": "00bcc508",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc90c",
      "incomplete_value": true,
      "site": "00bcc90c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc4e4",
      "incomplete_value": true,
      "site": "00bcc4e4",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc914",
      "incomplete_value": false,
      "site": "00bcc928",
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
            "const:cc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc4ec",
      "incomplete_value": false,
      "site": "00bcc500",
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
            "const:bf5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
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
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011263d0",
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
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc4dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d0:8"]]
+ 00bcc904 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00bcc4ec ["COPY", "tmp:0:8", ["const:bf5:8"]]
+ 00bcc914 ["COPY", "tmp:0:8", ["const:cc2:8"]]
- 00bcc500 ["INT_ADD", "register:40f0:8", ["const:bcc500:8", "const:4:8"]]
+ 00bcc928 ["INT_ADD", "register:40f0:8", ["const:bcc928:8", "const:4:8"]]
~~~


### [`00bcc538`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc538.md) → [`00bcc960`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc960.md) _ZN8firebase4auth17signinmethodquery10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc964",
      "incomplete_value": true,
      "site": "00bcc964",
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
                "const:ffffffffffffffe0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc53c",
      "incomplete_value": true,
      "site": "00bcc53c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc964",
      "incomplete_value": true,
      "site": "00bcc964",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc53c",
      "incomplete_value": true,
      "site": "00bcc53c",
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
                "const:10:8"
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc97c",
      "incomplete_value": false,
      "site": "00bcc980",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc554",
      "incomplete_value": false,
      "site": "00bcc558",
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
            "const:451:8"
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
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "011263e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "011267e8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc554 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bcc97c ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bcc558 ["INT_ADD", "register:40f0:8", ["const:bcc558:8", "const:4:8"]]
+ 00bcc980 ["INT_ADD", "register:40f0:8", ["const:bcc980:8", "const:4:8"]]
- 00bcc560 ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 00bcc988 ["COPY", "tmp:0:8", ["const:7e8:8"]]
~~~


### [`00bcc574`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc574.md) → [`00bcc99c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc99c.md) _ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc9c8",
      "incomplete_value": true,
      "site": "00bcc9c8",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc5a0",
      "incomplete_value": true,
      "site": "00bcc5a0",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc9b0",
      "incomplete_value": true,
      "site": "00bcc9b0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc588",
      "incomplete_value": true,
      "site": "00bcc588",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc9bc",
      "incomplete_value": false,
      "site": "00bcc9c0",
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
            "const:bda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc594",
      "incomplete_value": false,
      "site": "00bcc598",
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
            "const:b9a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b5b9a",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b5bda",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc584 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00bcc9ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f0:8"]]
- 00bcc594 ["COPY", "tmp:0:8", ["const:b9a:8"]]
+ 00bcc9bc ["COPY", "tmp:0:8", ["const:bda:8"]]
- 00bcc598 ["INT_ADD", "register:40f0:8", ["const:bcc598:8", "const:4:8"]]
+ 00bcc9c0 ["INT_ADD", "register:40f0:8", ["const:bcc9c0:8", "const:4:8"]]
~~~


### [`00bcc5b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5b4.md) → [`00bcc9dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc9dc.md) _ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcca08",
      "incomplete_value": true,
      "site": "00bcca08",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc5e0",
      "incomplete_value": true,
      "site": "00bcc5e0",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc9f0",
      "incomplete_value": true,
      "site": "00bcc9f0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc5c8",
      "incomplete_value": true,
      "site": "00bcc5c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "live",
            "register:4040:8"
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
      "definition_site": "00bcc9f8",
      "incomplete_value": false,
      "site": "00bcca00",
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
            "const:bda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc5d0",
      "incomplete_value": false,
      "site": "00bcc5d8",
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
            "const:b9a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b5b9a",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b5bda",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc5c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00bcc9ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f0:8"]]
- 00bcc5c8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bcc9f0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcc5d0 ["COPY", "tmp:0:8", ["const:b9a:8"]]
+ 00bcc9f8 ["COPY", "tmp:0:8", ["const:bda:8"]]
~~~


### [`00bcc5f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5f4.md) → [`00bcca1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcca1c.md) _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcca4c",
      "incomplete_value": true,
      "site": "00bcca4c",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc624",
      "incomplete_value": true,
      "site": "00bcc624",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcca30",
      "incomplete_value": true,
      "site": "00bcca30",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc608",
      "incomplete_value": true,
      "site": "00bcc608",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcca3c",
      "incomplete_value": true,
      "site": "00bcca44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:bda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc614",
      "incomplete_value": false,
      "site": "00bcc61c",
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
            "const:b9a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b5b9a",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b5bda",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc604 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00bcca2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f0:8"]]
- 00bcc608 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bcca30 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bcc614 ["COPY", "tmp:0:8", ["const:b9a:8"]]
+ 00bcca3c ["COPY", "tmp:0:8", ["const:bda:8"]]
~~~


### [`00bcc638`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc638.md) → [`00bcca60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcca60.md) _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcca90",
      "incomplete_value": true,
      "site": "00bcca90",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc668",
      "incomplete_value": true,
      "site": "00bcc668",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcca74",
      "incomplete_value": true,
      "site": "00bcca74",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc64c",
      "incomplete_value": true,
      "site": "00bcc64c",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcca7c",
      "incomplete_value": false,
      "site": "00bcca88",
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
            "const:bda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc654",
      "incomplete_value": false,
      "site": "00bcc660",
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
            "const:b9a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b5b9a",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b5bda",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc648 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00bcca70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f0:8"]]
- 00bcc654 ["COPY", "tmp:0:8", ["const:b9a:8"]]
+ 00bcca7c ["COPY", "tmp:0:8", ["const:bda:8"]]
- 00bcc660 ["INT_ADD", "register:40f0:8", ["const:bcc660:8", "const:4:8"]]
+ 00bcca88 ["INT_ADD", "register:40f0:8", ["const:bcca88:8", "const:4:8"]]
~~~


### [`00bcc688`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc688.md) → [`00bccab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccab0.md) _ZN8firebase4auth11jnilistener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_destination` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccab4",
      "incomplete_value": true,
      "site": "00bccab4",
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
                "const:ffffffffffffffd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc68c",
      "incomplete_value": true,
      "site": "00bcc68c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccab4",
      "incomplete_value": true,
      "site": "00bccab4",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc68c",
      "incomplete_value": true,
      "site": "00bcc68c",
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
                "const:10:8"
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccab8",
      "incomplete_value": true,
      "site": "00bccab8",
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
                "const:ffffffffffffffd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc690",
      "incomplete_value": true,
      "site": "00bcc690",
      "value": [
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
      ]
    },
    "ordinal": 3,
    "slot": 1
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
        "011263f8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "011263f8",
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
        "011267f8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "011267f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc69c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3f8:8"]]
+ 00bccac4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7f8:8"]]
- 00bcc6a0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bccac8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcc6a8 ["BRANCH", null, ["local:b4:8"]]
+ 00bccad0 ["BRANCH", null, ["local:b5:8"]]
~~~


### [`00bcc6f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc6f4.md) → [`00bccb1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccb1c.md) _ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccb58",
      "incomplete_value": true,
      "site": "00bccb58",
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
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc730",
      "incomplete_value": true,
      "site": "00bcc730",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccb78",
      "incomplete_value": true,
      "site": "00bccb78",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc750",
      "incomplete_value": true,
      "site": "00bcc750",
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
            "const:3f0:8"
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
      "definition_site": "00bccb34",
      "incomplete_value": true,
      "site": "00bccb34",
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
      "definition_site": "00bcc70c",
      "incomplete_value": true,
      "site": "00bcc70c",
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
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "011263f8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "011263f8",
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
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "011267f8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "011267f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc708 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f0:8"]]
+ 00bccb30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f0:8"]]
- 00bcc714 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3f8:8"]]
+ 00bccb3c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7f8:8"]]
- 00bcc72c ["INT_ADD", "register:40f0:8", ["const:bcc72c:8", "const:4:8"]]
+ 00bccb54 ["INT_ADD", "register:40f0:8", ["const:bccb54:8", "const:4:8"]]
~~~


### [`00bcc764`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc764.md) → [`00bccb8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccb8c.md) _ZN8firebase4auth11jnilistener14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccbcc",
      "incomplete_value": true,
      "site": "00bccbcc",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc7a4",
      "incomplete_value": true,
      "site": "00bcc7a4",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bccba8",
      "incomplete_value": true,
      "site": "00bccba8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc780",
      "incomplete_value": true,
      "site": "00bcc780",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bcc78c",
      "incomplete_value": true,
      "site": "00bcc79c",
      "value": [
        "live",
        "register:4098:8"
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
      20,
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b5b9a",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011263f0",
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
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b5bda",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc778 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f0:8"]]
+ 00bccba0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f0:8"]]
- 00bcc788 ["COPY", "tmp:0:8", ["const:b9a:8"]]
+ 00bccbb0 ["COPY", "tmp:0:8", ["const:bda:8"]]
- 00bcc79c ["INT_ADD", "register:40f0:8", ["const:bcc79c:8", "const:4:8"]]
+ 00bccbc4 ["INT_ADD", "register:40f0:8", ["const:bccbc4:8", "const:4:8"]]
~~~


### [`00bcc7d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc7d4.md) → [`00bccbfc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccbfc.md) _ZN8firebase4auth11jnilistener11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bccc18",
      "incomplete_value": false,
      "site": "00bccc1c",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc7f0",
      "incomplete_value": false,
      "site": "00bcc7f4",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00bcc800",
      "incomplete_value": true,
      "site": "00bcc80c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126400",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc7f0 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bccc18 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bcc7f4 ["INT_ADD", "register:40f0:8", ["const:bcc7f4:8", "const:4:8"]]
+ 00bccc1c ["INT_ADD", "register:40f0:8", ["const:bccc1c:8", "const:4:8"]]
- 00bcc7fc ["COPY", "tmp:0:8", ["const:400:8"]]
+ 00bccc24 ["COPY", "tmp:0:8", ["const:800:8"]]
~~~


### [`00bcc810`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc810.md) → [`00bccc38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccc38.md) _ZN8firebase4auth11jnilistener13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_condition` 1件, `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccc3c",
      "incomplete_value": true,
      "site": "00bccc3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc814",
      "incomplete_value": true,
      "site": "00bcc814",
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
                "const:ffffffffffffffe0:8"
              ]
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
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccc3c",
      "incomplete_value": true,
      "site": "00bccc3c",
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
                "const:10:8"
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
      "definition_site": "00bcc814",
      "incomplete_value": true,
      "site": "00bcc814",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccc78",
      "incomplete_value": true,
      "site": "00bccc78",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc850",
      "incomplete_value": true,
      "site": "00bcc850",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
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
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b5b9a",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011263f0",
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
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b5bda",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc824 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f0:8"]]
+ 00bccc4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f0:8"]]
- 00bcc82c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bccc54 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc834 ["COPY", "tmp:0:8", ["const:b9a:8"]]
+ 00bccc5c ["COPY", "tmp:0:8", ["const:bda:8"]]
~~~


### [`00bcc880`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc880.md) → [`00bccca8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccca8.md) _ZN8firebase4auth11jnilistener10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcccc4",
      "incomplete_value": false,
      "site": "00bcccc8",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc89c",
      "incomplete_value": false,
      "site": "00bcc8a0",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bcccd4",
      "incomplete_value": true,
      "site": "00bccce0",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc8ac",
      "incomplete_value": true,
      "site": "00bcc8b8",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126410",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126810",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc89c ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bcccc4 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bcc8a0 ["INT_ADD", "register:40f0:8", ["const:bcc8a0:8", "const:4:8"]]
+ 00bcccc8 ["INT_ADD", "register:40f0:8", ["const:bcccc8:8", "const:4:8"]]
- 00bcc8a8 ["COPY", "tmp:0:8", ["const:410:8"]]
+ 00bcccd0 ["COPY", "tmp:0:8", ["const:810:8"]]
~~~


### [`00bcc8bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc8bc.md) → [`00bccce4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccce4.md) _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, return_value_candidate, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccd10",
      "incomplete_value": true,
      "site": "00bccd10",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc8e8",
      "incomplete_value": true,
      "site": "00bcc8e8",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcccf8",
      "incomplete_value": true,
      "site": "00bcccf8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc8d0",
      "incomplete_value": true,
      "site": "00bcc8d0",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bccd04",
      "incomplete_value": false,
      "site": "00bccd08",
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
            "const:98a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc8dc",
      "incomplete_value": false,
      "site": "00bcc8e0",
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
            "const:8bd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc8cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00bcccf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:818:8"]]
- 00bcc8d0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bcccf8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc8dc ["COPY", "tmp:0:8", ["const:8bd:8"]]
+ 00bccd04 ["COPY", "tmp:0:8", ["const:98a:8"]]
~~~


### [`00bcc8fc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc8fc.md) → [`00bccd24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccd24.md) _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccd50",
      "incomplete_value": true,
      "site": "00bccd50",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc928",
      "incomplete_value": true,
      "site": "00bcc928",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bccd38",
      "incomplete_value": true,
      "site": "00bccd38",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc910",
      "incomplete_value": true,
      "site": "00bcc910",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bccd40",
      "incomplete_value": false,
      "site": "00bccd48",
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
            "const:98a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc918",
      "incomplete_value": false,
      "site": "00bcc920",
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
            "const:8bd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc90c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00bccd34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:818:8"]]
- 00bcc910 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bccd38 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcc918 ["COPY", "tmp:0:8", ["const:8bd:8"]]
+ 00bccd40 ["COPY", "tmp:0:8", ["const:98a:8"]]
~~~


### [`00bcc93c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc93c.md) → [`00bccd64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccd64.md) _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccd94",
      "incomplete_value": true,
      "site": "00bccd94",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc96c",
      "incomplete_value": true,
      "site": "00bcc96c",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bccd78",
      "incomplete_value": true,
      "site": "00bccd78",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc950",
      "incomplete_value": true,
      "site": "00bcc950",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bccd84",
      "incomplete_value": false,
      "site": "00bccd8c",
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
            "const:98a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc95c",
      "incomplete_value": false,
      "site": "00bcc964",
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
            "const:8bd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc94c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00bccd74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:818:8"]]
- 00bcc95c ["COPY", "tmp:0:8", ["const:8bd:8"]]
+ 00bccd84 ["COPY", "tmp:0:8", ["const:98a:8"]]
- 00bcc964 ["INT_ADD", "register:40f0:8", ["const:bcc964:8", "const:4:8"]]
+ 00bccd8c ["INT_ADD", "register:40f0:8", ["const:bccd8c:8", "const:4:8"]]
~~~


### [`00bcc980`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc980.md) → [`00bccda8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccda8.md) _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccdd8",
      "incomplete_value": true,
      "site": "00bccdd8",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc9b0",
      "incomplete_value": true,
      "site": "00bcc9b0",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bccdbc",
      "incomplete_value": true,
      "site": "00bccdbc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bcc994",
      "incomplete_value": true,
      "site": "00bcc994",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bcc9a0",
      "incomplete_value": false,
      "site": "00bcc9a8",
      "value": [
        "leaf",
        "const:0:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc990 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00bccdb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:818:8"]]
- 00bcc994 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bccdbc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc99c ["COPY", "tmp:0:8", ["const:8bd:8"]]
+ 00bccdc4 ["COPY", "tmp:0:8", ["const:98a:8"]]
~~~


### [`00bcc9d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc9d0.md) → [`00bccdf8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccdf8.md) _ZN8firebase4auth21jni_id_token_listener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcce00",
      "incomplete_value": true,
      "site": "00bcce00",
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
                "const:ffffffffffffffd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc9d8",
      "incomplete_value": true,
      "site": "00bcc9d8",
      "value": [
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
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcce00",
      "incomplete_value": true,
      "site": "00bcce00",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc9d8",
      "incomplete_value": true,
      "site": "00bcc9d8",
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
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcce50",
      "incomplete_value": true,
      "site": "00bcce50",
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
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcca28",
      "incomplete_value": true,
      "site": "00bcca28",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
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
        "01126420",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126420",
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
        "01126820",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126820",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcc9e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:420:8"]]
+ 00bcce0c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:820:8"]]
- 00bcc9e8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bcce10 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcc9f0 ["BRANCH", null, ["local:b4:8"]]
+ 00bcce18 ["BRANCH", null, ["local:b3:8"]]
~~~


### [`00bcca3c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcca3c.md) → [`00bcce64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcce64.md) _ZN8firebase4auth21jni_id_token_listener12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcce68",
      "incomplete_value": true,
      "site": "00bcce68",
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
                "const:ffffffffffffffd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcca40",
      "incomplete_value": true,
      "site": "00bcca40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcce68",
      "incomplete_value": true,
      "site": "00bcce68",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcca40",
      "incomplete_value": true,
      "site": "00bcca40",
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
                "const:10:8"
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcce6c",
      "incomplete_value": true,
      "site": "00bcce6c",
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
                "const:ffffffffffffffd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcca44",
      "incomplete_value": true,
      "site": "00bcca44",
      "value": [
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
      ]
    },
    "ordinal": 3,
    "slot": 1
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
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126420",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126420",
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
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126820",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126820",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcca50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
+ 00bcce78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:818:8"]]
- 00bcca5c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:420:8"]]
+ 00bcce84 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:820:8"]]
- 00bcca64 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bcce8c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
~~~


### [`00bccaac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccaac.md) → [`00bcced4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcced4.md) _ZN8firebase4auth21jni_id_token_listener14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccf14",
      "incomplete_value": true,
      "site": "00bccf14",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccaec",
      "incomplete_value": true,
      "site": "00bccaec",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bccef0",
      "incomplete_value": true,
      "site": "00bccef0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bccac8",
      "incomplete_value": true,
      "site": "00bccac8",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bccef8",
      "incomplete_value": false,
      "site": "00bccf0c",
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
            "const:98a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccad0",
      "incomplete_value": false,
      "site": "00bccae4",
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
            "const:8bd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
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
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126418",
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
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bccac0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
+ 00bccee8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:818:8"]]
- 00bccad0 ["COPY", "tmp:0:8", ["const:8bd:8"]]
+ 00bccef8 ["COPY", "tmp:0:8", ["const:98a:8"]]
- 00bccae4 ["INT_ADD", "register:40f0:8", ["const:bccae4:8", "const:4:8"]]
+ 00bccf0c ["INT_ADD", "register:40f0:8", ["const:bccf0c:8", "const:4:8"]]
~~~


### [`00bccb1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb1c.md) → [`00bccf44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf44.md) _ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bccf60",
      "incomplete_value": false,
      "site": "00bccf64",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccb38",
      "incomplete_value": false,
      "site": "00bccb3c",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00bccb48",
      "incomplete_value": true,
      "site": "00bccb54",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126428",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bccb38 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bccf60 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bccb3c ["INT_ADD", "register:40f0:8", ["const:bccb3c:8", "const:4:8"]]
+ 00bccf64 ["INT_ADD", "register:40f0:8", ["const:bccf64:8", "const:4:8"]]
- 00bccb44 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 00bccf6c ["COPY", "tmp:0:8", ["const:828:8"]]
~~~


### [`00bccb58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb58.md) → [`00bccf80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf80.md) _ZN8firebase4auth21jni_id_token_listener13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bccfc0",
      "incomplete_value": true,
      "site": "00bccfc0",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccb98",
      "incomplete_value": true,
      "site": "00bccb98",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bccf9c",
      "incomplete_value": true,
      "site": "00bccf9c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bccb74",
      "incomplete_value": true,
      "site": "00bccb74",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bccfa4",
      "incomplete_value": false,
      "site": "00bccfb8",
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
            "const:98a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccb7c",
      "incomplete_value": false,
      "site": "00bccb90",
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
            "const:8bd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
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
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126418",
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
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bccb6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
+ 00bccf94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:818:8"]]
- 00bccb7c ["COPY", "tmp:0:8", ["const:8bd:8"]]
+ 00bccfa4 ["COPY", "tmp:0:8", ["const:98a:8"]]
- 00bccb90 ["INT_ADD", "register:40f0:8", ["const:bccb90:8", "const:4:8"]]
+ 00bccfb8 ["INT_ADD", "register:40f0:8", ["const:bccfb8:8", "const:4:8"]]
~~~


### [`00bccbc8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccbc8.md) → [`00bccff0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccff0.md) _ZN8firebase4auth21jni_id_token_listener10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd00c",
      "incomplete_value": false,
      "site": "00bcd010",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bcd01c",
      "incomplete_value": true,
      "site": "00bcd028",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccbf4",
      "incomplete_value": true,
      "site": "00bccc00",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126438",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126838",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bccbdc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bcd004 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bccbe4 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bcd00c ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bccbe8 ["INT_ADD", "register:40f0:8", ["const:bccbe8:8", "const:4:8"]]
+ 00bcd010 ["INT_ADD", "register:40f0:8", ["const:bcd010:8", "const:4:8"]]
~~~


### [`00bccc04`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccc04.md) → [`00bcd02c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd02c.md) _ZN8firebase4auth18CacheAuthMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d840`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d840.md) · 呼出先 3件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md) [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5dc40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc40.md) · 呼出先 3件 [`00c5af10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md) [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 21件, `call_target` 1件, `store_condition` 1件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 3件, `call_argument_candidate` 2件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcd078",
      "incomplete_value": true,
      "site": "00bcd078",
      "value": [
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
    },
    "old": {
      "definition_site": "00bccc50",
      "incomplete_value": true,
      "site": "00bccc50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "definition_site": "00bcd0d0",
      "incomplete_value": true,
      "site": "00bcd0d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccca8",
      "incomplete_value": true,
      "site": "00bccca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:3d0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcd128",
      "incomplete_value": true,
      "site": "00bcd128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccd00",
      "incomplete_value": true,
      "site": "00bccd00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      48,
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      76,
      "WRITE",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      48,
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      76,
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bccc20 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:328:8"]]
+ 00bcd048 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 00bccc34 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00bcd05c ["COPY", "tmp:0:8", ["const:23c:8"]]
- 00bccc48 ["INT_ADD", "register:40f0:8", ["const:bccc48:8", "const:4:8"]]
+ 00bcd070 ["INT_ADD", "register:40f0:8", ["const:bcd070:8", "const:4:8"]]
~~~


### [`00bcce34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcce34.md) → [`00bcd25c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd25c.md) _ZN8firebase4auth18ReleaseAuthClassesEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d860`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d860.md) · 呼出先 1件 [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5dc60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc60.md) · 呼出先 1件 [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `call_target` 2件, `store_destination` 8件

アドレスに依存する影響 `branch_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcd298",
      "incomplete_value": true,
      "site": "00bcd298",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcce70",
      "incomplete_value": true,
      "site": "00bcce70",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcd2b8",
      "incomplete_value": true,
      "site": "00bcd2b8",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcce90",
      "incomplete_value": true,
      "site": "00bcce90",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcd2e4",
      "incomplete_value": true,
      "site": "00bcd2e4",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccebc",
      "incomplete_value": true,
      "site": "00bccebc",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
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
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "01126330",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126330",
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
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcce48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
+ 00bcd270 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00bcce58 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:330:8"]]
+ 00bcd280 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:730:8"]]
- 00bcce6c ["INT_ADD", "register:40f0:8", ["const:bcce6c:8", "const:4:8"]]
+ 00bcd294 ["INT_ADD", "register:40f0:8", ["const:bcd294:8", "const:4:8"]]
~~~


### [`00bccf88`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccf88.md) → [`00bcd3b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd3b0.md) _ZN8firebase4auth17UpdateCurrentUserEPNS0_8AuthDataE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d830`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d830.md) · 呼出先 7件 [`004977f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 1件 [`00c5dc30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc30.md) · 呼出先 7件 [`00497834`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcd408",
      "incomplete_value": true,
      "site": "00bcd408",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:101:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccfe0",
      "incomplete_value": true,
      "site": "00bccfe0",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_AND",
              [
                "leaf",
                "const:0:4"
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
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bccfb8",
      "incomplete_value": true,
      "site": "00bccfc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f8:8"
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
      "definition_site": "00bcd3e8",
      "incomplete_value": true,
      "site": "00bcd3f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccfc0",
      "incomplete_value": true,
      "site": "00bccfc8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:340:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      56,
      "READ",
      [
        "storage",
        "01126340",
        null,
        "undefined8"
      ]
    ],
    [
      120,
      "PARAM",
      [
        "storage",
        "002b8c49",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      56,
      "READ",
      [
        "storage",
        "01126740",
        null,
        "undefined8"
      ]
    ],
    [
      120,
      "PARAM",
      [
        "storage",
        "002b8c89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bccfa4 ["INT_ADD", "register:40f0:8", ["const:bccfa4:8", "const:4:8"]]
+ 00bcd3cc ["INT_ADD", "register:40f0:8", ["const:bcd3cc:8", "const:4:8"]]
- 00bccfb4 ["INT_ADD", "register:40f0:8", ["const:bccfb4:8", "const:4:8"]]
+ 00bcd3dc ["INT_ADD", "register:40f0:8", ["const:bcd3dc:8", "const:4:8"]]
- 00bccfc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:340:8"]]
+ 00bcd3e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:740:8"]]
~~~


### [`00bcd044`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd044.md) → [`00bcd46c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd46c.md) _ZN8firebase4auth14SetEmulatorJniEPNS0_8AuthDataEPKcj

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd4ac",
      "incomplete_value": true,
      "site": "00bcd4c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:788:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd084",
      "incomplete_value": true,
      "site": "00bcd098",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:388:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      64,
      "READ",
      [
        "storage",
        "01126388",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      64,
      "READ",
      [
        "storage",
        "01126788",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcd064 ["INT_ADD", "register:40f0:8", ["const:bcd064:8", "const:4:8"]]
+ 00bcd48c ["INT_ADD", "register:40f0:8", ["const:bcd48c:8", "const:4:8"]]
- 00bcd078 ["INT_ADD", "register:40f0:8", ["const:bcd078:8", "const:4:8"]]
+ 00bcd4a0 ["INT_ADD", "register:40f0:8", ["const:bcd4a0:8", "const:4:8"]]
- 00bcd084 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:388:8"]]
+ 00bcd4ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:788:8"]]
~~~


### [`00bcd0c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd0c4.md) → [`00bcd4ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd4ec.md) _ZN8firebase4auth13CheckEmulatorEPNS0_8AuthDataE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d820`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d820.md) · 呼出先 9件 [`00574cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c60.md) [`00c594a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c594a0.md)
- 新版 呼出元 1件 [`00c5dc20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc20.md) · 呼出先 9件 [`00574cec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58060.md) [`00c598a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c598a0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 9件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcd514",
      "incomplete_value": true,
      "site": "00bcd514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
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
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd0ec",
      "incomplete_value": true,
      "site": "00bcd0ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "00bcd618",
      "incomplete_value": true,
      "site": "00bcd618",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "00bcd1f0",
      "incomplete_value": true,
      "site": "00bcd1f0",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
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
      "definition_site": "00bcd510",
      "incomplete_value": false,
      "site": "00bcd518",
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
            "const:f13:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd0e8",
      "incomplete_value": false,
      "site": "00bcd0f0",
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
            "const:ed3:8"
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
      36,
      "PARAM",
      [
        "storage",
        "002baed3",
        null,
        "string"
      ]
    ],
    [
      56,
      "PARAM",
      [
        "storage",
        "002c1d43",
        null,
        "string"
      ]
    ],
    [
      68,
      "PARAM",
      [
        "storage",
        "002bd416",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      36,
      "PARAM",
      [
        "storage",
        "002baf13",
        null,
        "string"
      ]
    ],
    [
      56,
      "PARAM",
      [
        "storage",
        "002c1d83",
        null,
        "string"
      ]
    ],
    [
      68,
      "PARAM",
      [
        "storage",
        "002bd456",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcd0e8 ["COPY", "tmp:0:8", ["const:ed3:8"]]
+ 00bcd510 ["COPY", "tmp:0:8", ["const:f13:8"]]
- 00bcd0f0 ["INT_ADD", "register:40f0:8", ["const:bcd0f0:8", "const:4:8"]]
+ 00bcd518 ["INT_ADD", "register:40f0:8", ["const:bcd518:8", "const:4:8"]]
- 00bcd0f4 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00bcd51c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
~~~


### [`00bcd22c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd22c.md) → [`00bcd654`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd654.md) _ZN8firebase4auth18CreatePlatformAuthEPNS_3AppE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d5d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5d0.md) · 呼出先 21件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a7a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5aaa0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaa0.md)
- 新版 呼出元 1件 [`00c5d9d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9d0.md) · 呼出先 21件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aba0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aea0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aea0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcd698",
      "incomplete_value": true,
      "site": "00bcd698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd270",
      "incomplete_value": true,
      "site": "00bcd270",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:440:8"
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
      "definition_site": "00bcd6a8",
      "incomplete_value": true,
      "site": "00bcd6bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "old": {
      "definition_site": "00bcd280",
      "incomplete_value": true,
      "site": "00bcd294",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:328:8"
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
      "definition_site": "00bcd6ac",
      "incomplete_value": true,
      "site": "00bcd6bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "definition_site": "00bcd284",
      "incomplete_value": true,
      "site": "00bcd294",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "ordinal": 2,
    "slot": 3
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
        "01126440",
        null,
        "undefined4"
      ]
    ],
    [
      68,
      "WRITE",
      [
        "storage",
        "01126440",
        null,
        "undefined4"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "01126840",
        null,
        "undefined4"
      ]
    ],
    [
      68,
      "WRITE",
      [
        "storage",
        "01126840",
        null,
        "undefined4"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcd254 ["INT_ADD", "register:40f0:8", ["const:bcd254:8", "const:4:8"]]
+ 00bcd67c ["INT_ADD", "register:40f0:8", ["const:bcd67c:8", "const:4:8"]]
- 00bcd25c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:440:8"]]
+ 00bcd684 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:840:8"]]
- 00bcd270 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:440:8"]]
+ 00bcd698 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:840:8"]]
~~~


### [`00bcd468`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd468.md) → [`00bcd890`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd890.md) _ZN8firebase4auth4Auth16InitPlatformAuthEPNS0_8AuthDataE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d640`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d640.md) · 呼出先 6件 [`00574cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005896b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5ac80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5d820`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d820.md) [`00c5d830`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d830.md)
- 新版 呼出元 1件 [`00c5da40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da40.md) · 呼出先 6件 [`00574cec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005896f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5b080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5dc20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc20.md) [`00c5dc30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd8b4",
      "incomplete_value": true,
      "site": "00bcd8c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:7f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd48c",
      "incomplete_value": true,
      "site": "00bcd49c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:3f0:8"
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
      "definition_site": "00bcd8b8",
      "incomplete_value": true,
      "site": "00bcd8c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:800:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd490",
      "incomplete_value": true,
      "site": "00bcd49c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd8d4",
      "incomplete_value": true,
      "site": "00bcd8e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "old": {
      "definition_site": "00bcd4ac",
      "incomplete_value": true,
      "site": "00bcd4bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:360:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "01126400",
        null,
        "undefined8"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      36,
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      40,
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "01126760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcd480 ["INT_ADD", "register:40f0:8", ["const:bcd480:8", "const:4:8"]]
+ 00bcd8a8 ["INT_ADD", "register:40f0:8", ["const:bcd8a8:8", "const:4:8"]]
- 00bcd48c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3f0:8"]]
+ 00bcd8b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7f0:8"]]
- 00bcd490 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:400:8"]]
+ 00bcd8b8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:800:8"]]
~~~


### [`00bcd530`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd530.md) → [`00bcd958`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd958.md) _ZN8firebase4auth4Auth19DestroyPlatformAuthEPNS0_8AuthDataE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d650`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d650.md) · 呼出先 10件 [`00574cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab00.md) [`00c5abd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abd0.md) [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 1件 [`00c5da50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da50.md) · 呼出先 10件 [`00574cec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af00.md) [`00c5afd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5afd0.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcda60",
      "incomplete_value": true,
      "site": "00bcda60",
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
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd638",
      "incomplete_value": true,
      "site": "00bcd638",
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
            "const:440:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd9a4",
      "incomplete_value": true,
      "site": "00bcd9b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "old": {
      "definition_site": "00bcd57c",
      "incomplete_value": true,
      "site": "00bcd588",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:408:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd9c0",
      "incomplete_value": true,
      "site": "00bcd9d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "old": {
      "definition_site": "00bcd598",
      "incomplete_value": true,
      "site": "00bcd5a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:368:8"
              ]
            ]
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
      76,
      "READ",
      [
        "storage",
        "01126408",
        null,
        "undefined8"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "01126368",
        null,
        "undefined8"
      ]
    ],
    [
      132,
      "READ",
      [
        "storage",
        "01126430",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      76,
      "READ",
      [
        "storage",
        "01126808",
        null,
        "undefined8"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "01126768",
        null,
        "undefined8"
      ]
    ],
    [
      132,
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcd54c ["INT_ADD", "register:40f0:8", ["const:bcd54c:8", "const:4:8"]]
+ 00bcd974 ["INT_ADD", "register:40f0:8", ["const:bcd974:8", "const:4:8"]]
- 00bcd570 ["INT_ADD", "register:40f0:8", ["const:bcd570:8", "const:4:8"]]
+ 00bcd998 ["INT_ADD", "register:40f0:8", ["const:bcd998:8", "const:4:8"]]
- 00bcd57c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:408:8"]]
+ 00bcd9a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:808:8"]]
~~~


### [`00bcd68c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd68c.md) → [`00bcdab4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdab4.md) _ZN8firebase4auth12LogHeartbeatEPNS0_4AuthE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d590`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d590.md) · 呼出先 5件 [`00c5a7a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5baf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5baf0.md) [`00c5d680`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d680.md)
- 新版 呼出元 1件 [`00c5d990`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d990.md) · 呼出先 5件 [`00c5aba0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5bef0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bef0.md) [`00c5da80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da80.md)

変更の種類 call_argument_candidate, call_target, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcdabc",
      "incomplete_value": true,
      "site": "00bcdabc",
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
                "const:ffffffffffffffd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd694",
      "incomplete_value": true,
      "site": "00bcd694",
      "value": [
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
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcdabc",
      "incomplete_value": true,
      "site": "00bcdabc",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd694",
      "incomplete_value": true,
      "site": "00bcd694",
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
            "leaf",
            "const:8:8"
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
      "definition_site": "00bcdaec",
      "incomplete_value": true,
      "site": "00bcdb00",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "old": {
      "definition_site": "00bcd6c4",
      "incomplete_value": true,
      "site": "00bcd6d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:328:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      56,
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      56,
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcd6a8 ["INT_ADD", "register:40f0:8", ["const:bcd6a8:8", "const:4:8"]]
+ 00bcdad0 ["INT_ADD", "register:40f0:8", ["const:bcdad0:8", "const:4:8"]]
- 00bcd6b4 ["INT_ADD", "register:40f0:8", ["const:bcd6b4:8", "const:4:8"]]
+ 00bcdadc ["INT_ADD", "register:40f0:8", ["const:bcdadc:8", "const:4:8"]]
- 00bcd6b8 ["INT_ADD", "register:40f0:8", ["const:bcd6b8:8", "const:4:8"]]
+ 00bcdae0 ["INT_ADD", "register:40f0:8", ["const:bcdae0:8", "const:4:8"]]
~~~


### [`00bcd71c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd71c.md) → [`00bcdb44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdb44.md) _ZN8firebase4auth45JniAuthStateListener_nativeOnAuthStateChangedEP7_JNIEnvP8_jobjectl

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5d610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d610.md) [`00c5d830`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d830.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5da10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da10.md) [`00c5dc30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bcd728",
      "incomplete_value": true,
      "site": "00bcd730",
      "value": [
        "live",
        "register:4010:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


~~~diff
- 00bcd730 ["INT_ADD", "register:40f0:8", ["const:bcd730:8", "const:4:8"]]
+ 00bcdb58 ["INT_ADD", "register:40f0:8", ["const:bcdb58:8", "const:4:8"]]
~~~


### [`00bcd788`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md) → [`00bcdbb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md) _ZN8firebase4auth4Auth22FetchProvidersForEmailEPKc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`004977f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcda8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcda8c.md) [`00bcf478`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf478.md) [`00bcf604`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf604.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497834`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcdeb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdeb4.md) [`00bcf8a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf8a0.md) [`00bcfa2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfa2c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_destination` 11件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcdbb4",
      "incomplete_value": true,
      "site": "00bcdbb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd78c",
      "incomplete_value": true,
      "site": "00bcd78c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:90:8"
              ]
            ]
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcdbb4",
      "incomplete_value": true,
      "site": "00bcdbb4",
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
      "definition_site": "00bcd78c",
      "incomplete_value": true,
      "site": "00bcd78c",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcdbb8",
      "incomplete_value": true,
      "site": "00bcdbb8",
      "value": [
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
      ]
    },
    "old": {
      "definition_site": "00bcd790",
      "incomplete_value": true,
      "site": "00bcd790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:90:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      80,
      "READ",
      [
        "storage",
        "00c9b5f0",
        null,
        "pointer"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "00bcf478",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv",
        null
      ]
    ],
    [
      164,
      "READ",
      [
        "storage",
        "01126390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      80,
      "READ",
      [
        "storage",
        "00c9b9f0",
        null,
        "pointer"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "00bcf8a0",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv",
        null
      ]
    ],
    [
      164,
      "READ",
      [
        "storage",
        "01126790",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcd7c8 ["INT_ADD", "register:40f0:8", ["const:bcd7c8:8", "const:4:8"]]
+ 00bcdbf0 ["INT_ADD", "register:40f0:8", ["const:bcdbf0:8", "const:4:8"]]
- 00bcd7d8 ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:5f0:8"]]
+ 00bcdc00 ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:9f0:8"]]
- 00bcd7ec ["INT_ADD", "register:40f0:8", ["const:bcd7ec:8", "const:4:8"]]
+ 00bcdc14 ["INT_ADD", "register:40f0:8", ["const:bcdc14:8", "const:4:8"]]
~~~


### [`00bcd988`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd988.md) → [`00bcddb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcddb0.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4Auth20FetchProvidersResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFut

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d8e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d8e0.md) · 呼出先 6件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d7d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7d0.md)
- 新版 呼出元 1件 [`00c5dce0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dce0.md) · 呼出先 6件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dbd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbd0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcdde0",
      "incomplete_value": true,
      "site": "00bcdde4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:70:8"
              ]
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
      "definition_site": "00bcd9b8",
      "incomplete_value": true,
      "site": "00bcd9bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:18:8"
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
    "new": null,
    "old": {
      "definition_site": "00bcd9c8",
      "incomplete_value": true,
      "site": "00bcd9d0",
      "value": [
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
      "definition_site": "00bcd9cc",
      "incomplete_value": true,
      "site": "00bcd9d0",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


~~~diff
- 00bcd9bc ["INT_ADD", "register:40f0:8", ["const:bcd9bc:8", "const:4:8"]]
+ 00bcdde4 ["INT_ADD", "register:40f0:8", ["const:bcdde4:8", "const:4:8"]]
- 00bcd9c4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00bcddec ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00bcd9d0 ["INT_ADD", "register:40f0:8", ["const:bcd9d0:8", "const:4:8"]]
+ 00bcddf8 ["INT_ADD", "register:40f0:8", ["const:bcddf8:8", "const:4:8"]]
~~~


### [`00bcda8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcda8c.md) → [`00bcdeb4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdeb4.md) FUN_00bcdeb4

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00bcd788`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md) · 呼出先 10件 [`004977f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00576278`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00bcdbb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md) · 呼出先 10件 [`00497834`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bce060",
      "incomplete_value": true,
      "site": "00bce060",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcdc38",
      "incomplete_value": true,
      "site": "00bcdc38",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bcdf78",
      "value": [
        "live",
        "register:102:1"
      ]
    },
    "old": {
      "definition_site": "00bcdb4c",
      "incomplete_value": true,
      "site": "00bcdb50",
      "value": [
        "INT_LESSEQUAL",
        "1",
        [
          [
            "INT_SEXT",
            "8",
            [
              [
                "live",
                "register:4000:4"
              ]
            ]
          ],
          [
            "INT_MULT",
            "8",
            [
              "INT_SRIGHT",
              "INT_OR"
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcdf8c",
      "incomplete_value": true,
      "site": "00bcdf8c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SLESS",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:4"
              ]
            ]
          ],
          [
            "INT_SBORROW",
            "1",
            [
              [
                "live",
                "register:40c8:4"
              ],
              [
                "leaf",
                "const:1:4"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcdb64",
      "incomplete_value": true,
      "site": "00bcdb64",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:100:1"
          ],
          [
            "live",
            "register:103:1"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      88,
      "PARAM",
      [
        "storage",
        "002a0c58",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "011263e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      88,
      "PARAM",
      [
        "storage",
        "002a0d25",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "011267e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcdad0 ["INT_ADD", "register:40f0:8", ["const:bcdad0:8", "const:4:8"]]
+ 00bcdef8 ["INT_ADD", "register:40f0:8", ["const:bcdef8:8", "const:4:8"]]
- 00bcdae4 ["COPY", "tmp:0:8", ["const:c58:8"]]
+ 00bcdf0c ["COPY", "tmp:0:8", ["const:d25:8"]]
- 00bcdae8 ["INT_ADD", "register:40f0:8", ["const:bcdae8:8", "const:4:8"]]
+ 00bcdf10 ["INT_ADD", "register:40f0:8", ["const:bcdf10:8", "const:4:8"]]
~~~


### [`00bcdca0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdca0.md) → [`00bce0c8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce0c8.md) _ZN8firebase4auth4Auth21SignInWithCustomTokenEPKc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`004977f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497834`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bce0fc",
      "incomplete_value": true,
      "site": "00bce0fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:80:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcdcd4",
      "incomplete_value": true,
      "site": "00bcdcd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bce1b8",
      "incomplete_value": true,
      "site": "00bce1b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcdd90",
      "incomplete_value": true,
      "site": "00bcdd90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00bce22c",
      "incomplete_value": true,
      "site": "00bce22c",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:101:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcde04",
      "incomplete_value": true,
      "site": "00bcde04",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
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
      116,
      "READ",
      [
        "storage",
        "01126398",
        null,
        "undefined8"
      ]
    ],
    [
      236,
      "READ",
      [
        "storage",
        "00c9b620",
        null,
        "pointer"
      ]
    ],
    [
      240,
      "DATA",
      [
        "storage",
        "00bd4404",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      116,
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      236,
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ],
    [
      240,
      "DATA",
      [
        "storage",
        "00bd482c",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcdce8 ["INT_ADD", "register:40f0:8", ["const:bcdce8:8", "const:4:8"]]
+ 00bce110 ["INT_ADD", "register:40f0:8", ["const:bce110:8", "const:4:8"]]
- 00bcdcf4 ["INT_ADD", "register:40f0:8", ["const:bcdcf4:8", "const:4:8"]]
+ 00bce11c ["INT_ADD", "register:40f0:8", ["const:bce11c:8", "const:4:8"]]
- 00bcdd08 ["INT_ADD", "register:40f0:8", ["const:bcdd08:8", "const:4:8"]]
+ 00bce130 ["INT_ADD", "register:40f0:8", ["const:bce130:8", "const:4:8"]]
~~~


### [`00bcde64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcde64.md) → [`00bce28c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce28c.md) _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d800`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d800.md) · 呼出先 7件 [`00bcf8b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf8b0.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00c5dc00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc00.md) · 呼出先 7件 [`00bcfcd8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfcd8.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 13件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bce2c0",
      "incomplete_value": true,
      "site": "00bce2c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:70:8"
              ]
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
      "definition_site": "00bcde98",
      "incomplete_value": true,
      "site": "00bcde98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bce2d4",
      "incomplete_value": true,
      "site": "00bce2d4",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcdeac",
      "incomplete_value": true,
      "site": "00bcdeac",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bce2e0",
      "incomplete_value": true,
      "site": "00bce2e0",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcdeb8",
      "incomplete_value": true,
      "site": "00bcdeb8",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      140,
      "READ",
      [
        "storage",
        "00c9b5e8",
        null,
        "pointer"
      ]
    ],
    [
      140,
      "PARAM",
      [
        "storage",
        "00bcf8b0",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv",
        null
      ]
    ]
  ],
  "added": [
    [
      140,
      "READ",
      [
        "storage",
        "00c9b9e8",
        null,
        "pointer"
      ]
    ],
    [
      140,
      "PARAM",
      [
        "storage",
        "00bcfcd8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv",
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcde9c ["INT_ADD", "register:40f0:8", ["const:bcde9c:8", "const:4:8"]]
+ 00bce2c4 ["INT_ADD", "register:40f0:8", ["const:bce2c4:8", "const:4:8"]]
- 00bcdee8 ["INT_ADD", "register:40f0:8", ["const:bcdee8:8", "const:4:8"]]
+ 00bce310 ["INT_ADD", "register:40f0:8", ["const:bce310:8", "const:4:8"]]
- 00bcdef0 ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:5e8:8"]]
+ 00bce318 ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:9e8:8"]]
~~~


### [`00bcdfb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdfb0.md) → [`00bce3d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce3d8.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d8d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d8d0.md) · 呼出先 6件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d7c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7c0.md)
- 新版 呼出元 1件 [`00c5dcd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dcd0.md) · 呼出先 6件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dbc0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbc0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 8件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bce3e0",
      "incomplete_value": true,
      "site": "00bce3e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:70:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcdfb8",
      "incomplete_value": true,
      "site": "00bcdfb8",
      "value": [
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
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bce3e0",
      "incomplete_value": true,
      "site": "00bce3e0",
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
                "const:50:8"
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
      "definition_site": "00bcdfb8",
      "incomplete_value": true,
      "site": "00bcdfb8",
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
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bce3e4",
      "incomplete_value": true,
      "site": "00bce3e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:70:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcdfbc",
      "incomplete_value": true,
      "site": "00bcdfbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


~~~diff
- 00bcdfe4 ["INT_ADD", "register:40f0:8", ["const:bcdfe4:8", "const:4:8"]]
+ 00bce40c ["INT_ADD", "register:40f0:8", ["const:bce40c:8", "const:4:8"]]
- 00bcdfec ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00bce414 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bcdff8 ["INT_ADD", "register:40f0:8", ["const:bcdff8:8", "const:4:8"]]
+ 00bce420 ["INT_ADD", "register:40f0:8", ["const:bce420:8", "const:4:8"]]
~~~


### [`00bce468`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce468.md) → [`00bce890`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce890.md) _ZN8firebase4auth4Auth35SignInAndRetrieveDataWithCredentialERKNS0_10CredentialE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a5e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5e0.md) · 呼出先 13件 [`004977f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5a9e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a9e0.md) · 呼出先 13件 [`00497834`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 13件, `store_destination` 11件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bce894",
      "incomplete_value": true,
      "site": "00bce894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bce46c",
      "incomplete_value": true,
      "site": "00bce46c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:90:8"
              ]
            ]
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00bce894",
      "incomplete_value": true,
      "site": "00bce894",
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
      "definition_site": "00bce46c",
      "incomplete_value": true,
      "site": "00bce46c",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bce898",
      "incomplete_value": true,
      "site": "00bce898",
      "value": [
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
      ]
    },
    "old": {
      "definition_site": "00bce470",
      "incomplete_value": true,
      "site": "00bce470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:90:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      168,
      "READ",
      [
        "storage",
        "011263a0",
        null,
        "undefined8"
      ]
    ],
    [
      264,
      "READ",
      [
        "storage",
        "00c9b620",
        null,
        "pointer"
      ]
    ],
    [
      268,
      "DATA",
      [
        "storage",
        "00bd4404",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      168,
      "READ",
      [
        "storage",
        "011267a0",
        null,
        "undefined8"
      ]
    ],
    [
      264,
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ],
    [
      268,
      "DATA",
      [
        "storage",
        "00bd482c",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bce4b0 ["INT_ADD", "register:40f0:8", ["const:bce4b0:8", "const:4:8"]]
+ 00bce8d8 ["INT_ADD", "register:40f0:8", ["const:bce8d8:8", "const:4:8"]]
- 00bce4bc ["INT_ADD", "register:40f0:8", ["const:bce4bc:8", "const:4:8"]]
+ 00bce8e4 ["INT_ADD", "register:40f0:8", ["const:bce8e4:8", "const:4:8"]]
- 00bce4c4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bce8ec ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
~~~


### [`00bce654`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce654.md) → [`00bcea7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcea7c.md) _ZN8firebase4auth4Auth18SignInWithProviderEPNS0_21FederatedAuthProviderE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a790`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a790.md) · 呼出先 3件 [`00c5a7e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5ab90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab90.md) · 呼出先 3件 [`00c5abe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bceab8",
      "incomplete_value": false,
      "site": "00bceabc",
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
            "const:bc2:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bceac0",
      "incomplete_value": true,
      "site": "00bceac8",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bceacc",
      "incomplete_value": true,
      "site": "00bceadc",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      60,
      "PARAM",
      [
        "storage",
        "002b5b82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      60,
      "PARAM",
      [
        "storage",
        "002b5bc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bce664 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bcea8c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bce690 ["COPY", "tmp:0:8", ["const:b82:8"]]
+ 00bceab8 ["COPY", "tmp:0:8", ["const:bc2:8"]]
- 00bce694 ["INT_ADD", "register:40f0:8", ["const:bce694:8", "const:4:8"]]
+ 00bceabc ["INT_ADD", "register:40f0:8", ["const:bceabc:8", "const:4:8"]]
~~~


### [`00bce6d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce6d8.md) → [`00bceb00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bceb00.md) _ZN8firebase4auth4Auth17SignInAnonymouslyEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`004977f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497834`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 11件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bceb04",
      "incomplete_value": true,
      "site": "00bceb04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:80:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bce6dc",
      "incomplete_value": true,
      "site": "00bce6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bceb04",
      "incomplete_value": true,
      "site": "00bceb04",
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
                "const:30:8"
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
      "definition_site": "00bce6dc",
      "incomplete_value": true,
      "site": "00bce6dc",
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
                "const:30:8"
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bceb08",
      "incomplete_value": true,
      "site": "00bceb08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:80:8"
              ]
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
      "definition_site": "00bce6e0",
      "incomplete_value": true,
      "site": "00bce6e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      92,
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      184,
      "READ",
      [
        "storage",
        "00c9b620",
        null,
        "pointer"
      ]
    ],
    [
      188,
      "DATA",
      [
        "storage",
        "00bd4404",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      92,
      "READ",
      [
        "storage",
        "011267a8",
        null,
        "undefined8"
      ]
    ],
    [
      184,
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ],
    [
      188,
      "DATA",
      [
        "storage",
        "00bd482c",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bce71c ["INT_ADD", "register:40f0:8", ["const:bce71c:8", "const:4:8"]]
+ 00bceb44 ["INT_ADD", "register:40f0:8", ["const:bceb44:8", "const:4:8"]]
- 00bce728 ["INT_ADD", "register:40f0:8", ["const:bce728:8", "const:4:8"]]
+ 00bceb50 ["INT_ADD", "register:40f0:8", ["const:bceb50:8", "const:4:8"]]
- 00bce734 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3a8:8"]]
+ 00bceb5c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7a8:8"]]
~~~


### [`00bce864`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce864.md) → [`00bcec8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcec8c.md) _ZN8firebase4auth4Auth26SignInWithEmailAndPasswordEPKcS3_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`004977f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00497834`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcecc0",
      "incomplete_value": true,
      "site": "00bcecc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:90:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bce898",
      "incomplete_value": true,
      "site": "00bce898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcecb0",
      "incomplete_value": true,
      "site": "00bcecc0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:1660:8"
              ],
              [
                "leaf",
                "const:28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bce898",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcedd0",
      "incomplete_value": true,
      "site": "00bcedd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00bce9a8",
      "incomplete_value": true,
      "site": "00bce9a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:620:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      176,
      "READ",
      [
        "storage",
        "011263b0",
        null,
        "undefined8"
      ]
    ],
    [
      320,
      "READ",
      [
        "storage",
        "00c9b620",
        null,
        "pointer"
      ]
    ],
    [
      324,
      "DATA",
      [
        "storage",
        "00bd4404",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      176,
      "READ",
      [
        "storage",
        "011267b0",
        null,
        "undefined8"
      ]
    ],
    [
      320,
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ],
    [
      324,
      "DATA",
      [
        "storage",
        "00bd482c",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bce8b0 ["INT_ADD", "register:40f0:8", ["const:bce8b0:8", "const:4:8"]]
+ 00bcecd8 ["INT_ADD", "register:40f0:8", ["const:bcecd8:8", "const:4:8"]]
- 00bce8bc ["INT_ADD", "register:40f0:8", ["const:bce8bc:8", "const:4:8"]]
+ 00bcece4 ["INT_ADD", "register:40f0:8", ["const:bcece4:8", "const:4:8"]]
- 00bce8cc ["INT_ADD", "register:40f0:8", ["const:bce8cc:8", "const:4:8"]]
+ 00bcecf4 ["INT_ADD", "register:40f0:8", ["const:bcecf4:8", "const:4:8"]]
~~~


### [`00bceaf0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceaf0.md) → [`00bcef18`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcef18.md) _ZN8firebase4auth4Auth30CreateUserWithEmailAndPasswordEPKcS3_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`004977f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00497834`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcf05c",
      "incomplete_value": true,
      "site": "00bcf05c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00bcec34",
      "incomplete_value": true,
      "site": "00bcec34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcefc8",
      "incomplete_value": true,
      "site": "00bcefe0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:7b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bceba0",
      "incomplete_value": true,
      "site": "00bcebb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:3b8:8"
              ]
            ]
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
      "definition_site": "00bcf014",
      "incomplete_value": true,
      "site": "00bcf01c",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": null,
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      176,
      "READ",
      [
        "storage",
        "011263b8",
        null,
        "undefined8"
      ]
    ],
    [
      320,
      "READ",
      [
        "storage",
        "00c9b620",
        null,
        "pointer"
      ]
    ],
    [
      324,
      "DATA",
      [
        "storage",
        "00bd4404",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      176,
      "READ",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ],
    [
      320,
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ],
    [
      324,
      "DATA",
      [
        "storage",
        "00bd482c",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bceb3c ["INT_ADD", "register:40f0:8", ["const:bceb3c:8", "const:4:8"]]
+ 00bcef64 ["INT_ADD", "register:40f0:8", ["const:bcef64:8", "const:4:8"]]
- 00bceb40 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00bcef68 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bceb48 ["INT_ADD", "register:40f0:8", ["const:bceb48:8", "const:4:8"]]
+ 00bcef70 ["INT_ADD", "register:40f0:8", ["const:bcef70:8", "const:4:8"]]
~~~


### [`00bced7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bced7c.md) → [`00bcf1a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf1a4.md) _ZN8firebase4auth4Auth12current_userEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a630`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a630.md) · 呼出先 3件 [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a640`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a640.md)
- 新版 呼出元 1件 [`00c5aa30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa30.md) · 呼出先 3件 [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aa40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa40.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `store_condition` 11件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcf200",
      "incomplete_value": true,
      "site": "00bcf220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcedd8",
      "incomplete_value": true,
      "site": "00bcedf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcf240",
      "incomplete_value": true,
      "site": "00bcf260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcee18",
      "incomplete_value": true,
      "site": "00bcee38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcf1bc",
      "incomplete_value": true,
      "site": "00bcf1bc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bced94",
      "incomplete_value": true,
      "site": "00bced94",
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
              [
                "live",
                "register:4000:8"
              ]
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
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      76,
      "READ",
      [
        "storage",
        "00c9b5c0",
        null,
        "pointer"
      ]
    ],
    [
      124,
      "DATA",
      [
        "storage",
        "00c924a8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      140,
      "READ",
      [
        "storage",
        "00c9b5c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      76,
      "READ",
      [
        "storage",
        "00c9b9c0",
        null,
        "pointer"
      ]
    ],
    [
      124,
      "DATA",
      [
        "storage",
        "00c928a8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      140,
      "READ",
      [
        "storage",
        "00c9b9c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bced94 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bcf1bc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bceda4 ["INT_ADD", "register:40f0:8", ["const:bceda4:8", "const:4:8"]]
+ 00bcf1cc ["INT_ADD", "register:40f0:8", ["const:bcf1cc:8", "const:4:8"]]
- 00bcedb0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bcf1d8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
~~~


### [`00bceefc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceefc.md) → [`00bcf324`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf324.md) _ZN8firebase4auth4Auth17set_language_codeEPKc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf374",
      "incomplete_value": true,
      "site": "00bcf384",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:750:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcef4c",
      "incomplete_value": true,
      "site": "00bcef5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      80,
      "READ",
      [
        "storage",
        "01126350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      80,
      "READ",
      [
        "storage",
        "01126750",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcef10 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00bcf338 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bcef20 ["INT_ADD", "register:40f0:8", ["const:bcef20:8", "const:4:8"]]
+ 00bcf348 ["INT_ADD", "register:40f0:8", ["const:bcf348:8", "const:4:8"]]
- 00bcef3c ["INT_ADD", "register:40f0:8", ["const:bcef3c:8", "const:4:8"]]
+ 00bcf364 ["INT_ADD", "register:40f0:8", ["const:bcf364:8", "const:4:8"]]
~~~


### [`00bcef9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bcef9c.md) → [`00bcf3c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf3c4.md) _ZN8firebase4auth4Auth14UseAppLanguageEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf3ec",
      "incomplete_value": true,
      "site": "00bcf3f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcefc4",
      "incomplete_value": true,
      "site": "00bcefd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:358:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "READ",
      [
        "storage",
        "01126358",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcefac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bcf3d4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcefb8 ["INT_ADD", "register:40f0:8", ["const:bcefb8:8", "const:4:8"]]
+ 00bcf3e0 ["INT_ADD", "register:40f0:8", ["const:bcf3e0:8", "const:4:8"]]
- 00bcefc4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:358:8"]]
+ 00bcf3ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:758:8"]]
~~~


### [`00bceff0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceff0.md) → [`00bcf418`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf418.md) _ZN8firebase4auth4Auth7SignOutEv

根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a620`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a620.md) · 呼出先 6件 [`00574cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 1件 [`00c5aa20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa20.md) · 呼出先 6件 [`00574cec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bcf020",
      "incomplete_value": true,
      "site": "00bcf024",
      "value": [
        "LOAD",
        "8",
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
                "const:1f8:8"
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
    "new": null,
    "old": {
      "definition_site": "00bcf018",
      "incomplete_value": true,
      "site": "00bcf024",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:380:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "READ",
      [
        "storage",
        "01126380",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "01126780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcf00c ["INT_ADD", "register:40f0:8", ["const:bcf00c:8", "const:4:8"]]
+ 00bcf434 ["INT_ADD", "register:40f0:8", ["const:bcf434:8", "const:4:8"]]
- 00bcf018 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:380:8"]]
+ 00bcf440 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:780:8"]]
- 00bcf024 ["INT_ADD", "register:40f0:8", ["const:bcf024:8", "const:4:8"]]
+ 00bcf44c ["INT_ADD", "register:40f0:8", ["const:bcf44c:8", "const:4:8"]]
~~~


### [`00bcf088`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf088.md) → [`00bcf4b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf4b0.md) _ZN8firebase4auth4Auth22SendPasswordResetEmailEPKc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`004977f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bd0098`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0098.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497834`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd04c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd04c0.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 10件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcf67c",
      "incomplete_value": true,
      "site": "00bcf67c",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "00bcf254",
      "incomplete_value": true,
      "site": "00bcf254",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
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
      "definition_site": "00bcf4fc",
      "incomplete_value": true,
      "site": "00bcf500",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf0d4",
      "incomplete_value": true,
      "site": "00bcf0d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              [
                "live",
                "register:4000:8"
              ]
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
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bcf0b8",
      "incomplete_value": false,
      "site": "00bcf0d8",
      "value": [
        "leaf",
        "const:8:8"
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
      160,
      "READ",
      [
        "storage",
        "011263c0",
        null,
        "undefined8"
      ]
    ],
    [
      316,
      "PARAM",
      [
        "storage",
        "002b36d9",
        null,
        "string"
      ]
    ],
    [
      376,
      "READ",
      [
        "storage",
        "00c9b618",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      160,
      "READ",
      [
        "storage",
        "011267c0",
        null,
        "undefined8"
      ]
    ],
    [
      316,
      "PARAM",
      [
        "storage",
        "002b3719",
        null,
        "string"
      ]
    ],
    [
      376,
      "READ",
      [
        "storage",
        "00c9ba18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcf0d8 ["INT_ADD", "register:40f0:8", ["const:bcf0d8:8", "const:4:8"]]
+ 00bcf500 ["INT_ADD", "register:40f0:8", ["const:bcf500:8", "const:4:8"]]
- 00bcf0e4 ["INT_ADD", "register:40f0:8", ["const:bcf0e4:8", "const:4:8"]]
+ 00bcf50c ["INT_ADD", "register:40f0:8", ["const:bcf50c:8", "const:4:8"]]
- 00bcf0ec ["INT_ADD", "register:40f0:8", ["const:bcf0ec:8", "const:4:8"]]
+ 00bcf514 ["INT_ADD", "register:40f0:8", ["const:bcf514:8", "const:4:8"]]
~~~


### [`00bcf2d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf2d4.md) → [`00bcf6fc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf6fc.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorIvEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d900`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d900.md) · 呼出先 6件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a9a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9a0.md) [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00c5dd00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd00.md) · 呼出先 6件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ada0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ada0.md) [`00c5ae00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `store_destination` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcf720",
      "incomplete_value": true,
      "site": "00bcf720",
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
                "const:60:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:ffffffffffffffd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf2f8",
      "incomplete_value": true,
      "site": "00bcf2f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40e8:8"
          ],
          [
            "leaf",
            "const:ffffffffffffffd8:8"
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
      "definition_site": "00bcf720",
      "incomplete_value": true,
      "site": "00bcf720",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:1660:8"
              ],
              [
                "leaf",
                "const:28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf2f8",
      "incomplete_value": true,
      "site": "00bcf2f8",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcf724",
      "incomplete_value": true,
      "site": "00bcf724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:70:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf2fc",
      "incomplete_value": true,
      "site": "00bcf2fc",
      "value": [
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
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


~~~diff
- 00bcf308 ["INT_ADD", "register:40f0:8", ["const:bcf308:8", "const:4:8"]]
+ 00bcf730 ["INT_ADD", "register:40f0:8", ["const:bcf730:8", "const:4:8"]]
- 00bcf310 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00bcf738 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00bcf31c ["INT_ADD", "register:40f0:8", ["const:bcf31c:8", "const:4:8"]]
+ 00bcf744 ["INT_ADD", "register:40f0:8", ["const:bcf744:8", "const:4:8"]]
~~~


### [`00bcf3d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf3d8.md) → [`00bcf800`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf800.md) _ZN8firebase4auth4Auth11UseEmulatorENSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEj

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf850",
      "incomplete_value": true,
      "site": "00bcf864",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:788:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf428",
      "incomplete_value": true,
      "site": "00bcf43c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:388:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00bcf878",
      "incomplete_value": true,
      "site": "00bcf878",
      "value": [
        "LOAD",
        "8",
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
                "const:b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf450",
      "incomplete_value": true,
      "site": "00bcf450",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf86c",
      "incomplete_value": true,
      "site": "00bcf878",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      80,
      "READ",
      [
        "storage",
        "01126388",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      80,
      "READ",
      [
        "storage",
        "01126788",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcf3f4 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
+ 00bcf81c ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
- 00bcf3fc ["BRANCH", null, ["local:b4:8"]]
+ 00bcf824 ["BRANCH", null, ["local:b3:8"]]
- 00bcf408 ["INT_ADD", "register:40f0:8", ["const:bcf408:8", "const:4:8"]]
+ 00bcf830 ["INT_ADD", "register:40f0:8", ["const:bcf830:8", "const:4:8"]]
~~~


### [`00bcf478`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf478.md) → [`00bcf8a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf8a0.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bcd788`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md) · 呼出先 1件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00bcdbb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md) · 呼出先 1件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcf8bc",
      "incomplete_value": true,
      "site": "00bcf8bc",
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
              [
                "live",
                "register:4000:8"
              ]
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
      "definition_site": "00bcf494",
      "incomplete_value": true,
      "site": "00bcf494",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:40a0:8"
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


~~~diff
- 00bcf478 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00bcf8a0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bcf494 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00bcf8bc ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00bcf4a0 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 00bcf8c8 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
~~~


### [`00bcf4fc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf4fc.md) → [`00bcf924`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf924.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4Auth20FetchProvidersResultEEEvRKNS_12FutureHand

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d7d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7d0.md) · 呼出先 10件 [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5dbd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbd0.md) · 呼出先 10件 [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf988",
      "incomplete_value": false,
      "site": "00bcf98c",
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
            "const:e4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf560",
      "incomplete_value": false,
      "site": "00bcf564",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf990",
      "incomplete_value": true,
      "site": "00bcf9a0",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf994",
      "incomplete_value": true,
      "site": "00bcf9a0",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "old": null,
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
      100,
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcf528 ["INT_ADD", "register:40f0:8", ["const:bcf528:8", "const:4:8"]]
+ 00bcf950 ["INT_ADD", "register:40f0:8", ["const:bcf950:8", "const:4:8"]]
- 00bcf534 ["INT_ADD", "register:40f0:8", ["const:bcf534:8", "const:4:8"]]
+ 00bcf95c ["INT_ADD", "register:40f0:8", ["const:bcf95c:8", "const:4:8"]]
- 00bcf538 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00bcf960 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
~~~


### [`00bcf6d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf6d8.md) → [`00bcfb00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfb00.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4Auth20FetchProvidersResultEZNS2_14FutureCallbackIS4_EEvP7_JNIEnvP8_jobje

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d7a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7a0.md) · 呼出先 10件 [`00c5a600`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5dba0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dba0.md) · 呼出先 10件 [`00c5aa00`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcfb6c",
      "incomplete_value": false,
      "site": "00bcfb70",
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
            "const:e4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf744",
      "incomplete_value": false,
      "site": "00bcf748",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
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
        "002a7008",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      108,
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bcf70c ["INT_ADD", "register:40f0:8", ["const:bcf70c:8", "const:4:8"]]
+ 00bcfb34 ["INT_ADD", "register:40f0:8", ["const:bcfb34:8", "const:4:8"]]
- 00bcf718 ["INT_ADD", "register:40f0:8", ["const:bcf718:8", "const:4:8"]]
+ 00bcfb40 ["INT_ADD", "register:40f0:8", ["const:bcfb40:8", "const:4:8"]]
- 00bcf734 ["INT_ADD", "register:40f0:8", ["const:bcf734:8", "const:4:8"]]
+ 00bcfb5c ["INT_ADD", "register:40f0:8", ["const:bcfb5c:8", "const:4:8"]]
~~~


