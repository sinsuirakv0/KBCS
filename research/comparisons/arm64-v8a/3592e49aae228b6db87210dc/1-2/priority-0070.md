# v16.0.0 → v16.0.1 · 最優先の変更候補 (70)

[一覧の目次](README.md)

### [`00af6318`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6318.md) → [`00af6740`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6740.md) FUN_00af6740

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af633c",
      "incomplete_value": true,
      "site": "00af6340",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


~~~diff
- 00af632c ["INT_ADD", "register:40f0:8", ["const:af632c:8", "const:4:8"]]
+ 00af6754 ["INT_ADD", "register:40f0:8", ["const:af6754:8", "const:4:8"]]
- 00af6340 ["INT_ADD", "register:40f0:8", ["const:af6340:8", "const:4:8"]]
+ 00af6768 ["INT_ADD", "register:40f0:8", ["const:af6768:8", "const:4:8"]]
- 00af6344 ["CBRANCH", null, ["local:b4:8", "tmp:3:1"]]
+ 00af676c ["CBRANCH", null, ["local:b5:8", "tmp:3:1"]]
~~~


### [`00af6388`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6388.md) → [`00af67b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af67b0.md) FUN_00af67b0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00710090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007100d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af67b4",
      "incomplete_value": true,
      "site": "00af67b4",
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
      "definition_site": "00af638c",
      "incomplete_value": true,
      "site": "00af638c",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af67b4",
      "incomplete_value": true,
      "site": "00af67b4",
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
      "definition_site": "00af638c",
      "incomplete_value": true,
      "site": "00af638c",
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
    "ordinal": 3,
    "slot": 1
  }
]
~~~


~~~diff
- 00af639c ["INT_ADD", "register:40f0:8", ["const:af639c:8", "const:4:8"]]
+ 00af67c4 ["INT_ADD", "register:40f0:8", ["const:af67c4:8", "const:4:8"]]
- 00af63b0 ["INT_ADD", "register:40f0:8", ["const:af63b0:8", "const:4:8"]]
+ 00af67d8 ["INT_ADD", "register:40f0:8", ["const:af67d8:8", "const:4:8"]]
- 00af63b4 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
+ 00af67dc ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
~~~


### [`00af63f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af63f8.md) → [`00af6820`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6820.md) FUN_00af6820

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`00710090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md) [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) [`00716d50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 4件 [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007100d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) [`00716d90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af6824",
      "incomplete_value": true,
      "site": "00af6824",
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
      "definition_site": "00af63fc",
      "incomplete_value": true,
      "site": "00af63fc",
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
      "definition_site": "00af6824",
      "incomplete_value": true,
      "site": "00af6824",
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
      "definition_site": "00af63fc",
      "incomplete_value": true,
      "site": "00af63fc",
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
  }
]
~~~


~~~diff
- 00af640c ["INT_ADD", "register:40f0:8", ["const:af640c:8", "const:4:8"]]
+ 00af6834 ["INT_ADD", "register:40f0:8", ["const:af6834:8", "const:4:8"]]
- 00af6420 ["INT_ADD", "register:40f0:8", ["const:af6420:8", "const:4:8"]]
+ 00af6848 ["INT_ADD", "register:40f0:8", ["const:af6848:8", "const:4:8"]]
- 00af6424 ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
+ 00af684c ["CBRANCH", null, ["local:b13:8", "tmp:3:1"]]
~~~


### [`00af6468`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6468.md) → [`00af6890`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6890.md) FUN_00af6890

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00710090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007100d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af68b4",
      "incomplete_value": true,
      "site": "00af68b8",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


~~~diff
- 00af647c ["INT_ADD", "register:40f0:8", ["const:af647c:8", "const:4:8"]]
+ 00af68a4 ["INT_ADD", "register:40f0:8", ["const:af68a4:8", "const:4:8"]]
- 00af6490 ["INT_ADD", "register:40f0:8", ["const:af6490:8", "const:4:8"]]
+ 00af68b8 ["INT_ADD", "register:40f0:8", ["const:af68b8:8", "const:4:8"]]
- 00af6494 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
+ 00af68bc ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
~~~


### [`00af65b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af65b8.md) → [`00af69e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af69e0.md) FUN_00af69e0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 7件 [`005fb400`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb400.md) [`005fb8fc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb8fc.md) [`00700ab8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`00710090`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 7件 [`005fb440`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb440.md) [`005fb93c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb93c.md) [`00700af8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007100d0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af6a04",
      "incomplete_value": true,
      "site": "00af6a08",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


~~~diff
- 00af65cc ["INT_ADD", "register:40f0:8", ["const:af65cc:8", "const:4:8"]]
+ 00af69f4 ["INT_ADD", "register:40f0:8", ["const:af69f4:8", "const:4:8"]]
- 00af65e0 ["INT_ADD", "register:40f0:8", ["const:af65e0:8", "const:4:8"]]
+ 00af6a08 ["INT_ADD", "register:40f0:8", ["const:af6a08:8", "const:4:8"]]
- 00af65e4 ["CBRANCH", null, ["local:b5:8", "tmp:3:1"]]
+ 00af6a0c ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
~~~


### [`00af6628`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6628.md) → [`00af6a50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6a50.md) FUN_00af6a50

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

~~~diff
- 00af663c ["INT_ADD", "register:40f0:8", ["const:af663c:8", "const:4:8"]]
+ 00af6a64 ["INT_ADD", "register:40f0:8", ["const:af6a64:8", "const:4:8"]]
- 00af6650 ["INT_ADD", "register:40f0:8", ["const:af6650:8", "const:4:8"]]
+ 00af6a78 ["INT_ADD", "register:40f0:8", ["const:af6a78:8", "const:4:8"]]
- 00af6654 ["CBRANCH", null, ["local:b4:8", "tmp:3:1"]]
+ 00af6a7c ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
~~~


### [`00af6698`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6698.md) → [`00af6ac0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6ac0.md) FUN_00af6ac0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af6ae4",
      "incomplete_value": true,
      "site": "00af6ae8",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


~~~diff
- 00af66ac ["INT_ADD", "register:40f0:8", ["const:af66ac:8", "const:4:8"]]
+ 00af6ad4 ["INT_ADD", "register:40f0:8", ["const:af6ad4:8", "const:4:8"]]
- 00af66c0 ["INT_ADD", "register:40f0:8", ["const:af66c0:8", "const:4:8"]]
+ 00af6ae8 ["INT_ADD", "register:40f0:8", ["const:af6ae8:8", "const:4:8"]]
- 00af66c4 ["CBRANCH", null, ["local:b12:8", "tmp:3:1"]]
+ 00af6aec ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
~~~


### [`00af67e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af67e8.md) → [`00af6c10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6c10.md) FUN_00af6c10

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af6c14",
      "incomplete_value": true,
      "site": "00af6c14",
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
      "definition_site": "00af67ec",
      "incomplete_value": true,
      "site": "00af67ec",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af6c14",
      "incomplete_value": true,
      "site": "00af6c14",
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
      "definition_site": "00af67ec",
      "incomplete_value": true,
      "site": "00af67ec",
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
      "definition_site": "00af6c18",
      "incomplete_value": true,
      "site": "00af6c18",
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
    "old": {
      "definition_site": "00af67f0",
      "incomplete_value": true,
      "site": "00af67f0",
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
    "ordinal": 4,
    "slot": 1
  }
]
~~~


~~~diff
- 00af6804 ["INT_ADD", "register:40f0:8", ["const:af6804:8", "const:4:8"]]
+ 00af6c2c ["INT_ADD", "register:40f0:8", ["const:af6c2c:8", "const:4:8"]]
- 00af6818 ["INT_ADD", "register:40f0:8", ["const:af6818:8", "const:4:8"]]
+ 00af6c40 ["INT_ADD", "register:40f0:8", ["const:af6c40:8", "const:4:8"]]
- 00af6824 ["INT_ADD", "register:40f0:8", ["const:af6824:8", "const:4:8"]]
+ 00af6c4c ["INT_ADD", "register:40f0:8", ["const:af6c4c:8", "const:4:8"]]
~~~


