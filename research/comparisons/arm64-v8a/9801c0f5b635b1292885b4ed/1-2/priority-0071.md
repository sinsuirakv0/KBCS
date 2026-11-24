# v16.0.0 → v16.0.1 · 最優先の変更候補 (71)

[一覧の目次](README.md)

<a id="compare-a3b1eb4a573096019043f80d35c9e075"></a>

### [`00b47174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47174.md) → [`00b4759c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4759c.md) _ZN8firebase4util8activity12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b475d8",
      "incomplete_value": true,
      "site": "00b475d8",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b471b0",
      "incomplete_value": true,
      "site": "00b471b0",
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
            "const:3d0:8"
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
      "definition_site": "00b47628",
      "incomplete_value": true,
      "site": "00b47628",
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
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47200",
      "incomplete_value": true,
      "site": "00b47200",
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
            "const:3c8:8"
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
      "definition_site": "00b475b4",
      "incomplete_value": true,
      "site": "00b475b4",
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
      "definition_site": "00b4718c",
      "incomplete_value": true,
      "site": "00b4718c",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b475b0",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b475bc",
      "READ",
      [
        "storage",
        "011253d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b475d8",
      "WRITE",
      [
        "storage",
        "011253d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b475b0",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b475bc",
      "READ",
      [
        "storage",
        "011257d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b475d8",
      "WRITE",
      [
        "storage",
        "011257d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b471b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47174.md#insn-00b471b0) · [`00b471fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47174.md#insn-00b471fc) · [`00b47200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47174.md#insn-00b47200)
- 新版 [`00b475d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4759c.md#insn-00b475d8) · [`00b47624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4759c.md#insn-00b47624) · [`00b47628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4759c.md#insn-00b47628)

~~~diff
- 00b471b0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b471b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b471b0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3d0:8"]]
- 00b471b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b475d8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b475d8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b475d8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7d0:8"]]
+ 00b475d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b471b0 bytes bf420f39
+ 00b475d8 bytes bf421f39
- 00b471fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b471fc ["INT_ADD", "register:40f0:8", ["const:b471fc:8", "const:4:8"]]
- 00b471fc ["CALLIND", null, ["register:0:8"]]
+ 00b47624 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47624 ["INT_ADD", "register:40f0:8", ["const:b47624:8", "const:4:8"]]
+ 00b47624 ["CALLIND", null, ["register:0:8"]]
- 00b471fc bytes 00013fd6
+ 00b47624 bytes 00013fd6
- 00b47200 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00b47200 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b47200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b47628 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
+ 00b47628 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b47628 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b47200 bytes 9fe601f9
+ 00b47628 bytes 9fe603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98b9d37b30bf8c48166c7d20b2135665"></a>

### [`00b47214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47214.md) → [`00b4763c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4763c.md) _ZN8firebase4util8activity14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4767c",
      "incomplete_value": true,
      "site": "00b4767c",
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
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47254",
      "incomplete_value": true,
      "site": "00b47254",
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
            "const:3c8:8"
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
      "definition_site": "00b47658",
      "incomplete_value": true,
      "site": "00b47658",
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
      "definition_site": "00b47230",
      "incomplete_value": true,
      "site": "00b47230",
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
      "definition_site": "00b47660",
      "incomplete_value": false,
      "site": "00b47674",
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
            "const:5d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47238",
      "incomplete_value": false,
      "site": "00b4724c",
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
            "const:591:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47650",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47660",
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      "00b4767c",
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47650",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47660",
      "PARAM",
      [
        "storage",
        "002be5d1",
        null,
        "string"
      ]
    ],
    [
      "00b4767c",
      "WRITE",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4724c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47214.md#insn-00b4724c) · [`00b47254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47214.md#insn-00b47254) · [`00b47228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47214.md#insn-00b47228)
- 新版 [`00b47674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4763c.md#insn-00b47674) · [`00b4767c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4763c.md#insn-00b4767c) · [`00b47650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4763c.md#insn-00b47650)

~~~diff
- 00b4724c ["INT_ADD", "register:40f0:8", ["const:b4724c:8", "const:4:8"]]
- 00b4724c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47674 ["INT_ADD", "register:40f0:8", ["const:b47674:8", "const:4:8"]]
+ 00b47674 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4724c bytes 314e0494
+ 00b47674 bytes 274e0494
- 00b47254 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00b47254 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4767c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
+ 00b4767c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47254 bytes 80e601f9
+ 00b4767c bytes 80e603f9
- 00b47228 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00b47228 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47650 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
+ 00b47650 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47228 bytes 81e641f9
+ 00b47650 bytes 81e643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9fa9081f6d3e236f004e406c3342030"></a>

### [`00b47284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47284.md) → [`00b476ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476ac.md) _ZN8firebase4util8activity11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b150.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5b550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b550.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b476c8",
      "incomplete_value": false,
      "site": "00b476cc",
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
      "definition_site": "00b472a0",
      "incomplete_value": false,
      "site": "00b472a4",
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
      "definition_site": "00b476d8",
      "incomplete_value": true,
      "site": "00b476e4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b472b0",
      "incomplete_value": true,
      "site": "00b472bc",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b476c8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b476d8",
      "DATA",
      [
        "storage",
        "011253d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b476c8",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b476d8",
      "DATA",
      [
        "storage",
        "011257d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b472a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47284.md#insn-00b472a4) · [`00b472a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47284.md#insn-00b472a0) · [`00b472ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47284.md#insn-00b472ac)
- 新版 [`00b476cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476ac.md#insn-00b476cc) · [`00b476c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476ac.md#insn-00b476c8) · [`00b476d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476ac.md#insn-00b476d4)

~~~diff
- 00b472a4 ["INT_ADD", "register:40f0:8", ["const:b472a4:8", "const:4:8"]]
- 00b472a4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b476cc ["INT_ADD", "register:40f0:8", ["const:b476cc:8", "const:4:8"]]
+ 00b476cc ["CALL", null, ["callee:00c5b000:8"]]
- 00b472a4 bytes 574e0494
+ 00b476cc bytes 4d4e0494
- 00b472a0 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b472a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b472a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b472a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b476c8 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b476c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b476c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b476c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b472a0 bytes 00680a91
+ 00b476c8 bytes 009c0d91
- 00b472ac ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 00b472ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b472ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b472ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b476d4 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 00b476d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b476d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b476d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b472ac bytes 08610f91
+ 00b476d4 bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c759339ae27940f3e5f071eddd29541a"></a>

### [`00b472c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b472c0.md) → [`00b476e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476e8.md) _ZN8firebase4util8activity13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47728",
      "incomplete_value": true,
      "site": "00b47728",
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
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47300",
      "incomplete_value": true,
      "site": "00b47300",
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
            "const:3c8:8"
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
      "definition_site": "00b47704",
      "incomplete_value": true,
      "site": "00b47704",
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
      "definition_site": "00b472dc",
      "incomplete_value": true,
      "site": "00b472dc",
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
      "definition_site": "00b4770c",
      "incomplete_value": false,
      "site": "00b47720",
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
            "const:5d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b472e4",
      "incomplete_value": false,
      "site": "00b472f8",
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
            "const:591:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b476fc",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4770c",
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      "00b47728",
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b476fc",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4770c",
      "PARAM",
      [
        "storage",
        "002be5d1",
        null,
        "string"
      ]
    ],
    [
      "00b47728",
      "WRITE",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b472f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b472c0.md#insn-00b472f8) · [`00b47300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b472c0.md#insn-00b47300) · [`00b472d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b472c0.md#insn-00b472d4)
- 新版 [`00b47720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476e8.md#insn-00b47720) · [`00b47728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476e8.md#insn-00b47728) · [`00b476fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476e8.md#insn-00b476fc)

~~~diff
- 00b472f8 ["INT_ADD", "register:40f0:8", ["const:b472f8:8", "const:4:8"]]
- 00b472f8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47720 ["INT_ADD", "register:40f0:8", ["const:b47720:8", "const:4:8"]]
+ 00b47720 ["CALL", null, ["callee:00c5af10:8"]]
- 00b472f8 bytes 064e0494
+ 00b47720 bytes fc4d0494
- 00b47300 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00b47300 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47728 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
+ 00b47728 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47300 bytes 80e601f9
+ 00b47728 bytes 80e603f9
- 00b472d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00b472d4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b476fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
+ 00b476fc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b472d4 bytes 81e641f9
+ 00b476fc bytes 81e643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4f9f726605db3118338eddd206d2e36"></a>

### [`00b47330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47330.md) → [`00b47758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47758.md) _ZN8firebase4util8activity10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47774",
      "incomplete_value": false,
      "site": "00b47778",
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
      "definition_site": "00b4734c",
      "incomplete_value": false,
      "site": "00b47350",
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
      "definition_site": "00b47784",
      "incomplete_value": true,
      "site": "00b47790",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4735c",
      "incomplete_value": true,
      "site": "00b47368",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47774",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b47784",
      "DATA",
      [
        "storage",
        "01125428",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b47774",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b47784",
      "DATA",
      [
        "storage",
        "01125828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47330.md#insn-00b47350) · [`00b4734c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47330.md#insn-00b4734c) · [`00b47358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47330.md#insn-00b47358)
- 新版 [`00b47778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47758.md#insn-00b47778) · [`00b47774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47758.md#insn-00b47774) · [`00b47780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47758.md#insn-00b47780)

~~~diff
- 00b47350 ["INT_ADD", "register:40f0:8", ["const:b47350:8", "const:4:8"]]
- 00b47350 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b47778 ["INT_ADD", "register:40f0:8", ["const:b47778:8", "const:4:8"]]
+ 00b47778 ["CALL", null, ["callee:00c5b000:8"]]
- 00b47350 bytes 2c4e0494
+ 00b47778 bytes 224e0494
- 00b4734c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4734c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4734c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4734c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47774 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b47774 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47774 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47774 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4734c bytes 00441191
+ 00b47774 bytes 00781491
- 00b47358 ["COPY", "tmp:0:8", ["const:428:8"]]
- 00b47358 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b47358 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b47358 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b47780 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 00b47780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b47358 bytes 08a11091
+ 00b47780 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2af0a78bc2a9e0439beeb2e2f1d3466"></a>

### [`00b4736c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4736c.md) → [`00b47794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47794.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b477c0",
      "incomplete_value": true,
      "site": "00b477c0",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47398",
      "incomplete_value": true,
      "site": "00b47398",
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
            "const:430:8"
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
      "definition_site": "00b477a8",
      "incomplete_value": true,
      "site": "00b477a8",
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
      "definition_site": "00b47380",
      "incomplete_value": true,
      "site": "00b47380",
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
      "definition_site": "00b477b4",
      "incomplete_value": false,
      "site": "00b477b8",
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
            "const:114:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4738c",
      "incomplete_value": false,
      "site": "00b47390",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b477a4",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b477b4",
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      "00b477c0",
      "WRITE",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b477a4",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b477b4",
      "PARAM",
      [
        "storage",
        "002a7114",
        null,
        "string"
      ]
    ],
    [
      "00b477c0",
      "WRITE",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4736c.md#insn-00b47390) · [`00b47398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4736c.md#insn-00b47398) · [`00b4737c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4736c.md#insn-00b4737c)
- 新版 [`00b477b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47794.md#insn-00b477b8) · [`00b477c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47794.md#insn-00b477c0) · [`00b477a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47794.md#insn-00b477a4)

~~~diff
- 00b47390 ["INT_ADD", "register:40f0:8", ["const:b47390:8", "const:4:8"]]
- 00b47390 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b477b8 ["INT_ADD", "register:40f0:8", ["const:b477b8:8", "const:4:8"]]
+ 00b477b8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b47390 bytes e04d0494
+ 00b477b8 bytes d64d0494
- 00b47398 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:430:8"]]
- 00b47398 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b477c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00b477c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47398 bytes 601a02f9
+ 00b477c0 bytes 601a04f9
- 00b4737c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:430:8"]]
- 00b4737c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b477a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00b477a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4737c bytes 681a42f9
+ 00b477a4 bytes 681a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-432219e07cfc0e481da74443c2e42f8f"></a>

### [`00b473ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b473ac.md) → [`00b477d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b477d4.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47800",
      "incomplete_value": true,
      "site": "00b47800",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b473d8",
      "incomplete_value": true,
      "site": "00b473d8",
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
            "const:430:8"
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
      "definition_site": "00b477e8",
      "incomplete_value": true,
      "site": "00b477e8",
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
      "definition_site": "00b473c0",
      "incomplete_value": true,
      "site": "00b473c0",
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
      "definition_site": "00b477f0",
      "incomplete_value": false,
      "site": "00b477f8",
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
            "const:114:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b473c8",
      "incomplete_value": false,
      "site": "00b473d0",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b477e4",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b477f0",
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      "00b47800",
      "WRITE",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b477e4",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b477f0",
      "PARAM",
      [
        "storage",
        "002a7114",
        null,
        "string"
      ]
    ],
    [
      "00b47800",
      "WRITE",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b473d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b473ac.md#insn-00b473d0) · [`00b473d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b473ac.md#insn-00b473d8) · [`00b473bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b473ac.md#insn-00b473bc)
- 新版 [`00b477f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b477d4.md#insn-00b477f8) · [`00b47800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b477d4.md#insn-00b47800) · [`00b477e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b477d4.md#insn-00b477e4)

~~~diff
- 00b473d0 ["INT_ADD", "register:40f0:8", ["const:b473d0:8", "const:4:8"]]
- 00b473d0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b477f8 ["INT_ADD", "register:40f0:8", ["const:b477f8:8", "const:4:8"]]
+ 00b477f8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b473d0 bytes d04d0494
+ 00b477f8 bytes c64d0494
- 00b473d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:430:8"]]
- 00b473d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47800 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00b47800 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b473d8 bytes 601a02f9
+ 00b47800 bytes 601a04f9
- 00b473bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:430:8"]]
- 00b473bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b477e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00b477e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b473bc bytes 681a42f9
+ 00b477e4 bytes 681a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e6a183de2feb9a2f7d13980340ac42f"></a>

### [`00b473ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b473ec.md) → [`00b47814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47814.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47844",
      "incomplete_value": true,
      "site": "00b47844",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4741c",
      "incomplete_value": true,
      "site": "00b4741c",
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
            "const:430:8"
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
      "definition_site": "00b47828",
      "incomplete_value": true,
      "site": "00b47828",
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
      "definition_site": "00b47400",
      "incomplete_value": true,
      "site": "00b47400",
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
      "definition_site": "00b47834",
      "incomplete_value": false,
      "site": "00b4783c",
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
            "const:114:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4740c",
      "incomplete_value": false,
      "site": "00b47414",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47824",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47834",
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      "00b47844",
      "WRITE",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47824",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47834",
      "PARAM",
      [
        "storage",
        "002a7114",
        null,
        "string"
      ]
    ],
    [
      "00b47844",
      "WRITE",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b473ec.md#insn-00b47414) · [`00b4741c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b473ec.md#insn-00b4741c) · [`00b473fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b473ec.md#insn-00b473fc)
- 新版 [`00b4783c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47814.md#insn-00b4783c) · [`00b47844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47814.md#insn-00b47844) · [`00b47824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47814.md#insn-00b47824)

~~~diff
- 00b47414 ["INT_ADD", "register:40f0:8", ["const:b47414:8", "const:4:8"]]
- 00b47414 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4783c ["INT_ADD", "register:40f0:8", ["const:b4783c:8", "const:4:8"]]
+ 00b4783c ["CALL", null, ["callee:00c5af10:8"]]
- 00b47414 bytes bf4d0494
+ 00b4783c bytes b54d0494
- 00b4741c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:430:8"]]
- 00b4741c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47844 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00b47844 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4741c bytes 601a02f9
+ 00b47844 bytes 601a04f9
- 00b473fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:430:8"]]
- 00b473fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47824 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00b47824 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b473fc bytes 681a42f9
+ 00b47824 bytes 681a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e688e0e6400e4cc614f61c0e65a0cfe"></a>

### [`00b47430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47430.md) → [`00b47858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47858.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47888",
      "incomplete_value": true,
      "site": "00b47888",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47460",
      "incomplete_value": true,
      "site": "00b47460",
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
            "const:430:8"
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
      "definition_site": "00b4786c",
      "incomplete_value": true,
      "site": "00b4786c",
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
      "definition_site": "00b47444",
      "incomplete_value": true,
      "site": "00b47444",
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
      "definition_site": "00b47874",
      "incomplete_value": false,
      "site": "00b47880",
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
            "const:114:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4744c",
      "incomplete_value": false,
      "site": "00b47458",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47868",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47874",
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      "00b47888",
      "WRITE",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47868",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47874",
      "PARAM",
      [
        "storage",
        "002a7114",
        null,
        "string"
      ]
    ],
    [
      "00b47888",
      "WRITE",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47430.md#insn-00b47458) · [`00b47460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47430.md#insn-00b47460) · [`00b47440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47430.md#insn-00b47440)
- 新版 [`00b47880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47858.md#insn-00b47880) · [`00b47888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47858.md#insn-00b47888) · [`00b47868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47858.md#insn-00b47868)

~~~diff
- 00b47458 ["INT_ADD", "register:40f0:8", ["const:b47458:8", "const:4:8"]]
- 00b47458 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47880 ["INT_ADD", "register:40f0:8", ["const:b47880:8", "const:4:8"]]
+ 00b47880 ["CALL", null, ["callee:00c5af10:8"]]
- 00b47458 bytes ae4d0494
+ 00b47880 bytes a44d0494
- 00b47460 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:430:8"]]
- 00b47460 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47888 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00b47888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47460 bytes 601a02f9
+ 00b47888 bytes 601a04f9
- 00b47440 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:430:8"]]
- 00b47440 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00b47868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47440 bytes 681a42f9
+ 00b47868 bytes 681a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da908ab3b5b0c12ade59b8878e7da136"></a>

### [`00b47480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47480.md) → [`00b478a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b478a8.md) _ZN8firebase4util10array_list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47930",
      "incomplete_value": true,
      "site": "00b47930",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47508",
      "incomplete_value": true,
      "site": "00b47508",
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
            "const:438:8"
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
      "definition_site": "00b478dc",
      "incomplete_value": true,
      "site": "00b478e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b474b4",
      "incomplete_value": true,
      "site": "00b474c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:430:8"
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
      "00b478bc",
      "READ",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ],
    [
      "00b478dc",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47930",
      "WRITE",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b478bc",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined1"
      ]
    ],
    [
      "00b478dc",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47930",
      "WRITE",
      [
        "storage",
        "01125838",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b474c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47480.md#insn-00b474c0) · [`00b47508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47480.md#insn-00b47508) · [`00b47494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47480.md#insn-00b47494)
- 新版 [`00b478e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b478a8.md#insn-00b478e8) · [`00b47930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b478a8.md#insn-00b47930) · [`00b478bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b478a8.md#insn-00b478bc)

~~~diff
- 00b474c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b474c0 ["INT_ADD", "register:40f0:8", ["const:b474c0:8", "const:4:8"]]
- 00b474c0 ["CALLIND", null, ["register:0:8"]]
+ 00b478e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b478e8 ["INT_ADD", "register:40f0:8", ["const:b478e8:8", "const:4:8"]]
+ 00b478e8 ["CALLIND", null, ["register:0:8"]]
- 00b474c0 bytes 00013fd6
+ 00b478e8 bytes 00013fd6
- 00b47508 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b47508 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:438:8"]]
- 00b47508 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b47930 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b47930 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:838:8"]]
+ 00b47930 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b47508 bytes a0e21039
+ 00b47930 bytes a0e22039
- 00b47494 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:438:8"]]
- 00b47494 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b47494 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b478bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:838:8"]]
+ 00b478bc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b478bc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b47494 bytes a8e25039
+ 00b478bc bytes a8e26039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90c75417a3d62d0b21c211ecb1201e4d"></a>

### [`00b4751c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4751c.md) → [`00b47944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47944.md) _ZN8firebase4util10array_list12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47980",
      "incomplete_value": true,
      "site": "00b47980",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47558",
      "incomplete_value": true,
      "site": "00b47558",
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
            "const:438:8"
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
      "definition_site": "00b479d0",
      "incomplete_value": true,
      "site": "00b479d0",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b475a8",
      "incomplete_value": true,
      "site": "00b475a8",
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
            "const:430:8"
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
      "definition_site": "00b4795c",
      "incomplete_value": true,
      "site": "00b4795c",
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
      "definition_site": "00b47534",
      "incomplete_value": true,
      "site": "00b47534",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47958",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47964",
      "READ",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47980",
      "WRITE",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47958",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47964",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47980",
      "WRITE",
      [
        "storage",
        "01125838",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4751c.md#insn-00b47558) · [`00b475a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4751c.md#insn-00b475a4) · [`00b475a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4751c.md#insn-00b475a8)
- 新版 [`00b47980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47944.md#insn-00b47980) · [`00b479cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47944.md#insn-00b479cc) · [`00b479d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47944.md#insn-00b479d0)

~~~diff
- 00b47558 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b47558 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b47558 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:438:8"]]
- 00b47558 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b47980 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b47980 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b47980 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:838:8"]]
+ 00b47980 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b47558 bytes bfe21039
+ 00b47980 bytes bfe22039
- 00b475a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b475a4 ["INT_ADD", "register:40f0:8", ["const:b475a4:8", "const:4:8"]]
- 00b475a4 ["CALLIND", null, ["register:0:8"]]
+ 00b479cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b479cc ["INT_ADD", "register:40f0:8", ["const:b479cc:8", "const:4:8"]]
+ 00b479cc ["CALLIND", null, ["register:0:8"]]
- 00b475a4 bytes 00013fd6
+ 00b479cc bytes 00013fd6
- 00b475a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:430:8"]]
- 00b475a8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b475a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b479d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
+ 00b479d0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b479d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b475a8 bytes 9f1a02f9
+ 00b479d0 bytes 9f1a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0edfcfa549ddf6e0411e433a18824c1c"></a>

### [`00b475bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b475bc.md) → [`00b479e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b479e4.md) _ZN8firebase4util10array_list14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47a24",
      "incomplete_value": true,
      "site": "00b47a24",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b475fc",
      "incomplete_value": true,
      "site": "00b475fc",
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
            "const:430:8"
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
      "definition_site": "00b47a00",
      "incomplete_value": true,
      "site": "00b47a00",
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
      "definition_site": "00b475d8",
      "incomplete_value": true,
      "site": "00b475d8",
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
      "definition_site": "00b47a08",
      "incomplete_value": false,
      "site": "00b47a1c",
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
            "const:114:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b475e0",
      "incomplete_value": false,
      "site": "00b475f4",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b479f8",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47a08",
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      "00b47a24",
      "WRITE",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b479f8",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47a08",
      "PARAM",
      [
        "storage",
        "002a7114",
        null,
        "string"
      ]
    ],
    [
      "00b47a24",
      "WRITE",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b475f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b475bc.md#insn-00b475f4) · [`00b475fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b475bc.md#insn-00b475fc) · [`00b475d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b475bc.md#insn-00b475d0)
- 新版 [`00b47a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b479e4.md#insn-00b47a1c) · [`00b47a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b479e4.md#insn-00b47a24) · [`00b479f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b479e4.md#insn-00b479f8)

~~~diff
- 00b475f4 ["INT_ADD", "register:40f0:8", ["const:b475f4:8", "const:4:8"]]
- 00b475f4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47a1c ["INT_ADD", "register:40f0:8", ["const:b47a1c:8", "const:4:8"]]
+ 00b47a1c ["CALL", null, ["callee:00c5af10:8"]]
- 00b475f4 bytes 474d0494
+ 00b47a1c bytes 3d4d0494
- 00b475fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:430:8"]]
- 00b475fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47a24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
+ 00b47a24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b475fc bytes 801a02f9
+ 00b47a24 bytes 801a04f9
- 00b475d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:430:8"]]
- 00b475d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b479f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
+ 00b479f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b475d0 bytes 811a42f9
+ 00b479f8 bytes 811a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e2f5eeed1bed825d649f37c9697500a"></a>

### [`00b4762c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4762c.md) → [`00b47a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a54.md) _ZN8firebase4util10array_list11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5aab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aab0.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5aeb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aeb0.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47a70",
      "incomplete_value": false,
      "site": "00b47a74",
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
      "definition_site": "00b47648",
      "incomplete_value": false,
      "site": "00b4764c",
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
      "definition_site": "00b47a80",
      "incomplete_value": true,
      "site": "00b47a8c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b47658",
      "incomplete_value": true,
      "site": "00b47664",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47a70",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b47a80",
      "DATA",
      [
        "storage",
        "01125440",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47a70",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b47a80",
      "DATA",
      [
        "storage",
        "01125840",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4764c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4762c.md#insn-00b4764c) · [`00b47648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4762c.md#insn-00b47648) · [`00b47654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4762c.md#insn-00b47654)
- 新版 [`00b47a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a54.md#insn-00b47a74) · [`00b47a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a54.md#insn-00b47a70) · [`00b47a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a54.md#insn-00b47a7c)

~~~diff
- 00b4764c ["INT_ADD", "register:40f0:8", ["const:b4764c:8", "const:4:8"]]
- 00b4764c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b47a74 ["INT_ADD", "register:40f0:8", ["const:b47a74:8", "const:4:8"]]
+ 00b47a74 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4764c bytes 6d4d0494
+ 00b47a74 bytes 634d0494
- 00b47648 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b47648 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47648 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47648 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47a70 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b47a70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47a70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47a70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47648 bytes 00680a91
+ 00b47a70 bytes 009c0d91
- 00b47654 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00b47654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b47654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b47654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b47a7c ["COPY", "tmp:0:8", ["const:840:8"]]
+ 00b47a7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47a7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47a7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b47654 bytes 08011191
+ 00b47a7c bytes 08012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df38ce673e014ace741d47b27a970d41"></a>

### [`00b47668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47668.md) → [`00b47a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a90.md) _ZN8firebase4util10array_list13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47ad0",
      "incomplete_value": true,
      "site": "00b47ad0",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b476a8",
      "incomplete_value": true,
      "site": "00b476a8",
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
            "const:430:8"
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
      "definition_site": "00b47aac",
      "incomplete_value": true,
      "site": "00b47aac",
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
      "definition_site": "00b47684",
      "incomplete_value": true,
      "site": "00b47684",
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
      "definition_site": "00b47ab4",
      "incomplete_value": false,
      "site": "00b47ac8",
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
            "const:114:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4768c",
      "incomplete_value": false,
      "site": "00b476a0",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47aa4",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47ab4",
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      "00b47ad0",
      "WRITE",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47aa4",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47ab4",
      "PARAM",
      [
        "storage",
        "002a7114",
        null,
        "string"
      ]
    ],
    [
      "00b47ad0",
      "WRITE",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b476a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47668.md#insn-00b476a0) · [`00b476a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47668.md#insn-00b476a8) · [`00b4767c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47668.md#insn-00b4767c)
- 新版 [`00b47ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a90.md#insn-00b47ac8) · [`00b47ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a90.md#insn-00b47ad0) · [`00b47aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a90.md#insn-00b47aa4)

~~~diff
- 00b476a0 ["INT_ADD", "register:40f0:8", ["const:b476a0:8", "const:4:8"]]
- 00b476a0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47ac8 ["INT_ADD", "register:40f0:8", ["const:b47ac8:8", "const:4:8"]]
+ 00b47ac8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b476a0 bytes 1c4d0494
+ 00b47ac8 bytes 124d0494
- 00b476a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:430:8"]]
- 00b476a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47ad0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
+ 00b47ad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b476a8 bytes 801a02f9
+ 00b47ad0 bytes 801a04f9
- 00b4767c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:430:8"]]
- 00b4767c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47aa4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
+ 00b47aa4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4767c bytes 811a42f9
+ 00b47aa4 bytes 811a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6ff36072e3c7cd8761c9e012b81812d"></a>

### [`00b476d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b476d8.md) → [`00b47b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b00.md) _ZN8firebase4util10array_list10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47b1c",
      "incomplete_value": false,
      "site": "00b47b20",
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
      "definition_site": "00b476f4",
      "incomplete_value": false,
      "site": "00b476f8",
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
      "definition_site": "00b47b2c",
      "incomplete_value": true,
      "site": "00b47b38",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b47704",
      "incomplete_value": true,
      "site": "00b47710",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47b1c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b47b2c",
      "DATA",
      [
        "storage",
        "01125458",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b47b1c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b47b2c",
      "DATA",
      [
        "storage",
        "01125858",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b476f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b476d8.md#insn-00b476f8) · [`00b476f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b476d8.md#insn-00b476f4) · [`00b47700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b476d8.md#insn-00b47700)
- 新版 [`00b47b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b00.md#insn-00b47b20) · [`00b47b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b00.md#insn-00b47b1c) · [`00b47b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b00.md#insn-00b47b28)

~~~diff
- 00b476f8 ["INT_ADD", "register:40f0:8", ["const:b476f8:8", "const:4:8"]]
- 00b476f8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b47b20 ["INT_ADD", "register:40f0:8", ["const:b47b20:8", "const:4:8"]]
+ 00b47b20 ["CALL", null, ["callee:00c5b000:8"]]
- 00b476f8 bytes 424d0494
+ 00b47b20 bytes 384d0494
- 00b476f4 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b476f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b476f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b476f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47b1c ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b47b1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47b1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47b1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b476f4 bytes 00441191
+ 00b47b1c bytes 00781491
- 00b47700 ["COPY", "tmp:0:8", ["const:458:8"]]
- 00b47700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b47700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b47700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b47b28 ["COPY", "tmp:0:8", ["const:858:8"]]
+ 00b47b28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47b28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47b28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b47700 bytes 08611191
+ 00b47b28 bytes 08612191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efedaa6732d7fbcf05b44c036183c6df"></a>

### [`00b47714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47714.md) → [`00b47b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b3c.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47740"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47b68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47b50",
      "incomplete_value": true,
      "site": "00b47b50",
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
      "definition_site": "00b47728",
      "incomplete_value": true,
      "site": "00b47728",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47b4c",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47b50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b47744"
      ]
    ],
    [
      "unmatched:00b47734",
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b47b4c",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47b50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47b6c"
      ]
    ],
    [
      "00b47b5c",
      "PARAM",
      [
        "storage",
        "002bf7be",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47714.md#insn-00b47738) · [`00b47740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47714.md#insn-00b47740) · [`00b47750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47714.md#insn-00b47750)

~~~diff
- 00b47738 ["INT_ADD", "register:40f0:8", ["const:b47738:8", "const:4:8"]]
- 00b47738 ["CALL", null, ["callee:00c5af10:8"]]
- 00b47738 bytes f64c0494
- 00b47740 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:460:8"]]
- 00b47740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47740 bytes 603202f9
- 00b47750 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b47750 ["RETURN", null, ["register:0:8"]]
- 00b47750 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a1f520c4027e9323cf9037a6d04420f"></a>

### [`00b47754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47754.md) → [`00b47b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b7c.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47ba8",
      "incomplete_value": true,
      "site": "00b47ba8",
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
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47780",
      "incomplete_value": true,
      "site": "00b47780",
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
            "const:460:8"
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
      "definition_site": "00b47b90",
      "incomplete_value": true,
      "site": "00b47b90",
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
      "definition_site": "00b47768",
      "incomplete_value": true,
      "site": "00b47768",
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
      "definition_site": "00b47b98",
      "incomplete_value": false,
      "site": "00b47ba0",
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
            "const:7be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47770",
      "incomplete_value": false,
      "site": "00b47778",
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
            "const:77e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47b8c",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47b98",
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ],
    [
      "00b47ba8",
      "WRITE",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47b8c",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47b98",
      "PARAM",
      [
        "storage",
        "002bf7be",
        null,
        "string"
      ]
    ],
    [
      "00b47ba8",
      "WRITE",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47754.md#insn-00b47778) · [`00b47780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47754.md#insn-00b47780) · [`00b47764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47754.md#insn-00b47764)
- 新版 [`00b47ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b7c.md#insn-00b47ba0) · [`00b47ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b7c.md#insn-00b47ba8) · [`00b47b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b7c.md#insn-00b47b8c)

~~~diff
- 00b47778 ["INT_ADD", "register:40f0:8", ["const:b47778:8", "const:4:8"]]
- 00b47778 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47ba0 ["INT_ADD", "register:40f0:8", ["const:b47ba0:8", "const:4:8"]]
+ 00b47ba0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b47778 bytes e64c0494
+ 00b47ba0 bytes dc4c0494
- 00b47780 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:460:8"]]
- 00b47780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47ba8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
+ 00b47ba8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47780 bytes 603202f9
+ 00b47ba8 bytes 603204f9
- 00b47764 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:460:8"]]
- 00b47764 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47b8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
+ 00b47b8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47764 bytes 683242f9
+ 00b47b8c bytes 683244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1ef289d5b22d0ee69de5af9a45e74bc"></a>

### [`00b47794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47794.md) → [`00b47bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47bbc.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47bec",
      "incomplete_value": true,
      "site": "00b47bec",
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
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b477c4",
      "incomplete_value": true,
      "site": "00b477c4",
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
            "const:460:8"
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
      "definition_site": "00b47bd0",
      "incomplete_value": true,
      "site": "00b47bd0",
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
      "definition_site": "00b477a8",
      "incomplete_value": true,
      "site": "00b477a8",
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
      "definition_site": "00b47bdc",
      "incomplete_value": false,
      "site": "00b47be4",
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
            "const:7be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b477b4",
      "incomplete_value": false,
      "site": "00b477bc",
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
            "const:77e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47bcc",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47bdc",
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ],
    [
      "00b47bec",
      "WRITE",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47bcc",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47bdc",
      "PARAM",
      [
        "storage",
        "002bf7be",
        null,
        "string"
      ]
    ],
    [
      "00b47bec",
      "WRITE",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b477bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47794.md#insn-00b477bc) · [`00b477c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47794.md#insn-00b477c4) · [`00b477a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47794.md#insn-00b477a4)
- 新版 [`00b47be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47bbc.md#insn-00b47be4) · [`00b47bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47bbc.md#insn-00b47bec) · [`00b47bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47bbc.md#insn-00b47bcc)

~~~diff
- 00b477bc ["INT_ADD", "register:40f0:8", ["const:b477bc:8", "const:4:8"]]
- 00b477bc ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47be4 ["INT_ADD", "register:40f0:8", ["const:b47be4:8", "const:4:8"]]
+ 00b47be4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b477bc bytes d54c0494
+ 00b47be4 bytes cb4c0494
- 00b477c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:460:8"]]
- 00b477c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47bec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
+ 00b47bec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b477c4 bytes 603202f9
+ 00b47bec bytes 603204f9
- 00b477a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:460:8"]]
- 00b477a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47bcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
+ 00b47bcc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b477a4 bytes 683242f9
+ 00b47bcc bytes 683244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca66e4dc58e9834324ed9f9c25a5a169"></a>

### [`00b477d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b477d8.md) → [`00b47c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c00.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47c30",
      "incomplete_value": true,
      "site": "00b47c30",
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
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47808",
      "incomplete_value": true,
      "site": "00b47808",
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
            "const:460:8"
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
      "definition_site": "00b47c14",
      "incomplete_value": true,
      "site": "00b47c14",
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
      "definition_site": "00b477ec",
      "incomplete_value": true,
      "site": "00b477ec",
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
      "definition_site": "00b47c1c",
      "incomplete_value": false,
      "site": "00b47c28",
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
            "const:7be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b477f4",
      "incomplete_value": false,
      "site": "00b47800",
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
            "const:77e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47c10",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47c1c",
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ],
    [
      "00b47c30",
      "WRITE",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47c10",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47c1c",
      "PARAM",
      [
        "storage",
        "002bf7be",
        null,
        "string"
      ]
    ],
    [
      "00b47c30",
      "WRITE",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b477d8.md#insn-00b47800) · [`00b47808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b477d8.md#insn-00b47808) · [`00b477e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b477d8.md#insn-00b477e8)
- 新版 [`00b47c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c00.md#insn-00b47c28) · [`00b47c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c00.md#insn-00b47c30) · [`00b47c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c00.md#insn-00b47c10)

~~~diff
- 00b47800 ["INT_ADD", "register:40f0:8", ["const:b47800:8", "const:4:8"]]
- 00b47800 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47c28 ["INT_ADD", "register:40f0:8", ["const:b47c28:8", "const:4:8"]]
+ 00b47c28 ["CALL", null, ["callee:00c5af10:8"]]
- 00b47800 bytes c44c0494
+ 00b47c28 bytes ba4c0494
- 00b47808 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:460:8"]]
- 00b47808 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47c30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
+ 00b47c30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47808 bytes 603202f9
+ 00b47c30 bytes 603204f9
- 00b477e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:460:8"]]
- 00b477e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47c10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
+ 00b47c10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b477e8 bytes 683242f9
+ 00b47c10 bytes 683244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc617d5ecd05596b1d8ce4eb84e0d59c"></a>

### [`00b47828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47828.md) → [`00b47c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c50.md) _ZN8firebase4util21asset_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47cd8",
      "incomplete_value": true,
      "site": "00b47cd8",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b478b0",
      "incomplete_value": true,
      "site": "00b478b0",
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
            "const:468:8"
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
      "definition_site": "00b47c84",
      "incomplete_value": true,
      "site": "00b47c90",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:860:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4785c",
      "incomplete_value": true,
      "site": "00b47868",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:460:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b478a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47c64",
      "READ",
      [
        "storage",
        "01125468",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47c84",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47cd8",
      "WRITE",
      [
        "storage",
        "01125468",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47c64",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47c84",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47cd8",
      "WRITE",
      [
        "storage",
        "01125868",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47828.md#insn-00b47868) · [`00b478a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47828.md#insn-00b478a4) · [`00b478b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47828.md#insn-00b478b0)
- 新版 [`00b47c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c50.md#insn-00b47c90) · [`00b47cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c50.md#insn-00b47cd8)

~~~diff
- 00b47868 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47868 ["INT_ADD", "register:40f0:8", ["const:b47868:8", "const:4:8"]]
- 00b47868 ["CALLIND", null, ["register:0:8"]]
+ 00b47c90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47c90 ["INT_ADD", "register:40f0:8", ["const:b47c90:8", "const:4:8"]]
+ 00b47c90 ["CALLIND", null, ["register:0:8"]]
- 00b47868 bytes 00013fd6
+ 00b47c90 bytes 00013fd6
- 00b478a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b478a4 ["INT_ADD", "register:40f0:8", ["const:b478a4:8", "const:4:8"]]
- 00b478a4 ["CALLIND", null, ["register:0:8"]]
- 00b478a4 bytes 00013fd6
- 00b478b0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b478b0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:468:8"]]
- 00b478b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b47cd8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b47cd8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:868:8"]]
+ 00b47cd8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b478b0 bytes a0a21139
+ 00b47cd8 bytes a0a22139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09271f5d9e8185584184b528b1acf25c"></a>

### [`00b478c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b478c4.md) → [`00b47cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47cec.md) _ZN8firebase4util21asset_file_descriptor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 77.78% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47d28",
      "incomplete_value": true,
      "site": "00b47d28",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47900",
      "incomplete_value": true,
      "site": "00b47900",
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
            "const:468:8"
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
      "definition_site": "00b47d78",
      "incomplete_value": true,
      "site": "00b47d78",
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
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47950",
      "incomplete_value": true,
      "site": "00b47950",
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
            "const:460:8"
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
      "definition_site": "00b47d04",
      "incomplete_value": true,
      "site": "00b47d04",
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
      "definition_site": "00b478dc",
      "incomplete_value": true,
      "site": "00b478dc",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47d00",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47d0c",
      "READ",
      [
        "storage",
        "01125468",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47d28",
      "WRITE",
      [
        "storage",
        "01125468",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47d00",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47d0c",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47d28",
      "WRITE",
      [
        "storage",
        "01125868",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b478dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b478c4.md#insn-00b478dc) · [`00b47900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b478c4.md#insn-00b47900) · [`00b47928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b478c4.md#insn-00b47928)
- 新版 [`00b47d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47cec.md#insn-00b47d04) · [`00b47d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47cec.md#insn-00b47d28)

~~~diff
- 00b478dc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b478dc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b47d04 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b47d04 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b478dc bytes c10300b4
+ 00b47d04 bytes c10300b4
- 00b47900 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b47900 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b47900 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:468:8"]]
- 00b47900 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b47d28 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b47d28 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b47d28 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:868:8"]]
+ 00b47d28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b47900 bytes bfa21139
+ 00b47d28 bytes bfa22139
- 00b47928 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47928 ["INT_ADD", "register:40f0:8", ["const:b47928:8", "const:4:8"]]
- 00b47928 ["CALLIND", null, ["register:0:8"]]
- 00b47928 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a3f6bda3cd9e00328d6cd934f5a081b"></a>

### [`00b47964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47964.md) → [`00b47d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47d8c.md) _ZN8firebase4util21asset_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b479a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47dcc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47980"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b47978",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b47980",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47dd0"
      ]
    ],
    [
      "unmatched:00b47988",
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b47da0",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47da8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47dd0"
      ]
    ],
    [
      "00b47db0",
      "PARAM",
      [
        "storage",
        "002bf7be",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47964.md#insn-00b47980) · [`00b4799c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47964.md#insn-00b4799c) · [`00b479a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47964.md#insn-00b479a4)
- 新版 [`00b47dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47d8c.md#insn-00b47dc4)

~~~diff
- 00b47980 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b47980 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b47980 bytes 410100b5
- 00b4799c ["INT_ADD", "register:40f0:8", ["const:b4799c:8", "const:4:8"]]
- 00b4799c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47dc4 ["INT_ADD", "register:40f0:8", ["const:b47dc4:8", "const:4:8"]]
+ 00b47dc4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4799c bytes 5d4c0494
+ 00b47dc4 bytes 534c0494
- 00b479a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:460:8"]]
- 00b479a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b479a4 bytes 803202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b317c5c322cbacae69bf114457a7e75a"></a>

### [`00b47a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47a10.md) → [`00b47e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47e38.md) _ZN8firebase4util21asset_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47e78",
      "incomplete_value": true,
      "site": "00b47e78",
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
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47a50",
      "incomplete_value": true,
      "site": "00b47a50",
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
            "const:460:8"
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
      "definition_site": "00b47e54",
      "incomplete_value": true,
      "site": "00b47e54",
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
      "definition_site": "00b47a2c",
      "incomplete_value": true,
      "site": "00b47a2c",
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
      "definition_site": "00b47e5c",
      "incomplete_value": false,
      "site": "00b47e70",
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
            "const:7be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47a34",
      "incomplete_value": false,
      "site": "00b47a48",
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
            "const:77e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47e4c",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47e5c",
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ],
    [
      "00b47e78",
      "WRITE",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47e4c",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47e5c",
      "PARAM",
      [
        "storage",
        "002bf7be",
        null,
        "string"
      ]
    ],
    [
      "00b47e78",
      "WRITE",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47a10.md#insn-00b47a48) · [`00b47a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47a10.md#insn-00b47a50) · [`00b47a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47a10.md#insn-00b47a24)
- 新版 [`00b47e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47e38.md#insn-00b47e70) · [`00b47e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47e38.md#insn-00b47e78) · [`00b47e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47e38.md#insn-00b47e4c)

~~~diff
- 00b47a48 ["INT_ADD", "register:40f0:8", ["const:b47a48:8", "const:4:8"]]
- 00b47a48 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47e70 ["INT_ADD", "register:40f0:8", ["const:b47e70:8", "const:4:8"]]
+ 00b47e70 ["CALL", null, ["callee:00c5af10:8"]]
- 00b47a48 bytes 324c0494
+ 00b47e70 bytes 284c0494
- 00b47a50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:460:8"]]
- 00b47a50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47e78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:860:8"]]
+ 00b47e78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47a50 bytes 803202f9
+ 00b47e78 bytes 803204f9
- 00b47a24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:460:8"]]
- 00b47a24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47e4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:860:8"]]
+ 00b47e4c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47a24 bytes 813242f9
+ 00b47e4c bytes 813244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36b34729cc3c19eb924b371007f6a806"></a>

### [`00b47a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47a80.md) → [`00b47ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ea8.md) _ZN8firebase4util21asset_file_descriptor10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47ec4",
      "incomplete_value": false,
      "site": "00b47ec8",
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
      "definition_site": "00b47a9c",
      "incomplete_value": false,
      "site": "00b47aa0",
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
      "definition_site": "00b47ed4",
      "incomplete_value": true,
      "site": "00b47ee0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b47aac",
      "incomplete_value": true,
      "site": "00b47ab8",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47ec4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b47ed4",
      "DATA",
      [
        "storage",
        "01125478",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b47ec4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b47ed4",
      "DATA",
      [
        "storage",
        "01125878",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47a80.md#insn-00b47aa0) · [`00b47a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47a80.md#insn-00b47a9c) · [`00b47aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47a80.md#insn-00b47aa8)
- 新版 [`00b47ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ea8.md#insn-00b47ec8) · [`00b47ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ea8.md#insn-00b47ec4) · [`00b47ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ea8.md#insn-00b47ed0)

~~~diff
- 00b47aa0 ["INT_ADD", "register:40f0:8", ["const:b47aa0:8", "const:4:8"]]
- 00b47aa0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b47ec8 ["INT_ADD", "register:40f0:8", ["const:b47ec8:8", "const:4:8"]]
+ 00b47ec8 ["CALL", null, ["callee:00c5b000:8"]]
- 00b47aa0 bytes 584c0494
+ 00b47ec8 bytes 4e4c0494
- 00b47a9c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b47a9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47a9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47a9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47ec4 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b47ec4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47ec4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47ec4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47a9c bytes 00441191
+ 00b47ec4 bytes 00781491
- 00b47aa8 ["COPY", "tmp:0:8", ["const:478:8"]]
- 00b47aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b47aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b47aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b47ed0 ["COPY", "tmp:0:8", ["const:878:8"]]
+ 00b47ed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47ed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47ed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b47aa8 bytes 08e11191
+ 00b47ed0 bytes 08e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75c93c82db720bed5967e687a3ba73bf"></a>

### [`00b47afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47afc.md) → [`00b47f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f24.md) _ZN8firebase4util13boolean_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47f50",
      "incomplete_value": true,
      "site": "00b47f50",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47b28",
      "incomplete_value": true,
      "site": "00b47b28",
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
            "const:480:8"
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
      "definition_site": "00b47f38",
      "incomplete_value": true,
      "site": "00b47f38",
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
      "definition_site": "00b47b10",
      "incomplete_value": true,
      "site": "00b47b10",
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
      "definition_site": "00b47f40",
      "incomplete_value": false,
      "site": "00b47f48",
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
            "const:3fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47b18",
      "incomplete_value": false,
      "site": "00b47b20",
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
            "const:32f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47f34",
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47f40",
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ],
    [
      "00b47f50",
      "WRITE",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47f34",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47f40",
      "PARAM",
      [
        "storage",
        "002a83fc",
        null,
        "string"
      ]
    ],
    [
      "00b47f50",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47afc.md#insn-00b47b20) · [`00b47b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47afc.md#insn-00b47b28) · [`00b47b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47afc.md#insn-00b47b0c)
- 新版 [`00b47f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f24.md#insn-00b47f48) · [`00b47f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f24.md#insn-00b47f50) · [`00b47f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f24.md#insn-00b47f34)

~~~diff
- 00b47b20 ["INT_ADD", "register:40f0:8", ["const:b47b20:8", "const:4:8"]]
- 00b47b20 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47f48 ["INT_ADD", "register:40f0:8", ["const:b47f48:8", "const:4:8"]]
+ 00b47f48 ["CALL", null, ["callee:00c5af10:8"]]
- 00b47b20 bytes fc4b0494
+ 00b47f48 bytes f24b0494
- 00b47b28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00b47b28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47f50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
+ 00b47f50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47b28 bytes 604202f9
+ 00b47f50 bytes 604204f9
- 00b47b0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00b47b0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47f34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
+ 00b47f34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47b0c bytes 684242f9
+ 00b47f34 bytes 684244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-570e570124ab20bc73e4b4b33f9cae80"></a>

### [`00b47b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47b3c.md) → [`00b47f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f64.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47f94",
      "incomplete_value": true,
      "site": "00b47f94",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47b6c",
      "incomplete_value": true,
      "site": "00b47b6c",
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
            "const:480:8"
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
      "definition_site": "00b47f78",
      "incomplete_value": true,
      "site": "00b47f78",
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
      "definition_site": "00b47b50",
      "incomplete_value": true,
      "site": "00b47b50",
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
      "definition_site": "00b47f84",
      "incomplete_value": false,
      "site": "00b47f8c",
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
            "const:3fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47b5c",
      "incomplete_value": false,
      "site": "00b47b64",
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
            "const:32f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47f74",
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47f84",
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ],
    [
      "00b47f94",
      "WRITE",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47f74",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47f84",
      "PARAM",
      [
        "storage",
        "002a83fc",
        null,
        "string"
      ]
    ],
    [
      "00b47f94",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47b3c.md#insn-00b47b64) · [`00b47b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47b3c.md#insn-00b47b6c) · [`00b47b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47b3c.md#insn-00b47b4c)
- 新版 [`00b47f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f64.md#insn-00b47f8c) · [`00b47f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f64.md#insn-00b47f94) · [`00b47f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f64.md#insn-00b47f74)

~~~diff
- 00b47b64 ["INT_ADD", "register:40f0:8", ["const:b47b64:8", "const:4:8"]]
- 00b47b64 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47f8c ["INT_ADD", "register:40f0:8", ["const:b47f8c:8", "const:4:8"]]
+ 00b47f8c ["CALL", null, ["callee:00c5af10:8"]]
- 00b47b64 bytes eb4b0494
+ 00b47f8c bytes e14b0494
- 00b47b6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00b47b6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47f94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
+ 00b47f94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47b6c bytes 604202f9
+ 00b47f94 bytes 604204f9
- 00b47b4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00b47b4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47f74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
+ 00b47f74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47b4c bytes 684242f9
+ 00b47f74 bytes 684244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5acea8539e29f691a9e7afd598ff181f"></a>

### [`00b47b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47b80.md) → [`00b47fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47fa8.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47fd8",
      "incomplete_value": true,
      "site": "00b47fd8",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47bb0",
      "incomplete_value": true,
      "site": "00b47bb0",
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
            "const:480:8"
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
      "definition_site": "00b47fbc",
      "incomplete_value": true,
      "site": "00b47fbc",
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
      "definition_site": "00b47b94",
      "incomplete_value": true,
      "site": "00b47b94",
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
      "definition_site": "00b47fc4",
      "incomplete_value": false,
      "site": "00b47fd0",
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
            "const:3fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47b9c",
      "incomplete_value": false,
      "site": "00b47ba8",
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
            "const:32f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47fb8",
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47fc4",
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ],
    [
      "00b47fd8",
      "WRITE",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47fb8",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47fc4",
      "PARAM",
      [
        "storage",
        "002a83fc",
        null,
        "string"
      ]
    ],
    [
      "00b47fd8",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47b80.md#insn-00b47ba8) · [`00b47bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47b80.md#insn-00b47bb0) · [`00b47b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47b80.md#insn-00b47b90)
- 新版 [`00b47fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47fa8.md#insn-00b47fd0) · [`00b47fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47fa8.md#insn-00b47fd8) · [`00b47fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47fa8.md#insn-00b47fb8)

~~~diff
- 00b47ba8 ["INT_ADD", "register:40f0:8", ["const:b47ba8:8", "const:4:8"]]
- 00b47ba8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b47fd0 ["INT_ADD", "register:40f0:8", ["const:b47fd0:8", "const:4:8"]]
+ 00b47fd0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b47ba8 bytes da4b0494
+ 00b47fd0 bytes d04b0494
- 00b47bb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00b47bb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47fd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
+ 00b47fd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47bb0 bytes 604202f9
+ 00b47fd8 bytes 604204f9
- 00b47b90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00b47b90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47fb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
+ 00b47fb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47b90 bytes 684242f9
+ 00b47fb8 bytes 684244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ef4ac1d2db10bbae2ade826e3257311"></a>

### [`00b47bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47bd0.md) → [`00b47ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ff8.md) _ZN8firebase4util13boolean_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48080",
      "incomplete_value": true,
      "site": "00b48080",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47c58",
      "incomplete_value": true,
      "site": "00b47c58",
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
            "const:488:8"
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
      "definition_site": "00b4802c",
      "incomplete_value": true,
      "site": "00b48038",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
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
      "definition_site": "00b47c04",
      "incomplete_value": true,
      "site": "00b47c10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47c3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4800c",
      "READ",
      [
        "storage",
        "01125488",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4802c",
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48080",
      "WRITE",
      [
        "storage",
        "01125488",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4800c",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4802c",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48080",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47bd0.md#insn-00b47c10) · [`00b47c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47bd0.md#insn-00b47c3c) · [`00b47c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47bd0.md#insn-00b47c58)
- 新版 [`00b48038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ff8.md#insn-00b48038) · [`00b48080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ff8.md#insn-00b48080)

~~~diff
- 00b47c10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47c10 ["INT_ADD", "register:40f0:8", ["const:b47c10:8", "const:4:8"]]
- 00b47c10 ["CALLIND", null, ["register:0:8"]]
+ 00b48038 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48038 ["INT_ADD", "register:40f0:8", ["const:b48038:8", "const:4:8"]]
+ 00b48038 ["CALLIND", null, ["register:0:8"]]
- 00b47c10 bytes 00013fd6
+ 00b48038 bytes 00013fd6
- 00b47c3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47c3c ["INT_ADD", "register:40f0:8", ["const:b47c3c:8", "const:4:8"]]
- 00b47c3c ["CALLIND", null, ["register:0:8"]]
- 00b47c3c bytes 00013fd6
- 00b47c58 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b47c58 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:488:8"]]
- 00b47c58 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b48080 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b48080 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:888:8"]]
+ 00b48080 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b47c58 bytes a0221239
+ 00b48080 bytes a0222239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b47f0a919e9e6d24afa0d18dfd079e9"></a>

### [`00b47c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47c6c.md) → [`00b48094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48094.md) _ZN8firebase4util13boolean_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 70.00% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b480d0",
      "incomplete_value": true,
      "site": "00b480d0",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47ca8",
      "incomplete_value": true,
      "site": "00b47ca8",
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
            "const:488:8"
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
      "definition_site": "00b48120",
      "incomplete_value": true,
      "site": "00b48120",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47cf8",
      "incomplete_value": true,
      "site": "00b47cf8",
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
            "const:480:8"
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
      "definition_site": "00b480ac",
      "incomplete_value": true,
      "site": "00b480ac",
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
      "definition_site": "00b47c84",
      "incomplete_value": true,
      "site": "00b47c84",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b480a8",
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      "00b480ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b47cfc"
      ]
    ],
    [
      "00b480b4",
      "READ",
      [
        "storage",
        "01125488",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b480a8",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b480ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48124"
      ]
    ],
    [
      "00b480b4",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47c6c.md#insn-00b47ca8) · [`00b47cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47c6c.md#insn-00b47cf4) · [`00b47cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47c6c.md#insn-00b47cf8)
- 新版 [`00b480d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48094.md#insn-00b480d0) · [`00b4811c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48094.md#insn-00b4811c) · [`00b48120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48094.md#insn-00b48120)

~~~diff
- 00b47ca8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b47ca8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b47ca8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:488:8"]]
- 00b47ca8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b480d0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b480d0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b480d0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:888:8"]]
+ 00b480d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b47ca8 bytes bf221239
+ 00b480d0 bytes bf222239
- 00b47cf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47cf4 ["INT_ADD", "register:40f0:8", ["const:b47cf4:8", "const:4:8"]]
- 00b47cf4 ["CALLIND", null, ["register:0:8"]]
+ 00b4811c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4811c ["INT_ADD", "register:40f0:8", ["const:b4811c:8", "const:4:8"]]
+ 00b4811c ["CALLIND", null, ["register:0:8"]]
- 00b47cf4 bytes 00013fd6
+ 00b4811c bytes 00013fd6
- 00b47cf8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00b47cf8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b47cf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b48120 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
+ 00b48120 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b48120 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b47cf8 bytes 9f4202f9
+ 00b48120 bytes 9f4204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be1e0fc89a00c4a5eaa0967da5696b99"></a>

### [`00b47d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47d0c.md) → [`00b48134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48134.md) _ZN8firebase4util13boolean_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48174",
      "incomplete_value": true,
      "site": "00b48174",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47d4c",
      "incomplete_value": true,
      "site": "00b47d4c",
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
            "const:480:8"
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
      "definition_site": "00b48150",
      "incomplete_value": true,
      "site": "00b48150",
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
      "definition_site": "00b47d28",
      "incomplete_value": true,
      "site": "00b47d28",
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
      "definition_site": "00b48158",
      "incomplete_value": false,
      "site": "00b4816c",
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
            "const:3fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47d30",
      "incomplete_value": false,
      "site": "00b47d44",
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
            "const:32f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48148",
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48158",
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ],
    [
      "00b48174",
      "WRITE",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48148",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48158",
      "PARAM",
      [
        "storage",
        "002a83fc",
        null,
        "string"
      ]
    ],
    [
      "00b48174",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47d0c.md#insn-00b47d44) · [`00b47d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47d0c.md#insn-00b47d4c) · [`00b47d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47d0c.md#insn-00b47d20)
- 新版 [`00b4816c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48134.md#insn-00b4816c) · [`00b48174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48134.md#insn-00b48174) · [`00b48148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48134.md#insn-00b48148)

~~~diff
- 00b47d44 ["INT_ADD", "register:40f0:8", ["const:b47d44:8", "const:4:8"]]
- 00b47d44 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4816c ["INT_ADD", "register:40f0:8", ["const:b4816c:8", "const:4:8"]]
+ 00b4816c ["CALL", null, ["callee:00c5af10:8"]]
- 00b47d44 bytes 734b0494
+ 00b4816c bytes 694b0494
- 00b47d4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00b47d4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48174 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
+ 00b48174 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47d4c bytes 804202f9
+ 00b48174 bytes 804204f9
- 00b47d20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00b47d20 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48148 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
+ 00b48148 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47d20 bytes 814242f9
+ 00b48148 bytes 814244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b5c84484712866f52bc0dfa1ef6300e"></a>

### [`00b47d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47d7c.md) → [`00b481a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481a4.md) _ZN8firebase4util13boolean_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5aec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aec0.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5b2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b2c0.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b481c0",
      "incomplete_value": false,
      "site": "00b481c4",
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
      "definition_site": "00b47d98",
      "incomplete_value": false,
      "site": "00b47d9c",
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
      "definition_site": "00b481d0",
      "incomplete_value": true,
      "site": "00b481dc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b47da8",
      "incomplete_value": true,
      "site": "00b47db4",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b481c0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b481d0",
      "DATA",
      [
        "storage",
        "01125490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b481c0",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b481d0",
      "DATA",
      [
        "storage",
        "01125890",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47d7c.md#insn-00b47d9c) · [`00b47d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47d7c.md#insn-00b47d98) · [`00b47da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47d7c.md#insn-00b47da4)
- 新版 [`00b481c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481a4.md#insn-00b481c4) · [`00b481c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481a4.md#insn-00b481c0) · [`00b481cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481a4.md#insn-00b481cc)

~~~diff
- 00b47d9c ["INT_ADD", "register:40f0:8", ["const:b47d9c:8", "const:4:8"]]
- 00b47d9c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b481c4 ["INT_ADD", "register:40f0:8", ["const:b481c4:8", "const:4:8"]]
+ 00b481c4 ["CALL", null, ["callee:00c5b000:8"]]
- 00b47d9c bytes 994b0494
+ 00b481c4 bytes 8f4b0494
- 00b47d98 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b47d98 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47d98 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47d98 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b481c0 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b481c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b481c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b481c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47d98 bytes 00680a91
+ 00b481c0 bytes 009c0d91
- 00b47da4 ["COPY", "tmp:0:8", ["const:490:8"]]
- 00b47da4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b47da4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b47da4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b481cc ["COPY", "tmp:0:8", ["const:890:8"]]
+ 00b481cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b481cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b481cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b47da4 bytes 08411291
+ 00b481cc bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72c8aff089fdac96ed3c040281c606a1"></a>

### [`00b47db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47db8.md) → [`00b481e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481e0.md) _ZN8firebase4util13boolean_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48220",
      "incomplete_value": true,
      "site": "00b48220",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47df8",
      "incomplete_value": true,
      "site": "00b47df8",
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
            "const:480:8"
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
      "definition_site": "00b481fc",
      "incomplete_value": true,
      "site": "00b481fc",
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
      "definition_site": "00b47dd4",
      "incomplete_value": true,
      "site": "00b47dd4",
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
      "definition_site": "00b48204",
      "incomplete_value": false,
      "site": "00b48218",
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
            "const:3fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47ddc",
      "incomplete_value": false,
      "site": "00b47df0",
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
            "const:32f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b481f4",
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48204",
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ],
    [
      "00b48220",
      "WRITE",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b481f4",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48204",
      "PARAM",
      [
        "storage",
        "002a83fc",
        null,
        "string"
      ]
    ],
    [
      "00b48220",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47db8.md#insn-00b47df0) · [`00b47df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47db8.md#insn-00b47df8) · [`00b47dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47db8.md#insn-00b47dcc)
- 新版 [`00b48218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481e0.md#insn-00b48218) · [`00b48220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481e0.md#insn-00b48220) · [`00b481f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481e0.md#insn-00b481f4)

~~~diff
- 00b47df0 ["INT_ADD", "register:40f0:8", ["const:b47df0:8", "const:4:8"]]
- 00b47df0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b48218 ["INT_ADD", "register:40f0:8", ["const:b48218:8", "const:4:8"]]
+ 00b48218 ["CALL", null, ["callee:00c5af10:8"]]
- 00b47df0 bytes 484b0494
+ 00b48218 bytes 3e4b0494
- 00b47df8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00b47df8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48220 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
+ 00b48220 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47df8 bytes 804202f9
+ 00b48220 bytes 804204f9
- 00b47dcc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00b47dcc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b481f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
+ 00b481f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47dcc bytes 814242f9
+ 00b481f4 bytes 814244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca7da5d5e9bf86af351da06035a6348a"></a>

### [`00b47e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47e28.md) → [`00b48250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48250.md) _ZN8firebase4util13boolean_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4826c",
      "incomplete_value": false,
      "site": "00b48270",
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
      "definition_site": "00b47e44",
      "incomplete_value": false,
      "site": "00b47e48",
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
      "definition_site": "00b4827c",
      "incomplete_value": true,
      "site": "00b48288",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b47e54",
      "incomplete_value": true,
      "site": "00b47e60",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4826c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4827c",
      "DATA",
      [
        "storage",
        "011254a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4826c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4827c",
      "DATA",
      [
        "storage",
        "011258a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47e28.md#insn-00b47e48) · [`00b47e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47e28.md#insn-00b47e44) · [`00b47e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47e28.md#insn-00b47e50)
- 新版 [`00b48270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48250.md#insn-00b48270) · [`00b4826c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48250.md#insn-00b4826c) · [`00b48278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48250.md#insn-00b48278)

~~~diff
- 00b47e48 ["INT_ADD", "register:40f0:8", ["const:b47e48:8", "const:4:8"]]
- 00b47e48 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b48270 ["INT_ADD", "register:40f0:8", ["const:b48270:8", "const:4:8"]]
+ 00b48270 ["CALL", null, ["callee:00c5b000:8"]]
- 00b47e48 bytes 6e4b0494
+ 00b48270 bytes 644b0494
- 00b47e44 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b47e44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47e44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47e44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4826c ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4826c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4826c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4826c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47e44 bytes 00441191
+ 00b4826c bytes 00781491
- 00b47e50 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 00b47e50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b47e50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b47e50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b48278 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00b48278 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b48278 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b48278 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b47e50 bytes 08811291
+ 00b48278 bytes 08812291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c63072a4b60f936a994274b56f08c287"></a>

### [`00b47e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47e64.md) → [`00b4828c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4828c.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b482b8",
      "incomplete_value": true,
      "site": "00b482b8",
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
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47e90",
      "incomplete_value": true,
      "site": "00b47e90",
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
            "const:4a8:8"
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
      "definition_site": "00b482a0",
      "incomplete_value": true,
      "site": "00b482a0",
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
      "definition_site": "00b47e78",
      "incomplete_value": true,
      "site": "00b47e78",
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
      "definition_site": "00b482ac",
      "incomplete_value": false,
      "site": "00b482b0",
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
            "const:99b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47e84",
      "incomplete_value": false,
      "site": "00b47e88",
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
            "const:95b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4829c",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b482ac",
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ],
    [
      "00b482b8",
      "WRITE",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4829c",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b482ac",
      "PARAM",
      [
        "storage",
        "002b999b",
        null,
        "string"
      ]
    ],
    [
      "00b482b8",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47e64.md#insn-00b47e88) · [`00b47e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47e64.md#insn-00b47e90) · [`00b47e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47e64.md#insn-00b47e74)
- 新版 [`00b482b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4828c.md#insn-00b482b0) · [`00b482b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4828c.md#insn-00b482b8) · [`00b4829c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4828c.md#insn-00b4829c)

~~~diff
- 00b47e88 ["INT_ADD", "register:40f0:8", ["const:b47e88:8", "const:4:8"]]
- 00b47e88 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b482b0 ["INT_ADD", "register:40f0:8", ["const:b482b0:8", "const:4:8"]]
+ 00b482b0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b47e88 bytes 224b0494
+ 00b482b0 bytes 184b0494
- 00b47e90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00b47e90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b482b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00b482b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47e90 bytes 605602f9
+ 00b482b8 bytes 605604f9
- 00b47e74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00b47e74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4829c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00b4829c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47e74 bytes 685642f9
+ 00b4829c bytes 685644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f24c1b2c202d6ef69de08f7692ef9718"></a>

### [`00b47ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47ea4.md) → [`00b482cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b482cc.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b482f8",
      "incomplete_value": true,
      "site": "00b482f8",
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
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47ed0",
      "incomplete_value": true,
      "site": "00b47ed0",
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
            "const:4a8:8"
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
      "definition_site": "00b482e0",
      "incomplete_value": true,
      "site": "00b482e0",
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
      "definition_site": "00b47eb8",
      "incomplete_value": true,
      "site": "00b47eb8",
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
      "definition_site": "00b482e8",
      "incomplete_value": false,
      "site": "00b482f0",
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
            "const:99b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47ec0",
      "incomplete_value": false,
      "site": "00b47ec8",
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
            "const:95b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b482dc",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b482e8",
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ],
    [
      "00b482f8",
      "WRITE",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b482dc",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b482e8",
      "PARAM",
      [
        "storage",
        "002b999b",
        null,
        "string"
      ]
    ],
    [
      "00b482f8",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47ea4.md#insn-00b47ec8) · [`00b47ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47ea4.md#insn-00b47ed0) · [`00b47eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47ea4.md#insn-00b47eb4)
- 新版 [`00b482f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b482cc.md#insn-00b482f0) · [`00b482f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b482cc.md#insn-00b482f8) · [`00b482dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b482cc.md#insn-00b482dc)

~~~diff
- 00b47ec8 ["INT_ADD", "register:40f0:8", ["const:b47ec8:8", "const:4:8"]]
- 00b47ec8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b482f0 ["INT_ADD", "register:40f0:8", ["const:b482f0:8", "const:4:8"]]
+ 00b482f0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b47ec8 bytes 124b0494
+ 00b482f0 bytes 084b0494
- 00b47ed0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00b47ed0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b482f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00b482f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47ed0 bytes 605602f9
+ 00b482f8 bytes 605604f9
- 00b47eb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00b47eb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b482dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00b482dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47eb4 bytes 685642f9
+ 00b482dc bytes 685644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb5cb9b7a7205091249808aa39776bd0"></a>

### [`00b47ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47ee4.md) → [`00b4830c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4830c.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47f14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4833c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48320",
      "incomplete_value": true,
      "site": "00b48320",
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
      "definition_site": "00b47ef8",
      "incomplete_value": true,
      "site": "00b47ef8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4831c",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b47f04",
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b47f0c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00b4831c",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4832c",
      "PARAM",
      [
        "storage",
        "002b999b",
        null,
        "string"
      ]
    ],
    [
      "00b48334",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47ee4.md#insn-00b47ef8) · [`00b47f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47ee4.md#insn-00b47f0c) · [`00b47f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47ee4.md#insn-00b47f14)
- 新版 [`00b48320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4830c.md#insn-00b48320)

~~~diff
- 00b47ef8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b47ef8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b48320 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b48320 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b47ef8 bytes 080100b5
+ 00b48320 bytes 080100b5
- 00b47f0c ["INT_ADD", "register:40f0:8", ["const:b47f0c:8", "const:4:8"]]
- 00b47f0c ["CALL", null, ["callee:00c5af10:8"]]
- 00b47f0c bytes 014b0494
- 00b47f14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00b47f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47f14 bytes 605602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b576dee9a20063b4ce1df85179213b72"></a>

### [`00b47f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47f28.md) → [`00b48350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48350.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47f58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48380"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48364",
      "incomplete_value": true,
      "site": "00b48364",
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
      "definition_site": "00b47f3c",
      "incomplete_value": true,
      "site": "00b47f3c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48360",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48364",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b47f5c"
      ]
    ],
    [
      "unmatched:00b47f44",
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48360",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48364",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48384"
      ]
    ],
    [
      "00b4836c",
      "PARAM",
      [
        "storage",
        "002b999b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47f28.md#insn-00b47f50) · [`00b47f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47f28.md#insn-00b47f58) · [`00b47f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47f28.md#insn-00b47f68)
- 新版 [`00b48378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48350.md#insn-00b48378)

~~~diff
- 00b47f50 ["INT_ADD", "register:40f0:8", ["const:b47f50:8", "const:4:8"]]
- 00b47f50 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b48378 ["INT_ADD", "register:40f0:8", ["const:b48378:8", "const:4:8"]]
+ 00b48378 ["CALL", null, ["callee:00c5af10:8"]]
- 00b47f50 bytes f04a0494
+ 00b48378 bytes e64a0494
- 00b47f58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00b47f58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47f58 bytes 605602f9
- 00b47f68 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b47f68 ["RETURN", null, ["register:0:8"]]
- 00b47f68 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d69c2569a5773e583df794c4ba4dc5b0"></a>

### [`00b47f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47f78.md) → [`00b483a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b483a0.md) _ZN8firebase4util6bundle15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 42.86% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47f78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47f7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47f7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b47f78",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b47f7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b47f80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b483a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b483a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b483a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47f78.md#insn-00b47f78) · [`00b47f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47f78.md#insn-00b47f7c) · [`00b47f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47f78.md#insn-00b47f80)

~~~diff
- 00b47f78 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b47f78 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b47f78 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b47f78 bytes f50f1df8
- 00b47f7c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b47f7c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b47f7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b47f7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b47f7c bytes f44f01a9
- 00b47f80 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b47f80 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b47f80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b47f80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b47f80 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9782f1c65d4a5895b40203403ccbcce5"></a>

### [`00b48014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48014.md) → [`00b4843c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4843c.md) _ZN8firebase4util6bundle12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 77.78% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48478",
      "incomplete_value": true,
      "site": "00b48478",
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
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48050",
      "incomplete_value": true,
      "site": "00b48050",
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
            "const:4b0:8"
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
      "definition_site": "00b484c8",
      "incomplete_value": true,
      "site": "00b484c8",
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
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b480a0",
      "incomplete_value": true,
      "site": "00b480a0",
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
            "const:4a8:8"
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
      "definition_site": "00b48454",
      "incomplete_value": true,
      "site": "00b48454",
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
      "definition_site": "00b4802c",
      "incomplete_value": true,
      "site": "00b4802c",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48450",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48454",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b480a4"
      ]
    ],
    [
      "00b4845c",
      "READ",
      [
        "storage",
        "011254b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48450",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48454",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b484cc"
      ]
    ],
    [
      "00b4845c",
      "READ",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48014.md#insn-00b48050) · [`00b4809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48014.md#insn-00b4809c) · [`00b480a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48014.md#insn-00b480a0)
- 新版 [`00b48478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4843c.md#insn-00b48478) · [`00b484c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4843c.md#insn-00b484c4) · [`00b484c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4843c.md#insn-00b484c8)

~~~diff
- 00b48050 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b48050 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b48050 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4b0:8"]]
- 00b48050 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b48478 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b48478 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b48478 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8b0:8"]]
+ 00b48478 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b48050 bytes bfc21239
+ 00b48478 bytes bfc22239
- 00b4809c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4809c ["INT_ADD", "register:40f0:8", ["const:b4809c:8", "const:4:8"]]
- 00b4809c ["CALLIND", null, ["register:0:8"]]
+ 00b484c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b484c4 ["INT_ADD", "register:40f0:8", ["const:b484c4:8", "const:4:8"]]
+ 00b484c4 ["CALLIND", null, ["register:0:8"]]
- 00b4809c bytes 00013fd6
+ 00b484c4 bytes 00013fd6
- 00b480a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00b480a0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b480a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b484c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
+ 00b484c8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b484c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b480a0 bytes 9f5602f9
+ 00b484c8 bytes 9f5604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6c4b45b96e48b9ee3bf6fbe8d7660fc"></a>

### [`00b480b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b480b4.md) → [`00b484dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b484dc.md) _ZN8firebase4util6bundle14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b480f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4851c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b480d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b480c8",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b480d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48520"
      ]
    ],
    [
      "unmatched:00b480d8",
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b484f0",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b484f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48520"
      ]
    ],
    [
      "00b48500",
      "PARAM",
      [
        "storage",
        "002b999b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b480d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b480b4.md#insn-00b480d0) · [`00b480ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b480b4.md#insn-00b480ec) · [`00b480f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b480b4.md#insn-00b480f4)
- 新版 [`00b48514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b484dc.md#insn-00b48514)

~~~diff
- 00b480d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b480d0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b480d0 bytes 410100b5
- 00b480ec ["INT_ADD", "register:40f0:8", ["const:b480ec:8", "const:4:8"]]
- 00b480ec ["CALL", null, ["callee:00c5af10:8"]]
+ 00b48514 ["INT_ADD", "register:40f0:8", ["const:b48514:8", "const:4:8"]]
+ 00b48514 ["CALL", null, ["callee:00c5af10:8"]]
- 00b480ec bytes 894a0494
+ 00b48514 bytes 7f4a0494
- 00b480f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00b480f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b480f4 bytes 805602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05ecaf01d1193ab9ca48549d00fd81a6"></a>

### [`00b48160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48160.md) → [`00b48588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48588.md) _ZN8firebase4util6bundle13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b481a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b485c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4817c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48174",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4817c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b485cc"
      ]
    ],
    [
      "unmatched:00b48184",
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4859c",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b485a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b485cc"
      ]
    ],
    [
      "00b485ac",
      "PARAM",
      [
        "storage",
        "002b999b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4817c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48160.md#insn-00b4817c) · [`00b48198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48160.md#insn-00b48198) · [`00b481a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48160.md#insn-00b481a0)
- 新版 [`00b485c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48588.md#insn-00b485c0)

~~~diff
- 00b4817c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4817c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4817c bytes 410100b5
- 00b48198 ["INT_ADD", "register:40f0:8", ["const:b48198:8", "const:4:8"]]
- 00b48198 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b485c0 ["INT_ADD", "register:40f0:8", ["const:b485c0:8", "const:4:8"]]
+ 00b485c0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b48198 bytes 5e4a0494
+ 00b485c0 bytes 544a0494
- 00b481a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00b481a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b481a0 bytes 805602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-414f9b4cd28a55f1ed62e4738711c43b"></a>

### [`00b4820c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4820c.md) → [`00b48634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48634.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48238"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48660"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48648",
      "incomplete_value": true,
      "site": "00b48648",
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
      "definition_site": "00b48220",
      "incomplete_value": true,
      "site": "00b48220",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48644",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4822c",
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b48230",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00b48644",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48654",
      "PARAM",
      [
        "storage",
        "002a6047",
        null,
        "string"
      ]
    ],
    [
      "00b48658",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4820c.md#insn-00b48220) · [`00b48230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4820c.md#insn-00b48230) · [`00b48238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4820c.md#insn-00b48238)
- 新版 [`00b48648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48634.md#insn-00b48648)

~~~diff
- 00b48220 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b48220 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b48648 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b48648 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b48220 bytes e80000b5
+ 00b48648 bytes e80000b5
- 00b48230 ["INT_ADD", "register:40f0:8", ["const:b48230:8", "const:4:8"]]
- 00b48230 ["CALL", null, ["callee:00c5af10:8"]]
- 00b48230 bytes 384a0494
- 00b48238 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00b48238 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48238 bytes 608602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4ce55af76195e20076db3edcd7c8fdd"></a>

### [`00b4824c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4824c.md) → [`00b48674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48674.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b486a0",
      "incomplete_value": true,
      "site": "00b486a0",
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
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48278",
      "incomplete_value": true,
      "site": "00b48278",
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
            "const:508:8"
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
      "definition_site": "00b48688",
      "incomplete_value": true,
      "site": "00b48688",
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
      "definition_site": "00b48260",
      "incomplete_value": true,
      "site": "00b48260",
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
      "definition_site": "00b48690",
      "incomplete_value": false,
      "site": "00b48698",
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
            "const:47:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48268",
      "incomplete_value": false,
      "site": "00b48270",
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
            "const:f6b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48684",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48690",
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ],
    [
      "00b486a0",
      "WRITE",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48684",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48690",
      "PARAM",
      [
        "storage",
        "002a6047",
        null,
        "string"
      ]
    ],
    [
      "00b486a0",
      "WRITE",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4824c.md#insn-00b48270) · [`00b48278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4824c.md#insn-00b48278) · [`00b4825c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4824c.md#insn-00b4825c)
- 新版 [`00b48698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48674.md#insn-00b48698) · [`00b486a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48674.md#insn-00b486a0) · [`00b48684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48674.md#insn-00b48684)

~~~diff
- 00b48270 ["INT_ADD", "register:40f0:8", ["const:b48270:8", "const:4:8"]]
- 00b48270 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b48698 ["INT_ADD", "register:40f0:8", ["const:b48698:8", "const:4:8"]]
+ 00b48698 ["CALL", null, ["callee:00c5af10:8"]]
- 00b48270 bytes 284a0494
+ 00b48698 bytes 1e4a0494
- 00b48278 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00b48278 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b486a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
+ 00b486a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48278 bytes 608602f9
+ 00b486a0 bytes 608604f9
- 00b4825c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00b4825c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48684 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
+ 00b48684 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4825c bytes 688642f9
+ 00b48684 bytes 688644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01fe77f4cd2750f11720f5096ae89fb6"></a>

### [`00b4828c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4828c.md) → [`00b486b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b486b4.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b486e4",
      "incomplete_value": true,
      "site": "00b486e4",
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
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b482bc",
      "incomplete_value": true,
      "site": "00b482bc",
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
            "const:508:8"
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
      "definition_site": "00b486c8",
      "incomplete_value": true,
      "site": "00b486c8",
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
      "definition_site": "00b482a0",
      "incomplete_value": true,
      "site": "00b482a0",
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
      "definition_site": "00b486d4",
      "incomplete_value": false,
      "site": "00b486dc",
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
            "const:47:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b482ac",
      "incomplete_value": false,
      "site": "00b482b4",
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
            "const:f6b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b486c4",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b486d4",
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ],
    [
      "00b486e4",
      "WRITE",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b486c4",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ],
    [
      "00b486d4",
      "PARAM",
      [
        "storage",
        "002a6047",
        null,
        "string"
      ]
    ],
    [
      "00b486e4",
      "WRITE",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b482b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4828c.md#insn-00b482b4) · [`00b482bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4828c.md#insn-00b482bc) · [`00b4829c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4828c.md#insn-00b4829c)
- 新版 [`00b486dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b486b4.md#insn-00b486dc) · [`00b486e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b486b4.md#insn-00b486e4) · [`00b486c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b486b4.md#insn-00b486c4)

~~~diff
- 00b482b4 ["INT_ADD", "register:40f0:8", ["const:b482b4:8", "const:4:8"]]
- 00b482b4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b486dc ["INT_ADD", "register:40f0:8", ["const:b486dc:8", "const:4:8"]]
+ 00b486dc ["CALL", null, ["callee:00c5af10:8"]]
- 00b482b4 bytes 174a0494
+ 00b486dc bytes 0d4a0494
- 00b482bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00b482bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b486e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
+ 00b486e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b482bc bytes 608602f9
+ 00b486e4 bytes 608604f9
- 00b4829c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00b4829c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b486c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
+ 00b486c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4829c bytes 688642f9
+ 00b486c4 bytes 688644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8148ef81ee171a0be2978c9e6c099389"></a>

### [`00b482d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b482d0.md) → [`00b486f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b486f8.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b482d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b482d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b482d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b482d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b482d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b48708",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b486f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b486fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b48708",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b482d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b482d0.md#insn-00b482d0) · [`00b482d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b482d0.md#insn-00b482d4) · [`00b482e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b482d0.md#insn-00b482e4)
- 新版 [`00b4870c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b486f8.md#insn-00b4870c)

~~~diff
- 00b482d0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b482d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b482d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b482d0 bytes f30f1ef8
- 00b482d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b482d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b482d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b482d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b482d4 bytes fd7b01a9
- 00b482e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b482e4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b4870c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4870c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b482e4 bytes 080100b5
+ 00b4870c bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e22cf060db421fe3c155c3bcf8df467"></a>

### [`00b48320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48320.md) → [`00b48748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48748.md) _ZN8firebase4util10byte_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b487d0",
      "incomplete_value": true,
      "site": "00b487d0",
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
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b483a8",
      "incomplete_value": true,
      "site": "00b483a8",
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
            "const:510:8"
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
      "definition_site": "00b4877c",
      "incomplete_value": true,
      "site": "00b48788",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48354",
      "incomplete_value": true,
      "site": "00b48360",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:508:8"
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
      "00b4875c",
      "READ",
      [
        "storage",
        "01125510",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4877c",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b487d0",
      "WRITE",
      [
        "storage",
        "01125510",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4875c",
      "READ",
      [
        "storage",
        "01125910",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4877c",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ],
    [
      "00b487d0",
      "WRITE",
      [
        "storage",
        "01125910",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48320.md#insn-00b48360) · [`00b483a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48320.md#insn-00b483a8) · [`00b48334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48320.md#insn-00b48334)
- 新版 [`00b48788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48748.md#insn-00b48788) · [`00b487d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48748.md#insn-00b487d0) · [`00b4875c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48748.md#insn-00b4875c)

~~~diff
- 00b48360 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48360 ["INT_ADD", "register:40f0:8", ["const:b48360:8", "const:4:8"]]
- 00b48360 ["CALLIND", null, ["register:0:8"]]
+ 00b48788 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48788 ["INT_ADD", "register:40f0:8", ["const:b48788:8", "const:4:8"]]
+ 00b48788 ["CALLIND", null, ["register:0:8"]]
- 00b48360 bytes 00013fd6
+ 00b48788 bytes 00013fd6
- 00b483a8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b483a8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:510:8"]]
- 00b483a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b487d0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b487d0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:910:8"]]
+ 00b487d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b483a8 bytes a0421439
+ 00b487d0 bytes a0422439
- 00b48334 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:510:8"]]
- 00b48334 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b48334 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4875c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:910:8"]]
+ 00b4875c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4875c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b48334 bytes a8425439
+ 00b4875c bytes a8426439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21c2d7378f02bbaaef03f0042ef78bfd"></a>

### [`00b483bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b483bc.md) → [`00b487e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b487e4.md) _ZN8firebase4util10byte_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 45.45% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48820",
      "incomplete_value": true,
      "site": "00b48820",
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
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b483f8",
      "incomplete_value": true,
      "site": "00b483f8",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48870"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b487f8",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48804",
      "READ",
      [
        "storage",
        "01125510",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48820",
      "WRITE",
      [
        "storage",
        "01125510",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b487f8",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48804",
      "READ",
      [
        "storage",
        "01125910",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48820",
      "WRITE",
      [
        "storage",
        "01125910",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b483d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b483bc.md#insn-00b483d4) · [`00b483f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b483bc.md#insn-00b483f8) · [`00b48444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b483bc.md#insn-00b48444)
- 新版 [`00b487fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b487e4.md#insn-00b487fc) · [`00b48820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b487e4.md#insn-00b48820)

~~~diff
- 00b483d4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b483d4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b487fc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b487fc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b483d4 bytes c10300b4
+ 00b487fc bytes c10300b4
- 00b483f8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b483f8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b483f8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:510:8"]]
- 00b483f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b48820 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b48820 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b48820 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:910:8"]]
+ 00b48820 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b483f8 bytes bf421439
+ 00b48820 bytes bf422439
- 00b48444 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48444 ["INT_ADD", "register:40f0:8", ["const:b48444:8", "const:4:8"]]
- 00b48444 ["CALLIND", null, ["register:0:8"]]
- 00b48444 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e928bcb9fb80b58ded4ba8e28cfbdad2"></a>

### [`00b4845c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4845c.md) → [`00b48884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48884.md) _ZN8firebase4util10byte_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4849c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b488c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48478"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48470",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b48478",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b488c8"
      ]
    ],
    [
      "unmatched:00b48480",
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48898",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ],
    [
      "00b488a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b488c8"
      ]
    ],
    [
      "00b488a8",
      "PARAM",
      [
        "storage",
        "002a6047",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4845c.md#insn-00b48478) · [`00b48494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4845c.md#insn-00b48494) · [`00b4849c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4845c.md#insn-00b4849c)
- 新版 [`00b488bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48884.md#insn-00b488bc)

~~~diff
- 00b48478 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b48478 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b48478 bytes 410100b5
- 00b48494 ["INT_ADD", "register:40f0:8", ["const:b48494:8", "const:4:8"]]
- 00b48494 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b488bc ["INT_ADD", "register:40f0:8", ["const:b488bc:8", "const:4:8"]]
+ 00b488bc ["CALL", null, ["callee:00c5af10:8"]]
- 00b48494 bytes 9f490494
+ 00b488bc bytes 95490494
- 00b4849c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00b4849c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4849c bytes 808602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96e2f4d6b64f692cc3e823560932d125"></a>

### [`00b484cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b484cc.md) → [`00b488f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b488f4.md) _ZN8firebase4util10byte_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48910",
      "incomplete_value": false,
      "site": "00b48914",
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
      "definition_site": "00b484e8",
      "incomplete_value": false,
      "site": "00b484ec",
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
      "definition_site": "00b48920",
      "incomplete_value": true,
      "site": "00b4892c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b484f8",
      "incomplete_value": true,
      "site": "00b48504",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48910",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b48920",
      "DATA",
      [
        "storage",
        "01125518",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b48910",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b48920",
      "DATA",
      [
        "storage",
        "01125918",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b484ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b484cc.md#insn-00b484ec) · [`00b484e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b484cc.md#insn-00b484e8) · [`00b484f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b484cc.md#insn-00b484f4)
- 新版 [`00b48914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b488f4.md#insn-00b48914) · [`00b48910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b488f4.md#insn-00b48910) · [`00b4891c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b488f4.md#insn-00b4891c)

~~~diff
- 00b484ec ["INT_ADD", "register:40f0:8", ["const:b484ec:8", "const:4:8"]]
- 00b484ec ["CALL", null, ["callee:00c5b000:8"]]
+ 00b48914 ["INT_ADD", "register:40f0:8", ["const:b48914:8", "const:4:8"]]
+ 00b48914 ["CALL", null, ["callee:00c5b000:8"]]
- 00b484ec bytes c5490494
+ 00b48914 bytes bb490494
- 00b484e8 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b484e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b484e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b484e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b48910 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b48910 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48910 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48910 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b484e8 bytes 00680a91
+ 00b48910 bytes 009c0d91
- 00b484f4 ["COPY", "tmp:0:8", ["const:518:8"]]
- 00b484f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b484f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b484f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4891c ["COPY", "tmp:0:8", ["const:918:8"]]
+ 00b4891c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4891c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4891c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b484f4 bytes 08611491
+ 00b4891c bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5469d69078854824c20fb311476c4a65"></a>

### [`00b48508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48508.md) → [`00b48930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48930.md) _ZN8firebase4util10byte_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48970",
      "incomplete_value": true,
      "site": "00b48970",
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
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48548",
      "incomplete_value": true,
      "site": "00b48548",
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
            "const:508:8"
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
      "definition_site": "00b4894c",
      "incomplete_value": true,
      "site": "00b4894c",
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
      "definition_site": "00b48524",
      "incomplete_value": true,
      "site": "00b48524",
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
      "definition_site": "00b48954",
      "incomplete_value": false,
      "site": "00b48968",
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
            "const:47:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4852c",
      "incomplete_value": false,
      "site": "00b48540",
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
            "const:f6b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48944",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48954",
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ],
    [
      "00b48970",
      "WRITE",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48944",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48954",
      "PARAM",
      [
        "storage",
        "002a6047",
        null,
        "string"
      ]
    ],
    [
      "00b48970",
      "WRITE",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48508.md#insn-00b48540) · [`00b48548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48508.md#insn-00b48548) · [`00b4851c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48508.md#insn-00b4851c)
- 新版 [`00b48968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48930.md#insn-00b48968) · [`00b48970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48930.md#insn-00b48970) · [`00b48944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48930.md#insn-00b48944)

~~~diff
- 00b48540 ["INT_ADD", "register:40f0:8", ["const:b48540:8", "const:4:8"]]
- 00b48540 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b48968 ["INT_ADD", "register:40f0:8", ["const:b48968:8", "const:4:8"]]
+ 00b48968 ["CALL", null, ["callee:00c5af10:8"]]
- 00b48540 bytes 74490494
+ 00b48968 bytes 6a490494
- 00b48548 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00b48548 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48970 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:908:8"]]
+ 00b48970 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48548 bytes 808602f9
+ 00b48970 bytes 808604f9
- 00b4851c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00b4851c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48944 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:908:8"]]
+ 00b48944 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4851c bytes 818642f9
+ 00b48944 bytes 818644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c8721e061002d1d887b1a76ca9fc88f"></a>

### [`00b48578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48578.md) → [`00b489a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b489a0.md) _ZN8firebase4util10byte_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b489bc",
      "incomplete_value": false,
      "site": "00b489c0",
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
      "definition_site": "00b48594",
      "incomplete_value": false,
      "site": "00b48598",
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
      "definition_site": "00b489cc",
      "incomplete_value": true,
      "site": "00b489d8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b485a4",
      "incomplete_value": true,
      "site": "00b485b0",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b489bc",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b489cc",
      "DATA",
      [
        "storage",
        "01125528",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b489bc",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b489cc",
      "DATA",
      [
        "storage",
        "01125928",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48578.md#insn-00b48598) · [`00b48594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48578.md#insn-00b48594) · [`00b485a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48578.md#insn-00b485a0)
- 新版 [`00b489c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b489a0.md#insn-00b489c0) · [`00b489bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b489a0.md#insn-00b489bc) · [`00b489c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b489a0.md#insn-00b489c8)

~~~diff
- 00b48598 ["INT_ADD", "register:40f0:8", ["const:b48598:8", "const:4:8"]]
- 00b48598 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b489c0 ["INT_ADD", "register:40f0:8", ["const:b489c0:8", "const:4:8"]]
+ 00b489c0 ["CALL", null, ["callee:00c5b000:8"]]
- 00b48598 bytes 9a490494
+ 00b489c0 bytes 90490494
- 00b48594 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b48594 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b48594 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b48594 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b489bc ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b489bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b489bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b489bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b48594 bytes 00441191
+ 00b489bc bytes 00781491
- 00b485a0 ["COPY", "tmp:0:8", ["const:528:8"]]
- 00b485a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b485a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b485a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b489c8 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 00b489c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b489c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b489c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b485a0 bytes 08a11491
+ 00b489c8 bytes 08a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1110d951e6e53566a7adfca84f31e44b"></a>

### [`00b485f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b485f4.md) → [`00b48a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48a1c.md) _ZN8firebase4util15character_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 43.75% / 新版 43.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48620"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48a48"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48a30",
      "incomplete_value": true,
      "site": "00b48a30",
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
      "definition_site": "00b48608",
      "incomplete_value": true,
      "site": "00b48608",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48a2c",
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48a30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b48624"
      ]
    ],
    [
      "unmatched:00b48610",
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48a2c",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48a30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48a4c"
      ]
    ],
    [
      "00b48a38",
      "PARAM",
      [
        "storage",
        "002bbdf9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b485f4.md#insn-00b48608) · [`00b48618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b485f4.md#insn-00b48618) · [`00b48620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b485f4.md#insn-00b48620)
- 新版 [`00b48a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48a1c.md#insn-00b48a30)

~~~diff
- 00b48608 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b48608 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b48a30 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b48a30 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b48608 bytes e80000b5
+ 00b48a30 bytes e80000b5
- 00b48618 ["INT_ADD", "register:40f0:8", ["const:b48618:8", "const:4:8"]]
- 00b48618 ["CALL", null, ["callee:00c5af10:8"]]
- 00b48618 bytes 3e490494
- 00b48620 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00b48620 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48620 bytes 609a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55740bbf60d0708419ba6e7781ed61f2"></a>

### [`00b48634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48634.md) → [`00b48a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48a5c.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48a8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48a70",
      "incomplete_value": true,
      "site": "00b48a70",
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
      "definition_site": "00b48648",
      "incomplete_value": true,
      "site": "00b48648",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48a6c",
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48a70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b48668"
      ]
    ],
    [
      "unmatched:00b48654",
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48a6c",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48a70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48a90"
      ]
    ],
    [
      "00b48a7c",
      "PARAM",
      [
        "storage",
        "002bbdf9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4865c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48634.md#insn-00b4865c) · [`00b48664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48634.md#insn-00b48664) · [`00b48674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48634.md#insn-00b48674)

~~~diff
- 00b4865c ["INT_ADD", "register:40f0:8", ["const:b4865c:8", "const:4:8"]]
- 00b4865c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4865c bytes 2d490494
- 00b48664 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00b48664 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48664 bytes 609a02f9
- 00b48674 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b48674 ["RETURN", null, ["register:0:8"]]
- 00b48674 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99fae92b1159c706b40354e1dda44368"></a>

### [`00b48678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48678.md) → [`00b48aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48aa0.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b486a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48ad0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48ab4",
      "incomplete_value": true,
      "site": "00b48ab4",
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
      "definition_site": "00b4868c",
      "incomplete_value": true,
      "site": "00b4868c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48ab0",
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48ab4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b486ac"
      ]
    ],
    [
      "unmatched:00b48694",
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48ab0",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48ab4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48ad4"
      ]
    ],
    [
      "00b48abc",
      "PARAM",
      [
        "storage",
        "002bbdf9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b486a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48678.md#insn-00b486a0) · [`00b486a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48678.md#insn-00b486a8) · [`00b486b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48678.md#insn-00b486b8)
- 新版 [`00b48ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48aa0.md#insn-00b48ac8)

~~~diff
- 00b486a0 ["INT_ADD", "register:40f0:8", ["const:b486a0:8", "const:4:8"]]
- 00b486a0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b48ac8 ["INT_ADD", "register:40f0:8", ["const:b48ac8:8", "const:4:8"]]
+ 00b48ac8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b486a0 bytes 1c490494
+ 00b48ac8 bytes 12490494
- 00b486a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00b486a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b486a8 bytes 609a02f9
- 00b486b8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b486b8 ["RETURN", null, ["register:0:8"]]
- 00b486b8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7660a3baed3b1fb55423289cb8bf91ff"></a>

### [`00b486c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b486c8.md) → [`00b48af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48af0.md) _ZN8firebase4util15character_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48b78",
      "incomplete_value": true,
      "site": "00b48b78",
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
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48750",
      "incomplete_value": true,
      "site": "00b48750",
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
            "const:538:8"
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
      "definition_site": "00b48b24",
      "incomplete_value": true,
      "site": "00b48b30",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
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
      "definition_site": "00b486fc",
      "incomplete_value": true,
      "site": "00b48708",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
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
      "00b48b04",
      "READ",
      [
        "storage",
        "01125538",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48b24",
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48b78",
      "WRITE",
      [
        "storage",
        "01125538",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48b04",
      "READ",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48b24",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48b78",
      "WRITE",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b486c8.md#insn-00b48708) · [`00b48750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b486c8.md#insn-00b48750) · [`00b486dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b486c8.md#insn-00b486dc)
- 新版 [`00b48b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48af0.md#insn-00b48b30) · [`00b48b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48af0.md#insn-00b48b78) · [`00b48b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48af0.md#insn-00b48b04)

~~~diff
- 00b48708 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48708 ["INT_ADD", "register:40f0:8", ["const:b48708:8", "const:4:8"]]
- 00b48708 ["CALLIND", null, ["register:0:8"]]
+ 00b48b30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48b30 ["INT_ADD", "register:40f0:8", ["const:b48b30:8", "const:4:8"]]
+ 00b48b30 ["CALLIND", null, ["register:0:8"]]
- 00b48708 bytes 00013fd6
+ 00b48b30 bytes 00013fd6
- 00b48750 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b48750 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:538:8"]]
- 00b48750 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b48b78 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b48b78 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:938:8"]]
+ 00b48b78 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b48750 bytes a0e21439
+ 00b48b78 bytes a0e22439
- 00b486dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:538:8"]]
- 00b486dc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b486dc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b48b04 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:938:8"]]
+ 00b48b04 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b48b04 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b486dc bytes a8e25439
+ 00b48b04 bytes a8e26439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57d450a61d3153e14e03da70ef797fc4"></a>

### [`00b48764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48764.md) → [`00b48b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48b8c.md) _ZN8firebase4util15character_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 77.78% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48bc8",
      "incomplete_value": true,
      "site": "00b48bc8",
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
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b487a0",
      "incomplete_value": true,
      "site": "00b487a0",
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
            "const:538:8"
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
      "definition_site": "00b48c18",
      "incomplete_value": true,
      "site": "00b48c18",
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
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b487f0",
      "incomplete_value": true,
      "site": "00b487f0",
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
            "const:530:8"
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
      "definition_site": "00b48ba4",
      "incomplete_value": true,
      "site": "00b48ba4",
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
      "definition_site": "00b4877c",
      "incomplete_value": true,
      "site": "00b4877c",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48ba0",
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48bac",
      "READ",
      [
        "storage",
        "01125538",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48bc8",
      "WRITE",
      [
        "storage",
        "01125538",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48ba0",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48bac",
      "READ",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48bc8",
      "WRITE",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4877c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48764.md#insn-00b4877c) · [`00b487a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48764.md#insn-00b487a0) · [`00b487ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48764.md#insn-00b487ec)
- 新版 [`00b48ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48b8c.md#insn-00b48ba4) · [`00b48bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48b8c.md#insn-00b48bc8) · [`00b48c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48b8c.md#insn-00b48c14)

~~~diff
- 00b4877c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4877c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b48ba4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b48ba4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b4877c bytes c10300b4
+ 00b48ba4 bytes c10300b4
- 00b487a0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b487a0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b487a0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:538:8"]]
- 00b487a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b48bc8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b48bc8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b48bc8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:938:8"]]
+ 00b48bc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b487a0 bytes bfe21439
+ 00b48bc8 bytes bfe22439
- 00b487ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b487ec ["INT_ADD", "register:40f0:8", ["const:b487ec:8", "const:4:8"]]
- 00b487ec ["CALLIND", null, ["register:0:8"]]
+ 00b48c14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48c14 ["INT_ADD", "register:40f0:8", ["const:b48c14:8", "const:4:8"]]
+ 00b48c14 ["CALLIND", null, ["register:0:8"]]
- 00b487ec bytes 00013fd6
+ 00b48c14 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21b8e4b8b58b270818fb7369f443a183"></a>

### [`00b48804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48804.md) → [`00b48c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48c2c.md) _ZN8firebase4util15character_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48844"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48c6c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48820"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48818",
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b48820",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48c70"
      ]
    ],
    [
      "unmatched:00b48828",
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48c40",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48c48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48c70"
      ]
    ],
    [
      "00b48c50",
      "PARAM",
      [
        "storage",
        "002bbdf9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48804.md#insn-00b48820) · [`00b4883c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48804.md#insn-00b4883c) · [`00b48844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48804.md#insn-00b48844)
- 新版 [`00b48c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48c2c.md#insn-00b48c64)

~~~diff
- 00b48820 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b48820 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b48820 bytes 410100b5
- 00b4883c ["INT_ADD", "register:40f0:8", ["const:b4883c:8", "const:4:8"]]
- 00b4883c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b48c64 ["INT_ADD", "register:40f0:8", ["const:b48c64:8", "const:4:8"]]
+ 00b48c64 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4883c bytes b5480494
+ 00b48c64 bytes ab480494
- 00b48844 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00b48844 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48844 bytes 809a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fe6bf7cead691d4c72a2615862a35b1"></a>

### [`00b488b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b488b0.md) → [`00b48cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48cd8.md) _ZN8firebase4util15character_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b488f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48d18"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b488cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b488c4",
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b488cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48d1c"
      ]
    ],
    [
      "unmatched:00b488d4",
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48cec",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48cf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48d1c"
      ]
    ],
    [
      "00b48cfc",
      "PARAM",
      [
        "storage",
        "002bbdf9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b488cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b488b0.md#insn-00b488cc) · [`00b488e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b488b0.md#insn-00b488e8) · [`00b488f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b488b0.md#insn-00b488f0)
- 新版 [`00b48d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48cd8.md#insn-00b48d10)

~~~diff
- 00b488cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b488cc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b488cc bytes 410100b5
- 00b488e8 ["INT_ADD", "register:40f0:8", ["const:b488e8:8", "const:4:8"]]
- 00b488e8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b48d10 ["INT_ADD", "register:40f0:8", ["const:b48d10:8", "const:4:8"]]
+ 00b48d10 ["CALL", null, ["callee:00c5af10:8"]]
- 00b488e8 bytes 8a480494
+ 00b48d10 bytes 80480494
- 00b488f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00b488f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b488f0 bytes 809a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa57703c4362786d1e47968721c0f314"></a>

### [`00b4895c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4895c.md) → [`00b48d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48d84.md) _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48db0",
      "incomplete_value": true,
      "site": "00b48db0",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48988",
      "incomplete_value": true,
      "site": "00b48988",
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
            "const:558:8"
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
      "definition_site": "00b48d98",
      "incomplete_value": true,
      "site": "00b48d98",
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
      "definition_site": "00b48970",
      "incomplete_value": true,
      "site": "00b48970",
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
      "definition_site": "00b48da4",
      "incomplete_value": false,
      "site": "00b48da8",
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
            "const:40e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4897c",
      "incomplete_value": false,
      "site": "00b48980",
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
            "const:341:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48d94",
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48da4",
      "PARAM",
      [
        "storage",
        "002a8341",
        null,
        "string"
      ]
    ],
    [
      "00b48db0",
      "WRITE",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48d94",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48da4",
      "PARAM",
      [
        "storage",
        "002a840e",
        null,
        "string"
      ]
    ],
    [
      "00b48db0",
      "WRITE",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4895c.md#insn-00b48980) · [`00b48988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4895c.md#insn-00b48988) · [`00b4896c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4895c.md#insn-00b4896c)
- 新版 [`00b48da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48d84.md#insn-00b48da8) · [`00b48db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48d84.md#insn-00b48db0) · [`00b48d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48d84.md#insn-00b48d94)

~~~diff
- 00b48980 ["INT_ADD", "register:40f0:8", ["const:b48980:8", "const:4:8"]]
- 00b48980 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b48da8 ["INT_ADD", "register:40f0:8", ["const:b48da8:8", "const:4:8"]]
+ 00b48da8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b48980 bytes 64480494
+ 00b48da8 bytes 5a480494
- 00b48988 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:558:8"]]
- 00b48988 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48db0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:958:8"]]
+ 00b48db0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48988 bytes 60ae02f9
+ 00b48db0 bytes 60ae04f9
- 00b4896c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:558:8"]]
- 00b4896c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48d94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:958:8"]]
+ 00b48d94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4896c bytes 68ae42f9
+ 00b48d94 bytes 68ae44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea49ecbcfeb5279ff0c6960faa2a2c71"></a>

### [`00b489dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b489dc.md) → [`00b48e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e04.md) _ZN8firebase4util11class_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48e34",
      "incomplete_value": true,
      "site": "00b48e34",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48a0c",
      "incomplete_value": true,
      "site": "00b48a0c",
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
            "const:558:8"
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
      "definition_site": "00b48e18",
      "incomplete_value": true,
      "site": "00b48e18",
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
      "definition_site": "00b489f0",
      "incomplete_value": true,
      "site": "00b489f0",
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
      "definition_site": "00b48e24",
      "incomplete_value": false,
      "site": "00b48e2c",
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
            "const:40e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b489fc",
      "incomplete_value": false,
      "site": "00b48a04",
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
            "const:341:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48e14",
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48e24",
      "PARAM",
      [
        "storage",
        "002a8341",
        null,
        "string"
      ]
    ],
    [
      "00b48e34",
      "WRITE",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48e14",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48e24",
      "PARAM",
      [
        "storage",
        "002a840e",
        null,
        "string"
      ]
    ],
    [
      "00b48e34",
      "WRITE",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b489dc.md#insn-00b48a04) · [`00b48a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b489dc.md#insn-00b48a0c) · [`00b489ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b489dc.md#insn-00b489ec)
- 新版 [`00b48e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e04.md#insn-00b48e2c) · [`00b48e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e04.md#insn-00b48e34) · [`00b48e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e04.md#insn-00b48e14)

~~~diff
- 00b48a04 ["INT_ADD", "register:40f0:8", ["const:b48a04:8", "const:4:8"]]
- 00b48a04 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b48e2c ["INT_ADD", "register:40f0:8", ["const:b48e2c:8", "const:4:8"]]
+ 00b48e2c ["CALL", null, ["callee:00c5af10:8"]]
- 00b48a04 bytes 43480494
+ 00b48e2c bytes 39480494
- 00b48a0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:558:8"]]
- 00b48a0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48e34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:958:8"]]
+ 00b48e34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48a0c bytes 60ae02f9
+ 00b48e34 bytes 60ae04f9
- 00b489ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:558:8"]]
- 00b489ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48e14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:958:8"]]
+ 00b48e14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b489ec bytes 68ae42f9
+ 00b48e14 bytes 68ae44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3ffb880b37102f1086444357992ed28"></a>

### [`00b48a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48a20.md) → [`00b48e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e48.md) _ZN8firebase4util11class_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48e78",
      "incomplete_value": true,
      "site": "00b48e78",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48a50",
      "incomplete_value": true,
      "site": "00b48a50",
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
            "const:558:8"
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
      "definition_site": "00b48e5c",
      "incomplete_value": true,
      "site": "00b48e5c",
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
      "definition_site": "00b48a34",
      "incomplete_value": true,
      "site": "00b48a34",
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
      "definition_site": "00b48e64",
      "incomplete_value": false,
      "site": "00b48e70",
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
            "const:40e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48a3c",
      "incomplete_value": false,
      "site": "00b48a48",
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
            "const:341:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48e58",
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48e64",
      "PARAM",
      [
        "storage",
        "002a8341",
        null,
        "string"
      ]
    ],
    [
      "00b48e78",
      "WRITE",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48e58",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48e64",
      "PARAM",
      [
        "storage",
        "002a840e",
        null,
        "string"
      ]
    ],
    [
      "00b48e78",
      "WRITE",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48a20.md#insn-00b48a48) · [`00b48a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48a20.md#insn-00b48a50) · [`00b48a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48a20.md#insn-00b48a30)
- 新版 [`00b48e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e48.md#insn-00b48e70) · [`00b48e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e48.md#insn-00b48e78) · [`00b48e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e48.md#insn-00b48e58)

~~~diff
- 00b48a48 ["INT_ADD", "register:40f0:8", ["const:b48a48:8", "const:4:8"]]
- 00b48a48 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b48e70 ["INT_ADD", "register:40f0:8", ["const:b48e70:8", "const:4:8"]]
+ 00b48e70 ["CALL", null, ["callee:00c5af10:8"]]
- 00b48a48 bytes 32480494
+ 00b48e70 bytes 28480494
- 00b48a50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:558:8"]]
- 00b48a50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48e78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:958:8"]]
+ 00b48e78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48a50 bytes 60ae02f9
+ 00b48e78 bytes 60ae04f9
- 00b48a30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:558:8"]]
- 00b48a30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48e58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:958:8"]]
+ 00b48e58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48a30 bytes 68ae42f9
+ 00b48e58 bytes 68ae44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e116fac2066cb7353923008ebd7e2b6a"></a>

### [`00b48a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48a70.md) → [`00b48e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e98.md) _ZN8firebase4util11class_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 22.22% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48a70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48a74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48a74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48a70",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48a74",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48a78",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b48e98",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b48e9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b48ea0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48a70.md#insn-00b48a70) · [`00b48a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48a70.md#insn-00b48a74) · [`00b48a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48a70.md#insn-00b48a78)

~~~diff
- 00b48a70 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b48a70 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b48a70 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b48a70 bytes f50f1df8
- 00b48a74 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b48a74 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b48a74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b48a74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b48a74 bytes f44f01a9
- 00b48a78 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b48a78 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b48a78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b48a78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b48a78 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93808cc19184f74012646e0cc43266fe"></a>

### [`00b48b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48b0c.md) → [`00b48f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48f34.md) _ZN8firebase4util11class_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 40.00% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48b48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48fc0",
      "incomplete_value": true,
      "site": "00b48fc0",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48b98",
      "incomplete_value": true,
      "site": "00b48b98",
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
            "const:558:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48f70"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48f48",
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48f54",
      "READ",
      [
        "storage",
        "01125560",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b48b48",
      "WRITE",
      [
        "storage",
        "01125560",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48f48",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48f54",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48f70",
      "WRITE",
      [
        "storage",
        "01125960",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48b0c.md#insn-00b48b24) · [`00b48b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48b0c.md#insn-00b48b48) · [`00b48b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48b0c.md#insn-00b48b94)
- 新版 [`00b48f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48f34.md#insn-00b48f4c) · [`00b48fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48f34.md#insn-00b48fbc)

~~~diff
- 00b48b24 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b48b24 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b48f4c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b48f4c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b48b24 bytes c10300b4
+ 00b48f4c bytes c10300b4
- 00b48b48 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b48b48 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b48b48 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:560:8"]]
- 00b48b48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b48b48 bytes bf821539
- 00b48b94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48b94 ["INT_ADD", "register:40f0:8", ["const:b48b94:8", "const:4:8"]]
- 00b48b94 ["CALLIND", null, ["register:0:8"]]
+ 00b48fbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48fbc ["INT_ADD", "register:40f0:8", ["const:b48fbc:8", "const:4:8"]]
+ 00b48fbc ["CALLIND", null, ["register:0:8"]]
- 00b48b94 bytes 00013fd6
+ 00b48fbc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c857f92ef843af0de6935abc63c11fa"></a>

### [`00b48bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48bac.md) → [`00b48fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48fd4.md) _ZN8firebase4util11class_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48bac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48bac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48bb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48bac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48bb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48bc0",
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48fd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b48fd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b48fe8",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48bac.md#insn-00b48bac) · [`00b48bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48bac.md#insn-00b48bb0) · [`00b48bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48bac.md#insn-00b48bc8)

~~~diff
- 00b48bac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b48bac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b48bac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b48bac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b48bac bytes f44fbea9
- 00b48bb0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b48bb0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b48bb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b48bb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b48bb0 bytes fd7b01a9
- 00b48bc8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b48bc8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b48bc8 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bb6ebcc8a3d43755d1d4b1331221bd7"></a>

### [`00b48c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48c1c.md) → [`00b49044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49044.md) _ZN8firebase4util11class_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49060",
      "incomplete_value": false,
      "site": "00b49064",
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
      "definition_site": "00b48c38",
      "incomplete_value": false,
      "site": "00b48c3c",
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
      "definition_site": "00b49070",
      "incomplete_value": true,
      "site": "00b4907c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b48c48",
      "incomplete_value": true,
      "site": "00b48c54",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49060",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b49070",
      "DATA",
      [
        "storage",
        "01125568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49060",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b49070",
      "DATA",
      [
        "storage",
        "01125968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48c1c.md#insn-00b48c3c) · [`00b48c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48c1c.md#insn-00b48c38) · [`00b48c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48c1c.md#insn-00b48c44)
- 新版 [`00b49064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49044.md#insn-00b49064) · [`00b49060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49044.md#insn-00b49060) · [`00b4906c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49044.md#insn-00b4906c)

~~~diff
- 00b48c3c ["INT_ADD", "register:40f0:8", ["const:b48c3c:8", "const:4:8"]]
- 00b48c3c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b49064 ["INT_ADD", "register:40f0:8", ["const:b49064:8", "const:4:8"]]
+ 00b49064 ["CALL", null, ["callee:00c5b000:8"]]
- 00b48c3c bytes f1470494
+ 00b49064 bytes e7470494
- 00b48c38 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b48c38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b48c38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b48c38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49060 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b49060 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49060 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49060 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b48c38 bytes 00680a91
+ 00b49060 bytes 009c0d91
- 00b48c44 ["COPY", "tmp:0:8", ["const:568:8"]]
- 00b48c44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b48c44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b48c44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4906c ["COPY", "tmp:0:8", ["const:968:8"]]
+ 00b4906c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4906c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4906c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b48c44 bytes 08a11591
+ 00b4906c bytes 08a12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d4d3f384ee1676c4af861bab10cb8af"></a>

### [`00b48c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48c58.md) → [`00b49080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49080.md) _ZN8firebase4util11class_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b490c0",
      "incomplete_value": true,
      "site": "00b490c0",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48c98",
      "incomplete_value": true,
      "site": "00b48c98",
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
            "const:558:8"
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
      "definition_site": "00b4909c",
      "incomplete_value": true,
      "site": "00b4909c",
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
      "definition_site": "00b48c74",
      "incomplete_value": true,
      "site": "00b48c74",
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
      "definition_site": "00b490a4",
      "incomplete_value": false,
      "site": "00b490b8",
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
            "const:40e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48c7c",
      "incomplete_value": false,
      "site": "00b48c90",
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
            "const:341:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49094",
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      "00b490a4",
      "PARAM",
      [
        "storage",
        "002a8341",
        null,
        "string"
      ]
    ],
    [
      "00b490c0",
      "WRITE",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49094",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ],
    [
      "00b490a4",
      "PARAM",
      [
        "storage",
        "002a840e",
        null,
        "string"
      ]
    ],
    [
      "00b490c0",
      "WRITE",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48c58.md#insn-00b48c90) · [`00b48c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48c58.md#insn-00b48c98) · [`00b48c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48c58.md#insn-00b48c6c)
- 新版 [`00b490b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49080.md#insn-00b490b8) · [`00b490c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49080.md#insn-00b490c0) · [`00b49094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49080.md#insn-00b49094)

~~~diff
- 00b48c90 ["INT_ADD", "register:40f0:8", ["const:b48c90:8", "const:4:8"]]
- 00b48c90 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b490b8 ["INT_ADD", "register:40f0:8", ["const:b490b8:8", "const:4:8"]]
+ 00b490b8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b48c90 bytes a0470494
+ 00b490b8 bytes 96470494
- 00b48c98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:558:8"]]
- 00b48c98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b490c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:958:8"]]
+ 00b490c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48c98 bytes 80ae02f9
+ 00b490c0 bytes 80ae04f9
- 00b48c6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:558:8"]]
- 00b48c6c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49094 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:958:8"]]
+ 00b49094 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48c6c bytes 81ae42f9
+ 00b49094 bytes 81ae44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d0c35aaf88fcc20d452801077954bf3"></a>

### [`00b48cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48cc8.md) → [`00b490f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b490f0.md) _ZN8firebase4util11class_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4910c",
      "incomplete_value": false,
      "site": "00b49110",
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
      "definition_site": "00b48ce4",
      "incomplete_value": false,
      "site": "00b48ce8",
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
      "definition_site": "00b4911c",
      "incomplete_value": true,
      "site": "00b49128",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b48cf4",
      "incomplete_value": true,
      "site": "00b48d00",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4910c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4911c",
      "DATA",
      [
        "storage",
        "01125578",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4910c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4911c",
      "DATA",
      [
        "storage",
        "01125978",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48cc8.md#insn-00b48ce8) · [`00b48ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48cc8.md#insn-00b48ce4) · [`00b48cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48cc8.md#insn-00b48cf0)
- 新版 [`00b49110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b490f0.md#insn-00b49110) · [`00b4910c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b490f0.md#insn-00b4910c) · [`00b49118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b490f0.md#insn-00b49118)

~~~diff
- 00b48ce8 ["INT_ADD", "register:40f0:8", ["const:b48ce8:8", "const:4:8"]]
- 00b48ce8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b49110 ["INT_ADD", "register:40f0:8", ["const:b49110:8", "const:4:8"]]
+ 00b49110 ["CALL", null, ["callee:00c5b000:8"]]
- 00b48ce8 bytes c6470494
+ 00b49110 bytes bc470494
- 00b48ce4 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b48ce4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b48ce4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b48ce4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4910c ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4910c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4910c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4910c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b48ce4 bytes 00441191
+ 00b4910c bytes 00781491
- 00b48cf0 ["COPY", "tmp:0:8", ["const:578:8"]]
- 00b48cf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b48cf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b48cf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b49118 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 00b49118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b48cf0 bytes 08e11591
+ 00b49118 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf9dc00fae06e2e388ae3fc1ebe38aac"></a>

### [`00b48d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d04.md) → [`00b4912c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4912c.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49158",
      "incomplete_value": true,
      "site": "00b49158",
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
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48d30",
      "incomplete_value": true,
      "site": "00b48d30",
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
            "const:580:8"
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
      "definition_site": "00b49140",
      "incomplete_value": true,
      "site": "00b49140",
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
      "definition_site": "00b48d18",
      "incomplete_value": true,
      "site": "00b48d18",
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
      "definition_site": "00b4914c",
      "incomplete_value": false,
      "site": "00b49150",
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
            "const:33f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48d24",
      "incomplete_value": false,
      "site": "00b48d28",
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
            "const:2ff:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4913c",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4914c",
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ],
    [
      "00b49158",
      "WRITE",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4913c",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4914c",
      "PARAM",
      [
        "storage",
        "002af33f",
        null,
        "string"
      ]
    ],
    [
      "00b49158",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d04.md#insn-00b48d28) · [`00b48d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d04.md#insn-00b48d30) · [`00b48d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d04.md#insn-00b48d14)
- 新版 [`00b49150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4912c.md#insn-00b49150) · [`00b49158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4912c.md#insn-00b49158) · [`00b4913c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4912c.md#insn-00b4913c)

~~~diff
- 00b48d28 ["INT_ADD", "register:40f0:8", ["const:b48d28:8", "const:4:8"]]
- 00b48d28 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b49150 ["INT_ADD", "register:40f0:8", ["const:b49150:8", "const:4:8"]]
+ 00b49150 ["CALL", null, ["callee:00c5af10:8"]]
- 00b48d28 bytes 7a470494
+ 00b49150 bytes 70470494
- 00b48d30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b48d30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49158 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b49158 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48d30 bytes 60c202f9
+ 00b49158 bytes 60c204f9
- 00b48d14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b48d14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4913c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b4913c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48d14 bytes 68c242f9
+ 00b4913c bytes 68c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93023f0b3e6dd23354cfa4d44b1a295a"></a>

### [`00b48d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d44.md) → [`00b4916c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4916c.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48d44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48d48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48d48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48d44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48d48",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4917c",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4916c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b49170",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4917c",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d44.md#insn-00b48d44) · [`00b48d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d44.md#insn-00b48d48) · [`00b48d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d44.md#insn-00b48d58)
- 新版 [`00b49180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4916c.md#insn-00b49180)

~~~diff
- 00b48d44 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b48d44 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b48d44 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b48d44 bytes f30f1ef8
- 00b48d48 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b48d48 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b48d48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b48d48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b48d48 bytes fd7b01a9
- 00b48d58 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b48d58 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b49180 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b49180 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b48d58 bytes e80000b5
+ 00b49180 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4059e5128fbf0f95a20a0f379f3b743f"></a>

### [`00b48d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d84.md) → [`00b491ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491ac.md) _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b491dc",
      "incomplete_value": true,
      "site": "00b491dc",
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
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48db4",
      "incomplete_value": true,
      "site": "00b48db4",
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
            "const:580:8"
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
      "definition_site": "00b491c0",
      "incomplete_value": true,
      "site": "00b491c0",
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
      "definition_site": "00b48d98",
      "incomplete_value": true,
      "site": "00b48d98",
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
      "definition_site": "00b491cc",
      "incomplete_value": false,
      "site": "00b491d4",
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
            "const:33f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48da4",
      "incomplete_value": false,
      "site": "00b48dac",
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
            "const:2ff:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b491bc",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b491cc",
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ],
    [
      "00b491dc",
      "WRITE",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b491bc",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b491cc",
      "PARAM",
      [
        "storage",
        "002af33f",
        null,
        "string"
      ]
    ],
    [
      "00b491dc",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d84.md#insn-00b48dac) · [`00b48db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d84.md#insn-00b48db4) · [`00b48d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d84.md#insn-00b48d94)
- 新版 [`00b491d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491ac.md#insn-00b491d4) · [`00b491dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491ac.md#insn-00b491dc) · [`00b491bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491ac.md#insn-00b491bc)

~~~diff
- 00b48dac ["INT_ADD", "register:40f0:8", ["const:b48dac:8", "const:4:8"]]
- 00b48dac ["CALL", null, ["callee:00c5af10:8"]]
+ 00b491d4 ["INT_ADD", "register:40f0:8", ["const:b491d4:8", "const:4:8"]]
+ 00b491d4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b48dac bytes 59470494
+ 00b491d4 bytes 4f470494
- 00b48db4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b48db4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b491dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b491dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48db4 bytes 60c202f9
+ 00b491dc bytes 60c204f9
- 00b48d94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b48d94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b491bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b491bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48d94 bytes 68c242f9
+ 00b491bc bytes 68c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed583b762bea430ae5b869d6efa75d1e"></a>

### [`00b48dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48dc8.md) → [`00b491f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491f0.md) _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49220",
      "incomplete_value": true,
      "site": "00b49220",
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
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48df8",
      "incomplete_value": true,
      "site": "00b48df8",
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
            "const:580:8"
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
      "definition_site": "00b49204",
      "incomplete_value": true,
      "site": "00b49204",
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
      "definition_site": "00b48ddc",
      "incomplete_value": true,
      "site": "00b48ddc",
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
      "definition_site": "00b4920c",
      "incomplete_value": false,
      "site": "00b49218",
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
            "const:33f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48de4",
      "incomplete_value": false,
      "site": "00b48df0",
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
            "const:2ff:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49200",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4920c",
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ],
    [
      "00b49220",
      "WRITE",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49200",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4920c",
      "PARAM",
      [
        "storage",
        "002af33f",
        null,
        "string"
      ]
    ],
    [
      "00b49220",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48dc8.md#insn-00b48df0) · [`00b48df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48dc8.md#insn-00b48df8) · [`00b48dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48dc8.md#insn-00b48dd8)
- 新版 [`00b49218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491f0.md#insn-00b49218) · [`00b49220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491f0.md#insn-00b49220) · [`00b49200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491f0.md#insn-00b49200)

~~~diff
- 00b48df0 ["INT_ADD", "register:40f0:8", ["const:b48df0:8", "const:4:8"]]
- 00b48df0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b49218 ["INT_ADD", "register:40f0:8", ["const:b49218:8", "const:4:8"]]
+ 00b49218 ["CALL", null, ["callee:00c5af10:8"]]
- 00b48df0 bytes 48470494
+ 00b49218 bytes 3e470494
- 00b48df8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b48df8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49220 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b49220 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48df8 bytes 60c202f9
+ 00b49220 bytes 60c204f9
- 00b48dd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b48dd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49200 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b49200 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48dd8 bytes 68c242f9
+ 00b49200 bytes 68c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a818d275b198c690a278befc1d2f3d0"></a>

### [`00b48e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48e18.md) → [`00b49240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49240.md) _ZN8firebase4util16content_resolver15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 50.00% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b492c8",
      "incomplete_value": true,
      "site": "00b492c8",
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
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48ea0",
      "incomplete_value": true,
      "site": "00b48ea0",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48e58"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b49280"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49254",
      "READ",
      [
        "storage",
        "01125588",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b48e4c",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b492c8",
      "WRITE",
      [
        "storage",
        "01125588",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49254",
      "READ",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49274",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b492c8",
      "WRITE",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48e18.md#insn-00b48e58) · [`00b48ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48e18.md#insn-00b48ea0)
- 新版 [`00b492c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49240.md#insn-00b492c8) · [`00b49280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49240.md#insn-00b49280)

~~~diff
- 00b48e58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48e58 ["INT_ADD", "register:40f0:8", ["const:b48e58:8", "const:4:8"]]
- 00b48e58 ["CALLIND", null, ["register:0:8"]]
- 00b48e58 bytes 00013fd6
- 00b48ea0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b48ea0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:588:8"]]
- 00b48ea0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b492c8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b492c8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:988:8"]]
+ 00b492c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b48ea0 bytes a0221639
+ 00b492c8 bytes a0222639
+ 00b49280 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49280 ["INT_ADD", "register:40f0:8", ["const:b49280:8", "const:4:8"]]
+ 00b49280 ["CALLIND", null, ["register:0:8"]]
+ 00b49280 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85097403ccb0767e443f92b51189b4a9"></a>

### [`00b48eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48eb4.md) → [`00b492dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b492dc.md) _ZN8firebase4util16content_resolver12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49318",
      "incomplete_value": true,
      "site": "00b49318",
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
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48ef0",
      "incomplete_value": true,
      "site": "00b48ef0",
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
            "const:588:8"
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
      "definition_site": "00b49368",
      "incomplete_value": true,
      "site": "00b49368",
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
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48f40",
      "incomplete_value": true,
      "site": "00b48f40",
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
            "const:580:8"
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
      "definition_site": "00b492f4",
      "incomplete_value": true,
      "site": "00b492f4",
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
      "definition_site": "00b48ecc",
      "incomplete_value": true,
      "site": "00b48ecc",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b492f0",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b492fc",
      "READ",
      [
        "storage",
        "01125588",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49318",
      "WRITE",
      [
        "storage",
        "01125588",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b492f0",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b492fc",
      "READ",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49318",
      "WRITE",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48eb4.md#insn-00b48ef0) · [`00b48f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48eb4.md#insn-00b48f3c) · [`00b48f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48eb4.md#insn-00b48f40)
- 新版 [`00b49318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b492dc.md#insn-00b49318) · [`00b49364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b492dc.md#insn-00b49364) · [`00b49368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b492dc.md#insn-00b49368)

~~~diff
- 00b48ef0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b48ef0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b48ef0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:588:8"]]
- 00b48ef0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b49318 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b49318 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b49318 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:988:8"]]
+ 00b49318 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b48ef0 bytes bf221639
+ 00b49318 bytes bf222639
- 00b48f3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48f3c ["INT_ADD", "register:40f0:8", ["const:b48f3c:8", "const:4:8"]]
- 00b48f3c ["CALLIND", null, ["register:0:8"]]
+ 00b49364 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49364 ["INT_ADD", "register:40f0:8", ["const:b49364:8", "const:4:8"]]
+ 00b49364 ["CALLIND", null, ["register:0:8"]]
- 00b48f3c bytes 00013fd6
+ 00b49364 bytes 00013fd6
- 00b48f40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00b48f40 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b48f40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b49368 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
+ 00b49368 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b49368 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b48f40 bytes 9fc202f9
+ 00b49368 bytes 9fc204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83827f780bdbab6ce2e4bc49e933095a"></a>

### [`00b48f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48f54.md) → [`00b4937c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4937c.md) _ZN8firebase4util16content_resolver14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48f94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b493bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48f70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48f68",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b48f70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b493c0"
      ]
    ],
    [
      "unmatched:00b48f78",
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b49390",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49398",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b493c0"
      ]
    ],
    [
      "00b493a0",
      "PARAM",
      [
        "storage",
        "002af33f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48f54.md#insn-00b48f70) · [`00b48f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48f54.md#insn-00b48f8c) · [`00b48f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48f54.md#insn-00b48f94)
- 新版 [`00b493b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4937c.md#insn-00b493b4)

~~~diff
- 00b48f70 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b48f70 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b48f70 bytes 410100b5
- 00b48f8c ["INT_ADD", "register:40f0:8", ["const:b48f8c:8", "const:4:8"]]
- 00b48f8c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b493b4 ["INT_ADD", "register:40f0:8", ["const:b493b4:8", "const:4:8"]]
+ 00b493b4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b48f8c bytes e1460494
+ 00b493b4 bytes d7460494
- 00b48f94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00b48f94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48f94 bytes 80c202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5238bbd7cc9a4b1acaab502d2102071a"></a>

### [`00b48fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48fc4.md) → [`00b493ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b493ec.md) _ZN8firebase4util16content_resolver11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49408",
      "incomplete_value": false,
      "site": "00b4940c",
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
      "definition_site": "00b48fe0",
      "incomplete_value": false,
      "site": "00b48fe4",
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
      "definition_site": "00b49418",
      "incomplete_value": true,
      "site": "00b49424",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b48ff0",
      "incomplete_value": true,
      "site": "00b48ffc",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49408",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b49418",
      "DATA",
      [
        "storage",
        "01125590",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49408",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b49418",
      "DATA",
      [
        "storage",
        "01125990",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48fc4.md#insn-00b48fe4) · [`00b48fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48fc4.md#insn-00b48fe0) · [`00b48fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48fc4.md#insn-00b48fec)
- 新版 [`00b4940c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b493ec.md#insn-00b4940c) · [`00b49408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b493ec.md#insn-00b49408) · [`00b49414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b493ec.md#insn-00b49414)

~~~diff
- 00b48fe4 ["INT_ADD", "register:40f0:8", ["const:b48fe4:8", "const:4:8"]]
- 00b48fe4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4940c ["INT_ADD", "register:40f0:8", ["const:b4940c:8", "const:4:8"]]
+ 00b4940c ["CALL", null, ["callee:00c5b000:8"]]
- 00b48fe4 bytes 07470494
+ 00b4940c bytes fd460494
- 00b48fe0 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b48fe0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b48fe0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b48fe0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49408 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b49408 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49408 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49408 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b48fe0 bytes 00680a91
+ 00b49408 bytes 009c0d91
- 00b48fec ["COPY", "tmp:0:8", ["const:590:8"]]
- 00b48fec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b48fec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b48fec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b49414 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 00b49414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b48fec bytes 08411691
+ 00b49414 bytes 08412691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d11025ea12f0c75cee21080b17cdd87"></a>

### [`00b49000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49000.md) → [`00b49428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49428.md) _ZN8firebase4util16content_resolver13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49468",
      "incomplete_value": true,
      "site": "00b49468",
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
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49040",
      "incomplete_value": true,
      "site": "00b49040",
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
            "const:580:8"
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
      "definition_site": "00b49444",
      "incomplete_value": true,
      "site": "00b49444",
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
      "definition_site": "00b4901c",
      "incomplete_value": true,
      "site": "00b4901c",
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
      "definition_site": "00b4944c",
      "incomplete_value": false,
      "site": "00b49460",
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
            "const:33f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49024",
      "incomplete_value": false,
      "site": "00b49038",
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
            "const:2ff:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4943c",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4944c",
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ],
    [
      "00b49468",
      "WRITE",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4943c",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4944c",
      "PARAM",
      [
        "storage",
        "002af33f",
        null,
        "string"
      ]
    ],
    [
      "00b49468",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49000.md#insn-00b49038) · [`00b49040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49000.md#insn-00b49040) · [`00b49014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49000.md#insn-00b49014)
- 新版 [`00b49460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49428.md#insn-00b49460) · [`00b49468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49428.md#insn-00b49468) · [`00b4943c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49428.md#insn-00b4943c)

~~~diff
- 00b49038 ["INT_ADD", "register:40f0:8", ["const:b49038:8", "const:4:8"]]
- 00b49038 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b49460 ["INT_ADD", "register:40f0:8", ["const:b49460:8", "const:4:8"]]
+ 00b49460 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49038 bytes b6460494
+ 00b49460 bytes ac460494
- 00b49040 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00b49040 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49468 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
+ 00b49468 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49040 bytes 80c202f9
+ 00b49468 bytes 80c204f9
- 00b49014 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00b49014 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4943c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
+ 00b4943c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49014 bytes 81c242f9
+ 00b4943c bytes 81c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-873007b51ce3141868af4cb6e94ed754"></a>

### [`00b490ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b490ac.md) → [`00b494d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b494d4.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_1

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49500",
      "incomplete_value": true,
      "site": "00b49500",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b490d8",
      "incomplete_value": true,
      "site": "00b490d8",
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
            "const:5a8:8"
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
      "definition_site": "00b494e8",
      "incomplete_value": true,
      "site": "00b494e8",
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
      "definition_site": "00b490c0",
      "incomplete_value": true,
      "site": "00b490c0",
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
      "definition_site": "00b494f4",
      "incomplete_value": false,
      "site": "00b494f8",
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
            "const:139:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b490cc",
      "incomplete_value": false,
      "site": "00b490d0",
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
            "const:f9:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b494e4",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b494f4",
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      "00b49500",
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b494e4",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b494f4",
      "PARAM",
      [
        "storage",
        "002ae139",
        null,
        "string"
      ]
    ],
    [
      "00b49500",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b490d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b490ac.md#insn-00b490d0) · [`00b490d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b490ac.md#insn-00b490d8) · [`00b490bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b490ac.md#insn-00b490bc)
- 新版 [`00b494f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b494d4.md#insn-00b494f8) · [`00b49500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b494d4.md#insn-00b49500) · [`00b494e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b494d4.md#insn-00b494e4)

~~~diff
- 00b490d0 ["INT_ADD", "register:40f0:8", ["const:b490d0:8", "const:4:8"]]
- 00b490d0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b494f8 ["INT_ADD", "register:40f0:8", ["const:b494f8:8", "const:4:8"]]
+ 00b494f8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b490d0 bytes 90460494
+ 00b494f8 bytes 86460494
- 00b490d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00b490d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49500 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b49500 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b490d8 bytes 60d602f9
+ 00b49500 bytes 60d604f9
- 00b490bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00b490bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b494e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b494e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b490bc bytes 68d642f9
+ 00b494e4 bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a313cee4dd534b206ab7c69ad5feb363"></a>

### [`00b490ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b490ec.md) → [`00b49514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49514.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49540",
      "incomplete_value": true,
      "site": "00b49540",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49118",
      "incomplete_value": true,
      "site": "00b49118",
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
            "const:5a8:8"
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
      "definition_site": "00b49528",
      "incomplete_value": true,
      "site": "00b49528",
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
      "definition_site": "00b49100",
      "incomplete_value": true,
      "site": "00b49100",
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
      "definition_site": "00b49530",
      "incomplete_value": false,
      "site": "00b49538",
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
            "const:139:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49108",
      "incomplete_value": false,
      "site": "00b49110",
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
            "const:f9:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49524",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49530",
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      "00b49540",
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49524",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49530",
      "PARAM",
      [
        "storage",
        "002ae139",
        null,
        "string"
      ]
    ],
    [
      "00b49540",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b490ec.md#insn-00b49110) · [`00b49118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b490ec.md#insn-00b49118) · [`00b490fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b490ec.md#insn-00b490fc)
- 新版 [`00b49538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49514.md#insn-00b49538) · [`00b49540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49514.md#insn-00b49540) · [`00b49524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49514.md#insn-00b49524)

~~~diff
- 00b49110 ["INT_ADD", "register:40f0:8", ["const:b49110:8", "const:4:8"]]
- 00b49110 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b49538 ["INT_ADD", "register:40f0:8", ["const:b49538:8", "const:4:8"]]
+ 00b49538 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49110 bytes 80460494
+ 00b49538 bytes 76460494
- 00b49118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00b49118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49540 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b49540 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49118 bytes 60d602f9
+ 00b49540 bytes 60d604f9
- 00b490fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00b490fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49524 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b49524 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b490fc bytes 68d642f9
+ 00b49524 bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d4e7d3438e6f4fb393bee430a1f3ee5"></a>

### [`00b4912c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4912c.md) → [`00b49554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49554.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49584",
      "incomplete_value": true,
      "site": "00b49584",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4915c",
      "incomplete_value": true,
      "site": "00b4915c",
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
            "const:5a8:8"
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
      "definition_site": "00b49568",
      "incomplete_value": true,
      "site": "00b49568",
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
      "definition_site": "00b49140",
      "incomplete_value": true,
      "site": "00b49140",
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
      "definition_site": "00b49574",
      "incomplete_value": false,
      "site": "00b4957c",
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
            "const:139:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4914c",
      "incomplete_value": false,
      "site": "00b49154",
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
            "const:f9:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49564",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49574",
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      "00b49584",
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49564",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49574",
      "PARAM",
      [
        "storage",
        "002ae139",
        null,
        "string"
      ]
    ],
    [
      "00b49584",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4912c.md#insn-00b49154) · [`00b4915c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4912c.md#insn-00b4915c) · [`00b4913c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4912c.md#insn-00b4913c)
- 新版 [`00b4957c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49554.md#insn-00b4957c) · [`00b49584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49554.md#insn-00b49584) · [`00b49564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49554.md#insn-00b49564)

~~~diff
- 00b49154 ["INT_ADD", "register:40f0:8", ["const:b49154:8", "const:4:8"]]
- 00b49154 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4957c ["INT_ADD", "register:40f0:8", ["const:b4957c:8", "const:4:8"]]
+ 00b4957c ["CALL", null, ["callee:00c5af10:8"]]
- 00b49154 bytes 6f460494
+ 00b4957c bytes 65460494
- 00b4915c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00b4915c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49584 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b49584 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4915c bytes 60d602f9
+ 00b49584 bytes 60d604f9
- 00b4913c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00b4913c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49564 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b49564 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4913c bytes 68d642f9
+ 00b49564 bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce02d53c29021bfed5b121433994915a"></a>

### [`00b49170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49170.md) → [`00b49598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49598.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b495c8",
      "incomplete_value": true,
      "site": "00b495c8",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b491a0",
      "incomplete_value": true,
      "site": "00b491a0",
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
            "const:5a8:8"
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
      "definition_site": "00b495ac",
      "incomplete_value": true,
      "site": "00b495ac",
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
      "definition_site": "00b49184",
      "incomplete_value": true,
      "site": "00b49184",
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
      "definition_site": "00b495b4",
      "incomplete_value": false,
      "site": "00b495c0",
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
            "const:139:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4918c",
      "incomplete_value": false,
      "site": "00b49198",
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
            "const:f9:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b495a8",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b495b4",
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      "00b495c8",
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b495a8",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b495b4",
      "PARAM",
      [
        "storage",
        "002ae139",
        null,
        "string"
      ]
    ],
    [
      "00b495c8",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49170.md#insn-00b49198) · [`00b491a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49170.md#insn-00b491a0) · [`00b49180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49170.md#insn-00b49180)
- 新版 [`00b495c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49598.md#insn-00b495c0) · [`00b495c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49598.md#insn-00b495c8) · [`00b495a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49598.md#insn-00b495a8)

~~~diff
- 00b49198 ["INT_ADD", "register:40f0:8", ["const:b49198:8", "const:4:8"]]
- 00b49198 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b495c0 ["INT_ADD", "register:40f0:8", ["const:b495c0:8", "const:4:8"]]
+ 00b495c0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49198 bytes 5e460494
+ 00b495c0 bytes 54460494
- 00b491a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00b491a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b495c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b495c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b491a0 bytes 60d602f9
+ 00b495c8 bytes 60d604f9
- 00b49180 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00b49180 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b495a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00b495a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49180 bytes 68d642f9
+ 00b495a8 bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9795e490a038ba34b0012c7b08149cac"></a>

### [`00b491c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b491c0.md) → [`00b495e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b495e8.md) _ZN8firebase4util7context15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 33.33% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49670",
      "incomplete_value": true,
      "site": "00b49670",
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
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49248",
      "incomplete_value": true,
      "site": "00b49248",
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
            "const:5b0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49200"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b49628"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b495fc",
      "READ",
      [
        "storage",
        "011255b0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b491f4",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49670",
      "WRITE",
      [
        "storage",
        "011255b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b495fc",
      "READ",
      [
        "storage",
        "011259b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4961c",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49670",
      "WRITE",
      [
        "storage",
        "011259b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b491c0.md#insn-00b49200) · [`00b49248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b491c0.md#insn-00b49248)
- 新版 [`00b49670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b495e8.md#insn-00b49670) · [`00b49628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b495e8.md#insn-00b49628)

~~~diff
- 00b49200 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49200 ["INT_ADD", "register:40f0:8", ["const:b49200:8", "const:4:8"]]
- 00b49200 ["CALLIND", null, ["register:0:8"]]
- 00b49200 bytes 00013fd6
- 00b49248 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b49248 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5b0:8"]]
- 00b49248 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b49670 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b49670 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9b0:8"]]
+ 00b49670 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b49248 bytes a0c21639
+ 00b49670 bytes a0c22639
+ 00b49628 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49628 ["INT_ADD", "register:40f0:8", ["const:b49628:8", "const:4:8"]]
+ 00b49628 ["CALLIND", null, ["register:0:8"]]
+ 00b49628 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b1d1c697f26354ff4e4e676ab9f3fb6"></a>

### [`00b4925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4925c.md) → [`00b49684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49684.md) _ZN8firebase4util7context12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 63.64% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b496c0",
      "incomplete_value": true,
      "site": "00b496c0",
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
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49298",
      "incomplete_value": true,
      "site": "00b49298",
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
            "const:5b0:8"
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
      "definition_site": "00b49710",
      "incomplete_value": true,
      "site": "00b49710",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b492e8",
      "incomplete_value": true,
      "site": "00b492e8",
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
            "const:5a8:8"
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
      "definition_site": "00b4969c",
      "incomplete_value": true,
      "site": "00b4969c",
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
      "definition_site": "00b49274",
      "incomplete_value": true,
      "site": "00b49274",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49698",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b496a4",
      "READ",
      [
        "storage",
        "011255b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b496c0",
      "WRITE",
      [
        "storage",
        "011255b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49698",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b496a4",
      "READ",
      [
        "storage",
        "011259b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b496c0",
      "WRITE",
      [
        "storage",
        "011259b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4925c.md#insn-00b49274) · [`00b49298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4925c.md#insn-00b49298) · [`00b492c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4925c.md#insn-00b492c0)
- 新版 [`00b4969c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49684.md#insn-00b4969c) · [`00b496c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49684.md#insn-00b496c0)

~~~diff
- 00b49274 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b49274 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b4969c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b4969c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b49274 bytes c10300b4
+ 00b4969c bytes c10300b4
- 00b49298 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b49298 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b49298 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5b0:8"]]
- 00b49298 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b496c0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b496c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b496c0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9b0:8"]]
+ 00b496c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b49298 bytes bfc21639
+ 00b496c0 bytes bfc22639
- 00b492c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b492c0 ["INT_ADD", "register:40f0:8", ["const:b492c0:8", "const:4:8"]]
- 00b492c0 ["CALLIND", null, ["register:0:8"]]
- 00b492c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4788d9a03ee55c020f4c6f09fe077eea"></a>

### [`00b492fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b492fc.md) → [`00b49724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49724.md) _ZN8firebase4util7context14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49764",
      "incomplete_value": true,
      "site": "00b49764",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4933c",
      "incomplete_value": true,
      "site": "00b4933c",
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
            "const:5a8:8"
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
      "definition_site": "00b49740",
      "incomplete_value": true,
      "site": "00b49740",
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
      "definition_site": "00b49318",
      "incomplete_value": true,
      "site": "00b49318",
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
      "definition_site": "00b49748",
      "incomplete_value": false,
      "site": "00b4975c",
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
            "const:139:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49320",
      "incomplete_value": false,
      "site": "00b49334",
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
            "const:f9:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49738",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49748",
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      "00b49764",
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49738",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49748",
      "PARAM",
      [
        "storage",
        "002ae139",
        null,
        "string"
      ]
    ],
    [
      "00b49764",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b492fc.md#insn-00b49334) · [`00b4933c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b492fc.md#insn-00b4933c) · [`00b49310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b492fc.md#insn-00b49310)
- 新版 [`00b4975c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49724.md#insn-00b4975c) · [`00b49764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49724.md#insn-00b49764) · [`00b49738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49724.md#insn-00b49738)

~~~diff
- 00b49334 ["INT_ADD", "register:40f0:8", ["const:b49334:8", "const:4:8"]]
- 00b49334 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4975c ["INT_ADD", "register:40f0:8", ["const:b4975c:8", "const:4:8"]]
+ 00b4975c ["CALL", null, ["callee:00c5af10:8"]]
- 00b49334 bytes f7450494
+ 00b4975c bytes ed450494
- 00b4933c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00b4933c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49764 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00b49764 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4933c bytes 80d602f9
+ 00b49764 bytes 80d604f9
- 00b49310 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00b49310 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49738 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00b49738 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49310 bytes 81d642f9
+ 00b49738 bytes 81d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-910b55aaec42df64da4dc52858005539"></a>

### [`00b4936c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4936c.md) → [`00b49794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49794.md) _ZN8firebase4util7context11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b140.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5b540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b540.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b497b0",
      "incomplete_value": false,
      "site": "00b497b4",
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
      "definition_site": "00b49388",
      "incomplete_value": false,
      "site": "00b4938c",
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
      "definition_site": "00b497c0",
      "incomplete_value": true,
      "site": "00b497cc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b49398",
      "incomplete_value": true,
      "site": "00b493a4",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b497b0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b497c0",
      "DATA",
      [
        "storage",
        "011255b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b497b0",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b497c0",
      "DATA",
      [
        "storage",
        "011259b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4938c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4936c.md#insn-00b4938c) · [`00b49388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4936c.md#insn-00b49388) · [`00b49394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4936c.md#insn-00b49394)
- 新版 [`00b497b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49794.md#insn-00b497b4) · [`00b497b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49794.md#insn-00b497b0) · [`00b497bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49794.md#insn-00b497bc)

~~~diff
- 00b4938c ["INT_ADD", "register:40f0:8", ["const:b4938c:8", "const:4:8"]]
- 00b4938c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b497b4 ["INT_ADD", "register:40f0:8", ["const:b497b4:8", "const:4:8"]]
+ 00b497b4 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4938c bytes 1d460494
+ 00b497b4 bytes 13460494
- 00b49388 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b49388 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b49388 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b49388 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b497b0 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b497b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b497b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b497b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b49388 bytes 00680a91
+ 00b497b0 bytes 009c0d91
- 00b49394 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 00b49394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b49394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b49394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b497bc ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 00b497bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b497bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b497bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b49394 bytes 08e11691
+ 00b497bc bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87d7fd3f3c467f58e23c9f72a63b176a"></a>

### [`00b493a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b493a8.md) → [`00b497d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b497d0.md) _ZN8firebase4util7context13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49810",
      "incomplete_value": true,
      "site": "00b49810",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b493e8",
      "incomplete_value": true,
      "site": "00b493e8",
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
            "const:5a8:8"
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
      "definition_site": "00b497ec",
      "incomplete_value": true,
      "site": "00b497ec",
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
      "definition_site": "00b493c4",
      "incomplete_value": true,
      "site": "00b493c4",
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
      "definition_site": "00b497f4",
      "incomplete_value": false,
      "site": "00b49808",
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
            "const:139:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b493cc",
      "incomplete_value": false,
      "site": "00b493e0",
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
            "const:f9:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b497e4",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b497f4",
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      "00b49810",
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b497e4",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b497f4",
      "PARAM",
      [
        "storage",
        "002ae139",
        null,
        "string"
      ]
    ],
    [
      "00b49810",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b493e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b493a8.md#insn-00b493e0) · [`00b493e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b493a8.md#insn-00b493e8) · [`00b493bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b493a8.md#insn-00b493bc)
- 新版 [`00b49808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b497d0.md#insn-00b49808) · [`00b49810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b497d0.md#insn-00b49810) · [`00b497e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b497d0.md#insn-00b497e4)

~~~diff
- 00b493e0 ["INT_ADD", "register:40f0:8", ["const:b493e0:8", "const:4:8"]]
- 00b493e0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b49808 ["INT_ADD", "register:40f0:8", ["const:b49808:8", "const:4:8"]]
+ 00b49808 ["CALL", null, ["callee:00c5af10:8"]]
- 00b493e0 bytes cc450494
+ 00b49808 bytes c2450494
- 00b493e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00b493e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49810 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00b49810 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b493e8 bytes 80d602f9
+ 00b49810 bytes 80d604f9
- 00b493bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00b493bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b497e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00b497e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b493bc bytes 81d642f9
+ 00b497e4 bytes 81d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ed80d71a921a29d1adb9f2c4f99f96c"></a>

### [`00b49454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49454.md) → [`00b4987c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4987c.md) _ZN8firebase4util6cursor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b498a8",
      "incomplete_value": true,
      "site": "00b498a8",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49480",
      "incomplete_value": true,
      "site": "00b49480",
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
            "const:5d8:8"
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
      "definition_site": "00b49890",
      "incomplete_value": true,
      "site": "00b49890",
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
      "definition_site": "00b49468",
      "incomplete_value": true,
      "site": "00b49468",
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
      "definition_site": "00b4989c",
      "incomplete_value": false,
      "site": "00b498a0",
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
            "const:b17:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49474",
      "incomplete_value": false,
      "site": "00b49478",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4988c",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4989c",
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ],
    [
      "00b498a8",
      "WRITE",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4988c",
      "READ",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4989c",
      "PARAM",
      [
        "storage",
        "002a3b17",
        null,
        "string"
      ]
    ],
    [
      "00b498a8",
      "WRITE",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49454.md#insn-00b49478) · [`00b49480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49454.md#insn-00b49480) · [`00b49464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49454.md#insn-00b49464)
- 新版 [`00b498a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4987c.md#insn-00b498a0) · [`00b498a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4987c.md#insn-00b498a8) · [`00b4988c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4987c.md#insn-00b4988c)

~~~diff
- 00b49478 ["INT_ADD", "register:40f0:8", ["const:b49478:8", "const:4:8"]]
- 00b49478 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b498a0 ["INT_ADD", "register:40f0:8", ["const:b498a0:8", "const:4:8"]]
+ 00b498a0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49478 bytes a6450494
+ 00b498a0 bytes 9c450494
- 00b49480 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
- 00b49480 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b498a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
+ 00b498a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49480 bytes 60ee02f9
+ 00b498a8 bytes 60ee04f9
- 00b49464 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
- 00b49464 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4988c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
+ 00b4988c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49464 bytes 68ee42f9
+ 00b4988c bytes 68ee44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f637e57306f93a7a6e3dfd7683e13eb6"></a>

### [`00b49494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49494.md) → [`00b498bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498bc.md) _ZN8firebase4util6cursor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b498e8",
      "incomplete_value": true,
      "site": "00b498e8",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b494c0",
      "incomplete_value": true,
      "site": "00b494c0",
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
            "const:5d8:8"
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
      "definition_site": "00b498d0",
      "incomplete_value": true,
      "site": "00b498d0",
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
      "definition_site": "00b494a8",
      "incomplete_value": true,
      "site": "00b494a8",
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
      "definition_site": "00b498d8",
      "incomplete_value": false,
      "site": "00b498e0",
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
            "const:b17:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b494b0",
      "incomplete_value": false,
      "site": "00b494b8",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b498cc",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b498d8",
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ],
    [
      "00b498e8",
      "WRITE",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b498cc",
      "READ",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b498d8",
      "PARAM",
      [
        "storage",
        "002a3b17",
        null,
        "string"
      ]
    ],
    [
      "00b498e8",
      "WRITE",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b494b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49494.md#insn-00b494b8) · [`00b494c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49494.md#insn-00b494c0) · [`00b494a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49494.md#insn-00b494a4)
- 新版 [`00b498e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498bc.md#insn-00b498e0) · [`00b498e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498bc.md#insn-00b498e8) · [`00b498cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498bc.md#insn-00b498cc)

~~~diff
- 00b494b8 ["INT_ADD", "register:40f0:8", ["const:b494b8:8", "const:4:8"]]
- 00b494b8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b498e0 ["INT_ADD", "register:40f0:8", ["const:b498e0:8", "const:4:8"]]
+ 00b498e0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b494b8 bytes 96450494
+ 00b498e0 bytes 8c450494
- 00b494c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
- 00b494c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b498e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
+ 00b498e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b494c0 bytes 60ee02f9
+ 00b498e8 bytes 60ee04f9
- 00b494a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
- 00b494a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b498cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
+ 00b498cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b494a4 bytes 68ee42f9
+ 00b498cc bytes 68ee44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-261d9d4435fb1b32a1505b504f448ddb"></a>

### [`00b494d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b494d4.md) → [`00b498fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498fc.md) _ZN8firebase4util6cursor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4992c",
      "incomplete_value": true,
      "site": "00b4992c",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49504",
      "incomplete_value": true,
      "site": "00b49504",
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
            "const:5d8:8"
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
      "definition_site": "00b49910",
      "incomplete_value": true,
      "site": "00b49910",
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
      "definition_site": "00b494e8",
      "incomplete_value": true,
      "site": "00b494e8",
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
      "definition_site": "00b4991c",
      "incomplete_value": false,
      "site": "00b49924",
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
            "const:b17:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b494f4",
      "incomplete_value": false,
      "site": "00b494fc",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4990c",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4991c",
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ],
    [
      "00b4992c",
      "WRITE",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4990c",
      "READ",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4991c",
      "PARAM",
      [
        "storage",
        "002a3b17",
        null,
        "string"
      ]
    ],
    [
      "00b4992c",
      "WRITE",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b494fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b494d4.md#insn-00b494fc) · [`00b49504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b494d4.md#insn-00b49504) · [`00b494e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b494d4.md#insn-00b494e4)
- 新版 [`00b49924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498fc.md#insn-00b49924) · [`00b4992c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498fc.md#insn-00b4992c) · [`00b4990c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498fc.md#insn-00b4990c)

~~~diff
- 00b494fc ["INT_ADD", "register:40f0:8", ["const:b494fc:8", "const:4:8"]]
- 00b494fc ["CALL", null, ["callee:00c5af10:8"]]
+ 00b49924 ["INT_ADD", "register:40f0:8", ["const:b49924:8", "const:4:8"]]
+ 00b49924 ["CALL", null, ["callee:00c5af10:8"]]
- 00b494fc bytes 85450494
+ 00b49924 bytes 7b450494
- 00b49504 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
- 00b49504 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4992c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
+ 00b4992c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49504 bytes 60ee02f9
+ 00b4992c bytes 60ee04f9
- 00b494e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
- 00b494e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4990c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
+ 00b4990c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b494e4 bytes 68ee42f9
+ 00b4990c bytes 68ee44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-520be982fb36565b72fec54e5210962b"></a>

### [`00b49518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49518.md) → [`00b49940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49940.md) _ZN8firebase4util6cursor10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49970",
      "incomplete_value": true,
      "site": "00b49970",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49548",
      "incomplete_value": true,
      "site": "00b49548",
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
            "const:5d8:8"
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
      "definition_site": "00b49954",
      "incomplete_value": true,
      "site": "00b49954",
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
      "definition_site": "00b4952c",
      "incomplete_value": true,
      "site": "00b4952c",
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
      "definition_site": "00b4995c",
      "incomplete_value": false,
      "site": "00b49968",
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
            "const:b17:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49534",
      "incomplete_value": false,
      "site": "00b49540",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49950",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4995c",
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ],
    [
      "00b49970",
      "WRITE",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49950",
      "READ",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4995c",
      "PARAM",
      [
        "storage",
        "002a3b17",
        null,
        "string"
      ]
    ],
    [
      "00b49970",
      "WRITE",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49518.md#insn-00b49540) · [`00b49548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49518.md#insn-00b49548) · [`00b49528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49518.md#insn-00b49528)
- 新版 [`00b49968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49940.md#insn-00b49968) · [`00b49970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49940.md#insn-00b49970) · [`00b49950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49940.md#insn-00b49950)

~~~diff
- 00b49540 ["INT_ADD", "register:40f0:8", ["const:b49540:8", "const:4:8"]]
- 00b49540 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b49968 ["INT_ADD", "register:40f0:8", ["const:b49968:8", "const:4:8"]]
+ 00b49968 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49540 bytes 74450494
+ 00b49968 bytes 6a450494
- 00b49548 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
- 00b49548 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49970 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
+ 00b49970 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49548 bytes 60ee02f9
+ 00b49970 bytes 60ee04f9
- 00b49528 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
- 00b49528 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
+ 00b49950 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49528 bytes 68ee42f9
+ 00b49950 bytes 68ee44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48a5bf66dd879c4b381457833e4b825a"></a>

### [`00b49568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49568.md) → [`00b49990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49990.md) _ZN8firebase4util6cursor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.36% / 新版 74.36%

CFGの説明率　旧版 42.86% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49568"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4956c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4956c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b49568",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4956c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49570",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49990",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b49994",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b49998",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49568.md#insn-00b49568) · [`00b4956c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49568.md#insn-00b4956c) · [`00b49570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49568.md#insn-00b49570)

~~~diff
- 00b49568 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b49568 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b49568 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b49568 bytes f50f1df8
- 00b4956c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4956c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4956c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4956c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4956c bytes f44f01a9
- 00b49570 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b49570 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b49570 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b49570 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49570 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9230f0c4d8548b1a591af51f9a9ee856"></a>

### [`00b49604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49604.md) → [`00b49a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49a2c.md) _ZN8firebase4util6cursor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49a68",
      "incomplete_value": true,
      "site": "00b49a68",
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
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49640",
      "incomplete_value": true,
      "site": "00b49640",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49690"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49ab8"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49a40",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49a4c",
      "READ",
      [
        "storage",
        "011255e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49a68",
      "WRITE",
      [
        "storage",
        "011255e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49a40",
      "READ",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49a4c",
      "READ",
      [
        "storage",
        "011259e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49a68",
      "WRITE",
      [
        "storage",
        "011259e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49604.md#insn-00b49640) · [`00b49668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49604.md#insn-00b49668) · [`00b4968c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49604.md#insn-00b4968c)
- 新版 [`00b49a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49a2c.md#insn-00b49a68)

~~~diff
- 00b49640 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b49640 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b49640 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5e0:8"]]
- 00b49640 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b49a68 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b49a68 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b49a68 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9e0:8"]]
+ 00b49a68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b49640 bytes bf821739
+ 00b49a68 bytes bf822739
- 00b49668 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49668 ["INT_ADD", "register:40f0:8", ["const:b49668:8", "const:4:8"]]
- 00b49668 ["CALLIND", null, ["register:0:8"]]
- 00b49668 bytes 00013fd6
- 00b4968c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4968c ["INT_ADD", "register:40f0:8", ["const:b4968c:8", "const:4:8"]]
- 00b4968c ["CALLIND", null, ["register:0:8"]]
- 00b4968c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6eef02ad257fa510c54d7596c8c9b72f"></a>

### [`00b496a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b496a4.md) → [`00b49acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49acc.md) _ZN8firebase4util6cursor14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b496e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49b0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b496c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b496b8",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b496c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49b10"
      ]
    ],
    [
      "unmatched:00b496c8",
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b49ae0",
      "READ",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49ae8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49b10"
      ]
    ],
    [
      "00b49af0",
      "PARAM",
      [
        "storage",
        "002a3b17",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b496c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b496a4.md#insn-00b496c0) · [`00b496dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b496a4.md#insn-00b496dc) · [`00b496e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b496a4.md#insn-00b496e4)
- 新版 [`00b49b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49acc.md#insn-00b49b04)

~~~diff
- 00b496c0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b496c0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b496c0 bytes 410100b5
- 00b496dc ["INT_ADD", "register:40f0:8", ["const:b496dc:8", "const:4:8"]]
- 00b496dc ["CALL", null, ["callee:00c5af10:8"]]
+ 00b49b04 ["INT_ADD", "register:40f0:8", ["const:b49b04:8", "const:4:8"]]
+ 00b49b04 ["CALL", null, ["callee:00c5af10:8"]]
- 00b496dc bytes 0d450494
+ 00b49b04 bytes 03450494
- 00b496e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5d8:8"]]
- 00b496e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b496e4 bytes 80ee02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-902d1a5554caa9e11573d0c0cf585c75"></a>

### [`00b49714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49714.md) → [`00b49b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49b3c.md) _ZN8firebase4util6cursor11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49b58",
      "incomplete_value": false,
      "site": "00b49b5c",
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
      "definition_site": "00b49730",
      "incomplete_value": false,
      "site": "00b49734",
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
      "definition_site": "00b49b68",
      "incomplete_value": true,
      "site": "00b49b74",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b49740",
      "incomplete_value": true,
      "site": "00b4974c",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49b58",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b49b68",
      "DATA",
      [
        "storage",
        "011255e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49b58",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b49b68",
      "DATA",
      [
        "storage",
        "011259e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49714.md#insn-00b49734) · [`00b49730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49714.md#insn-00b49730) · [`00b4973c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49714.md#insn-00b4973c)
- 新版 [`00b49b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49b3c.md#insn-00b49b5c) · [`00b49b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49b3c.md#insn-00b49b58) · [`00b49b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49b3c.md#insn-00b49b64)

~~~diff
- 00b49734 ["INT_ADD", "register:40f0:8", ["const:b49734:8", "const:4:8"]]
- 00b49734 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b49b5c ["INT_ADD", "register:40f0:8", ["const:b49b5c:8", "const:4:8"]]
+ 00b49b5c ["CALL", null, ["callee:00c5b000:8"]]
- 00b49734 bytes 33450494
+ 00b49b5c bytes 29450494
- 00b49730 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b49730 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b49730 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b49730 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49b58 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b49b58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49b58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49b58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b49730 bytes 00680a91
+ 00b49b58 bytes 009c0d91
- 00b4973c ["COPY", "tmp:0:8", ["const:5e8:8"]]
- 00b4973c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4973c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4973c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b49b64 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 00b49b64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49b64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49b64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4973c bytes 08a11791
+ 00b49b64 bytes 08a12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f3aada93321dfcc7dbf9fc02378e325"></a>

### [`00b49750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49750.md) → [`00b49b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49b78.md) _ZN8firebase4util6cursor13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49790"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49bb8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4976c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b49764",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4976c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49bbc"
      ]
    ],
    [
      "unmatched:00b49774",
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b49b8c",
      "READ",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49b94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49bbc"
      ]
    ],
    [
      "00b49b9c",
      "PARAM",
      [
        "storage",
        "002a3b17",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4976c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49750.md#insn-00b4976c) · [`00b49788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49750.md#insn-00b49788) · [`00b49790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49750.md#insn-00b49790)
- 新版 [`00b49bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49b78.md#insn-00b49bb0)

~~~diff
- 00b4976c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4976c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4976c bytes 410100b5
- 00b49788 ["INT_ADD", "register:40f0:8", ["const:b49788:8", "const:4:8"]]
- 00b49788 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b49bb0 ["INT_ADD", "register:40f0:8", ["const:b49bb0:8", "const:4:8"]]
+ 00b49bb0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49788 bytes e2440494
+ 00b49bb0 bytes d8440494
- 00b49790 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5d8:8"]]
- 00b49790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49790 bytes 80ee02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ab3707871217e71aac08ebfc5c2bf56"></a>

### [`00b497c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b497c0.md) → [`00b49be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49be8.md) _ZN8firebase4util6cursor10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49c04",
      "incomplete_value": false,
      "site": "00b49c08",
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
      "definition_site": "00b497dc",
      "incomplete_value": false,
      "site": "00b497e0",
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
      "definition_site": "00b49c14",
      "incomplete_value": true,
      "site": "00b49c20",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b497ec",
      "incomplete_value": true,
      "site": "00b497f8",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49c04",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b49c14",
      "DATA",
      [
        "storage",
        "01125608",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49c04",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b49c14",
      "DATA",
      [
        "storage",
        "01125a08",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b497e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b497c0.md#insn-00b497e0) · [`00b497dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b497c0.md#insn-00b497dc) · [`00b497e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b497c0.md#insn-00b497e8)
- 新版 [`00b49c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49be8.md#insn-00b49c08) · [`00b49c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49be8.md#insn-00b49c04) · [`00b49c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49be8.md#insn-00b49c10)

~~~diff
- 00b497e0 ["INT_ADD", "register:40f0:8", ["const:b497e0:8", "const:4:8"]]
- 00b497e0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b49c08 ["INT_ADD", "register:40f0:8", ["const:b49c08:8", "const:4:8"]]
+ 00b49c08 ["CALL", null, ["callee:00c5b000:8"]]
- 00b497e0 bytes 08450494
+ 00b49c08 bytes fe440494
- 00b497dc ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b497dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b497dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b497dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49c04 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b49c04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49c04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49c04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b497dc bytes 00441191
+ 00b49c04 bytes 00781491
- 00b497e8 ["COPY", "tmp:0:8", ["const:608:8"]]
- 00b497e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b497e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b497e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b49c10 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 00b49c10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49c10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49c10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b497e8 bytes 08211891
+ 00b49c10 bytes 08212891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c6d842c62f74f53468e007e02e3bc83"></a>

### [`00b4983c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4983c.md) → [`00b49c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49c64.md) _ZN8firebase4util4date19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49c90",
      "incomplete_value": true,
      "site": "00b49c90",
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
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49868",
      "incomplete_value": true,
      "site": "00b49868",
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
            "const:610:8"
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
      "definition_site": "00b49c78",
      "incomplete_value": true,
      "site": "00b49c78",
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
      "definition_site": "00b49850",
      "incomplete_value": true,
      "site": "00b49850",
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
      "definition_site": "00b49c80",
      "incomplete_value": false,
      "site": "00b49c88",
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
            "const:41e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49858",
      "incomplete_value": false,
      "site": "00b49860",
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
            "const:351:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49c74",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49c80",
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ],
    [
      "00b49c90",
      "WRITE",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49c74",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49c80",
      "PARAM",
      [
        "storage",
        "002a841e",
        null,
        "string"
      ]
    ],
    [
      "00b49c90",
      "WRITE",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4983c.md#insn-00b49860) · [`00b49868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4983c.md#insn-00b49868) · [`00b4984c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4983c.md#insn-00b4984c)
- 新版 [`00b49c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49c64.md#insn-00b49c88) · [`00b49c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49c64.md#insn-00b49c90) · [`00b49c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49c64.md#insn-00b49c74)

~~~diff
- 00b49860 ["INT_ADD", "register:40f0:8", ["const:b49860:8", "const:4:8"]]
- 00b49860 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b49c88 ["INT_ADD", "register:40f0:8", ["const:b49c88:8", "const:4:8"]]
+ 00b49c88 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49860 bytes ac440494
+ 00b49c88 bytes a2440494
- 00b49868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:610:8"]]
- 00b49868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49c90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
+ 00b49c90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49868 bytes 600a03f9
+ 00b49c90 bytes 600a05f9
- 00b4984c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:610:8"]]
- 00b4984c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49c74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
+ 00b49c74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4984c bytes 680a43f9
+ 00b49c74 bytes 680a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa1f8f111ddc973469910cb49b438de2"></a>

### [`00b498c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b498c0.md) → [`00b49ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ce8.md) _ZN8firebase4util4date10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49d18",
      "incomplete_value": true,
      "site": "00b49d18",
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
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b498f0",
      "incomplete_value": true,
      "site": "00b498f0",
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
            "const:610:8"
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
      "definition_site": "00b49cfc",
      "incomplete_value": true,
      "site": "00b49cfc",
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
      "definition_site": "00b498d4",
      "incomplete_value": true,
      "site": "00b498d4",
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
      "definition_site": "00b49d04",
      "incomplete_value": false,
      "site": "00b49d10",
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
            "const:41e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b498dc",
      "incomplete_value": false,
      "site": "00b498e8",
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
            "const:351:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49cf8",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49d04",
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ],
    [
      "00b49d18",
      "WRITE",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49cf8",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49d04",
      "PARAM",
      [
        "storage",
        "002a841e",
        null,
        "string"
      ]
    ],
    [
      "00b49d18",
      "WRITE",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b498e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b498c0.md#insn-00b498e8) · [`00b498f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b498c0.md#insn-00b498f0) · [`00b498d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b498c0.md#insn-00b498d0)
- 新版 [`00b49d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ce8.md#insn-00b49d10) · [`00b49d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ce8.md#insn-00b49d18) · [`00b49cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ce8.md#insn-00b49cf8)

~~~diff
- 00b498e8 ["INT_ADD", "register:40f0:8", ["const:b498e8:8", "const:4:8"]]
- 00b498e8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b49d10 ["INT_ADD", "register:40f0:8", ["const:b49d10:8", "const:4:8"]]
+ 00b49d10 ["CALL", null, ["callee:00c5af10:8"]]
- 00b498e8 bytes 8a440494
+ 00b49d10 bytes 80440494
- 00b498f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:610:8"]]
- 00b498f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49d18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
+ 00b49d18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b498f0 bytes 600a03f9
+ 00b49d18 bytes 600a05f9
- 00b498d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:610:8"]]
- 00b498d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49cf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
+ 00b49cf8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b498d0 bytes 680a43f9
+ 00b49cf8 bytes 680a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f77892f8672388bb5ffa52c5dabedc47"></a>

### [`00b49910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49910.md) → [`00b49d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49d38.md) _ZN8firebase4util4date15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49dc0",
      "incomplete_value": true,
      "site": "00b49dc0",
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
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49998",
      "incomplete_value": true,
      "site": "00b49998",
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
            "const:618:8"
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
      "definition_site": "00b49d6c",
      "incomplete_value": true,
      "site": "00b49d78",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:a10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49944",
      "incomplete_value": true,
      "site": "00b49950",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
      "00b49d4c",
      "READ",
      [
        "storage",
        "01125618",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49d6c",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49dc0",
      "WRITE",
      [
        "storage",
        "01125618",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49d4c",
      "READ",
      [
        "storage",
        "01125a18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49d6c",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49dc0",
      "WRITE",
      [
        "storage",
        "01125a18",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49910.md#insn-00b49950) · [`00b49998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49910.md#insn-00b49998) · [`00b49924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49910.md#insn-00b49924)
- 新版 [`00b49d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49d38.md#insn-00b49d78) · [`00b49dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49d38.md#insn-00b49dc0) · [`00b49d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49d38.md#insn-00b49d4c)

~~~diff
- 00b49950 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49950 ["INT_ADD", "register:40f0:8", ["const:b49950:8", "const:4:8"]]
- 00b49950 ["CALLIND", null, ["register:0:8"]]
+ 00b49d78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49d78 ["INT_ADD", "register:40f0:8", ["const:b49d78:8", "const:4:8"]]
+ 00b49d78 ["CALLIND", null, ["register:0:8"]]
- 00b49950 bytes 00013fd6
+ 00b49d78 bytes 00013fd6
- 00b49998 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b49998 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:618:8"]]
- 00b49998 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b49dc0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b49dc0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a18:8"]]
+ 00b49dc0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b49998 bytes a0621839
+ 00b49dc0 bytes a0622839
- 00b49924 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:618:8"]]
- 00b49924 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b49924 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b49d4c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a18:8"]]
+ 00b49d4c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b49d4c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b49924 bytes a8625839
+ 00b49d4c bytes a8626839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a554ef80a346ead2076d8eb088aa321"></a>

### [`00b499ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b499ac.md) → [`00b49dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49dd4.md) _ZN8firebase4util4date12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.50% / 新版 57.50%

CFGの説明率　旧版 25.00% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b499ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b499b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b499b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b499ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b499b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b499b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49dd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b49dd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b49ddc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b499ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b499ac.md#insn-00b499ac) · [`00b499b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b499ac.md#insn-00b499b0) · [`00b499b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b499ac.md#insn-00b499b4)

~~~diff
- 00b499ac ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b499ac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b499ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b499ac bytes f50f1df8
- 00b499b0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b499b0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b499b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b499b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b499b0 bytes f44f01a9
- 00b499b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b499b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b499b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b499b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b499b4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb0bf3790ad3b722027a369f5cf9ccd4"></a>

### [`00b49a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49a4c.md) → [`00b49e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49e74.md) _ZN8firebase4util4date14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49a8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49eb4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49a68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b49a60",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b49a68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49eb8"
      ]
    ],
    [
      "unmatched:00b49a70",
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b49e88",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49e90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49eb8"
      ]
    ],
    [
      "00b49e98",
      "PARAM",
      [
        "storage",
        "002a841e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49a4c.md#insn-00b49a68) · [`00b49a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49a4c.md#insn-00b49a84) · [`00b49a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49a4c.md#insn-00b49a8c)
- 新版 [`00b49eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49e74.md#insn-00b49eac)

~~~diff
- 00b49a68 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b49a68 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b49a68 bytes 410100b5
- 00b49a84 ["INT_ADD", "register:40f0:8", ["const:b49a84:8", "const:4:8"]]
- 00b49a84 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b49eac ["INT_ADD", "register:40f0:8", ["const:b49eac:8", "const:4:8"]]
+ 00b49eac ["CALL", null, ["callee:00c5af10:8"]]
- 00b49a84 bytes 23440494
+ 00b49eac bytes 19440494
- 00b49a8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:610:8"]]
- 00b49a8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49a8c bytes 800a03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