### [`00af6900`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6900.md) → [`00af6d28`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6d28.md) FUN_00af6d28

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af6d60",
      "incomplete_value": true,
      "site": "00af6d60",
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
                "register:4040:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af6938",
      "incomplete_value": true,
      "site": "00af6938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af691c ["INT_ADD", "register:40f0:8", ["const:af691c:8", "const:4:8"]]
+ 00af6d44 ["INT_ADD", "register:40f0:8", ["const:af6d44:8", "const:4:8"]]
~~~


### [`00af6a18`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6a18.md) → [`00af6e40`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6e40.md) FUN_00af6e40

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af6a34 ["INT_ADD", "register:40f0:8", ["const:af6a34:8", "const:4:8"]]
+ 00af6e5c ["INT_ADD", "register:40f0:8", ["const:af6e5c:8", "const:4:8"]]
~~~


### [`00af6a64`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6a64.md) → [`00af6e8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6e8c.md) FUN_00af6e8c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af6a80 ["INT_ADD", "register:40f0:8", ["const:af6a80:8", "const:4:8"]]
+ 00af6ea8 ["INT_ADD", "register:40f0:8", ["const:af6ea8:8", "const:4:8"]]
~~~


### [`00af6b94`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6b94.md) → [`00af6fbc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6fbc.md) FUN_00af6fbc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00af6bb0 ["INT_ADD", "register:40f0:8", ["const:af6bb0:8", "const:4:8"]]
+ 00af6fd8 ["INT_ADD", "register:40f0:8", ["const:af6fd8:8", "const:4:8"]]
~~~


### [`00af6c2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6c2c.md) → [`00af7054`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7054.md) FUN_00af7054

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af7058",
      "incomplete_value": true,
      "site": "00af7058",
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
      "definition_site": "00af6c30",
      "incomplete_value": true,
      "site": "00af6c30",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af705c",
      "incomplete_value": true,
      "site": "00af705c",
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
    "old": {
      "definition_site": "00af6c34",
      "incomplete_value": true,
      "site": "00af6c34",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af705c",
      "incomplete_value": true,
      "site": "00af705c",
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
    "old": {
      "definition_site": "00af6c34",
      "incomplete_value": true,
      "site": "00af6c34",
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
    "ordinal": 4,
    "slot": 1
  }
]
~~~


~~~diff
- 00af6c48 ["INT_ADD", "register:40f0:8", ["const:af6c48:8", "const:4:8"]]
+ 00af7070 ["INT_ADD", "register:40f0:8", ["const:af7070:8", "const:4:8"]]
~~~


### [`00af6ce8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6ce8.md) → [`00af7110`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7110.md) FUN_00af7110

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00af6d04 ["INT_ADD", "register:40f0:8", ["const:af6d04:8", "const:4:8"]]
+ 00af712c ["INT_ADD", "register:40f0:8", ["const:af712c:8", "const:4:8"]]
~~~


### [`00af6d34`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6d34.md) → [`00af715c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af715c.md) FUN_00af715c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

~~~diff
- 00af6d48 ["INT_ADD", "register:40f0:8", ["const:af6d48:8", "const:4:8"]]
+ 00af7170 ["INT_ADD", "register:40f0:8", ["const:af7170:8", "const:4:8"]]
- 00af6d5c ["INT_ADD", "register:40f0:8", ["const:af6d5c:8", "const:4:8"]]
+ 00af7184 ["INT_ADD", "register:40f0:8", ["const:af7184:8", "const:4:8"]]
- 00af6d60 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
+ 00af7188 ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
~~~


### [`00af6da4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6da4.md) → [`00af71cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af71cc.md) FUN_00af71cc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af6dc0 ["INT_ADD", "register:40f0:8", ["const:af6dc0:8", "const:4:8"]]
+ 00af71e8 ["INT_ADD", "register:40f0:8", ["const:af71e8:8", "const:4:8"]]
~~~


### [`00af6df0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6df0.md) → [`00af7218`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7218.md) FUN_00af7218

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`00710298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710298.md) [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007102d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

~~~diff
- 00af6e04 ["INT_ADD", "register:40f0:8", ["const:af6e04:8", "const:4:8"]]
+ 00af722c ["INT_ADD", "register:40f0:8", ["const:af722c:8", "const:4:8"]]
- 00af6e18 ["INT_ADD", "register:40f0:8", ["const:af6e18:8", "const:4:8"]]
+ 00af7240 ["INT_ADD", "register:40f0:8", ["const:af7240:8", "const:4:8"]]
- 00af6e1c ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
+ 00af7244 ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
~~~


### [`00af6eac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6eac.md) → [`00af72d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af72d4.md) FUN_00af72d4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af6ec0 ["INT_ADD", "register:40f0:8", ["const:af6ec0:8", "const:4:8"]]
+ 00af72e8 ["INT_ADD", "register:40f0:8", ["const:af72e8:8", "const:4:8"]]
~~~


### [`00af6f88`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6f88.md) → [`00af73b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af73b0.md) FUN_00af73b0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af73e8",
      "incomplete_value": true,
      "site": "00af73e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af6fc0",
      "incomplete_value": true,
      "site": "00af6fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af6fa4 ["INT_ADD", "register:40f0:8", ["const:af6fa4:8", "const:4:8"]]
+ 00af73cc ["INT_ADD", "register:40f0:8", ["const:af73cc:8", "const:4:8"]]
~~~


### [`00af6fd4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6fd4.md) → [`00af73fc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af73fc.md) FUN_00af73fc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00713318`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`0071421c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00713358`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`0071425c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate, store_destination

アドレスに依存する影響 `return_value_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af7400",
      "incomplete_value": true,
      "site": "00af7400",
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
      "definition_site": "00af6fd8",
      "incomplete_value": true,
      "site": "00af6fd8",
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
      "definition_site": "00af7400",
      "incomplete_value": true,
      "site": "00af7400",
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
      "definition_site": "00af6fd8",
      "incomplete_value": true,
      "site": "00af6fd8",
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
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af742c",
      "incomplete_value": true,
      "site": "00af7438",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00af7004",
      "incomplete_value": true,
      "site": "00af7010",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


~~~diff
- 00af6fe8 ["INT_ADD", "register:40f0:8", ["const:af6fe8:8", "const:4:8"]]
+ 00af7410 ["INT_ADD", "register:40f0:8", ["const:af7410:8", "const:4:8"]]
~~~


### [`00af7014`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7014.md) → [`00af743c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af743c.md) FUN_00af743c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00af7030 ["INT_ADD", "register:40f0:8", ["const:af7030:8", "const:4:8"]]
+ 00af7458 ["INT_ADD", "register:40f0:8", ["const:af7458:8", "const:4:8"]]
~~~


### [`00af7060`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7060.md) → [`00af7488`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7488.md) FUN_00af7488

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af707c ["INT_ADD", "register:40f0:8", ["const:af707c:8", "const:4:8"]]
+ 00af74a4 ["INT_ADD", "register:40f0:8", ["const:af74a4:8", "const:4:8"]]
~~~


### [`00af7178`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7178.md) → [`00af75a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af75a0.md) FUN_00af75a0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00713ce4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713ce4.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00713d24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af718c ["INT_ADD", "register:40f0:8", ["const:af718c:8", "const:4:8"]]
+ 00af75b4 ["INT_ADD", "register:40f0:8", ["const:af75b4:8", "const:4:8"]]
~~~


### [`00af7200`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7200.md) → [`00af7628`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7628.md) FUN_00af7628

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af721c ["INT_ADD", "register:40f0:8", ["const:af721c:8", "const:4:8"]]
+ 00af7644 ["INT_ADD", "register:40f0:8", ["const:af7644:8", "const:4:8"]]
~~~


### [`00af724c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af724c.md) → [`00af7674`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7674.md) FUN_00af7674

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00700ab8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00700af8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

~~~diff
- 00af7260 ["INT_ADD", "register:40f0:8", ["const:af7260:8", "const:4:8"]]
+ 00af7688 ["INT_ADD", "register:40f0:8", ["const:af7688:8", "const:4:8"]]
- 00af7274 ["INT_ADD", "register:40f0:8", ["const:af7274:8", "const:4:8"]]
+ 00af769c ["INT_ADD", "register:40f0:8", ["const:af769c:8", "const:4:8"]]
- 00af7278 ["CBRANCH", null, ["local:b4:8", "tmp:3:1"]]
+ 00af76a0 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
~~~


### [`00af72bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af72bc.md) → [`00af76e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af76e4.md) FUN_00af76e4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

~~~diff
- 00af72d8 ["INT_ADD", "register:40f0:8", ["const:af72d8:8", "const:4:8"]]
+ 00af7700 ["INT_ADD", "register:40f0:8", ["const:af7700:8", "const:4:8"]]
- 00af72ec ["INT_ADD", "register:40f0:8", ["const:af72ec:8", "const:4:8"]]
+ 00af7714 ["INT_ADD", "register:40f0:8", ["const:af7714:8", "const:4:8"]]
- 00af72f0 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
+ 00af7718 ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
~~~


### [`00af739c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af739c.md) → [`00af77c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af77c4.md) FUN_00af77c4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

~~~diff
- 00af73b8 ["INT_ADD", "register:40f0:8", ["const:af73b8:8", "const:4:8"]]
+ 00af77e0 ["INT_ADD", "register:40f0:8", ["const:af77e0:8", "const:4:8"]]
- 00af73cc ["INT_ADD", "register:40f0:8", ["const:af73cc:8", "const:4:8"]]
+ 00af77f4 ["INT_ADD", "register:40f0:8", ["const:af77f4:8", "const:4:8"]]
- 00af73d0 ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
+ 00af77f8 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
~~~


### [`00af7474`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7474.md) → [`00af789c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af789c.md) FUN_00af789c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af78f4",
      "incomplete_value": true,
      "site": "00af78f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af74cc",
      "incomplete_value": true,
      "site": "00af74cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
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
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af7490 ["INT_ADD", "register:40f0:8", ["const:af7490:8", "const:4:8"]]
+ 00af78b8 ["INT_ADD", "register:40f0:8", ["const:af78b8:8", "const:4:8"]]
- 00af74a4 ["INT_ADD", "register:40f0:8", ["const:af74a4:8", "const:4:8"]]
+ 00af78cc ["INT_ADD", "register:40f0:8", ["const:af78cc:8", "const:4:8"]]
- 00af74a8 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
+ 00af78d0 ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
~~~


### [`00af74e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af74e0.md) → [`00af7908`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7908.md) FUN_00af7908

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af7910",
      "incomplete_value": true,
      "site": "00af7910",
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
      "definition_site": "00af74e8",
      "incomplete_value": true,
      "site": "00af74e8",
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
      "definition_site": "00af7910",
      "incomplete_value": true,
      "site": "00af7910",
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
      "definition_site": "00af74e8",
      "incomplete_value": true,
      "site": "00af74e8",
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
      "definition_site": "00af7940",
      "incomplete_value": true,
      "site": "00af7940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af7518",
      "incomplete_value": true,
      "site": "00af7518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af74fc ["INT_ADD", "register:40f0:8", ["const:af74fc:8", "const:4:8"]]
+ 00af7924 ["INT_ADD", "register:40f0:8", ["const:af7924:8", "const:4:8"]]
~~~


### [`00af752c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af752c.md) → [`00af7954`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7954.md) FUN_00af7954

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 3件 [`007078ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/007078ec.md) [`00713318`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`0071421c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`0070792c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/0070792c.md) [`00713358`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`0071425c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      68,
      "DATA",
      [
        "storage",
        "0030a34c",
        null,
        null
      ]
    ],
    [
      124,
      "DATA",
      [
        "storage",
        "0030a358",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      68,
      "DATA",
      [
        "storage",
        "0030a38c",
        null,
        null
      ]
    ],
    [
      124,
      "DATA",
      [
        "storage",
        "0030a398",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00af7548 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
+ 00af7970 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00af7550 ["INT_ADD", "register:40f0:8", ["const:af7550:8", "const:4:8"]]
+ 00af7978 ["INT_ADD", "register:40f0:8", ["const:af7978:8", "const:4:8"]]
- 00af756c ["COPY", "tmp:0:8", ["const:34c:8"]]
+ 00af7994 ["COPY", "tmp:0:8", ["const:38c:8"]]
~~~


### [`00af7610`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7610.md) → [`00af7a38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7a38.md) FUN_00af7a38

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af7a8c",
      "incomplete_value": true,
      "site": "00af7a8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af7664",
      "incomplete_value": true,
      "site": "00af7664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      68,
      "DATA",
      [
        "storage",
        "002c3ecc",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      68,
      "DATA",
      [
        "storage",
        "002c3f0c",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00af7610 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00af7a38 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00af7634 ["INT_ADD", "register:40f0:8", ["const:af7634:8", "const:4:8"]]
+ 00af7a5c ["INT_ADD", "register:40f0:8", ["const:af7a5c:8", "const:4:8"]]
- 00af7640 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 00af7a68 ["COPY", "tmp:0:8", ["const:f10:8"]]
~~~


### [`00af7784`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7784.md) → [`00af7bac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7bac.md) FUN_00af7bac

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af7bf8",
      "incomplete_value": true,
      "site": "00af7bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af77d0",
      "incomplete_value": true,
      "site": "00af77d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
        "0030a358",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      60,
      "DATA",
      [
        "storage",
        "0030a398",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00af77a4 ["INT_ADD", "register:40f0:8", ["const:af77a4:8", "const:4:8"]]
+ 00af7bcc ["INT_ADD", "register:40f0:8", ["const:af7bcc:8", "const:4:8"]]
- 00af77bc ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00af7be4 ["COPY", "tmp:0:8", ["const:398:8"]]
~~~


### [`00af77e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af77e4.md) → [`00af7c0c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7c0c.md) FUN_00af7c0c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`007078ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/007078ec.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`0070792c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/0070792c.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af7d0c",
      "incomplete_value": true,
      "site": "00af7d1c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      68,
      "DATA",
      [
        "storage",
        "0030a34c",
        null,
        null
      ]
    ],
    [
      124,
      "DATA",
      [
        "storage",
        "0030a358",
        null,
        "undefined4"
      ]
    ],
    [
      240,
      "READ",
      [
        "storage",
        "0030a364",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      68,
      "DATA",
      [
        "storage",
        "0030a38c",
        null,
        null
      ]
    ],
    [
      124,
      "DATA",
      [
        "storage",
        "0030a398",
        null,
        "undefined4"
      ]
    ],
    [
      240,
      "READ",
      [
        "storage",
        "0030a3a4",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00af7800 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
+ 00af7c28 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 00af7808 ["INT_ADD", "register:40f0:8", ["const:af7808:8", "const:4:8"]]
+ 00af7c30 ["INT_ADD", "register:40f0:8", ["const:af7c30:8", "const:4:8"]]
- 00af7824 ["COPY", "tmp:0:8", ["const:34c:8"]]
+ 00af7c4c ["COPY", "tmp:0:8", ["const:38c:8"]]
~~~


### [`00af78f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af78f8.md) → [`00af7d20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7d20.md) FUN_00af7d20

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af7d6c",
      "incomplete_value": true,
      "site": "00af7d6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af7944",
      "incomplete_value": true,
      "site": "00af7944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
        "0030a364",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      60,
      "DATA",
      [
        "storage",
        "0030a3a4",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00af7918 ["INT_ADD", "register:40f0:8", ["const:af7918:8", "const:4:8"]]
+ 00af7d40 ["INT_ADD", "register:40f0:8", ["const:af7d40:8", "const:4:8"]]
- 00af7930 ["COPY", "tmp:0:8", ["const:364:8"]]
+ 00af7d58 ["COPY", "tmp:0:8", ["const:3a4:8"]]
~~~


### [`00af79a0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af79a0.md) → [`00af7dc8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7dc8.md) FUN_00af7dc8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00713ce4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713ce4.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00713d24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00af79b4 ["INT_ADD", "register:40f0:8", ["const:af79b4:8", "const:4:8"]]
+ 00af7ddc ["INT_ADD", "register:40f0:8", ["const:af7ddc:8", "const:4:8"]]
~~~


### [`00af7a6c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7a6c.md) → [`00af7e94`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7e94.md) FUN_00af7e94

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af7ecc",
      "incomplete_value": true,
      "site": "00af7ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
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
        ]
      ]
    },
    "old": {
      "definition_site": "00af7aa4",
      "incomplete_value": true,
      "site": "00af7aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af7a88 ["INT_ADD", "register:40f0:8", ["const:af7a88:8", "const:4:8"]]
+ 00af7eb0 ["INT_ADD", "register:40f0:8", ["const:af7eb0:8", "const:4:8"]]
~~~


### [`00af7ab8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7ab8.md) → [`00af7ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7ee0.md) FUN_00af7ee0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00710298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710298.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007102d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate, store_destination

アドレスに依存する影響 `return_value_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af7ee4",
      "incomplete_value": true,
      "site": "00af7ee4",
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
      "definition_site": "00af7abc",
      "incomplete_value": true,
      "site": "00af7abc",
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
      "definition_site": "00af7ee4",
      "incomplete_value": true,
      "site": "00af7ee4",
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
      "definition_site": "00af7abc",
      "incomplete_value": true,
      "site": "00af7abc",
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
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af7f10",
      "incomplete_value": true,
      "site": "00af7f1c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00af7ae8",
      "incomplete_value": true,
      "site": "00af7af4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


~~~diff
- 00af7acc ["INT_ADD", "register:40f0:8", ["const:af7acc:8", "const:4:8"]]
+ 00af7ef4 ["INT_ADD", "register:40f0:8", ["const:af7ef4:8", "const:4:8"]]
~~~


### [`00af7af8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7af8.md) → [`00af7f20`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7f20.md) FUN_00af7f20

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af7b14 ["INT_ADD", "register:40f0:8", ["const:af7b14:8", "const:4:8"]]
+ 00af7f3c ["INT_ADD", "register:40f0:8", ["const:af7f3c:8", "const:4:8"]]
~~~


### [`00af7b44`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7b44.md) → [`00af7f6c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7f6c.md) FUN_00af7f6c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00710298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710298.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007102d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af7b58 ["INT_ADD", "register:40f0:8", ["const:af7b58:8", "const:4:8"]]
+ 00af7f80 ["INT_ADD", "register:40f0:8", ["const:af7f80:8", "const:4:8"]]
~~~


### [`00af7b84`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7b84.md) → [`00af7fac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7fac.md) FUN_00af7fac

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af7fe4",
      "incomplete_value": true,
      "site": "00af7fe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af7bbc",
      "incomplete_value": true,
      "site": "00af7bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af7ba0 ["INT_ADD", "register:40f0:8", ["const:af7ba0:8", "const:4:8"]]
+ 00af7fc8 ["INT_ADD", "register:40f0:8", ["const:af7fc8:8", "const:4:8"]]
~~~


### [`00af7bd0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7bd0.md) → [`00af7ff8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7ff8.md) FUN_00af7ff8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00713ce4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713ce4.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00713d24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00af7c08",
      "incomplete_value": true,
      "site": "00af7c14",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
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


~~~diff
- 00af7be4 ["INT_ADD", "register:40f0:8", ["const:af7be4:8", "const:4:8"]]
+ 00af800c ["INT_ADD", "register:40f0:8", ["const:af800c:8", "const:4:8"]]
~~~


### [`00af7c18`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7c18.md) → [`00af8040`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8040.md) FUN_00af8040

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00713ce4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713ce4.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00713d24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af8070",
      "incomplete_value": true,
      "site": "00af807c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00af7c48",
      "incomplete_value": true,
      "site": "00af7c54",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


~~~diff
- 00af7c2c ["INT_ADD", "register:40f0:8", ["const:af7c2c:8", "const:4:8"]]
+ 00af8054 ["INT_ADD", "register:40f0:8", ["const:af8054:8", "const:4:8"]]
~~~


### [`00af7c58`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7c58.md) → [`00af8080`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8080.md) FUN_00af8080

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00713ce4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713ce4.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00713d24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00af7c90",
      "incomplete_value": true,
      "site": "00af7c9c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
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


~~~diff
- 00af7c6c ["INT_ADD", "register:40f0:8", ["const:af7c6c:8", "const:4:8"]]
+ 00af8094 ["INT_ADD", "register:40f0:8", ["const:af8094:8", "const:4:8"]]
~~~


### [`00af7ca0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7ca0.md) → [`00af80c8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af80c8.md) FUN_00af80c8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00713ce4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713ce4.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00713d24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00af7cd0",
      "incomplete_value": true,
      "site": "00af7cdc",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


~~~diff
- 00af7cb4 ["INT_ADD", "register:40f0:8", ["const:af7cb4:8", "const:4:8"]]
+ 00af80dc ["INT_ADD", "register:40f0:8", ["const:af80dc:8", "const:4:8"]]
~~~


### [`00af7d2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7d2c.md) → [`00af8154`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8154.md) FUN_00af8154

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate, store_destination

アドレスに依存する影響 `return_value_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8158",
      "incomplete_value": true,
      "site": "00af8158",
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
      "definition_site": "00af7d30",
      "incomplete_value": true,
      "site": "00af7d30",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8158",
      "incomplete_value": true,
      "site": "00af8158",
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
      "definition_site": "00af7d30",
      "incomplete_value": true,
      "site": "00af7d30",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00af7d5c",
      "incomplete_value": true,
      "site": "00af7d68",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


~~~diff
- 00af7d40 ["INT_ADD", "register:40f0:8", ["const:af7d40:8", "const:4:8"]]
+ 00af8168 ["INT_ADD", "register:40f0:8", ["const:af8168:8", "const:4:8"]]
~~~


### [`00af7db8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7db8.md) → [`00af81e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af81e0.md) FUN_00af81e0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00713318`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`0071421c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) [`00714f4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`00713358`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`0071425c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) [`00714f8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af8210",
      "incomplete_value": true,
      "site": "00af821c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00af7de8",
      "incomplete_value": true,
      "site": "00af7df4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


~~~diff
- 00af7dcc ["INT_ADD", "register:40f0:8", ["const:af7dcc:8", "const:4:8"]]
+ 00af81f4 ["INT_ADD", "register:40f0:8", ["const:af81f4:8", "const:4:8"]]
~~~


### [`00af7e38`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7e38.md) → [`00af8260`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8260.md) FUN_00af8260

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00af7e54 ["INT_ADD", "register:40f0:8", ["const:af7e54:8", "const:4:8"]]
+ 00af827c ["INT_ADD", "register:40f0:8", ["const:af827c:8", "const:4:8"]]
~~~


### [`00af7ec4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7ec4.md) → [`00af82ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af82ec.md) FUN_00af82ec

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af82f0",
      "incomplete_value": true,
      "site": "00af82f0",
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
      "definition_site": "00af7ec8",
      "incomplete_value": true,
      "site": "00af7ec8",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af82f4",
      "incomplete_value": true,
      "site": "00af82f4",
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
    "old": {
      "definition_site": "00af7ecc",
      "incomplete_value": true,
      "site": "00af7ecc",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af82f4",
      "incomplete_value": true,
      "site": "00af82f4",
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
    "old": {
      "definition_site": "00af7ecc",
      "incomplete_value": true,
      "site": "00af7ecc",
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
    "ordinal": 4,
    "slot": 1
  }
]
~~~


~~~diff
- 00af7ee0 ["INT_ADD", "register:40f0:8", ["const:af7ee0:8", "const:4:8"]]
+ 00af8308 ["INT_ADD", "register:40f0:8", ["const:af8308:8", "const:4:8"]]
~~~


### [`00af7f10`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7f10.md) → [`00af8338`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8338.md) FUN_00af8338

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00713318`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`0071421c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) [`00714f4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`00713358`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`0071425c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) [`00714f8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af8368",
      "incomplete_value": true,
      "site": "00af8374",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "old": null,
    "ordinal": 0,
    "slot": 0
  }
]
~~~


~~~diff
- 00af7f24 ["INT_ADD", "register:40f0:8", ["const:af7f24:8", "const:4:8"]]
+ 00af834c ["INT_ADD", "register:40f0:8", ["const:af834c:8", "const:4:8"]]
~~~


### [`00af7f50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7f50.md) → [`00af8378`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8378.md) FUN_00af8378

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00af7f6c ["INT_ADD", "register:40f0:8", ["const:af7f6c:8", "const:4:8"]]
+ 00af8394 ["INT_ADD", "register:40f0:8", ["const:af8394:8", "const:4:8"]]
~~~


### [`00af7f9c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7f9c.md) → [`00af83c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af83c4.md) FUN_00af83c4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00713318`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`0071421c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) [`00714f4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`00713358`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`0071425c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) [`00714f8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af7fb0 ["INT_ADD", "register:40f0:8", ["const:af7fb0:8", "const:4:8"]]
+ 00af83d8 ["INT_ADD", "register:40f0:8", ["const:af83d8:8", "const:4:8"]]
~~~


### [`00af7fdc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7fdc.md) → [`00af8404`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8404.md) FUN_00af8404

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af7ff8 ["INT_ADD", "register:40f0:8", ["const:af7ff8:8", "const:4:8"]]
+ 00af8420 ["INT_ADD", "register:40f0:8", ["const:af8420:8", "const:4:8"]]
~~~


### [`00af8028`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8028.md) → [`00af8450`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8450.md) FUN_00af8450

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af8044 ["INT_ADD", "register:40f0:8", ["const:af8044:8", "const:4:8"]]
+ 00af846c ["INT_ADD", "register:40f0:8", ["const:af846c:8", "const:4:8"]]
~~~


### [`00af8074`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8074.md) → [`00af849c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af849c.md) FUN_00af849c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af84d4",
      "incomplete_value": true,
      "site": "00af84d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
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
        ]
      ]
    },
    "old": {
      "definition_site": "00af80ac",
      "incomplete_value": true,
      "site": "00af80ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af8090 ["INT_ADD", "register:40f0:8", ["const:af8090:8", "const:4:8"]]
+ 00af84b8 ["INT_ADD", "register:40f0:8", ["const:af84b8:8", "const:4:8"]]
~~~


### [`00af80c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af80c0.md) → [`00af84e8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af84e8.md) FUN_00af84e8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00714f4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) [`007154c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) [`00716d50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`00714f8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) [`00715500`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) [`00716d90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00af80d4 ["INT_ADD", "register:40f0:8", ["const:af80d4:8", "const:4:8"]]
+ 00af84fc ["INT_ADD", "register:40f0:8", ["const:af84fc:8", "const:4:8"]]
~~~


### [`00af8100`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8100.md) → [`00af8528`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8528.md) FUN_00af8528

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8560",
      "incomplete_value": true,
      "site": "00af8560",
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
                "register:4040:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af8138",
      "incomplete_value": true,
      "site": "00af8138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af811c ["INT_ADD", "register:40f0:8", ["const:af811c:8", "const:4:8"]]
+ 00af8544 ["INT_ADD", "register:40f0:8", ["const:af8544:8", "const:4:8"]]
~~~


### [`00af814c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af814c.md) → [`00af8574`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8574.md) FUN_00af8574

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00714f4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) [`007154c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) [`00716d50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`00714f8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) [`00715500`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) [`00716d90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00af817c",
      "incomplete_value": true,
      "site": "00af8188",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


~~~diff
- 00af8160 ["INT_ADD", "register:40f0:8", ["const:af8160:8", "const:4:8"]]
+ 00af8588 ["INT_ADD", "register:40f0:8", ["const:af8588:8", "const:4:8"]]
~~~


### [`00af818c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af818c.md) → [`00af85b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af85b4.md) FUN_00af85b4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af81a8 ["INT_ADD", "register:40f0:8", ["const:af81a8:8", "const:4:8"]]
+ 00af85d0 ["INT_ADD", "register:40f0:8", ["const:af85d0:8", "const:4:8"]]
~~~


### [`00af82a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af82a4.md) → [`00af86cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af86cc.md) FUN_00af86cc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af82c0 ["INT_ADD", "register:40f0:8", ["const:af82c0:8", "const:4:8"]]
+ 00af86e8 ["INT_ADD", "register:40f0:8", ["const:af86e8:8", "const:4:8"]]
~~~


### [`00af82f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af82f0.md) → [`00af8718`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8718.md) FUN_00af8718

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00714f4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) [`007154c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) [`00716d50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`00714f8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) [`00715500`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) [`00716d90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af8748",
      "incomplete_value": true,
      "site": "00af8754",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "old": null,
    "ordinal": 0,
    "slot": 0
  }
]
~~~


~~~diff
- 00af8304 ["INT_ADD", "register:40f0:8", ["const:af8304:8", "const:4:8"]]
+ 00af872c ["INT_ADD", "register:40f0:8", ["const:af872c:8", "const:4:8"]]
~~~


### [`00af837c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af837c.md) → [`00af87a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af87a4.md) FUN_00af87a4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00714f4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00714f8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af87dc",
      "incomplete_value": true,
      "site": "00af87e8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
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


~~~diff
- 00af8390 ["INT_ADD", "register:40f0:8", ["const:af8390:8", "const:4:8"]]
+ 00af87b8 ["INT_ADD", "register:40f0:8", ["const:af87b8:8", "const:4:8"]]
~~~


### [`00af83c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af83c4.md) → [`00af87ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af87ec.md) FUN_00af87ec

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00714f4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00714f8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8824",
      "incomplete_value": true,
      "site": "00af8824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af83fc",
      "incomplete_value": true,
      "site": "00af83fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af83e0 ["INT_ADD", "register:40f0:8", ["const:af83e0:8", "const:4:8"]]
+ 00af8808 ["INT_ADD", "register:40f0:8", ["const:af8808:8", "const:4:8"]]
~~~


### [`00af8410`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8410.md) → [`00af8838`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8838.md) FUN_00af8838

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00714f4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00714f8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af8868",
      "incomplete_value": true,
      "site": "00af8874",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00af8440",
      "incomplete_value": true,
      "site": "00af844c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


~~~diff
- 00af8424 ["INT_ADD", "register:40f0:8", ["const:af8424:8", "const:4:8"]]
+ 00af884c ["INT_ADD", "register:40f0:8", ["const:af884c:8", "const:4:8"]]
~~~


### [`00af8450`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8450.md) → [`00af8878`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8878.md) FUN_00af8878

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af88b0",
      "incomplete_value": true,
      "site": "00af88b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af8488",
      "incomplete_value": true,
      "site": "00af8488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af846c ["INT_ADD", "register:40f0:8", ["const:af846c:8", "const:4:8"]]
+ 00af8894 ["INT_ADD", "register:40f0:8", ["const:af8894:8", "const:4:8"]]
~~~


### [`00af849c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af849c.md) → [`00af88c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af88c4.md) FUN_00af88c4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00714f4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00714f8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00af84d4",
      "incomplete_value": true,
      "site": "00af84e0",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
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


~~~diff
- 00af84b0 ["INT_ADD", "register:40f0:8", ["const:af84b0:8", "const:4:8"]]
+ 00af88d8 ["INT_ADD", "register:40f0:8", ["const:af88d8:8", "const:4:8"]]
~~~


### [`00af84e4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af84e4.md) → [`00af890c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af890c.md) FUN_00af890c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00714f4c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00714f8c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8910",
      "incomplete_value": true,
      "site": "00af8910",
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
      "definition_site": "00af84e8",
      "incomplete_value": true,
      "site": "00af84e8",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8914",
      "incomplete_value": true,
      "site": "00af8914",
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
      "definition_site": "00af84ec",
      "incomplete_value": true,
      "site": "00af84ec",
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
      "definition_site": "00af8914",
      "incomplete_value": true,
      "site": "00af8914",
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
      "definition_site": "00af84ec",
      "incomplete_value": true,
      "site": "00af84ec",
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
  }
]
~~~


~~~diff
- 00af8500 ["INT_ADD", "register:40f0:8", ["const:af8500:8", "const:4:8"]]
+ 00af8928 ["INT_ADD", "register:40f0:8", ["const:af8928:8", "const:4:8"]]
~~~


### [`00af8530`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8530.md) → [`00af8958`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8958.md) FUN_00af8958

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00713318`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`0071421c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00713358`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`0071425c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af8988",
      "incomplete_value": true,
      "site": "00af8994",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00af8560",
      "incomplete_value": true,
      "site": "00af856c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


~~~diff
- 00af8544 ["INT_ADD", "register:40f0:8", ["const:af8544:8", "const:4:8"]]
+ 00af896c ["INT_ADD", "register:40f0:8", ["const:af896c:8", "const:4:8"]]
~~~


### [`00af85fc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af85fc.md) → [`00af8a24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8a24.md) FUN_00af8a24

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8a5c",
      "incomplete_value": true,
      "site": "00af8a5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af8634",
      "incomplete_value": true,
      "site": "00af8634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af8618 ["INT_ADD", "register:40f0:8", ["const:af8618:8", "const:4:8"]]
+ 00af8a40 ["INT_ADD", "register:40f0:8", ["const:af8a40:8", "const:4:8"]]
~~~


### [`00af8648`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8648.md) → [`00af8a70`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8a70.md) FUN_00af8a70

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00713318`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`0071421c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00713358`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`0071425c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af865c ["INT_ADD", "register:40f0:8", ["const:af865c:8", "const:4:8"]]
+ 00af8a84 ["INT_ADD", "register:40f0:8", ["const:af8a84:8", "const:4:8"]]
~~~


### [`00af86d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af86d4.md) → [`00af8afc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8afc.md) FUN_00af8afc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`007154c0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00715500`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af86e8 ["INT_ADD", "register:40f0:8", ["const:af86e8:8", "const:4:8"]]
+ 00af8b10 ["INT_ADD", "register:40f0:8", ["const:af8b10:8", "const:4:8"]]
~~~


### [`00af8760`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8760.md) → [`00af8b88`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8b88.md) FUN_00af8b88

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00a51dcc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a51dcc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00a51fc4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8b90",
      "incomplete_value": true,
      "site": "00af8b90",
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
      "definition_site": "00af8768",
      "incomplete_value": true,
      "site": "00af8768",
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
      "definition_site": "00af8b90",
      "incomplete_value": true,
      "site": "00af8b90",
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
      "definition_site": "00af8768",
      "incomplete_value": true,
      "site": "00af8768",
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
  }
]
~~~


~~~diff
- 00af877c ["INT_ADD", "register:40f0:8", ["const:af877c:8", "const:4:8"]]
+ 00af8ba4 ["INT_ADD", "register:40f0:8", ["const:af8ba4:8", "const:4:8"]]
~~~


### [`00af87ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af87ac.md) → [`00af8bd4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8bd4.md) FUN_00af8bd4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00af87e4",
      "incomplete_value": true,
      "site": "00af87f0",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "INT_RIGHT",
            "4",
            [
              [
                "live",
                "register:4040:4"
              ],
              [
                "leaf",
                "const:1f:4"
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


~~~diff
- 00af87c0 ["INT_ADD", "register:40f0:8", ["const:af87c0:8", "const:4:8"]]
+ 00af8be8 ["INT_ADD", "register:40f0:8", ["const:af8be8:8", "const:4:8"]]
~~~


### [`00af87f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af87f4.md) → [`00af8c1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8c1c.md) FUN_00af8c1c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a51dcc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a51dcc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a51fc4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

~~~diff
- 00af8808 ["INT_ADD", "register:40f0:8", ["const:af8808:8", "const:4:8"]]
+ 00af8c30 ["INT_ADD", "register:40f0:8", ["const:af8c30:8", "const:4:8"]]
~~~


### [`00af8834`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8834.md) → [`00af8c5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8c5c.md) FUN_00af8c5c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8c94",
      "incomplete_value": true,
      "site": "00af8c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af886c",
      "incomplete_value": true,
      "site": "00af886c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af8850 ["INT_ADD", "register:40f0:8", ["const:af8850:8", "const:4:8"]]
+ 00af8c78 ["INT_ADD", "register:40f0:8", ["const:af8c78:8", "const:4:8"]]
~~~


### [`00af8908`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8908.md) → [`00af8d30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8d30.md) FUN_00af8d30

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af30cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af30cc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af34f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af34f4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00af8924 ["INT_ADD", "register:40f0:8", ["const:af8924:8", "const:4:8"]]
+ 00af8d4c ["INT_ADD", "register:40f0:8", ["const:af8d4c:8", "const:4:8"]]
~~~


### [`00af8954`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8954.md) → [`00af8d7c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8d7c.md) FUN_00af8d7c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00710298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710298.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007102d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00af8984",
      "incomplete_value": true,
      "site": "00af8990",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


~~~diff
- 00af8968 ["INT_ADD", "register:40f0:8", ["const:af8968:8", "const:4:8"]]
+ 00af8d90 ["INT_ADD", "register:40f0:8", ["const:af8d90:8", "const:4:8"]]
~~~


### [`00af8994`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8994.md) → [`00af8dbc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8dbc.md) FUN_00af8dbc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af30d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af30d8.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af3500`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3500.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8df4",
      "incomplete_value": true,
      "site": "00af8df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af89cc",
      "incomplete_value": true,
      "site": "00af89cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af89b0 ["INT_ADD", "register:40f0:8", ["const:af89b0:8", "const:4:8"]]
+ 00af8dd8 ["INT_ADD", "register:40f0:8", ["const:af8dd8:8", "const:4:8"]]
~~~


### [`00af8a28`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8a28.md) → [`00af8e50`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8e50.md) FUN_00af8e50

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00713ce4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713ce4.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00713d24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af8e80",
      "incomplete_value": true,
      "site": "00af8e8c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "old": null,
    "ordinal": 0,
    "slot": 0
  }
]
~~~


~~~diff
- 00af8a3c ["INT_ADD", "register:40f0:8", ["const:af8a3c:8", "const:4:8"]]
+ 00af8e64 ["INT_ADD", "register:40f0:8", ["const:af8e64:8", "const:4:8"]]
~~~


### [`00af8a68`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8a68.md) → [`00af8e90`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8e90.md) FUN_00af8e90

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af30ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af30ec.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af3514`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3514.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8e94",
      "incomplete_value": true,
      "site": "00af8e94",
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
      "definition_site": "00af8a6c",
      "incomplete_value": true,
      "site": "00af8a6c",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8e98",
      "incomplete_value": true,
      "site": "00af8e98",
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
      "definition_site": "00af8a70",
      "incomplete_value": true,
      "site": "00af8a70",
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
      "definition_site": "00af8e98",
      "incomplete_value": true,
      "site": "00af8e98",
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
      "definition_site": "00af8a70",
      "incomplete_value": true,
      "site": "00af8a70",
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
  }
]
~~~


~~~diff
- 00af8a84 ["INT_ADD", "register:40f0:8", ["const:af8a84:8", "const:4:8"]]
+ 00af8eac ["INT_ADD", "register:40f0:8", ["const:af8eac:8", "const:4:8"]]
~~~


### [`00af8ab4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8ab4.md) → [`00af8edc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8edc.md) FUN_00af8edc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00710298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710298.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007102d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00af8ae4",
      "incomplete_value": true,
      "site": "00af8af0",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


~~~diff
- 00af8ac8 ["INT_ADD", "register:40f0:8", ["const:af8ac8:8", "const:4:8"]]
+ 00af8ef0 ["INT_ADD", "register:40f0:8", ["const:af8ef0:8", "const:4:8"]]
~~~


### [`00af8af4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8af4.md) → [`00af8f1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8f1c.md) FUN_00af8f1c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af30f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af30f8.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af3520`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3520.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8f54",
      "incomplete_value": true,
      "site": "00af8f54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af8b2c",
      "incomplete_value": true,
      "site": "00af8b2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af8b10 ["INT_ADD", "register:40f0:8", ["const:af8b10:8", "const:4:8"]]
+ 00af8f38 ["INT_ADD", "register:40f0:8", ["const:af8f38:8", "const:4:8"]]
~~~


### [`00af8b88`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8b88.md) → [`00af8fb0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8fb0.md) FUN_00af8fb0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00713ce4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713ce4.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00713d24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00af8b9c ["INT_ADD", "register:40f0:8", ["const:af8b9c:8", "const:4:8"]]
+ 00af8fc4 ["INT_ADD", "register:40f0:8", ["const:af8fc4:8", "const:4:8"]]
~~~


### [`00af8c54`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8c54.md) → [`00af907c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af907c.md) FUN_00af907c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af90b4",
      "incomplete_value": true,
      "site": "00af90b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af8c8c",
      "incomplete_value": true,
      "site": "00af8c8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af8c70 ["INT_ADD", "register:40f0:8", ["const:af8c70:8", "const:4:8"]]
+ 00af9098 ["INT_ADD", "register:40f0:8", ["const:af9098:8", "const:4:8"]]
~~~


### [`00af8ca0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8ca0.md) → [`00af90c8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af90c8.md) FUN_00af90c8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00710298`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710298.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007102d8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af90f8",
      "incomplete_value": true,
      "site": "00af9104",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00af8cd0",
      "incomplete_value": true,
      "site": "00af8cdc",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


~~~diff
- 00af8cb4 ["INT_ADD", "register:40f0:8", ["const:af8cb4:8", "const:4:8"]]
+ 00af90dc ["INT_ADD", "register:40f0:8", ["const:af90dc:8", "const:4:8"]]
~~~


### [`00af8d2c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8d2c.md) → [`00af9154`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9154.md) FUN_00af9154

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00713ce4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713ce4.md) [`00af3104`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3104.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00713d24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) [`00af352c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af352c.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af918c",
      "incomplete_value": true,
      "site": "00af9198",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
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


~~~diff
- 00af8d40 ["INT_ADD", "register:40f0:8", ["const:af8d40:8", "const:4:8"]]
+ 00af9168 ["INT_ADD", "register:40f0:8", ["const:af9168:8", "const:4:8"]]
~~~


### [`00af8d74`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8d74.md) → [`00af919c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af919c.md) FUN_00af919c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00713ce4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713ce4.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00713d24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00af8d88 ["INT_ADD", "register:40f0:8", ["const:af8d88:8", "const:4:8"]]
+ 00af91b0 ["INT_ADD", "register:40f0:8", ["const:af91b0:8", "const:4:8"]]
~~~


### [`00af8db4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8db4.md) → [`00af91dc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af91dc.md) FUN_00af91dc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af310c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af310c.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af3534`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3534.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00af8dd0 ["INT_ADD", "register:40f0:8", ["const:af8dd0:8", "const:4:8"]]
+ 00af91f8 ["INT_ADD", "register:40f0:8", ["const:af91f8:8", "const:4:8"]]
~~~


### [`00af8ecc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8ecc.md) → [`00af92f4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af92f4.md) FUN_00af92f4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00af8ee8 ["INT_ADD", "register:40f0:8", ["const:af8ee8:8", "const:4:8"]]
+ 00af9310 ["INT_ADD", "register:40f0:8", ["const:af9310:8", "const:4:8"]]
~~~


### [`00af8f18`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8f18.md) → [`00af9340`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9340.md) FUN_00af9340

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af9370",
      "incomplete_value": true,
      "site": "00af937c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00af8f48",
      "incomplete_value": true,
      "site": "00af8f54",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


~~~diff
- 00af8f2c ["INT_ADD", "register:40f0:8", ["const:af8f2c:8", "const:4:8"]]
+ 00af9354 ["INT_ADD", "register:40f0:8", ["const:af9354:8", "const:4:8"]]
~~~


### [`00af8fa4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8fa4.md) → [`00af93cc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af93cc.md) FUN_00af93cc

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 3件 [`005f2d28`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2d28.md) [`00707ea0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) · 呼出先 9件 [`005e0eac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0eac.md) [`005e1af0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1af0.md) [`0068996c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00689/0068996c.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00936428`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936428.md)
- 新版 呼出元 3件 [`005f2d68`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f2/005f2d68.md) [`00707ee0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) · 呼出先 9件 [`005e0eec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0eec.md) [`005e1b30`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b30.md) [`006899ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/006899ac.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`009365c4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00936/009365c4.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00af9518",
      "incomplete_value": true,
      "site": "00af9528",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4040:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af90f0",
      "incomplete_value": true,
      "site": "00af9100",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:b1c:8"
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
      "definition_site": "00af951c",
      "incomplete_value": true,
      "site": "00af952c",
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
                "live",
                "register:4040:8"
              ],
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
      "definition_site": "00af90f4",
      "incomplete_value": true,
      "site": "00af9104",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00af9520",
      "incomplete_value": true,
      "site": "00af9530",
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
                "const:790:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af90f8",
      "incomplete_value": true,
      "site": "00af9108",
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
                "const:750:8"
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
      332,
      "READ",
      [
        "storage",
        "002b6b1c",
        null,
        "string"
      ]
    ],
    [
      336,
      "READ",
      [
        "storage",
        "002b6b25",
        null,
        "string"
      ]
    ],
    [
      340,
      "READ",
      [
        "storage",
        "002c2750",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      332,
      "READ",
      [
        "storage",
        "002b6b5c",
        null,
        "string"
      ]
    ],
    [
      336,
      "READ",
      [
        "storage",
        "002b6b65",
        null,
        "string"
      ]
    ],
    [
      340,
      "READ",
      [
        "storage",
        "002c2790",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00af8fd8 ["INT_ADD", "register:40f0:8", ["const:af8fd8:8", "const:4:8"]]
+ 00af9400 ["INT_ADD", "register:40f0:8", ["const:af9400:8", "const:4:8"]]
- 00af8ffc ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00af9424 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00af9004 ["INT_ADD", "register:40f0:8", ["const:af9004:8", "const:4:8"]]
+ 00af942c ["INT_ADD", "register:40f0:8", ["const:af942c:8", "const:4:8"]]
~~~


### [`00af920c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af920c.md) → [`00af9634`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9634.md) FUN_00af9634

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af9230",
      "incomplete_value": true,
      "site": "00af9234",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


~~~diff
- 00af9220 ["INT_ADD", "register:40f0:8", ["const:af9220:8", "const:4:8"]]
+ 00af9648 ["INT_ADD", "register:40f0:8", ["const:af9648:8", "const:4:8"]]
- 00af9234 ["INT_ADD", "register:40f0:8", ["const:af9234:8", "const:4:8"]]
+ 00af965c ["INT_ADD", "register:40f0:8", ["const:af965c:8", "const:4:8"]]
- 00af9238 ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
+ 00af9660 ["CBRANCH", null, ["local:b4:8", "tmp:3:1"]]
~~~


### [`00af927c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af927c.md) → [`00af96a4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af96a4.md) FUN_00af96a4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af9700",
      "incomplete_value": true,
      "site": "00af9700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af92d8",
      "incomplete_value": true,
      "site": "00af92d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af9298 ["INT_ADD", "register:40f0:8", ["const:af9298:8", "const:4:8"]]
+ 00af96c0 ["INT_ADD", "register:40f0:8", ["const:af96c0:8", "const:4:8"]]
- 00af92ac ["INT_ADD", "register:40f0:8", ["const:af92ac:8", "const:4:8"]]
+ 00af96d4 ["INT_ADD", "register:40f0:8", ["const:af96d4:8", "const:4:8"]]
- 00af92b0 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
+ 00af96d8 ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
~~~


### [`00af92ec`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af92ec.md) → [`00af9714`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9714.md) FUN_00af9714

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af9718",
      "incomplete_value": true,
      "site": "00af9718",
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
      "definition_site": "00af92f0",
      "incomplete_value": true,
      "site": "00af92f0",
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
      "definition_site": "00af9718",
      "incomplete_value": true,
      "site": "00af9718",
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
      "definition_site": "00af92f0",
      "incomplete_value": true,
      "site": "00af92f0",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af9738",
      "incomplete_value": true,
      "site": "00af973c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af9310",
      "incomplete_value": true,
      "site": "00af9314",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


~~~diff
- 00af9300 ["INT_ADD", "register:40f0:8", ["const:af9300:8", "const:4:8"]]
+ 00af9728 ["INT_ADD", "register:40f0:8", ["const:af9728:8", "const:4:8"]]
- 00af9314 ["INT_ADD", "register:40f0:8", ["const:af9314:8", "const:4:8"]]
+ 00af973c ["INT_ADD", "register:40f0:8", ["const:af973c:8", "const:4:8"]]
- 00af9318 ["CBRANCH", null, ["local:b4:8", "tmp:3:1"]]
+ 00af9740 ["CBRANCH", null, ["local:b6:8", "tmp:3:1"]]
~~~


### [`00af935c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af935c.md) → [`00af9784`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9784.md) FUN_00af9784

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af9788",
      "incomplete_value": true,
      "site": "00af9788",
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
      "definition_site": "00af9360",
      "incomplete_value": true,
      "site": "00af9360",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af978c",
      "incomplete_value": true,
      "site": "00af978c",
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
      "definition_site": "00af9364",
      "incomplete_value": true,
      "site": "00af9364",
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
      "definition_site": "00af978c",
      "incomplete_value": true,
      "site": "00af978c",
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
      "definition_site": "00af9364",
      "incomplete_value": true,
      "site": "00af9364",
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
  }
]
~~~


~~~diff
- 00af9378 ["INT_ADD", "register:40f0:8", ["const:af9378:8", "const:4:8"]]
+ 00af97a0 ["INT_ADD", "register:40f0:8", ["const:af97a0:8", "const:4:8"]]
- 00af938c ["INT_ADD", "register:40f0:8", ["const:af938c:8", "const:4:8"]]
+ 00af97b4 ["INT_ADD", "register:40f0:8", ["const:af97b4:8", "const:4:8"]]
- 00af9390 ["CBRANCH", null, ["local:b6:8", "tmp:3:1"]]
+ 00af97b8 ["CBRANCH", null, ["local:b10:8", "tmp:3:1"]]
~~~


### [`00af943c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af943c.md) → [`00af9864`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9864.md) FUN_00af9864

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af98c0",
      "incomplete_value": true,
      "site": "00af98c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00af9498",
      "incomplete_value": true,
      "site": "00af9498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_MULT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


~~~diff
- 00af9458 ["INT_ADD", "register:40f0:8", ["const:af9458:8", "const:4:8"]]
+ 00af9880 ["INT_ADD", "register:40f0:8", ["const:af9880:8", "const:4:8"]]
- 00af946c ["INT_ADD", "register:40f0:8", ["const:af946c:8", "const:4:8"]]
+ 00af9894 ["INT_ADD", "register:40f0:8", ["const:af9894:8", "const:4:8"]]
- 00af9470 ["CBRANCH", null, ["local:b3:8", "tmp:3:1"]]
+ 00af9898 ["CBRANCH", null, ["local:b5:8", "tmp:3:1"]]
~~~


### [`00af94ac`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af94ac.md) → [`00af98d4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af98d4.md) FUN_00af98d4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af98f8",
      "incomplete_value": true,
      "site": "00af98fc",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af94d0",
      "incomplete_value": true,
      "site": "00af94d4",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


~~~diff
- 00af94c0 ["INT_ADD", "register:40f0:8", ["const:af94c0:8", "const:4:8"]]
+ 00af98e8 ["INT_ADD", "register:40f0:8", ["const:af98e8:8", "const:4:8"]]
- 00af94d4 ["INT_ADD", "register:40f0:8", ["const:af94d4:8", "const:4:8"]]
+ 00af98fc ["INT_ADD", "register:40f0:8", ["const:af98fc:8", "const:4:8"]]
- 00af94d8 ["CBRANCH", null, ["local:b4:8", "tmp:3:1"]]
+ 00af9900 ["CBRANCH", null, ["local:b2:8", "tmp:3:1"]]
~~~


### [`00af951c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af951c.md) → [`00af9944`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9944.md) FUN_00af9944

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies

~~~diff
- 00af9538 ["INT_ADD", "register:40f0:8", ["const:af9538:8", "const:4:8"]]
+ 00af9960 ["INT_ADD", "register:40f0:8", ["const:af9960:8", "const:4:8"]]
- 00af954c ["INT_ADD", "register:40f0:8", ["const:af954c:8", "const:4:8"]]
+ 00af9974 ["INT_ADD", "register:40f0:8", ["const:af9974:8", "const:4:8"]]
- 00af955c ["INT_ADD", "register:40f0:8", ["const:af955c:8", "const:4:8"]]
+ 00af9984 ["INT_ADD", "register:40f0:8", ["const:af9984:8", "const:4:8"]]
~~~


### [`00af958c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af958c.md) → [`00af99b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af99b4.md) FUN_00af99b4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af99d8",
      "incomplete_value": true,
      "site": "00af99dc",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


~~~diff
- 00af95a0 ["INT_ADD", "register:40f0:8", ["const:af95a0:8", "const:4:8"]]
+ 00af99c8 ["INT_ADD", "register:40f0:8", ["const:af99c8:8", "const:4:8"]]
- 00af95b4 ["INT_ADD", "register:40f0:8", ["const:af95b4:8", "const:4:8"]]
+ 00af99dc ["INT_ADD", "register:40f0:8", ["const:af99dc:8", "const:4:8"]]
- 00af95c0 ["BRANCH", null, ["local:b8:8"]]
+ 00af99e8 ["BRANCH", null, ["local:b7:8"]]
~~~


### [`00af95fc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af95fc.md) → [`00af9a24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9a24.md) FUN_00af9a24

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af9a50",
      "incomplete_value": true,
      "site": "00af9a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


~~~diff
- 00af9618 ["INT_ADD", "register:40f0:8", ["const:af9618:8", "const:4:8"]]
+ 00af9a40 ["INT_ADD", "register:40f0:8", ["const:af9a40:8", "const:4:8"]]
- 00af962c ["INT_ADD", "register:40f0:8", ["const:af962c:8", "const:4:8"]]
+ 00af9a54 ["INT_ADD", "register:40f0:8", ["const:af9a54:8", "const:4:8"]]
- 00af9630 ["CBRANCH", null, ["local:b8:8", "tmp:3:1"]]
+ 00af9a58 ["CBRANCH", null, ["local:b5:8", "tmp:3:1"]]
~~~


### [`00af966c`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af966c.md) → [`00af9a94`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9a94.md) FUN_00af9a94

根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00713ce4`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713ce4.md) · 呼出先 1件 [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00713d24`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) · 呼出先 1件 [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/775a135419c80d4191cfe2001bc4b3ca8f259c02/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate, store_destination

アドレスに依存する影響 `return_value_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af9a98",
      "incomplete_value": true,
      "site": "00af9a98",
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
      "definition_site": "00af9670",
      "incomplete_value": true,
      "site": "00af9670",
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
      "definition_site": "00af9a98",
      "incomplete_value": true,
      "site": "00af9a98",
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
      "definition_site": "00af9670",
      "incomplete_value": true,
      "site": "00af9670",
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
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00af96a4",
      "incomplete_value": true,
      "site": "00af96b0",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
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


~~~diff
- 00af9680 ["INT_ADD", "register:40f0:8", ["const:af9680:8", "const:4:8"]]
+ 00af9aa8 ["INT_ADD", "register:40f0:8", ["const:af9aa8:8", "const:4:8"]]
~~~


