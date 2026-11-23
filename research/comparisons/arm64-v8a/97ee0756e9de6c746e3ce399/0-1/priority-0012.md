# v15.7.2 → v15.7.3 · 最優先の変更候補 (12)

[一覧の目次](README.md)

<a id="compare-544fa662de0dcaa46ffbf1345e3508de"></a>

### [`004f8c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f8/004f8c10.md) → [`004f8c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8c10.md) _ZNK5Botan14Cert_Extension20Certificate_Policies12encode_innerEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00483ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483ed8.md) [`00512c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512c94.md) [`00512ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512ca8.md) [`00529d48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00529/00529d48.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00529d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00529/00529d48.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.17% / 新版 97.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8c7c",
      "incomplete_value": true,
      "site": "004f8c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f8c7c",
      "incomplete_value": true,
      "site": "004f8c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8ca0",
      "incomplete_value": true,
      "site": "004f8ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f8ca0",
      "incomplete_value": true,
      "site": "004f8ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f8dd4",
      "incomplete_value": true,
      "site": "004f8dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f8dd4",
      "incomplete_value": true,
      "site": "004f8dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f8c60",
      "READ",
      [
        "storage",
        "00c1ae50",
        null,
        "pointer"
      ]
    ],
    [
      "004f8c84",
      "DATA",
      [
        "storage",
        "00be91c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f8c90",
      "READ",
      [
        "storage",
        "00c1ae50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f8c60",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "004f8c84",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f8c90",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f8c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f8/004f8c10.md#insn-004f8c60) · [`004f8c78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f8/004f8c10.md#insn-004f8c78) · [`004f8c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f8/004f8c10.md#insn-004f8c90)
- 新版 [`004f8c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8c10.md#insn-004f8c60) · [`004f8c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8c10.md#insn-004f8c78) · [`004f8c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8c10.md#insn-004f8c90)

~~~diff
- 004f8c60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e50:8"]]
- 004f8c60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f8c60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f00:8"]]
+ 004f8c60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f8c60 bytes 292947f9
+ 004f8c60 bytes 298147f9
- 004f8c78 ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 004f8c78 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 004f8c78 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 004f8c78 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 004f8c78 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 004f8c78 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 004f8c78 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 004f8c78 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 004f8c78 bytes 73220f91
+ 004f8c78 bytes 73e21191
- 004f8c90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e50:8"]]
- 004f8c90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f8c90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 004f8c90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f8c90 bytes 082947f9
+ 004f8c90 bytes 088147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e605a93b691cd27eef7c65289e5be6d8"></a>

### [`004f9190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f9/004f9190.md) → [`004f9190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9190.md) _ZN5Botan14Cert_Extension20Certificate_Policies12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`0041e0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e0fc.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00512c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512c94.md) [`0051ab34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051a/0051ab34.md) [`00528a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00528/00528a6c.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`0051ab34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051a/0051ab34.md) [`00528a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00528/00528a6c.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f9218",
      "incomplete_value": true,
      "site": "004f9218",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f9218",
      "incomplete_value": true,
      "site": "004f9218",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f94ac",
      "incomplete_value": true,
      "site": "004f94ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
        ]
      ]
    },
    "old": {
      "definition_site": "004f94ac",
      "incomplete_value": true,
      "site": "004f94ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:4098:8"
              ],
              [
                "leaf",
                "const:678:8"
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
      "definition_site": "004f94f0",
      "incomplete_value": true,
      "site": "004f94f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
        ]
      ]
    },
    "old": {
      "definition_site": "004f94f0",
      "incomplete_value": true,
      "site": "004f94f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:4098:8"
              ],
              [
                "leaf",
                "const:678:8"
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
      "004f91f8",
      "READ",
      [
        "storage",
        "00c1ae50",
        null,
        "pointer"
      ]
    ],
    [
      "004f9218",
      "DATA",
      [
        "storage",
        "00be91c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f9244",
      "DATA",
      [
        "storage",
        "00bed3c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f91f8",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "004f9218",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f9244",
      "DATA",
      [
        "storage",
        "00bed478",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f91f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f9/004f9190.md#insn-004f91f8) · [`004f9208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f9/004f9190.md#insn-004f9208) · [`004f949c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f9/004f9190.md#insn-004f949c)
- 新版 [`004f91f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9190.md#insn-004f91f8) · [`004f9208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9190.md#insn-004f9208) · [`004f949c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9190.md#insn-004f949c)

~~~diff
- 004f91f8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:e50:8"]]
- 004f91f8 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f91f8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:f00:8"]]
+ 004f91f8 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 004f91f8 bytes 182b47f9
+ 004f91f8 bytes 188347f9
- 004f9208 ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 004f9208 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
- 004f9208 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
- 004f9208 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
+ 004f9208 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 004f9208 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
+ 004f9208 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
+ 004f9208 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
- 004f9208 bytes 9c230f91
+ 004f9208 bytes 9ce31191
- 004f949c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:678:8"]]
- 004f949c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f949c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 004f949c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f949c bytes 693e43f9
+ 004f949c bytes 699643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db45c0ea4e30da609a7f8f851afb3e71"></a>

### [`004f97e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f9/004f97e4.md) → [`004f97e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f97e4.md) _ZNK5Botan14Cert_Extension20Certificate_Policies11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`004dc2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dc2c8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb960.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f9824",
      "incomplete_value": true,
      "site": "004f9838",
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
    "old": {
      "definition_site": "004f9824",
      "incomplete_value": true,
      "site": "004f9838",
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
                "const:30a:8"
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
      "definition_site": "004f983c",
      "incomplete_value": true,
      "site": "004f9840",
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
      "definition_site": "004f983c",
      "incomplete_value": true,
      "site": "004f9840",
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
      "004f9824",
      "READ",
      [
        "storage",
        "0029e30a",
        null,
        "string"
      ]
    ],
    [
      "004f983c",
      "READ",
      [
        "storage",
        "0029e314",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f9824",
      "READ",
      [
        "storage",
        "0029e397",
        null,
        "string"
      ]
    ],
    [
      "004f983c",
      "READ",
      [
        "storage",
        "0029e3a1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f981c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f9/004f97e4.md#insn-004f981c)
- 新版 [`004f981c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f97e4.md#insn-004f981c)

~~~diff
- 004f981c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 004f981c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f981c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f981c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f981c ["COPY", "tmp:0:8", ["const:397:8"]]
+ 004f981c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f981c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f981c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f981c bytes 29290c91
+ 004f981c bytes 295d0e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-324f67b0212cdc763648c3fa13a589c8"></a>

### [`004f9bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f9/004f9bd8.md) → [`004f9bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9bd8.md) _ZNK5Botan14Cert_Extension28Authority_Information_Access12encode_innerEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00483ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512ca8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

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
      "definition_site": "004f9c58",
      "incomplete_value": true,
      "site": "004f9c58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:463:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f9c58",
      "incomplete_value": true,
      "site": "004f9c58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:46a:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "004f9d4c",
      "incomplete_value": true,
      "site": "004f9d4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004f9d4c",
      "incomplete_value": true,
      "site": "004f9d4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:678:8"
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
      "004f9c48",
      "READ",
      [
        "storage",
        "002a546a",
        null,
        "string"
      ]
    ],
    [
      "004f9d3c",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f9c48",
      "READ",
      [
        "storage",
        "002a5463",
        null,
        "string"
      ]
    ],
    [
      "004f9d3c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f9c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f9/004f9bd8.md#insn-004f9c40) · [`004f9d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f9/004f9bd8.md#insn-004f9d3c)
- 新版 [`004f9c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9bd8.md#insn-004f9c40) · [`004f9d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9bd8.md#insn-004f9d3c)

~~~diff
- 004f9c40 ["COPY", "tmp:0:8", ["const:46a:8"]]
- 004f9c40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f9c40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f9c40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f9c40 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 004f9c40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f9c40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f9c40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f9c40 bytes 29a91191
+ 004f9c40 bytes 298d1191
- 004f9d3c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004f9d3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f9d3c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004f9d3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f9d3c bytes 293d43f9
+ 004f9d3c bytes 299543f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53e966cdc533d8e12554f28776b38341"></a>

### [`004f9e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f9/004f9e04.md) → [`004f9e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9e04.md) _ZN5Botan14Cert_Extension28Authority_Information_Access12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.33% / 新版 96.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f9e90",
      "incomplete_value": true,
      "site": "004f9e90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004f9e90",
      "incomplete_value": true,
      "site": "004f9e90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:678:8"
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
      "definition_site": "004fa130",
      "incomplete_value": true,
      "site": "004fa130",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004fa130",
      "incomplete_value": true,
      "site": "004fa130",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:678:8"
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
      "definition_site": "004fa3f4",
      "incomplete_value": true,
      "site": "004fa3f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004fa3f4",
      "incomplete_value": true,
      "site": "004fa3f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f9e80",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004f9f40",
      "READ",
      [
        "storage",
        "002a546a",
        null,
        "string"
      ]
    ],
    [
      "004fa120",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f9e80",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004f9f40",
      "READ",
      [
        "storage",
        "002a5463",
        null,
        "string"
      ]
    ],
    [
      "004fa120",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f9e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f9/004f9e04.md#insn-004f9e80) · [`004f9ec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f9/004f9e04.md#insn-004f9ec4) · [`004f9ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f9/004f9e04.md#insn-004f9ec8)
- 新版 [`004f9e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9e04.md#insn-004f9e80) · [`004f9ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f9/004f9e04.md#insn-004f9ec4)

~~~diff
- 004f9e80 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:678:8"]]
- 004f9e80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f9e80 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
+ 004f9e80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f9e80 bytes 093f43f9
+ 004f9e80 bytes 099743f9
- 004f9ec4 ["COPY", "tmp:0:8", ["const:46a:8"]]
- 004f9ec4 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
- 004f9ec4 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
- 004f9ec4 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
+ 004f9ec4 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 004f9ec4 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
+ 004f9ec4 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
+ 004f9ec4 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
- 004f9ec4 bytes 9cab1191
+ 004f9ec4 bytes 9c8f1191
- 004f9ec8 ["COPY", "register:40d8:8", ["const:2a1000:8"]]
- 004f9ec8 bytes 5bedff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc91144579cf24d89c06103fbdd9a0b9"></a>

### [`004fa630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fa630.md) → [`004fa630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa630.md) _ZNK5Botan14Cert_Extension28Authority_Information_Access11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dc2c8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.24% / 新版 93.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa6cc",
      "incomplete_value": true,
      "site": "004fa6d4",
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
                "const:3c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa6cc",
      "incomplete_value": true,
      "site": "004fa6d4",
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
                "const:338:8"
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
      "definition_site": "004fa6cc",
      "incomplete_value": true,
      "site": "004fa6d8",
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
      "definition_site": "004fa6cc",
      "incomplete_value": true,
      "site": "004fa6d8",
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
      "004fa6cc",
      "READ",
      [
        "storage",
        "002a1338",
        null,
        "string"
      ]
    ],
    [
      "004fa6cc",
      "READ",
      [
        "storage",
        "002a1348",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fa6cc",
      "READ",
      [
        "storage",
        "002a13c5",
        null,
        "string"
      ]
    ],
    [
      "004fa6cc",
      "READ",
      [
        "storage",
        "002a13d5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fa6c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fa630.md#insn-004fa6c4) · [`004fa6c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fa630.md#insn-004fa6c8)
- 新版 [`004fa6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa630.md#insn-004fa6c4) · [`004fa6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa630.md#insn-004fa6c8)

~~~diff
- 004fa6c4 ["COPY", "tmp:0:8", ["const:338:8"]]
- 004fa6c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004fa6c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004fa6c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004fa6c4 ["COPY", "tmp:0:8", ["const:3c5:8"]]
+ 004fa6c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004fa6c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004fa6c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004fa6c4 bytes 29e10c91
+ 004fa6c4 bytes 29150f91
- 004fa6c8 ["COPY", "register:4040:8", ["const:2b1000:8"]]
- 004fa6c8 bytes a8edfff0
+ 004fa6c8 ["COPY", "register:4040:8", ["const:2b1000:8"]]
+ 004fa6c8 bytes a8edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4badde53a205b90bd9b08fbd72f70acc"></a>

### [`004fa788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fa788.md) → [`004fa788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa788.md) _ZNK5Botan14Cert_Extension10CRL_Number14get_crl_numberEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdce60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce60.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md)
- 新版 呼出元 1件 [`00bdcf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf10.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)

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
      "definition_site": "004fa7ec",
      "incomplete_value": false,
      "site": "004fa7f4",
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
            "const:5ae:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa7ec",
      "incomplete_value": false,
      "site": "004fa7f4",
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
            "const:521:8"
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
      "definition_site": "004fa828",
      "incomplete_value": true,
      "site": "004fa834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004fa828",
      "incomplete_value": true,
      "site": "004fa834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "004fa7ec",
      "PARAM",
      [
        "storage",
        "0029f521",
        null,
        "string"
      ]
    ],
    [
      "004fa828",
      "READ",
      [
        "storage",
        "00c1ae58",
        null,
        "pointer"
      ]
    ],
    [
      "004fa828",
      "PARAM",
      [
        "storage",
        "00be92d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004fa7ec",
      "PARAM",
      [
        "storage",
        "0029f5ae",
        null,
        "string"
      ]
    ],
    [
      "004fa828",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004fa828",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fa7ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fa788.md#insn-004fa7ec) · [`004fa828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fa788.md#insn-004fa828)
- 新版 [`004fa7ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa788.md#insn-004fa7ec) · [`004fa828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa788.md#insn-004fa828)

~~~diff
- 004fa7ec ["COPY", "tmp:0:8", ["const:521:8"]]
- 004fa7ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004fa7ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004fa7ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004fa7ec ["COPY", "tmp:0:8", ["const:5ae:8"]]
+ 004fa7ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004fa7ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004fa7ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004fa7ec bytes 21841491
+ 004fa7ec bytes 21b81691
- 004fa828 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e58:8"]]
- 004fa828 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa828 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
+ 004fa828 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004fa828 bytes 212c47f9
+ 004fa828 bytes 218447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ae76e90892ab6978fcbd76e3ee9998a"></a>

### [`004fa888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fa888.md) → [`004fa888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa888.md) _ZNK5Botan14Cert_Extension10CRL_Number4copyEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
            "const:604:8"
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
            "const:698:8"
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
                "const:f08:8"
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
                "const:e58:8"
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
        "00c1b2b0",
        null,
        "pointer"
      ]
    ],
    [
      "004fa8d8",
      "DATA",
      [
        "storage",
        "00bebc00",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "004fa914",
      "PARAM",
      [
        "storage",
        "002a7698",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fa8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fa888.md#insn-004fa8c4) · [`004fa914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fa888.md#insn-004fa914) · [`004fa950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fa888.md#insn-004fa950)
- 新版 [`004fa8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa888.md#insn-004fa8c4) · [`004fa914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa888.md#insn-004fa914) · [`004fa950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa888.md#insn-004fa950)

~~~diff
- 004fa8c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
- 004fa8c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa8c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:360:8"]]
+ 004fa8c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fa8c4 bytes 085941f9
+ 004fa8c4 bytes 08b141f9
- 004fa914 ["COPY", "tmp:0:8", ["const:698:8"]]
- 004fa914 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004fa914 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004fa914 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004fa914 ["COPY", "tmp:0:8", ["const:604:8"]]
+ 004fa914 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004fa914 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004fa914 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004fa914 bytes 21601a91
+ 004fa914 bytes 21101891
- 004fa950 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e58:8"]]
- 004fa950 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa950 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
+ 004fa950 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004fa950 bytes 212c47f9
+ 004fa950 bytes 218447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8f68e18e23d5f52efb3067ecb1def39"></a>

### [`004fa9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fa9b0.md) → [`004fa9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa9b0.md) _ZNK5Botan14Cert_Extension10CRL_Number12encode_innerEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00483ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512ca8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004faa90",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004faa18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fa9b0.md#insn-004faa18) · [`004faa90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fa9b0.md#insn-004faa90)
- 新版 [`004faa18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa9b0.md#insn-004faa18) · [`004faa90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa9b0.md#insn-004faa90)

~~~diff
- 004faa18 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004faa18 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004faa18 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004faa18 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004faa18 bytes c93e43f9
+ 004faa18 bytes c99643f9
- 004faa90 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004faa90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004faa90 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004faa90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004faa90 bytes c93e43f9
+ 004faa90 bytes c99643f9
~~~


<a id="compare-d889a8f4cbbc4af265824c357511ac59"></a>

### [`004fabf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fabf4.md) → [`004fabf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fabf4.md) _ZNK5Botan14Cert_Extension10CRL_Number11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dc2c8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8f0.md)

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
                "const:350:8"
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
                "const:2c3:8"
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
        "0029b2c3",
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
        "0029b350",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fac0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fabf4.md#insn-004fac0c)
- 新版 [`004fac0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fabf4.md#insn-004fac0c)

~~~diff
- 004fac0c ["COPY", "tmp:0:8", ["const:2c3:8"]]
- 004fac0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004fac0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004fac0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004fac0c ["COPY", "tmp:0:8", ["const:350:8"]]
+ 004fac0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004fac0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004fac0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004fac0c bytes 290d0b91
+ 004fac0c bytes 29410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2238edeaa5c42caff54a251167afb31d"></a>

### [`004faccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004faccc.md) → [`004faccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faccc.md) _ZNK5Botan14Cert_Extension14CRL_ReasonCode12encode_innerEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00483ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512ca8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004fadac",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fad34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004faccc.md#insn-004fad34) · [`004fadac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004faccc.md#insn-004fadac)
- 新版 [`004fad34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faccc.md#insn-004fad34) · [`004fadac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faccc.md#insn-004fadac)

~~~diff
- 004fad34 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004fad34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fad34 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004fad34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fad34 bytes c93e43f9
+ 004fad34 bytes c99643f9
- 004fadac ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004fadac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fadac ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004fadac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fadac bytes c93e43f9
+ 004fadac bytes c99643f9
~~~


<a id="compare-ae70c83aada8a0c59c6b902deb7cb7e8"></a>

### [`004faf14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004faf14.md) → [`004faf14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faf14.md) _ZNK5Botan14Cert_Extension14CRL_ReasonCode11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dc2c8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8f0.md)

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
                "const:61e:8"
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
                "const:6b2:8"
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
        "002a76b2",
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
        "002a761e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004faf2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004faf14.md#insn-004faf2c)
- 新版 [`004faf2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faf14.md#insn-004faf2c)

~~~diff
- 004faf2c ["COPY", "tmp:0:8", ["const:6b2:8"]]
- 004faf2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004faf2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004faf2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004faf2c ["COPY", "tmp:0:8", ["const:61e:8"]]
+ 004faf2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004faf2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004faf2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004faf2c bytes 4ac91a91
+ 004faf2c bytes 4a791891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-740f50339364de7b4107f6f9da7cb75b"></a>

### [`004faff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004faff8.md) → [`004faff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faff8.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points12encode_innerEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

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
                "const:49f:8"
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
                "const:412:8"
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
                "const:190:8"
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
                "const:e0:8"
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
        "0029b412",
        null,
        "string"
      ]
    ],
    [
      "004fb038",
      "READ",
      [
        "storage",
        "0029b422",
        null,
        "string"
      ]
    ],
    [
      "004fb07c",
      "READ",
      [
        "storage",
        "00c1b0e0",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004faff8.md#insn-004fb030) · [`004fb034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004faff8.md#insn-004fb034)
- 新版 [`004fb030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faff8.md#insn-004fb030) · [`004fb034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faff8.md#insn-004fb034)

~~~diff
- 004fb030 ["COPY", "tmp:0:8", ["const:412:8"]]
- 004fb030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004fb030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004fb030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004fb030 ["COPY", "tmp:0:8", ["const:49f:8"]]
+ 004fb030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004fb030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004fb030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004fb030 bytes 08491091
+ 004fb030 bytes 087d1291
- 004fb034 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004fb034 bytes a9edffd0
+ 004fb034 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004fb034 bytes a9edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f2ade2002e987f83da58fcf2c897384"></a>

### [`004fb0d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb0d8.md) → [`004fb0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb0d8.md) _ZN5Botan14Cert_Extension23CRL_Distribution_Points12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md) [`0042e9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.52% / 新版 95.52%

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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004fb218",
      "PARAM",
      [
        "storage",
        "002ac6bf",
        null,
        null
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
    ]
  ],
  "added": [
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
      "004fb218",
      "PARAM",
      [
        "storage",
        "002ac6b6",
        null,
        null
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
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb0d8.md#insn-004fb154) · [`004fb194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb0d8.md#insn-004fb194) · [`004fb19c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb0d8.md#insn-004fb19c)
- 新版 [`004fb154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb0d8.md#insn-004fb154) · [`004fb194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb0d8.md#insn-004fb194)

~~~diff
- 004fb154 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004fb154 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fb154 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004fb154 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fb154 bytes 293d43f9
+ 004fb154 bytes 299543f9
- 004fb194 ["COPY", "tmp:0:8", ["const:6bf:8"]]
- 004fb194 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 004fb194 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 004fb194 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 004fb194 ["COPY", "tmp:0:8", ["const:6b6:8"]]
+ 004fb194 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 004fb194 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 004fb194 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 004fb194 bytes 94fe1a91
+ 004fb194 bytes 94da1a91
- 004fb19c ["COPY", "register:40a8:8", ["const:291000:8"]]
- 004fb19c bytes b5ecffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4350bbd5dfe0bfd52e58178f5257203c"></a>

### [`004fb4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb4c0.md) → [`004fb4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb4c0.md) _ZN5Botan11BER_Decoder11decode_listINS_14Cert_Extension23CRL_Distribution_Points18Distribution_PointEEERS0_RNSt6__ndk16vectorIT_NS6_9allocat

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf10.md) · 呼出先 11件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00517bcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00517/00517bcc.md) [`005180b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/005180b8.md) [`00519bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00519/00519bb0.md) [`0051a694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051a/0051a694.md)
- 新版 呼出元 1件 [`00bdcfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfc0.md) · 呼出先 11件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00517bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00517/00517bcc.md) [`005180b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005180b8.md) [`00519bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00519/00519bb0.md) [`0051a694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051a/0051a694.md)

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
                "const:728:8"
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
                "const:678:8"
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
        "00c1b2f8",
        null,
        "pointer"
      ]
    ],
    [
      "004fb518",
      "READ",
      [
        "storage",
        "00c1b1d8",
        null,
        "pointer"
      ]
    ],
    [
      "004fb52c",
      "DATA",
      [
        "storage",
        "00bebd68",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb4c0.md#insn-004fb514) · [`004fb518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb4c0.md#insn-004fb518) · [`004fb6cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb4c0.md#insn-004fb6cc)
- 新版 [`004fb514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb4c0.md#insn-004fb514) · [`004fb518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb4c0.md#insn-004fb518) · [`004fb6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb4c0.md#insn-004fb6cc)

~~~diff
- 004fb514 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f8:8"]]
- 004fb514 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fb514 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a8:8"]]
+ 004fb514 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fb514 bytes 087d41f9
+ 004fb514 bytes 08d541f9
- 004fb518 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1d8:8"]]
- 004fb518 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fb518 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:288:8"]]
+ 004fb518 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fb518 bytes 29ed40f9
+ 004fb518 bytes 294541f9
- 004fb6cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 004fb6cc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fb6cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 004fb6cc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fb6cc bytes 293d43f9
+ 004fb6cc bytes 299543f9
~~~


<a id="compare-0413d68949149cc9561410974710572f"></a>

### [`004fb79c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb79c.md) → [`004fb79c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb79c.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`004dc2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dc2c8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
                "const:675:8"
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
                "const:709:8"
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
        "002a9709",
        null,
        "string"
      ]
    ],
    [
      "004fb7e0",
      "READ",
      [
        "storage",
        "002a9716",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb79c.md#insn-004fb7d4)
- 新版 [`004fb7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb79c.md#insn-004fb7d4)

~~~diff
- 004fb7d4 ["COPY", "tmp:0:8", ["const:709:8"]]
- 004fb7d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004fb7d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004fb7d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004fb7d4 ["COPY", "tmp:0:8", ["const:675:8"]]
+ 004fb7d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004fb7d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004fb7d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004fb7d4 bytes 08251c91
+ 004fb7d4 bytes 08d51991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1753fb6b99fcfe178ed571ed35645a3f"></a>

### [`004fb898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb898.md) → [`004fb898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb898.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points18Distribution_Point11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

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
                "const:49f:8"
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
                "const:412:8"
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
                "const:190:8"
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
                "const:e0:8"
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
        "0029b412",
        null,
        "string"
      ]
    ],
    [
      "004fb8d8",
      "READ",
      [
        "storage",
        "0029b422",
        null,
        "string"
      ]
    ],
    [
      "004fb91c",
      "READ",
      [
        "storage",
        "00c1b0e0",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb898.md#insn-004fb8d0) · [`004fb8d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb898.md#insn-004fb8d4)
- 新版 [`004fb8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb898.md#insn-004fb8d0) · [`004fb8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb898.md#insn-004fb8d4)

~~~diff
- 004fb8d0 ["COPY", "tmp:0:8", ["const:412:8"]]
- 004fb8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004fb8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004fb8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004fb8d0 ["COPY", "tmp:0:8", ["const:49f:8"]]
+ 004fb8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004fb8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004fb8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004fb8d0 bytes 08491091
+ 004fb8d0 bytes 087d1291
- 004fb8d4 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004fb8d4 bytes a9edffd0
+ 004fb8d4 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004fb8d4 bytes a9edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd347e5d18c842b003addde21c9102b8"></a>

### [`004fb978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb978.md) → [`004fb978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb978.md) _ZN5Botan14Cert_Extension23CRL_Distribution_Points18Distribution_Point11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/005180b8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005180b8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004fbac8",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fba84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb978.md#insn-004fba84) · [`004fbac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb978.md#insn-004fbac8)
- 新版 [`004fba84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb978.md#insn-004fba84) · [`004fbac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb978.md#insn-004fbac8)

~~~diff
- 004fba84 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 004fba84 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fba84 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 004fba84 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fba84 bytes a93e43f9
+ 004fba84 bytes a99643f9
- 004fbac8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 004fbac8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fbac8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 004fbac8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fbac8 bytes a93e43f9
+ 004fbac8 bytes a99643f9
~~~


<a id="compare-d2e12becb0ff367fe016765b59100dac"></a>

### [`004fbd34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fbd34.md) → [`004fbd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fbd34.md) FUN_004fbd34

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

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
                "const:480:8"
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
                "const:3f3:8"
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
        "002a23f3",
        null,
        "string"
      ]
    ],
    [
      "004fbd74",
      "READ",
      [
        "storage",
        "002a2403",
        null,
        "string"
      ]
    ],
    [
      "004fbd7c",
      "READ",
      [
        "storage",
        "002a2412",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fbd6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fbd34.md#insn-004fbd6c) · [`004fbd70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fbd34.md#insn-004fbd70)
- 新版 [`004fbd6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fbd34.md#insn-004fbd6c) · [`004fbd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fbd34.md#insn-004fbd70)

~~~diff
- 004fbd6c ["COPY", "tmp:0:8", ["const:3f3:8"]]
- 004fbd6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004fbd6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004fbd6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004fbd6c ["COPY", "tmp:0:8", ["const:480:8"]]
+ 004fbd6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004fbd6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004fbd6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004fbd6c bytes 08cd0f91
+ 004fbd6c bytes 08011291
- 004fbd70 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 004fbd70 bytes a9edffb0
+ 004fbd70 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 004fbd70 bytes a9edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a609d558ae87936fac8451801b8723ae"></a>

### [`004fbef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fbef4.md) → [`004fbef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fbef4.md) FUN_004fbef4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0042e9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`004dc2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dc2c8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.39% / 新版 89.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fc00c",
      "incomplete_value": true,
      "site": "004fc028",
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
                "const:942:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fc00c",
      "incomplete_value": true,
      "site": "004fc028",
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
                "const:94b:8"
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
      "definition_site": "004fc00c",
      "incomplete_value": true,
      "site": "004fc028",
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
      "definition_site": "004fc00c",
      "incomplete_value": true,
      "site": "004fc028",
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
    "ordinal": 15,
    "slot": 2
  },
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fbf90",
      "PARAM",
      [
        "storage",
        "002ac6bf",
        null,
        null
      ]
    ],
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
      "004fc00c",
      "READ",
      [
        "storage",
        "002ad94b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fbf90",
      "PARAM",
      [
        "storage",
        "002ac6b6",
        null,
        null
      ]
    ],
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
      "004fc00c",
      "READ",
      [
        "storage",
        "002ad942",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fbf4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fbef4.md#insn-004fbf4c) · [`004fbf54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fbef4.md#insn-004fbf54)
- 新版 [`004fbf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fbef4.md#insn-004fbf4c) · [`004fbf54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fbef4.md#insn-004fbf54)

~~~diff
- 004fbf4c ["COPY", "tmp:0:8", ["const:6bf:8"]]
- 004fbf4c ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 004fbf4c ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 004fbf4c ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 004fbf4c ["COPY", "tmp:0:8", ["const:6b6:8"]]
+ 004fbf4c ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 004fbf4c ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 004fbf4c ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 004fbf4c bytes 94fe1a91
+ 004fbf4c bytes 94da1a91
- 004fbf54 ["COPY", "register:40a8:8", ["const:291000:8"]]
- 004fbf54 bytes b5ecffd0
+ 004fbf54 ["COPY", "register:40a8:8", ["const:291000:8"]]
+ 004fbf54 bytes b5ecffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e75fd6aa5c09eb11218bbfad4dec528"></a>

### [`004fc31c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fc31c.md) → [`004fc31c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc31c.md) _ZN5Botan11X509_Object11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00482aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00482/00482aa8.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdb7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7b0.md) [`00bdb7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00482aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482aa8.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb860.md) [`00bdb870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb870.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004fc420",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fc3dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fc31c.md#insn-004fc3dc) · [`004fc420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fc31c.md#insn-004fc420)
- 新版 [`004fc3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc31c.md#insn-004fc3dc) · [`004fc420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc31c.md#insn-004fc420)

~~~diff
- 004fc3dc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004fc3dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fc3dc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004fc3dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fc3dc bytes c93e43f9
+ 004fc3dc bytes c99643f9
- 004fc420 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 004fc420 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fc420 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 004fc420 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fc420 bytes c93e43f9
+ 004fc420 bytes c99643f9
~~~


<a id="compare-441b9245ebeefa57d893e7ccf61b6e67"></a>

### [`004fc6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fc6ac.md) → [`004fc6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc6ac.md) _ZNK5Botan11X509_Object23hash_used_for_signatureEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf40.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004fcb38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fcb38.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00524/00524c98.md)
- 新版 呼出元 1件 [`00bdcff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcff0.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004fcb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fcb38.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c98.md)

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
            "const:6a0:8"
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
            "const:5f0:8"
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
            "const:4a8:8"
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
            "const:41b:8"
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
                "const:f08:8"
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
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004fc734",
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ],
    [
      "004fc734",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fc6e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fc6ac.md#insn-004fc6e8) · [`004fc94c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fc6ac.md#insn-004fc94c) · [`004fc9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fc6ac.md#insn-004fc9a0)
- 新版 [`004fc6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc6ac.md#insn-004fc6e8) · [`004fc94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc6ac.md#insn-004fc94c) · [`004fc9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc6ac.md#insn-004fc9a0)

~~~diff
- 004fc6e8 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 004fc6e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004fc6e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004fc6e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004fc6e8 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 004fc6e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004fc6e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004fc6e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004fc6e8 bytes 08c11791
+ 004fc6e8 bytes 08811a91
- 004fc94c ["COPY", "tmp:0:8", ["const:41b:8"]]
- 004fc94c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004fc94c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004fc94c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004fc94c ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 004fc94c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004fc94c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004fc94c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004fc94c bytes 426c1091
+ 004fc94c bytes 42a01291
- 004fc9a0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004fc9a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fc9a0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fb8:8"]]
+ 004fc9a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004fc9a0 bytes 218447f9
+ 004fc9a0 bytes 21dc47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1280051e4a704c42dd149ae3168cc18"></a>

### [`004fcb38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fcb38.md) → [`004fcb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fcb38.md) FUN_004fcb38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004fc6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fc6ac.md) [`004fd178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fd178.md) · 呼出先 15件 [`004828a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00482/004828a4.md) [`00483ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512ca8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 2件 [`004fc6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc6ac.md) [`004fd178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fd178.md) · 呼出先 15件 [`004828a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004828a4.md) [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004fcb78",
      "DATA",
      [
        "storage",
        "00be90e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004fcba4",
      "DATA",
      [
        "storage",
        "00be90e8",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fcb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fcb38.md#insn-004fcb60) · [`004fce10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fcb38.md#insn-004fce10) · [`004fce94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fcb38.md#insn-004fce94)
- 新版 [`004fcb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fcb38.md#insn-004fcb60) · [`004fce10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fcb38.md#insn-004fce10) · [`004fce94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fcb38.md#insn-004fce94)

~~~diff
- 004fcb60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e48:8"]]
- 004fcb60 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fcb60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ef8:8"]]
+ 004fcb60 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 004fcb60 bytes 942647f9
+ 004fcb60 bytes 947e47f9
- 004fce10 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:678:8"]]
- 004fce10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fce10 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
+ 004fce10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fce10 bytes e93e43f9
+ 004fce10 bytes e99643f9
- 004fce94 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:678:8"]]
- 004fce94 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fce94 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
+ 004fce94 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fce94 bytes e93e43f9
+ 004fce94 bytes e99643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a105511aa738428ac6e7b018325e5af3"></a>

### [`004fd178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fd178.md) → [`004fd178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fd178.md) _ZNK5Botan11X509_Object16verify_signatureERKNS_10Public_KeyE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcd60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd60.md) · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00483d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483d44.md) [`00489d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00489/00489d4c.md) [`004fcb38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fcb38.md) [`00524c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00524/00524c3c.md)
- 新版 呼出元 1件 [`00bdce10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce10.md) · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00483d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483d44.md) [`00489d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/00489d4c.md) [`004fcb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fcb38.md) [`00524c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c3c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 1件

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
            "const:6a0:8"
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
            "const:5f0:8"
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
            "const:da1:8"
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
            "const:d14:8"
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
      "definition_site": "004fd568",
      "incomplete_value": false,
      "site": "004fd570",
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
            "const:52d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fd568",
      "incomplete_value": false,
      "site": "004fd570",
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
            "const:527:8"
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
      "004fd1c0",
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004fd204",
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ],
    [
      "004fd204",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fd1b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fd178.md#insn-004fd1b8) · [`004fd554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fd178.md#insn-004fd554) · [`004fd568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fd178.md#insn-004fd568)
- 新版 [`004fd1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fd178.md#insn-004fd1b8) · [`004fd554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fd178.md#insn-004fd554) · [`004fd568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fd178.md#insn-004fd568)

~~~diff
- 004fd1b8 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 004fd1b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004fd1b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004fd1b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004fd1b8 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 004fd1b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004fd1b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004fd1b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004fd1b8 bytes 08c11791
+ 004fd1b8 bytes 08811a91
- 004fd554 ["COPY", "tmp:0:8", ["const:d14:8"]]
- 004fd554 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004fd554 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004fd554 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004fd554 ["COPY", "tmp:0:8", ["const:da1:8"]]
+ 004fd554 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004fd554 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004fd554 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004fd554 bytes 21503491
+ 004fd554 bytes 21843691
- 004fd568 ["COPY", "tmp:0:8", ["const:527:8"]]
- 004fd568 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004fd568 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004fd568 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004fd568 ["COPY", "tmp:0:8", ["const:52d:8"]]
+ 004fd568 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004fd568 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004fd568 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004fd568 bytes 219c1491
+ 004fd568 bytes 21b41491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f2c493f8b97dc62fcfc10e4a31649b8"></a>

### [`004fdb0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdb0c.md) → [`004fdb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdb0c.md) _ZNK5Botan16X509_Certificate9PEM_labelEv

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
                "const:68b:8"
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
                "const:71f:8"
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
        "002a971f",
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
        "002a968b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fdb14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdb0c.md#insn-004fdb14)
- 新版 [`004fdb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdb0c.md#insn-004fdb14)

~~~diff
- 004fdb14 ["COPY", "tmp:0:8", ["const:71f:8"]]
- 004fdb14 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004fdb14 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004fdb14 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004fdb14 ["COPY", "tmp:0:8", ["const:68b:8"]]
+ 004fdb14 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004fdb14 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004fdb14 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004fdb14 bytes 4a7d1c91
+ 004fdb14 bytes 4a2d1a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a82d822556016e462a019898bcbfc10c"></a>

### [`004fdb38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdb38.md) → [`004fdb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdb38.md) _ZNK5Botan16X509_Certificate20alternate_PEM_labelsEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00450668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/00450668.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
                "const:650:8"
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
                "const:5c3:8"
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
        "002a15c3",
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
        "002a1650",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fdb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdb38.md#insn-004fdb50)
- 新版 [`004fdb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdb38.md#insn-004fdb50)

~~~diff
- 004fdb50 ["COPY", "tmp:0:8", ["const:5c3:8"]]
- 004fdb50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004fdb50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004fdb50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004fdb50 ["COPY", "tmp:0:8", ["const:650:8"]]
+ 004fdb50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004fdb50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004fdb50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004fdb50 bytes 290d1791
+ 004fdb50 bytes 29411991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-563fb0294c40f5a160c4bb38fb69a212"></a>

### [`004fdbe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdbe0.md) → [`004fdbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdbe0.md) _ZN5Botan16X509_CertificateC2ERNS_10DataSourceE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md) [`00bdcd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md) [`00bdcde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcde0.md)

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
        "00c1b268",
        null,
        "pointer"
      ]
    ],
    [
      "004fdc08",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004fdc20",
      "DATA",
      [
        "storage",
        "00bec960",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fdc00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdbe0.md#insn-004fdc00) · [`004fdc08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdbe0.md#insn-004fdc08) · [`004fdc54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdbe0.md#insn-004fdc54)
- 新版 [`004fdc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdbe0.md#insn-004fdc00) · [`004fdc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdbe0.md#insn-004fdc08) · [`004fdc54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdbe0.md#insn-004fdc54)

~~~diff
- 004fdc00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
- 004fdc00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fdc00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004fdc00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fdc00 bytes 083541f9
+ 004fdc00 bytes 088d41f9
- 004fdc08 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e48:8"]]
- 004fdc08 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fdc08 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
+ 004fdc08 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004fdc08 bytes 4a2547f9
+ 004fdc08 bytes 4a7d47f9
- 004fdc54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f0:8"]]
- 004fdc54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fdc54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
+ 004fdc54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fdc54 bytes 08f940f9
+ 004fdc54 bytes 085141f9
~~~


<a id="compare-b3d49fa93a53a99af88aa263d377e2c8"></a>

### [`004fdd34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdd34.md) → [`004fdd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdd34.md) _ZN5Botan16X509_CertificateC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcc70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcc70.md) · 呼出先 7件 [`0051d4f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d4f0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 1件 [`00bdcd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd20.md) · 呼出先 7件 [`0051d4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d4f0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

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
        "00c1b268",
        null,
        "pointer"
      ]
    ],
    [
      "004fdd5c",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004fdd74",
      "DATA",
      [
        "storage",
        "00bec960",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fdd54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdd34.md#insn-004fdd54) · [`004fdd5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdd34.md#insn-004fdd5c) · [`004fddb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdd34.md#insn-004fddb0)
- 新版 [`004fdd54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdd34.md#insn-004fdd54) · [`004fdd5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdd34.md#insn-004fdd5c) · [`004fddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdd34.md#insn-004fddb0)

~~~diff
- 004fdd54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
- 004fdd54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fdd54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004fdd54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fdd54 bytes 083541f9
+ 004fdd54 bytes 088d41f9
- 004fdd5c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e48:8"]]
- 004fdd5c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fdd5c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
+ 004fdd5c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004fdd5c bytes 4a2547f9
+ 004fdd5c bytes 4a7d47f9
- 004fddb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f0:8"]]
- 004fddb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fddb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
+ 004fddb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fddb0 bytes 08f940f9
+ 004fddb0 bytes 085141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc4c16c3b385f6ae7cc9894b73866fc7"></a>

### [`004fdeac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdeac.md) → [`004fdeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdeac.md) _ZN5Botan16X509_CertificateC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcb10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcb10.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md) [`00bdc710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc710.md) [`00bdc720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc720.md)
- 新版 呼出元 1件 [`00bdcbc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcbc0.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md) [`00bdc7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7c0.md) [`00bdc7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7d0.md)

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
        "00c1b268",
        null,
        "pointer"
      ]
    ],
    [
      "004fded4",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004fdeec",
      "DATA",
      [
        "storage",
        "00bec960",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fdecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdeac.md#insn-004fdecc) · [`004fded4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdeac.md#insn-004fded4) · [`004fdf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdeac.md#insn-004fdf20)
- 新版 [`004fdecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdeac.md#insn-004fdecc) · [`004fded4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdeac.md#insn-004fded4) · [`004fdf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdeac.md#insn-004fdf20)

~~~diff
- 004fdecc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
- 004fdecc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fdecc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004fdecc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fdecc bytes 083541f9
+ 004fdecc bytes 088d41f9
- 004fded4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e48:8"]]
- 004fded4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fded4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
+ 004fded4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004fded4 bytes 4a2547f9
+ 004fded4 bytes 4a7d47f9
- 004fdf20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f0:8"]]
- 004fdf20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fdf20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
+ 004fdf20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fdf20 bytes 08f940f9
+ 004fdf20 bytes 085141f9
~~~


<a id="compare-9ec869bc092f381e14cc9d03aed7a4dc"></a>

### [`004fdfd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdfd8.md) → [`004fdfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdfd8.md) _ZN5Botan16X509_Certificate12force_decodeEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 68件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`004828a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00482/004828a4.md)
- 新版 呼出元 0件  · 呼出先 68件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`004828a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004828a4.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.82% / 新版 94.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `call_target` 8件, `store_value` 13件

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
            "const:6a0:8"
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
            "const:5f0:8"
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
                "const:38d:8"
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
                "const:300:8"
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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "004fe274",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004fe280",
      "DATA",
      [
        "storage",
        "00be90e8",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fe150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdfd8.md#insn-004fe150) · [`004fe274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdfd8.md#insn-004fe274) · [`004fe314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdfd8.md#insn-004fe314)
- 新版 [`004fe150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdfd8.md#insn-004fe150) · [`004fe274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdfd8.md#insn-004fe274) · [`004fe314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdfd8.md#insn-004fe314)

~~~diff
- 004fe150 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:678:8"]]
- 004fe150 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fe150 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
+ 004fe150 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fe150 bytes 293f43f9
+ 004fe150 bytes 299743f9
- 004fe274 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e48:8"]]
- 004fe274 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fe274 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef8:8"]]
+ 004fe274 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fe274 bytes 082547f9
+ 004fe274 bytes 087d47f9
- 004fe314 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:678:8"]]
- 004fe314 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fe314 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
+ 004fe314 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fe314 bytes 293f43f9
+ 004fe314 bytes 299743f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b6de58e23a527eed51ba2fa472013e3"></a>

### [`004ff98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ff/004ff98c.md) → [`004ff98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ff/004ff98c.md) _ZNK5Botan16X509_Certificate4dataEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcaa0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md)
- 新版 呼出元 1件 [`00bdcb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb50.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)

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
            "const:66a:8"
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
            "const:5dd:8"
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
                "const:f08:8"
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
                "const:e58:8"
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
        "002a05dd",
        null,
        "string"
      ]
    ],
    [
      "004ffa28",
      "READ",
      [
        "storage",
        "00c1ae58",
        null,
        "pointer"
      ]
    ],
    [
      "004ffa28",
      "PARAM",
      [
        "storage",
        "00be92d8",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ff9ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ff/004ff98c.md#insn-004ff9ec) · [`004ffa28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ff/004ff98c.md#insn-004ffa28)
- 新版 [`004ff9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ff/004ff98c.md#insn-004ff9ec) · [`004ffa28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ff/004ff98c.md#insn-004ffa28)

~~~diff
- 004ff9ec ["COPY", "tmp:0:8", ["const:5dd:8"]]
- 004ff9ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004ff9ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004ff9ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004ff9ec ["COPY", "tmp:0:8", ["const:66a:8"]]
+ 004ff9ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004ff9ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004ff9ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004ff9ec bytes 21741791
+ 004ff9ec bytes 21a81991
- 004ffa28 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e58:8"]]
- 004ffa28 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ffa28 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
+ 004ffa28 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004ffa28 bytes 212c47f9
+ 004ffa28 bytes 218447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b16a795846231de0549d9949aa53f3b"></a>

### [`004ffc88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ff/004ffc88.md) → [`004ffc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ff/004ffc88.md) _ZNK5Botan16X509_Certificate13allowed_usageENS_10Usage_TypeE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf50.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdcaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcaa0.md) [`00bdccf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdccf0.md)
- 新版 呼出元 1件 [`00bdd000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd000.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdcb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb50.md) [`00bdcda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcda0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.30% / 新版 90.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

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
                "const:382:8"
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
                "const:389:8"
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
      "definition_site": "004ffdbc",
      "incomplete_value": true,
      "site": "004ffdbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ffdbc",
      "incomplete_value": true,
      "site": "004ffdbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e8:8"
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
      "definition_site": "004ffdb0",
      "incomplete_value": true,
      "site": "004ffdc0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ffdb0",
      "incomplete_value": true,
      "site": "004ffdc0",
      "value": [
        "LOAD",
        "8",
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
        "002a4389",
        null,
        "string"
      ]
    ],
    [
      "004ffdac",
      "READ",
      [
        "storage",
        "002ad8e8",
        null,
        "string"
      ]
    ],
    [
      "004ffdb0",
      "READ",
      [
        "storage",
        "002ad8ef",
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
        "002a4382",
        null,
        "string"
      ]
    ],
    [
      "004ffdac",
      "READ",
      [
        "storage",
        "002ad8df",
        null,
        "string"
      ]
    ],
    [
      "004ffdb0",
      "READ",
      [
        "storage",
        "002ad8e6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ffd0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ff/004ffc88.md#insn-004ffd0c) · [`004ffda4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ff/004ffc88.md#insn-004ffda4) · [`004ffe38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ff/004ffc88.md#insn-004ffe38)
- 新版 [`004ffd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ff/004ffc88.md#insn-004ffd0c) · [`004ffda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ff/004ffc88.md#insn-004ffda4) · [`004ffe38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ff/004ffc88.md#insn-004ffe38)

~~~diff
- 004ffd0c ["COPY", "tmp:0:8", ["const:389:8"]]
- 004ffd0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ffd0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ffd0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ffd0c ["COPY", "tmp:0:8", ["const:382:8"]]
+ 004ffd0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ffd0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ffd0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ffd0c bytes 29250e91
+ 004ffd0c bytes 29090e91
- 004ffda4 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 004ffda4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ffda4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ffda4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ffda4 ["COPY", "tmp:0:8", ["const:8df:8"]]
+ 004ffda4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ffda4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ffda4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ffda4 bytes 29a12391
+ 004ffda4 bytes 297d2391
- 004ffe38 ["COPY", "tmp:0:8", ["const:4a4:8"]]
- 004ffe38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ffe38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ffe38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ffe38 ["COPY", "tmp:0:8", ["const:410:8"]]
+ 004ffe38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ffe38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ffe38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ffe38 bytes 29911291
+ 004ffe38 bytes 29411091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94c682fb237b1fa76519e3be58b07387"></a>

### [`005001f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00500/005001f4.md) → [`005001f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00500/005001f4.md) _ZNK5Botan16X509_Certificate12subject_infoERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf60.md) · 呼出先 16件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0041f354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f354.md) [`00450668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/00450668.md) [`005251c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/005251c0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00bdd010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd010.md) · 呼出先 16件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041f354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md) [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`005251c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/005251c0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
            "const:4c0:8"
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
            "const:433:8"
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
            "const:56d:8"
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
            "const:574:8"
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
            "const:bb0:8"
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
            "const:b23:8"
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
        "0029b433",
        null,
        "string"
      ]
    ],
    [
      "00500564",
      "PARAM",
      [
        "storage",
        "002a4574",
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
  ],
  "added": [
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00500528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00500/005001f4.md#insn-00500528) · [`00500564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00500/005001f4.md#insn-00500564) · [`005005a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00500/005001f4.md#insn-005005a0)
- 新版 [`00500528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00500/005001f4.md#insn-00500528) · [`00500564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00500/005001f4.md#insn-00500564) · [`005005a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00500/005001f4.md#insn-005005a0)

~~~diff
- 00500528 ["COPY", "tmp:0:8", ["const:433:8"]]
- 00500528 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00500528 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00500528 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00500528 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 00500528 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00500528 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00500528 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00500528 bytes 21cc1091
+ 00500528 bytes 21001391
- 00500564 ["COPY", "tmp:0:8", ["const:574:8"]]
- 00500564 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00500564 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00500564 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00500564 ["COPY", "tmp:0:8", ["const:56d:8"]]
+ 00500564 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00500564 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00500564 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00500564 bytes 21d01591
+ 00500564 bytes 21b41591
- 005005a0 ["COPY", "tmp:0:8", ["const:b23:8"]]
- 005005a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005005a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005005a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005005a0 ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 005005a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005005a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005005a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005005a0 bytes 218c2c91
+ 005005a0 bytes 21c02e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5d3eb7f8c6b3f3e56644e6dcbca9b06"></a>

### [`00501b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00501/00501b08.md) → [`00501b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00501/00501b08.md) _ZNK5Botan16X509_Certificate9to_stringEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 27件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004365f8.md) [`00512c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512c94.md) [`0051bf98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051b/0051bf98.md)
- 新版 呼出元 0件  · 呼出先 27件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`0051bf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051b/0051bf98.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.07% / 新版 93.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 45件, `store_destination` 2件, `store_value` 8件

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
        "00c1ad98",
        null,
        "pointer"
      ]
    ],
    [
      "00501b44",
      "READ",
      [
        "storage",
        "00c1acc8",
        null,
        "pointer"
      ]
    ],
    [
      "00501b58",
      "READ",
      [
        "storage",
        "00c13360",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00501b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00501/00501b08.md#insn-00501b34) · [`00501b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00501/00501b08.md#insn-00501b44) · [`00501bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00501/00501b08.md#insn-00501bb0)
- 新版 [`00501b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00501/00501b08.md#insn-00501b34) · [`00501b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00501/00501b08.md#insn-00501b44) · [`00501bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00501/00501b08.md#insn-00501bb0)

~~~diff
- 00501b34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d98:8"]]
- 00501b34 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00501b34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00501b34 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00501b34 bytes 73ce46f9
+ 00501b34 bytes 732647f9
- 00501b44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cc8:8"]]
- 00501b44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00501b44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d78:8"]]
+ 00501b44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00501b44 bytes 296546f9
+ 00501b44 bytes 29bd46f9
- 00501bb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
- 00501bb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00501bb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
+ 00501bb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00501bb0 bytes 086946f9
+ 00501bb0 bytes 08c146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72ed391e1996bedd2df065571a83a46d"></a>

### [`00503408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/00503408.md) → [`00503408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503408.md) _ZN5Botan17X509_Cert_Options17add_ex_constraintERKNS_3OIDE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512c94.md) [`00528a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00528/00528a6c.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00528a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00528/00528a6c.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
        "00c1ae50",
        null,
        "pointer"
      ]
    ],
    [
      "0050344c",
      "DATA",
      [
        "storage",
        "00be91c8",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050343c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/00503408.md#insn-0050343c)
- 新版 [`0050343c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503408.md#insn-0050343c)

~~~diff
- 0050343c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e50:8"]]
- 0050343c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050343c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 0050343c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050343c bytes 082947f9
+ 0050343c bytes 088147f9
~~~


<a id="compare-7c23bcb5daf29b06b8b75d8e6324fb62"></a>

### [`005034d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/005034d8.md) → [`005034d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/005034d8.md) _ZN5Botan17X509_Cert_Options17add_ex_constraintERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0052a96c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052a/0052a96c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb730.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0052a96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052a/0052a96c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7e0.md)

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
        "00c1ae50",
        null,
        "pointer"
      ]
    ],
    [
      "00503530",
      "DATA",
      [
        "storage",
        "00be91c8",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00503520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/005034d8.md#insn-00503520)
- 新版 [`00503520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/005034d8.md#insn-00503520)

~~~diff
- 00503520 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e50:8"]]
- 00503520 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00503520 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f00:8"]]
+ 00503520 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00503520 bytes 292947f9
+ 00503520 bytes 298147f9
~~~


<a id="compare-f2b776b2cf0674d1e3158834b990b57a"></a>

### [`005035d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/005035d4.md) → [`005035d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/005035d4.md) _ZN5Botan17X509_Cert_OptionsC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00524/00524c98.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c98.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
        "00c1aec0",
        null,
        "pointer"
      ]
    ],
    [
      "00503650",
      "DATA",
      [
        "storage",
        "00be92b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00503658",
      "DATA",
      [
        "storage",
        "00be92b8",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050363c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/005035d4.md#insn-0050363c) · [`0050366c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/005035d4.md#insn-0050366c) · [`0050369c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/005035d4.md#insn-0050369c)
- 新版 [`0050363c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/005035d4.md#insn-0050363c) · [`0050366c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/005035d4.md#insn-0050366c) · [`0050369c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/005035d4.md#insn-0050369c)

~~~diff
- 0050363c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec0:8"]]
- 0050363c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050363c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
+ 0050363c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050363c bytes 086147f9
+ 0050363c bytes 08b947f9
- 0050366c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:220:8"]]
- 0050366c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050366c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2d0:8"]]
+ 0050366c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050366c bytes 081141f9
+ 0050366c bytes 086941f9
- 0050369c ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 0050369c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0050369c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0050369c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0050369c ["COPY", "tmp:0:8", ["const:866:8"]]
+ 0050369c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0050369c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0050369c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0050369c bytes 21641f91
+ 0050369c bytes 21982191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-deaf3957437d398ee029a4b8db951fd1"></a>

### [`00503af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/00503af8.md) → [`00503af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503af8.md) _ZN5Botan4PKIX11check_chainERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEENS1_6chrono10time_pointINSC_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf90.md) · 呼出先 29件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`004ee34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004ee34c.md) [`00504ee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00504/00504ee4.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md)
- 新版 呼出元 1件 [`00bdd040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd040.md) · 呼出先 29件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004ee34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee34c.md) [`00504ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00504/00504ee4.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md)

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
            "const:293:8"
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
            "const:327:8"
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
                "const:ef0:8"
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
                "const:e40:8"
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
        "00c253e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00504194",
      "READ",
      [
        "storage",
        "00c253e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00504d24",
      "PARAM",
      [
        "storage",
        "002a8327",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00503fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/00503af8.md#insn-00503fec) · [`0050401c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/00503af8.md#insn-0050401c) · [`0050408c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/00503af8.md#insn-0050408c)
- 新版 [`00503fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503af8.md#insn-00503fec) · [`0050401c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503af8.md#insn-0050401c) · [`0050408c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503af8.md#insn-0050408c)

~~~diff
- 00503fec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3e8:8"]]
- 00503fec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00503fec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4a8:8"]]
+ 00503fec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00503fec bytes 08f541f9
+ 00503fec bytes 085542f9
- 0050401c ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 0050401c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050401c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050401c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0050401c ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 0050401c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0050401c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0050401c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050401c bytes 4aa10f91
+ 0050401c bytes 4aa11291
- 0050408c ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 0050408c ["INT_CARRY", "register:105:1", ["register:4068:8", "tmp:0:8"]]
- 0050408c ["INT_SCARRY", "register:106:1", ["register:4068:8", "tmp:0:8"]]
- 0050408c ["INT_ADD", "tmp:1:8", ["register:4068:8", "tmp:0:8"]]
+ 0050408c ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 0050408c ["INT_CARRY", "register:105:1", ["register:4068:8", "tmp:0:8"]]
+ 0050408c ["INT_SCARRY", "register:106:1", ["register:4068:8", "tmp:0:8"]]
+ 0050408c ["INT_ADD", "tmp:1:8", ["register:4068:8", "tmp:0:8"]]
- 0050408c bytes ada10f91
+ 0050408c bytes ada11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3933963f8b9ae7f04066650bad637892"></a>

### [`00504f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00504/00504f50.md) → [`00504f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00504/00504f50.md) _ZN5Botan4PKIX10check_ocspERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_4OCSP8Respons

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcfa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcfa0.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`004de718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004de/004de718.md) [`00504ee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00504/00504ee4.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md)
- 新版 呼出元 1件 [`00bdd050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd050.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004de718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004de718.md) [`00504ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00504/00504ee4.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md)

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
            "const:52d:8"
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
            "const:4a0:8"
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
                "const:ef0:8"
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
                "const:e40:8"
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
        "0029e4a0",
        null,
        "string"
      ]
    ],
    [
      "005053f8",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "005053f8",
      "PARAM",
      [
        "storage",
        "00be91e8",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005053bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00504/00504f50.md#insn-005053bc) · [`005053f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00504/00504f50.md#insn-005053f8)
- 新版 [`005053bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00504/00504f50.md#insn-005053bc) · [`005053f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00504/00504f50.md#insn-005053f8)

~~~diff
- 005053bc ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 005053bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005053bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005053bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005053bc ["COPY", "tmp:0:8", ["const:52d:8"]]
+ 005053bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005053bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005053bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005053bc bytes 21801291
+ 005053bc bytes 21b41491
- 005053f8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 005053f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005053f8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 005053f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005053f8 bytes 212047f9
+ 005053f8 bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a9ecd1e1d80d7ec51478fd440436107"></a>

### [`005054cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00505/005054cc.md) → [`005054cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00505/005054cc.md) _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_8X509_CRLEEENS7

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcfb0.md) · 呼出先 29件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`0051c938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051c/0051c938.md)
- 新版 呼出元 1件 [`00bdd060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd060.md) · 呼出先 29件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051c938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c938.md)

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
            "const:921:8"
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
            "const:894:8"
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
                "const:ef0:8"
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
                "const:e40:8"
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
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00505f60",
      "PARAM",
      [
        "storage",
        "00be91e8",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00505f24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00505/005054cc.md#insn-00505f24) · [`00505f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00505/005054cc.md#insn-00505f60)
- 新版 [`00505f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00505/005054cc.md#insn-00505f24) · [`00505f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00505/005054cc.md#insn-00505f60)

~~~diff
- 00505f24 ["COPY", "tmp:0:8", ["const:894:8"]]
- 00505f24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00505f24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00505f24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00505f24 ["COPY", "tmp:0:8", ["const:921:8"]]
+ 00505f24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00505f24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00505f24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00505f24 bytes 21502291
+ 00505f24 bytes 21842491
- 00505f60 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 00505f60 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00505f60 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 00505f60 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00505f60 bytes 212047f9
+ 00505f60 bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7797e339df4bcb2dd984122d2c76d7b"></a>

### [`005060a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00506/005060a8.md) → [`005060a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/005060a8.md) _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_IPNS_17Certificate_StoreE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcfc0.md) · 呼出先 16件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00525e44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00525/00525e44.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md)
- 新版 呼出元 1件 [`00bdd070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd070.md) · 呼出先 16件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00525e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525e44.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)

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
            "const:be4:8"
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
            "const:b57:8"
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
            "const:866:8"
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
            "const:7d9:8"
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
            "const:692:8"
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
            "const:699:8"
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
        "002a5699",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005062f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00506/005060a8.md#insn-005062f0) · [`005062f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00506/005060a8.md#insn-005062f8) · [`00506300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00506/005060a8.md#insn-00506300)
- 新版 [`005062f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/005060a8.md#insn-005062f0) · [`005062f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/005060a8.md#insn-005062f8) · [`00506300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/005060a8.md#insn-00506300)

~~~diff
- 005062f0 ["COPY", "tmp:0:8", ["const:b57:8"]]
- 005062f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005062f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005062f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005062f0 ["COPY", "tmp:0:8", ["const:be4:8"]]
+ 005062f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005062f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005062f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005062f0 bytes 005c2d91
+ 005062f0 bytes 00902f91
- 005062f8 ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 005062f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005062f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005062f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005062f8 ["COPY", "tmp:0:8", ["const:866:8"]]
+ 005062f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005062f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005062f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005062f8 bytes 21641f91
+ 005062f8 bytes 21982191
- 00506300 ["COPY", "tmp:0:8", ["const:699:8"]]
- 00506300 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00506300 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00506300 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00506300 ["COPY", "tmp:0:8", ["const:692:8"]]
+ 00506300 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00506300 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00506300 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00506300 bytes 42641a91
+ 00506300 bytes 42481a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45c6494c6c56a780ac8aa8ba3b34975f"></a>

### [`0050645c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00506/0050645c.md) → [`0050645c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/0050645c.md) _ZN5Botan4PKIX22build_certificate_pathERNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_IPNS_17Certi

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 20件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`004df920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004df/004df920.md) [`005180b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/005180b8.md) [`0051d9f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d9f8.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`004df920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004df920.md) [`005180b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005180b8.md) [`0051d9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d9f8.md)

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
        "00c1b208",
        null,
        "pointer"
      ]
    ],
    [
      "005066c4",
      "DATA",
      [
        "storage",
        "00bea6d8",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005066b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00506/0050645c.md#insn-005066b8)
- 新版 [`005066b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/0050645c.md#insn-005066b8)

~~~diff
- 005066b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:208:8"]]
- 005066b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005066b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b8:8"]]
+ 005066b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005066b8 bytes 080541f9
+ 005066b8 bytes 085d41f9
~~~


<a id="compare-c5925b7c1039f6f9e3b6ff88cbfc90a4"></a>

### [`00508250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00508/00508250.md) → [`00508250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508250.md) _ZN5Botan4PKIX23merge_revocation_statusERNSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcfd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcfd0.md) · 呼出先 8件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bdd080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd080.md) · 呼出先 8件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
            "const:941:8"
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
            "const:8b4:8"
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
                "const:ef0:8"
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
                "const:e40:8"
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
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "0050869c",
      "PARAM",
      [
        "storage",
        "00be91e8",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00508660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00508/00508250.md#insn-00508660) · [`0050869c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00508/00508250.md#insn-0050869c)
- 新版 [`00508660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508250.md#insn-00508660) · [`0050869c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508250.md#insn-0050869c)

~~~diff
- 00508660 ["COPY", "tmp:0:8", ["const:8b4:8"]]
- 00508660 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00508660 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00508660 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00508660 ["COPY", "tmp:0:8", ["const:941:8"]]
+ 00508660 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00508660 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00508660 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00508660 bytes 21d02291
+ 00508660 bytes 21042591
- 0050869c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 0050869c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050869c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 0050869c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0050869c bytes 212047f9
+ 0050869c bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5098f4da13e67a721c91907e716a7b4"></a>

### [`005086fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00508/005086fc.md) → [`005086fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/005086fc.md) _ZN5Botan4PKIX14overall_statusERKNSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS9_EEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcfe0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`00bdd090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd090.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

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
            "const:501:8"
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
            "const:474:8"
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
                "const:ef0:8"
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
                "const:e40:8"
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
        "002a2474",
        null,
        "string"
      ]
    ],
    [
      "00508800",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00508800",
      "PARAM",
      [
        "storage",
        "00be91e8",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005087c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00508/005086fc.md#insn-005087c4) · [`00508800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00508/005086fc.md#insn-00508800)
- 新版 [`005087c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/005086fc.md#insn-005087c4) · [`00508800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/005086fc.md#insn-00508800)

~~~diff
- 005087c4 ["COPY", "tmp:0:8", ["const:474:8"]]
- 005087c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005087c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005087c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005087c4 ["COPY", "tmp:0:8", ["const:501:8"]]
+ 005087c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005087c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005087c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005087c4 bytes 21d01191
+ 005087c4 bytes 21041491
- 00508800 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
- 00508800 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00508800 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
+ 00508800 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00508800 bytes 212047f9
+ 00508800 bytes 217847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-747678b5d15797456116e3d35fc08be3"></a>

### [`00508860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00508/00508860.md) → [`00508860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508860.md) _ZN5Botan18x509_path_validateERKNSt6__ndk16vectorINS_16X509_CertificateENS0_9allocatorIS2_EEEERKNS_28Path_Validation_RestrictionsERKNS1_IPNS

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcff0.md) · 呼出先 28件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00506ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00506/00506ee0.md) [`0050936c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00509/0050936c.md) [`0050947c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00509/0050947c.md)
- 新版 呼出元 1件 [`00bdd0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd0a0.md) · 呼出先 28件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00506ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/00506ee0.md) [`0050936c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00509/0050936c.md) [`0050947c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00509/0050947c.md)

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
            "const:54e:8"
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
            "const:4c1:8"
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
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "005088dc",
      "DATA",
      [
        "storage",
        "00bed680",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005088f8",
      "READ",
      [
        "storage",
        "00c1b1f0",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005088d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00508/00508860.md#insn-005088d0) · [`005088f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00508/00508860.md#insn-005088f8) · [`005091c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00508/00508860.md#insn-005091c4)
- 新版 [`005088d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508860.md#insn-005088d0) · [`005088f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508860.md#insn-005088f8) · [`005091c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508860.md#insn-005091c4)

~~~diff
- 005088d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1e8:8"]]
- 005088d0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005088d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:298:8"]]
+ 005088d0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 005088d0 bytes 94f640f9
+ 005088d0 bytes 944e41f9
- 005088f8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:1f0:8"]]
- 005088f8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005088f8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:2a0:8"]]
+ 005088f8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 005088f8 bytes d6fa40f9
+ 005088f8 bytes d65241f9
- 005091c4 ["COPY", "tmp:0:8", ["const:4c1:8"]]
- 005091c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005091c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005091c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005091c4 ["COPY", "tmp:0:8", ["const:54e:8"]]
+ 005091c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005091c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005091c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005091c4 bytes 21041391
+ 005091c4 bytes 21381591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4983b3166a49f3eb8365c06ffa9cc65f"></a>

### [`0050a23c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a23c.md) → [`0050a23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a23c.md) _ZNK5Botan22Path_Validation_Result10trust_rootEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050a2ac",
      "incomplete_value": false,
      "site": "0050a2b4",
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
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050a2ac",
      "incomplete_value": false,
      "site": "0050a2b4",
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
            "const:ad9:8"
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
                "const:e98:8"
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
                "const:f48:8"
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
                "const:e98:8"
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
      "0050a2ac",
      "PARAM",
      [
        "storage",
        "002adad9",
        null,
        "string"
      ]
    ],
    [
      "0050a2e8",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "0050a2e8",
      "PARAM",
      [
        "storage",
        "00be9188",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0050a2ac",
      "PARAM",
      [
        "storage",
        "002adad0",
        null,
        "string"
      ]
    ],
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
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050a2ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a23c.md#insn-0050a2ac) · [`0050a2e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a23c.md#insn-0050a2e8) · [`0050a34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a23c.md#insn-0050a34c)
- 新版 [`0050a2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a23c.md#insn-0050a2ac) · [`0050a2e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a23c.md#insn-0050a2e8) · [`0050a34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a23c.md#insn-0050a34c)

~~~diff
- 0050a2ac ["COPY", "tmp:0:8", ["const:ad9:8"]]
- 0050a2ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0050a2ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0050a2ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0050a2ac ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 0050a2ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0050a2ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0050a2ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0050a2ac bytes 21642b91
+ 0050a2ac bytes 21402b91
- 0050a2e8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e98:8"]]
- 0050a2e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050a2e8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
+ 0050a2e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0050a2e8 bytes 214c47f9
+ 0050a2e8 bytes 21a447f9
- 0050a34c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e98:8"]]
- 0050a34c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050a34c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
+ 0050a34c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0050a34c bytes 214c47f9
+ 0050a34c bytes 21a447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e0f5ba6c7c98d250add6de20e97313b"></a>

### [`0050a638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a638.md) → [`0050a638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md) _ZN5Botan4X50923create_self_signed_certERKNS_17X509_Cert_OptionsERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9al

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 27件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`0049dba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0049d/0049dba0.md) [`004de034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004de/004de034.md) [`004e23fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e2/004e23fc.md) [`004ed188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ed188.md)
- 新版 呼出元 0件  · 呼出先 27件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0049dba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dba0.md) [`004de034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004de034.md) [`004e23fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e2/004e23fc.md) [`004ed188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ed188.md)

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
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "0050a68c",
      "DATA",
      [
        "storage",
        "00be90e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050a6c4",
      "READ",
      [
        "storage",
        "00c1b1e0",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050a674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a638.md#insn-0050a674) · [`0050a6c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a638.md#insn-0050a6c4) · [`0050a730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a638.md#insn-0050a730)
- 新版 [`0050a674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md#insn-0050a674) · [`0050a6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md#insn-0050a6c4) · [`0050a730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md#insn-0050a730)

~~~diff
- 0050a674 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e48:8"]]
- 0050a674 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050a674 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ef8:8"]]
+ 0050a674 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050a674 bytes 292547f9
+ 0050a674 bytes 297d47f9
- 0050a6c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
- 0050a6c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050a6c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 0050a6c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050a6c4 bytes 08f140f9
+ 0050a6c4 bytes 084941f9
- 0050a730 ["COPY", "tmp:0:8", ["const:57a:8"]]
- 0050a730 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0050a730 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0050a730 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0050a730 ["COPY", "tmp:0:8", ["const:607:8"]]
+ 0050a730 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0050a730 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0050a730 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0050a730 bytes 21e81591
+ 0050a730 bytes 211c1891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f217cfb1cc7eab76aea31e24939bcfac"></a>

### [`0050af44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050af44.md) → [`0050af44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050af44.md) FUN_0050af44

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0050a638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050b/0050b45c.md) · 呼出先 10件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`004dc4a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004dc/004dc4a4.md) [`005180b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/005180b8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 2件 [`0050a638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md) · 呼出先 10件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`004dc4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc4a4.md) [`005180b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005180b8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.04% / 新版 90.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 10件

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
                "const:9fa:8"
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
                "const:96d:8"
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
      "definition_site": "0050aff4",
      "incomplete_value": true,
      "site": "0050aff4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:56e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050aff4",
      "incomplete_value": true,
      "site": "0050aff4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
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
      "0050afe0",
      "READ",
      [
        "storage",
        "002aa568",
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
      "0050afe0",
      "READ",
      [
        "storage",
        "002aa56e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050af64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050af44.md#insn-0050af64) · [`0050afd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050af44.md#insn-0050afd8) · [`0050b03c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050af44.md#insn-0050b03c)
- 新版 [`0050af64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050af44.md#insn-0050af64) · [`0050afd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050af44.md#insn-0050afd8) · [`0050b03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050af44.md#insn-0050b03c)

~~~diff
- 0050af64 ["COPY", "tmp:0:8", ["const:96d:8"]]
- 0050af64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050af64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050af64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050af64 ["COPY", "tmp:0:8", ["const:9fa:8"]]
+ 0050af64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050af64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050af64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050af64 bytes 29b52591
+ 0050af64 bytes 29e92791
- 0050afd8 ["COPY", "tmp:0:8", ["const:568:8"]]
- 0050afd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050afd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050afd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050afd8 ["COPY", "tmp:0:8", ["const:56e:8"]]
+ 0050afd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050afd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050afd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050afd8 bytes 29a11591
+ 0050afd8 bytes 29b91591
- 0050b03c ["COPY", "tmp:0:8", ["const:97d:8"]]
- 0050b03c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050b03c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050b03c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050b03c ["COPY", "tmp:0:8", ["const:a0a:8"]]
+ 0050b03c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050b03c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050b03c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050b03c bytes 29f52591
+ 0050b03c bytes 29292891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89034bdaf5e4295934a47ec94e788a74"></a>

### [`0050b45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050b/0050b45c.md) → [`0050b45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md) _ZN5Botan4X50915create_cert_reqERKNS_17X509_Cert_OptionsERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9allocatorI

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 42件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00483ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483ed8.md) [`0049dba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0049d/0049dba0.md) [`004de034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004de/004de034.md) [`004e23fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e2/004e23fc.md)
- 新版 呼出元 0件  · 呼出先 42件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`0049dba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dba0.md) [`004de034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004de034.md) [`004e23fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e2/004e23fc.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.04% / 新版 94.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 5件, `store_value` 10件

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
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "0050b4b0",
      "DATA",
      [
        "storage",
        "00be90e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050b4e8",
      "READ",
      [
        "storage",
        "00c1b1e0",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050b498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050b/0050b45c.md#insn-0050b498) · [`0050b4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050b/0050b45c.md#insn-0050b4e8) · [`0050b554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050b/0050b45c.md#insn-0050b554)
- 新版 [`0050b498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md#insn-0050b498) · [`0050b4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md#insn-0050b4e8) · [`0050b554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md#insn-0050b554)

~~~diff
- 0050b498 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e48:8"]]
- 0050b498 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050b498 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ef8:8"]]
+ 0050b498 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050b498 bytes 292547f9
+ 0050b498 bytes 297d47f9
- 0050b4e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
- 0050b4e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050b4e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 0050b4e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050b4e8 bytes 08f140f9
+ 0050b4e8 bytes 084941f9
- 0050b554 ["COPY", "tmp:0:8", ["const:57a:8"]]
- 0050b554 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0050b554 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0050b554 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0050b554 ["COPY", "tmp:0:8", ["const:607:8"]]
+ 0050b554 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0050b554 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0050b554 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0050b554 bytes 21e81591
+ 0050b554 bytes 211c1891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4188e18934c9be31f692b752189577c"></a>

### [`0050c0e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c0e8.md) → [`0050c0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c0e8.md) FUN_0050c0e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050c1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c1dc.md) · 呼出先 2件 [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`0050c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c1dc.md) · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "0050c13c",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "0050c168",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c0e8.md#insn-0050c110) · [`0050c13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c0e8.md#insn-0050c13c) · [`0050c168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c0e8.md#insn-0050c168)
- 新版 [`0050c110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c0e8.md#insn-0050c110) · [`0050c13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c0e8.md#insn-0050c13c) · [`0050c168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c0e8.md#insn-0050c168)

~~~diff
- 0050c110 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050c110 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c110 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050c110 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c110 bytes a93e43f9
+ 0050c110 bytes a99643f9
- 0050c13c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050c13c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c13c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050c13c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c13c bytes a93e43f9
+ 0050c13c bytes a99643f9
- 0050c168 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050c168 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c168 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050c168 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c168 bytes a93e43f9
+ 0050c168 bytes a99643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73521eff8d901b74103183d7b3d4be6d"></a>

### [`0050c390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c390.md) → [`0050c390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c390.md) FUN_0050c390

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
        "00c1af20",
        null,
        "pointer"
      ]
    ],
    [
      "0050c3b0",
      "DATA",
      [
        "storage",
        "00beaa10",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c3a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c390.md#insn-0050c3a8)
- 新版 [`0050c3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c390.md#insn-0050c3a8)

~~~diff
- 0050c3a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
- 0050c3a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c3a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd0:8"]]
+ 0050c3a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c3a8 bytes 089147f9
+ 0050c3a8 bytes 08e947f9
~~~


<a id="compare-3bcab977270657d8054e2bb8105b8f90"></a>

### [`0050c3d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c3d4.md) → [`0050c3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c3d4.md) FUN_0050c3d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050c4c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c4c8.md) · 呼出先 2件 [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`0050c4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c4c8.md) · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "0050c428",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "0050c454",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c3fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c3d4.md#insn-0050c3fc) · [`0050c428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c3d4.md#insn-0050c428) · [`0050c454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c3d4.md#insn-0050c454)
- 新版 [`0050c3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c3d4.md#insn-0050c3fc) · [`0050c428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c3d4.md#insn-0050c428) · [`0050c454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c3d4.md#insn-0050c454)

~~~diff
- 0050c3fc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050c3fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c3fc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050c3fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c3fc bytes a93e43f9
+ 0050c3fc bytes a99643f9
- 0050c428 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050c428 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c428 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050c428 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c428 bytes a93e43f9
+ 0050c428 bytes a99643f9
- 0050c454 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050c454 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c454 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050c454 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c454 bytes a93e43f9
+ 0050c454 bytes a99643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5037715e5a86b79e1e10cca1405a11ef"></a>

### [`0050c67c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c67c.md) → [`0050c67c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c67c.md) FUN_0050c67c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
        "00c1af28",
        null,
        "pointer"
      ]
    ],
    [
      "0050c69c",
      "DATA",
      [
        "storage",
        "00beaae8",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c67c.md#insn-0050c694)
- 新版 [`0050c694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c67c.md#insn-0050c694)

~~~diff
- 0050c694 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f28:8"]]
- 0050c694 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c694 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd8:8"]]
+ 0050c694 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c694 bytes 089547f9
+ 0050c694 bytes 08ed47f9
~~~


<a id="compare-f6944b2cb62fb54cbd43710dfcf55786"></a>

### [`0050c6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c6c0.md) → [`0050c6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c6c0.md) FUN_0050c6c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050c7b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c7b4.md) · 呼出先 2件 [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`0050c7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c7b4.md) · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "0050c714",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "0050c740",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c6e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c6c0.md#insn-0050c6e8) · [`0050c714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c6c0.md#insn-0050c714) · [`0050c740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c6c0.md#insn-0050c740)
- 新版 [`0050c6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c6c0.md#insn-0050c6e8) · [`0050c714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c6c0.md#insn-0050c714) · [`0050c740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c6c0.md#insn-0050c740)

~~~diff
- 0050c6e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050c6e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c6e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050c6e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c6e8 bytes a93e43f9
+ 0050c6e8 bytes a99643f9
- 0050c714 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050c714 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c714 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050c714 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c714 bytes a93e43f9
+ 0050c714 bytes a99643f9
- 0050c740 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050c740 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c740 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050c740 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c740 bytes a93e43f9
+ 0050c740 bytes a99643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12f8ba2a45486d5edd280b29b9f2aff6"></a>

### [`0050c968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c968.md) → [`0050c968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c968.md) FUN_0050c968

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
        "00c1af30",
        null,
        "pointer"
      ]
    ],
    [
      "0050c988",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c968.md#insn-0050c980)
- 新版 [`0050c980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c968.md#insn-0050c980)

~~~diff
- 0050c980 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f30:8"]]
- 0050c980 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c980 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 0050c980 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c980 bytes 089947f9
+ 0050c980 bytes 08f147f9
~~~


<a id="compare-fe2705ba9c632039db3a2d882b97f363"></a>

### [`0050c9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c9c4.md) → [`0050c9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c9c4.md) FUN_0050c9c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
        "00bea678",
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
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c9e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c9c4.md#insn-0050c9e8)
- 新版 [`0050c9e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c9c4.md#insn-0050c9e8)

~~~diff
- 0050c9e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 0050c9e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c9e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 0050c9e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c9e8 bytes 293d43f9
+ 0050c9e8 bytes 299543f9
~~~


<a id="compare-862b664560c2e64710259cd8d7272ef6"></a>

### [`0050ca48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050ca48.md) → [`0050ca48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050ca48.md) FUN_0050ca48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "0050ca68",
      "DATA",
      [
        "storage",
        "00be9360",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050ca7c",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ca5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050ca48.md#insn-0050ca5c) · [`0050ca7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050ca48.md#insn-0050ca7c)
- 新版 [`0050ca5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050ca48.md#insn-0050ca5c) · [`0050ca7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050ca48.md#insn-0050ca7c)

~~~diff
- 0050ca5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 0050ca5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050ca5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 0050ca5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ca5c bytes 08a147f9
+ 0050ca5c bytes 08f947f9
- 0050ca7c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 0050ca7c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050ca7c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 0050ca7c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ca7c bytes 293d43f9
+ 0050ca7c bytes 299543f9
~~~


<a id="compare-fe7ce0d06f11ca5c21053919347aa995"></a>

### [`0050cadc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cadc.md) → [`0050cadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cadc.md) FUN_0050cadc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "0050cafc",
      "DATA",
      [
        "storage",
        "00be9360",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050cb10",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050caf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cadc.md#insn-0050caf0) · [`0050cb10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cadc.md#insn-0050cb10)
- 新版 [`0050caf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cadc.md#insn-0050caf0) · [`0050cb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cadc.md#insn-0050cb10)

~~~diff
- 0050caf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 0050caf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050caf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 0050caf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050caf0 bytes 08a147f9
+ 0050caf0 bytes 08f947f9
- 0050cb10 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 0050cb10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cb10 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 0050cb10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cb10 bytes 293d43f9
+ 0050cb10 bytes 299543f9
~~~


<a id="compare-42d3733d41696b853eda66f3be490e1a"></a>

### [`0050cb74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cb74.md) → [`0050cb74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cb74.md) FUN_0050cb74

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "0050cb94",
      "DATA",
      [
        "storage",
        "00be9360",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050cba8",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050cb88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cb74.md#insn-0050cb88) · [`0050cba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cb74.md#insn-0050cba8)
- 新版 [`0050cb88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cb74.md#insn-0050cb88) · [`0050cba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cb74.md#insn-0050cba8)

~~~diff
- 0050cb88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 0050cb88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cb88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 0050cb88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cb88 bytes 08a147f9
+ 0050cb88 bytes 08f947f9
- 0050cba8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:678:8"]]
- 0050cba8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cba8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 0050cba8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cba8 bytes 293d43f9
+ 0050cba8 bytes 299543f9
~~~


<a id="compare-9c160c796a194e581946086a4d79fe92"></a>

### [`0050cc08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cc08.md) → [`0050cc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cc08.md) FUN_0050cc08

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
        "00c1b0a8",
        null,
        "pointer"
      ]
    ],
    [
      "0050cc30",
      "DATA",
      [
        "storage",
        "00beae60",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050cc40",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050cc24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cc08.md#insn-0050cc24) · [`0050cc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cc08.md#insn-0050cc40) · [`0050cc60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cc08.md#insn-0050cc60)
- 新版 [`0050cc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cc08.md#insn-0050cc24) · [`0050cc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cc08.md#insn-0050cc40) · [`0050cc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cc08.md#insn-0050cc60)

~~~diff
- 0050cc24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a8:8"]]
- 0050cc24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cc24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 0050cc24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cc24 bytes 085540f9
+ 0050cc24 bytes 08ad40f9
- 0050cc40 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050cc40 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cc40 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050cc40 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cc40 bytes a93e43f9
+ 0050cc40 bytes a99643f9
- 0050cc60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 0050cc60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cc60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 0050cc60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cc60 bytes 08a147f9
+ 0050cc60 bytes 08f947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f6e2580fcff03a8b1fc135b7c72679f"></a>

### [`0050cce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cce4.md) → [`0050cce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cce4.md) FUN_0050cce4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
        "00c1b0a8",
        null,
        "pointer"
      ]
    ],
    [
      "0050cd0c",
      "DATA",
      [
        "storage",
        "00beae60",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050cd1c",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050cd00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cce4.md#insn-0050cd00) · [`0050cd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cce4.md#insn-0050cd1c) · [`0050cd3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cce4.md#insn-0050cd3c)
- 新版 [`0050cd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cce4.md#insn-0050cd00) · [`0050cd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cce4.md#insn-0050cd1c) · [`0050cd3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cce4.md#insn-0050cd3c)

~~~diff
- 0050cd00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a8:8"]]
- 0050cd00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cd00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 0050cd00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cd00 bytes 085540f9
+ 0050cd00 bytes 08ad40f9
- 0050cd1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050cd1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cd1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050cd1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cd1c bytes a93e43f9
+ 0050cd1c bytes a99643f9
- 0050cd3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 0050cd3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cd3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 0050cd3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cd3c bytes 08a147f9
+ 0050cd3c bytes 08f947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91a1025b7f5c33a64b7a66a8aaadf3a7"></a>

### [`0050cdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cdc8.md) → [`0050cdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cdc8.md) FUN_0050cdc8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
        "00c1b0a8",
        null,
        "pointer"
      ]
    ],
    [
      "0050cdf0",
      "DATA",
      [
        "storage",
        "00beae60",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050ce00",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050cde4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cdc8.md#insn-0050cde4) · [`0050ce00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cdc8.md#insn-0050ce00) · [`0050ce20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cdc8.md#insn-0050ce20)
- 新版 [`0050cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cdc8.md#insn-0050cde4) · [`0050ce00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cdc8.md#insn-0050ce00) · [`0050ce20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cdc8.md#insn-0050ce20)

~~~diff
- 0050cde4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a8:8"]]
- 0050cde4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cde4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 0050cde4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cde4 bytes 085540f9
+ 0050cde4 bytes 08ad40f9
- 0050ce00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050ce00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050ce00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050ce00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ce00 bytes a93e43f9
+ 0050ce00 bytes a99643f9
- 0050ce20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 0050ce20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050ce20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 0050ce20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ce20 bytes 08a147f9
+ 0050ce20 bytes 08f947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7b1503d495f91df7afacbc8854a9307"></a>

### [`0050cf9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cf9c.md) → [`0050cf9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cf9c.md) FUN_0050cf9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "0050cfc0",
      "DATA",
      [
        "storage",
        "00be9418",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050cfa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cf9c.md#insn-0050cfa8) · [`0050cfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cf9c.md#insn-0050cfb0)
- 新版 [`0050cfa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cf9c.md#insn-0050cfa8) · [`0050cfb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cf9c.md#insn-0050cfb0)

~~~diff
- 0050cfa8 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0050cfa8 ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050cfa8 bytes 683800d0
+ 0050cfa8 bytes 683800f0
- 0050cfb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f58:8"]]
- 0050cfb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cfb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
+ 0050cfb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cfb0 bytes 08ad47f9
+ 0050cfb0 bytes 080540f9
~~~


<a id="compare-6a0513f54cf6b8099ca2a182aa265b01"></a>

### [`0050cffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cffc.md) → [`0050cffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cffc.md) FUN_0050cffc

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
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "0050d020",
      "DATA",
      [
        "storage",
        "00be9418",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cffc.md#insn-0050d008) · [`0050d010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050cffc.md#insn-0050d010)
- 新版 [`0050d008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cffc.md#insn-0050d008) · [`0050d010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cffc.md#insn-0050d010)

~~~diff
- 0050d008 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0050d008 ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050d008 bytes 683800b0
+ 0050d008 bytes 683800d0
- 0050d010 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f58:8"]]
- 0050d010 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d010 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
+ 0050d010 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d010 bytes 08ad47f9
+ 0050d010 bytes 080540f9
~~~


<a id="compare-3505a3f02831b739edcea213be4b0f58"></a>

### [`0050d060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d060.md) → [`0050d060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d060.md) FUN_0050d060

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "0050d084",
      "DATA",
      [
        "storage",
        "00be9418",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d06c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d060.md#insn-0050d06c) · [`0050d074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d060.md#insn-0050d074)
- 新版 [`0050d06c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d060.md#insn-0050d06c) · [`0050d074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d060.md#insn-0050d074)

~~~diff
- 0050d06c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0050d06c ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050d06c bytes 683800b0
+ 0050d06c bytes 683800d0
- 0050d074 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f58:8"]]
- 0050d074 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d074 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
+ 0050d074 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d074 bytes 08ad47f9
+ 0050d074 bytes 080540f9
~~~


<a id="compare-abf162277b60766eeb742b34a0197733"></a>

### [`0050d410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d410.md) → [`0050d410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d410.md) FUN_0050d410

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050d4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d4e4.md) · 呼出先 2件 [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`0050d4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d4e4.md) · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "0050d464",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "0050d484",
      "READ",
      [
        "storage",
        "00c1b048",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d410.md#insn-0050d438) · [`0050d464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d410.md#insn-0050d464) · [`0050d484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d410.md#insn-0050d484)
- 新版 [`0050d438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d410.md#insn-0050d438) · [`0050d464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d410.md#insn-0050d464) · [`0050d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d410.md#insn-0050d484)

~~~diff
- 0050d438 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050d438 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d438 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050d438 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d438 bytes a93e43f9
+ 0050d438 bytes a99643f9
- 0050d464 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050d464 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d464 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050d464 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d464 bytes a93e43f9
+ 0050d464 bytes a99643f9
- 0050d484 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 0050d484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d484 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
+ 0050d484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d484 bytes 082540f9
+ 0050d484 bytes 087d40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0eea5a1f8c00348100185345b31cc39"></a>

### [`0050d5a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d5a0.md) → [`0050d5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d5a0.md) FUN_0050d5a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
        "00c1b0d8",
        null,
        "pointer"
      ]
    ],
    [
      "0050d5e4",
      "DATA",
      [
        "storage",
        "00beb470",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d5dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d5a0.md#insn-0050d5dc)
- 新版 [`0050d5dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d5a0.md#insn-0050d5dc)

~~~diff
- 0050d5dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d8:8"]]
- 0050d5dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d5dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:188:8"]]
+ 0050d5dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d5dc bytes 296d40f9
+ 0050d5dc bytes 29c540f9
~~~


<a id="compare-66ddb607c99ad1e0ff6ce0b419966681"></a>

### [`0050d608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d608.md) → [`0050d608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d608.md) FUN_0050d608

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb010.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

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
            "const:e7c:8"
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
            "const:def:8"
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
            "const:286:8"
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
            "const:1f9:8"
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
        "0029b1f9",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d608.md#insn-0050d640) · [`0050d66c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d608.md#insn-0050d66c)
- 新版 [`0050d640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d608.md#insn-0050d640) · [`0050d66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d608.md#insn-0050d66c)

~~~diff
- 0050d640 ["COPY", "tmp:0:8", ["const:def:8"]]
- 0050d640 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0050d640 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0050d640 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0050d640 ["COPY", "tmp:0:8", ["const:e7c:8"]]
+ 0050d640 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0050d640 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0050d640 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0050d640 bytes 42bc3791
+ 0050d640 bytes 42f03991
- 0050d66c ["COPY", "tmp:0:8", ["const:1f9:8"]]
- 0050d66c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0050d66c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0050d66c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0050d66c ["COPY", "tmp:0:8", ["const:286:8"]]
+ 0050d66c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0050d66c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0050d66c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0050d66c bytes 21e40791
+ 0050d66c bytes 21180a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f9af84b4b4cda0b6ceb6b0db880482c"></a>

### [`0050d78c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d78c.md) → [`0050d78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d78c.md) FUN_0050d78c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00c1b0e8",
        null,
        "pointer"
      ]
    ],
    [
      "0050d7b4",
      "DATA",
      [
        "storage",
        "00be9fe8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "0050d7c4",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d7a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d78c.md#insn-0050d7a8) · [`0050d7c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d78c.md#insn-0050d7c4) · [`0050d7f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d78c.md#insn-0050d7f0)
- 新版 [`0050d7a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d78c.md#insn-0050d7a8) · [`0050d7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d78c.md#insn-0050d7c4) · [`0050d7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d78c.md#insn-0050d7f0)

~~~diff
- 0050d7a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e8:8"]]
- 0050d7a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d7a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:198:8"]]
+ 0050d7a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d7a8 bytes 087540f9
+ 0050d7a8 bytes 08cd40f9
- 0050d7c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050d7c4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d7c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050d7c4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d7c4 bytes a93e43f9
+ 0050d7c4 bytes a99643f9
- 0050d7f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050d7f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d7f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050d7f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d7f0 bytes a93e43f9
+ 0050d7f0 bytes a99643f9
~~~


<a id="compare-1a8df3054a46d3d8b8459515f60994ad"></a>

### [`0050d830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d830.md) → [`0050d830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d830.md) FUN_0050d830

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00c1b0e8",
        null,
        "pointer"
      ]
    ],
    [
      "0050d858",
      "DATA",
      [
        "storage",
        "00be9fe8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "0050d868",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d84c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d830.md#insn-0050d84c) · [`0050d868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d830.md#insn-0050d868) · [`0050d894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d830.md#insn-0050d894)
- 新版 [`0050d84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d830.md#insn-0050d84c) · [`0050d868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d830.md#insn-0050d868) · [`0050d894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d830.md#insn-0050d894)

~~~diff
- 0050d84c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e8:8"]]
- 0050d84c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d84c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:198:8"]]
+ 0050d84c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d84c bytes 087540f9
+ 0050d84c bytes 08cd40f9
- 0050d868 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050d868 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d868 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050d868 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d868 bytes a93e43f9
+ 0050d868 bytes a99643f9
- 0050d894 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050d894 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d894 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050d894 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d894 bytes a93e43f9
+ 0050d894 bytes a99643f9
~~~


<a id="compare-1fc5ab74863418eb736cb85a4571c379"></a>

### [`0050d8f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d8f4.md) → [`0050d8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d8f4.md) FUN_0050d8f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`004a4d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004a4/004a4d4c.md) [`004a4d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004a4/004a4d88.md) [`0050d9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d9e0.md) [`0050da6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050da6c.md) [`0050da74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050da74.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 6件 [`004a4d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4d4c.md) [`004a4d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4d88.md) [`0050d9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d9e0.md) [`0050da6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050da6c.md) [`0050da74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050da74.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00c1af80",
        null,
        "pointer"
      ]
    ],
    [
      "0050d930",
      "DATA",
      [
        "storage",
        "00be9918",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050d950",
      "READ",
      [
        "storage",
        "00bea678",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d91c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d8f4.md#insn-0050d91c) · [`0050d920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d8f4.md#insn-0050d920) · [`0050d950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d8f4.md#insn-0050d950)
- 新版 [`0050d91c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d8f4.md#insn-0050d91c) · [`0050d920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d8f4.md#insn-0050d920) · [`0050d950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d8f4.md#insn-0050d950)

~~~diff
- 0050d91c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0050d91c ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050d91c bytes 683800b0
+ 0050d91c bytes 683800d0
- 0050d920 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f80:8"]]
- 0050d920 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d920 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
+ 0050d920 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d920 bytes 08c147f9
+ 0050d920 bytes 081940f9
- 0050d950 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 0050d950 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d950 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
+ 0050d950 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d950 bytes c93e43f9
+ 0050d950 bytes c99643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b76105496eb6e6ff4be64cbc4243325e"></a>

### [`0050da9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050da9c.md) → [`0050da9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050da9c.md) FUN_0050da9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050db70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050db70.md) · 呼出先 2件 [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`0050db70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050db70.md) · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "0050daf0",
      "READ",
      [
        "storage",
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "0050db10",
      "READ",
      [
        "storage",
        "00c1b048",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050dac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050da9c.md#insn-0050dac4) · [`0050daf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050da9c.md#insn-0050daf0) · [`0050db10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050da9c.md#insn-0050db10)
- 新版 [`0050dac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050da9c.md#insn-0050dac4) · [`0050daf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050da9c.md#insn-0050daf0) · [`0050db10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050da9c.md#insn-0050db10)

~~~diff
- 0050dac4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050dac4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050dac4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050dac4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dac4 bytes a93e43f9
+ 0050dac4 bytes a99643f9
- 0050daf0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050daf0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050daf0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050daf0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050daf0 bytes a93e43f9
+ 0050daf0 bytes a99643f9
- 0050db10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 0050db10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050db10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
+ 0050db10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050db10 bytes 082540f9
+ 0050db10 bytes 087d40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33edf6c643d18a3dbe22c9b83ccc2497"></a>

### [`0050dbfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dbfc.md) → [`0050dbfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dbfc.md) FUN_0050dbfc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "0050dc44",
      "READ",
      [
        "storage",
        "00c1b048",
        null,
        "pointer"
      ]
    ],
    [
      "0050dc50",
      "DATA",
      [
        "storage",
        "00be9c18",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050dc24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dbfc.md#insn-0050dc24) · [`0050dc44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dbfc.md#insn-0050dc44) · [`0050dc60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dbfc.md#insn-0050dc60)
- 新版 [`0050dc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dbfc.md#insn-0050dc24) · [`0050dc44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dbfc.md#insn-0050dc44) · [`0050dc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dbfc.md#insn-0050dc60)

~~~diff
- 0050dc24 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050dc24 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050dc24 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050dc24 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dc24 bytes a93e43f9
+ 0050dc24 bytes a99643f9
- 0050dc44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 0050dc44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050dc44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
+ 0050dc44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dc44 bytes 082540f9
+ 0050dc44 bytes 087d40f9
- 0050dc60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050dc60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050dc60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050dc60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dc60 bytes a93e43f9
+ 0050dc60 bytes a99643f9
~~~


<a id="compare-bf523ad8c8e3de7f689f0cd8860ba396"></a>

### [`0050dca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dca0.md) → [`0050dca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dca0.md) FUN_0050dca0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "0050dce8",
      "READ",
      [
        "storage",
        "00c1b048",
        null,
        "pointer"
      ]
    ],
    [
      "0050dcf4",
      "DATA",
      [
        "storage",
        "00be9c18",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050dcc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dca0.md#insn-0050dcc8) · [`0050dce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dca0.md#insn-0050dce8) · [`0050dd04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dca0.md#insn-0050dd04)
- 新版 [`0050dcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dca0.md#insn-0050dcc8) · [`0050dce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dca0.md#insn-0050dce8) · [`0050dd04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dca0.md#insn-0050dd04)

~~~diff
- 0050dcc8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050dcc8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050dcc8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050dcc8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dcc8 bytes a93e43f9
+ 0050dcc8 bytes a99643f9
- 0050dce8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 0050dce8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050dce8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
+ 0050dce8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dce8 bytes 082540f9
+ 0050dce8 bytes 087d40f9
- 0050dd04 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050dd04 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050dd04 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050dd04 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dd04 bytes a93e43f9
+ 0050dd04 bytes a99643f9
~~~


<a id="compare-bbb93a54c54b3c1b325eaf2a61fe03b4"></a>

### [`0050dda4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dda4.md) → [`0050dda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dda4.md) FUN_0050dda4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "0050ddec",
      "READ",
      [
        "storage",
        "00c1b048",
        null,
        "pointer"
      ]
    ],
    [
      "0050ddf8",
      "DATA",
      [
        "storage",
        "00be9c18",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ddcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dda4.md#insn-0050ddcc) · [`0050ddec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dda4.md#insn-0050ddec) · [`0050de08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dda4.md#insn-0050de08)
- 新版 [`0050ddcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dda4.md#insn-0050ddcc) · [`0050ddec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dda4.md#insn-0050ddec) · [`0050de08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dda4.md#insn-0050de08)

~~~diff
- 0050ddcc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050ddcc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050ddcc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050ddcc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ddcc bytes a93e43f9
+ 0050ddcc bytes a99643f9
- 0050ddec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 0050ddec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050ddec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
+ 0050ddec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ddec bytes 082540f9
+ 0050ddec bytes 087d40f9
- 0050de08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050de08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050de08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050de08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050de08 bytes a93e43f9
+ 0050de08 bytes a99643f9
~~~


<a id="compare-c45922f0e3924e57ea8ad97aa6373e18"></a>

### [`0050de48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050de48.md) → [`0050de48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050de48.md) FUN_0050de48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`010a5058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)

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
                "const:728:8"
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
                "const:678:8"
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
                "const:728:8"
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
                "const:678:8"
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
        "00bea678",
        null,
        "pointer"
      ]
    ],
    [
      "0050de90",
      "READ",
      [
        "storage",
        "00c1b048",
        null,
        "pointer"
      ]
    ],
    [
      "0050de9c",
      "DATA",
      [
        "storage",
        "00be9c18",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050de70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050de48.md#insn-0050de70) · [`0050de90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050de48.md#insn-0050de90) · [`0050deac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050de48.md#insn-0050deac)
- 新版 [`0050de70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050de48.md#insn-0050de70) · [`0050de90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050de48.md#insn-0050de90) · [`0050deac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050de48.md#insn-0050deac)

~~~diff
- 0050de70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050de70 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050de70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050de70 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050de70 bytes a93e43f9
+ 0050de70 bytes a99643f9
- 0050de90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 0050de90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050de90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
+ 0050de90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050de90 bytes 082540f9
+ 0050de90 bytes 087d40f9
- 0050deac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 0050deac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050deac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
+ 0050deac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050deac bytes a93e43f9
+ 0050deac bytes a99643f9
~~~


<a id="compare-8b9e7c5319082897c8047ead9cdd78a9"></a>

### [`0050dfd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dfd4.md) → [`0050dfd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dfd4.md) FUN_0050dfd4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

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
                "const:6ec:8"
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
                "const:6f3:8"
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
        "002a66f3",
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
        "002a66ec",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050dff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dfd4.md#insn-0050dff0)
- 新版 [`0050dff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dfd4.md#insn-0050dff0)

~~~diff
- 0050dff0 ["COPY", "tmp:0:8", ["const:6f3:8"]]
- 0050dff0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050dff0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050dff0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050dff0 ["COPY", "tmp:0:8", ["const:6ec:8"]]
+ 0050dff0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050dff0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050dff0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050dff0 bytes 29cd1b91
+ 0050dff0 bytes 29b11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4240c887e853dc3621d2fb527ac5ebd0"></a>

### [`0050e0cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e0cc.md) → [`0050e0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e0cc.md) FUN_0050e0cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
        "00c1b298",
        null,
        "pointer"
      ]
    ],
    [
      "0050e0fc",
      "DATA",
      [
        "storage",
        "00bea890",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e0ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e0cc.md#insn-0050e0ec)
- 新版 [`0050e0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e0cc.md#insn-0050e0ec)

~~~diff
- 0050e0ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:298:8"]]
- 0050e0ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050e0ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:348:8"]]
+ 0050e0ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e0ec bytes 294d41f9
+ 0050e0ec bytes 29a541f9
~~~


<a id="compare-c56c205b3c9ea8c6f94c2a1a40b1dfe6"></a>

### [`0050e114`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e114.md) → [`0050e114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e114.md) FUN_0050e114

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

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
                "const:38d:8"
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
                "const:300:8"
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
        "0029e300",
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
        "0029e38d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e114.md#insn-0050e130)
- 新版 [`0050e130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e114.md#insn-0050e130)

~~~diff
- 0050e130 ["COPY", "tmp:0:8", ["const:300:8"]]
- 0050e130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050e130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050e130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050e130 ["COPY", "tmp:0:8", ["const:38d:8"]]
+ 0050e130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050e130 bytes 29010c91
+ 0050e130 bytes 29350e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5448d21075db5cf8a5d9f13bd11834f"></a>

### [`0050e1bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e1bc.md) → [`0050e1bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e1bc.md) FUN_0050e1bc

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
                "const:c41:8"
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
  ],
  "added": [
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e1c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e1bc.md#insn-0050e1c4)
- 新版 [`0050e1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e1bc.md#insn-0050e1c4)

~~~diff
- 0050e1c4 ["COPY", "tmp:0:8", ["const:bb4:8"]]
- 0050e1c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050e1c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050e1c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0050e1c4 ["COPY", "tmp:0:8", ["const:c41:8"]]
+ 0050e1c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0050e1c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0050e1c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050e1c4 bytes 4ad12e91
+ 0050e1c4 bytes 4a053191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f8ec20574fff9e94a2207b2f3055610"></a>

### [`0050e234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e234.md) → [`0050e234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e234.md) FUN_0050e234

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

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
                "const:3d3:8"
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
                "const:3da:8"
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
        "002a43da",
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
        "002a43d3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e234.md#insn-0050e250)
- 新版 [`0050e250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e234.md#insn-0050e250)

~~~diff
- 0050e250 ["COPY", "tmp:0:8", ["const:3da:8"]]
- 0050e250 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050e250 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050e250 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050e250 ["COPY", "tmp:0:8", ["const:3d3:8"]]
+ 0050e250 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e250 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e250 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050e250 bytes 29690f91
+ 0050e250 bytes 294d0f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d97e518cfbc375f9a8ab55fb0199a12"></a>

### [`0050e2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e2dc.md) → [`0050e2dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e2dc.md) FUN_0050e2dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
                "const:2a9:8"
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
                "const:21c:8"
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
        "002a221c",
        null,
        "string"
      ]
    ],
    [
      "0050e304",
      "READ",
      [
        "storage",
        "002a2227",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e2f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e2dc.md#insn-0050e2f8) · [`0050e2fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e2dc.md#insn-0050e2fc)
- 新版 [`0050e2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e2dc.md#insn-0050e2f8) · [`0050e2fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e2dc.md#insn-0050e2fc)

~~~diff
- 0050e2f8 ["COPY", "tmp:0:8", ["const:21c:8"]]
- 0050e2f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050e2f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050e2f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050e2f8 ["COPY", "tmp:0:8", ["const:2a9:8"]]
+ 0050e2f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050e2f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050e2f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050e2f8 bytes 08710891
+ 0050e2f8 bytes 08a50a91
- 0050e2fc ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0050e2fc bytes 09edfff0
+ 0050e2fc ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0050e2fc bytes 09edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5de8862cedf97e311b4480e30bf3ebc1"></a>

### [`0050e32c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e32c.md) → [`0050e32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e32c.md) FUN_0050e32c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

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
        "00c1b2c0",
        null,
        "pointer"
      ]
    ],
    [
      "0050e36c",
      "DATA",
      [
        "storage",
        "00bea968",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e32c.md#insn-0050e350)
- 新版 [`0050e350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e32c.md#insn-0050e350)

~~~diff
- 0050e350 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c0:8"]]
- 0050e350 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050e350 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 0050e350 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e350 bytes 086141f9
+ 0050e350 bytes 08b941f9
~~~


<a id="compare-87ec088768bf85178f680eafd8671756"></a>

### [`0050e43c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e43c.md) → [`0050e43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e43c.md) FUN_0050e43c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

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
                "const:7ad:8"
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
      "0050e464",
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
      "0050e464",
      "READ",
      [
        "storage",
        "002947ad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e43c.md#insn-0050e458)
- 新版 [`0050e458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e43c.md#insn-0050e458)

~~~diff
- 0050e458 ["COPY", "tmp:0:8", ["const:720:8"]]
- 0050e458 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050e458 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050e458 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050e458 ["COPY", "tmp:0:8", ["const:7ad:8"]]
+ 0050e458 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e458 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e458 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050e458 bytes 29811c91
+ 0050e458 bytes 29b51e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e8481b306dc3d987d9985a2a7151ef4"></a>

### [`0050e4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e4e4.md) → [`0050e4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e4e4.md) FUN_0050e4e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0050e508",
      "incomplete_value": true,
      "site": "0050e518",
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
                "const:584:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e508",
      "incomplete_value": true,
      "site": "0050e518",
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
                "const:57e:8"
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
      "definition_site": "0050e50c",
      "incomplete_value": true,
      "site": "0050e51c",
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
      "definition_site": "0050e50c",
      "incomplete_value": true,
      "site": "0050e51c",
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
      "0050e508",
      "READ",
      [
        "storage",
        "002ab57e",
        null,
        "string"
      ]
    ],
    [
      "0050e50c",
      "READ",
      [
        "storage",
        "002ab58b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050e508",
      "READ",
      [
        "storage",
        "002ab584",
        null,
        "string"
      ]
    ],
    [
      "0050e50c",
      "READ",
      [
        "storage",
        "002ab591",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e4e4.md#insn-0050e500) · [`0050e504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e4e4.md#insn-0050e504)
- 新版 [`0050e500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e4e4.md#insn-0050e500) · [`0050e504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e4e4.md#insn-0050e504)

~~~diff
- 0050e500 ["COPY", "tmp:0:8", ["const:57e:8"]]
- 0050e500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050e500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050e500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050e500 ["COPY", "tmp:0:8", ["const:584:8"]]
+ 0050e500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050e500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050e500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050e500 bytes 08f91591
+ 0050e500 bytes 08111691
- 0050e504 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0050e504 bytes 09edfff0
+ 0050e504 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0050e504 bytes 09edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90894094236fd852813f38f533b38135"></a>

### [`0050e534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e534.md) → [`0050e534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e534.md) FUN_0050e534

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

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
        "00c1b2a0",
        null,
        "pointer"
      ]
    ],
    [
      "0050e574",
      "DATA",
      [
        "storage",
        "00beb900",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e534.md#insn-0050e558)
- 新版 [`0050e558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e534.md#insn-0050e558)

~~~diff
- 0050e558 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
- 0050e558 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050e558 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
+ 0050e558 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e558 bytes 085141f9
+ 0050e558 bytes 08a941f9
~~~


<a id="compare-e6caec404e58ddaf045ed698c1d140ce"></a>

### [`0050e67c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e67c.md) → [`0050e67c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e67c.md) FUN_0050e67c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

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
                "const:55e:8"
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
      "0050e6a4",
      "READ",
      [
        "storage",
        "002aa55e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050e6a4",
      "READ",
      [
        "storage",
        "002aa564",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e67c.md#insn-0050e698)
- 新版 [`0050e698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e67c.md#insn-0050e698)

~~~diff
- 0050e698 ["COPY", "tmp:0:8", ["const:55e:8"]]
- 0050e698 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050e698 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050e698 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050e698 ["COPY", "tmp:0:8", ["const:564:8"]]
+ 0050e698 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e698 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e698 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050e698 bytes 29791591
+ 0050e698 bytes 29911591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be31caf2e9d24b65ac7c85e7a8928a01"></a>

### [`0050e724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e724.md) → [`0050e724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e724.md) FUN_0050e724

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
                "const:78f:8"
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
                "const:702:8"
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
  ],
  "added": [
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e724.md#insn-0050e740) · [`0050e744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e724.md#insn-0050e744)
- 新版 [`0050e740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e724.md#insn-0050e740) · [`0050e744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e724.md#insn-0050e744)

~~~diff
- 0050e740 ["COPY", "tmp:0:8", ["const:702:8"]]
- 0050e740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050e740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050e740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050e740 ["COPY", "tmp:0:8", ["const:78f:8"]]
+ 0050e740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050e740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050e740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050e740 bytes 08091c91
+ 0050e740 bytes 083d1e91
- 0050e744 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0050e744 bytes 09edfff0
+ 0050e744 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0050e744 bytes 09edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6d414224d1edbb16262c1eab1ac9bd7"></a>

### [`0050e774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e774.md) → [`0050e774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e774.md) FUN_0050e774

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00519a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00519/00519a68.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00519a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00519/00519a68.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
        "00c1b2a8",
        null,
        "pointer"
      ]
    ],
    [
      "0050e79c",
      "DATA",
      [
        "storage",
        "00beb990",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e774.md#insn-0050e794)
- 新版 [`0050e794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e774.md#insn-0050e794)

~~~diff
- 0050e794 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a8:8"]]
- 0050e794 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050e794 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:358:8"]]
+ 0050e794 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e794 bytes 085541f9
+ 0050e794 bytes 08ad41f9
~~~


<a id="compare-c1a78cfa3459089d676da54abc5340ec"></a>

### [`0050e84c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e84c.md) → [`0050e84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e84c.md) FUN_0050e84c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

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
                "const:80c:8"
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
                "const:77f:8"
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
        "0029277f",
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
        "0029280c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e84c.md#insn-0050e868)
- 新版 [`0050e868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e84c.md#insn-0050e868)

~~~diff
- 0050e868 ["COPY", "tmp:0:8", ["const:77f:8"]]
- 0050e868 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050e868 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050e868 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050e868 ["COPY", "tmp:0:8", ["const:80c:8"]]
+ 0050e868 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e868 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e868 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050e868 bytes 29fd1d91
+ 0050e868 bytes 29312091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3636f7d18e94d6a9f6c72679f0a6bc83"></a>

### [`0050e8f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e8f4.md) → [`0050e8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e8f4.md) FUN_0050e8f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0050e918",
      "incomplete_value": true,
      "site": "0050e928",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:7ac:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e918",
      "incomplete_value": true,
      "site": "0050e928",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:7b5:8"
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
      "definition_site": "0050e91c",
      "incomplete_value": true,
      "site": "0050e92c",
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
      "definition_site": "0050e91c",
      "incomplete_value": true,
      "site": "0050e92c",
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
      "0050e918",
      "READ",
      [
        "storage",
        "002ac7b5",
        null,
        "string"
      ]
    ],
    [
      "0050e91c",
      "READ",
      [
        "storage",
        "002ac7c1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050e918",
      "READ",
      [
        "storage",
        "002ac7ac",
        null,
        "string"
      ]
    ],
    [
      "0050e91c",
      "READ",
      [
        "storage",
        "002ac7b8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e8f4.md#insn-0050e910) · [`0050e914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e8f4.md#insn-0050e914)
- 新版 [`0050e910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e8f4.md#insn-0050e910) · [`0050e914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e8f4.md#insn-0050e914)

~~~diff
- 0050e910 ["COPY", "tmp:0:8", ["const:7b5:8"]]
- 0050e910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050e910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050e910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050e910 ["COPY", "tmp:0:8", ["const:7ac:8"]]
+ 0050e910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050e910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050e910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050e910 bytes 08d51e91
+ 0050e910 bytes 08b11e91
- 0050e914 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0050e914 bytes 09edfff0
+ 0050e914 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0050e914 bytes 09edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28e631bbc710c4f6d034c74b7d925c2a"></a>

### [`0050e944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e944.md) → [`0050e944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e944.md) FUN_0050e944

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00519a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00519/00519a68.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00519a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00519/00519a68.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
        "00c1b2c8",
        null,
        "pointer"
      ]
    ],
    [
      "0050e96c",
      "DATA",
      [
        "storage",
        "00beba08",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e944.md#insn-0050e964)
- 新版 [`0050e964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e944.md#insn-0050e964)

~~~diff
- 0050e964 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c8:8"]]
- 0050e964 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050e964 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:378:8"]]
+ 0050e964 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e964 bytes 086541f9
+ 0050e964 bytes 08bd41f9
~~~


<a id="compare-1e2efc74073f6236e5b8eae15ee9b3da"></a>

### [`0050ea1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050ea1c.md) → [`0050ea1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ea1c.md) FUN_0050ea1c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

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
                "const:36b:8"
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
                "const:2de:8"
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
        "0029b2de",
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
        "0029b36b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ea38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050ea1c.md#insn-0050ea38)
- 新版 [`0050ea38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ea1c.md#insn-0050ea38)

~~~diff
- 0050ea38 ["COPY", "tmp:0:8", ["const:2de:8"]]
- 0050ea38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050ea38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050ea38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050ea38 ["COPY", "tmp:0:8", ["const:36b:8"]]
+ 0050ea38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050ea38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050ea38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050ea38 bytes 29790b91
+ 0050ea38 bytes 29ad0d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4374e9e33cf01a9ff8d29ee796656b9"></a>

### [`0050eac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050eac4.md) → [`0050eac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050eac4.md) FUN_0050eac4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
                "const:47c:8"
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
                "const:510:8"
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
        "002a9510",
        null,
        "string"
      ]
    ],
    [
      "0050eaec",
      "READ",
      [
        "storage",
        "002a951f",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050eae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050eac4.md#insn-0050eae0) · [`0050eae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050eac4.md#insn-0050eae4)
- 新版 [`0050eae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050eac4.md#insn-0050eae0) · [`0050eae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050eac4.md#insn-0050eae4)

~~~diff
- 0050eae0 ["COPY", "tmp:0:8", ["const:510:8"]]
- 0050eae0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050eae0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050eae0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050eae0 ["COPY", "tmp:0:8", ["const:47c:8"]]
+ 0050eae0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050eae0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050eae0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050eae0 bytes 08411491
+ 0050eae0 bytes 08f11191
- 0050eae4 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0050eae4 bytes 09edffd0
+ 0050eae4 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0050eae4 bytes 09edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0416f79d9ee49c2da4f5cebad7b42fa"></a>

### [`0050eb14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050eb14.md) → [`0050eb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050eb14.md) FUN_0050eb14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0051bf98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d7fc.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0051bf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d7fc.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
        "00c1b290",
        null,
        "pointer"
      ]
    ],
    [
      "0050eb6c",
      "DATA",
      [
        "storage",
        "00bea830",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050eb54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050eb14.md#insn-0050eb54)
- 新版 [`0050eb54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050eb14.md#insn-0050eb54)

~~~diff
- 0050eb54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 0050eb54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050eb54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:340:8"]]
+ 0050eb54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050eb54 bytes 084941f9
+ 0050eb54 bytes 08a141f9
~~~


<a id="compare-fe43ead0338596b29b52c41c3b239b3e"></a>

### [`0050edd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050edd4.md) → [`0050edd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050edd4.md) FUN_0050edd4

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
                "const:a07:8"
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
  ],
  "added": [
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050eddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050edd4.md#insn-0050eddc)
- 新版 [`0050eddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050edd4.md#insn-0050eddc)

~~~diff
- 0050eddc ["COPY", "tmp:0:8", ["const:97a:8"]]
- 0050eddc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050eddc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050eddc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0050eddc ["COPY", "tmp:0:8", ["const:a07:8"]]
+ 0050eddc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0050eddc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0050eddc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050eddc bytes 4ae92591
+ 0050eddc bytes 4a1d2891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9a6a7d25f04c7990c21a01ec395e83f"></a>

### [`0050edfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050edfc.md) → [`0050edfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050edfc.md) FUN_0050edfc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051ca38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051c/0051ca38.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0051ca38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051ca38.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
        "00c1b2d0",
        null,
        "pointer"
      ]
    ],
    [
      "0050ee24",
      "DATA",
      [
        "storage",
        "00beba98",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ee1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050edfc.md#insn-0050ee1c)
- 新版 [`0050ee1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050edfc.md#insn-0050ee1c)

~~~diff
- 0050ee1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2d0:8"]]
- 0050ee1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050ee1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:380:8"]]
+ 0050ee1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ee1c bytes 086941f9
+ 0050ee1c bytes 08c141f9
~~~


<a id="compare-351160995ab89e2932a258001e8ee3bd"></a>

### [`0050ee8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050ee8c.md) → [`0050ee8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ee8c.md) FUN_0050ee8c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb740.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)

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
                "const:3ec:8"
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
                "const:35f:8"
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
        "0029d35f",
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
        "0029d3ec",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050eea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050ee8c.md#insn-0050eea8)
- 新版 [`0050eea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ee8c.md#insn-0050eea8)

~~~diff
- 0050eea8 ["COPY", "tmp:0:8", ["const:35f:8"]]
- 0050eea8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050eea8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050eea8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050eea8 ["COPY", "tmp:0:8", ["const:3ec:8"]]
+ 0050eea8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050eea8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050eea8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050eea8 bytes 297d0d91
+ 0050eea8 bytes 29b10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66446ae440dd4095a6d0869d64aa2e79"></a>

### [`0050ef34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050ef34.md) → [`0050ef34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ef34.md) FUN_0050ef34

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
                "const:397:8"
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
                "const:30a:8"
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
        "0029e30a",
        null,
        "string"
      ]
    ],
    [
      "0050ef5c",
      "READ",
      [
        "storage",
        "0029e314",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ef50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050ef34.md#insn-0050ef50) · [`0050ef54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050ef34.md#insn-0050ef54)
- 新版 [`0050ef50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ef34.md#insn-0050ef50) · [`0050ef54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ef34.md#insn-0050ef54)

~~~diff
- 0050ef50 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0050ef50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050ef50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050ef50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050ef50 ["COPY", "tmp:0:8", ["const:397:8"]]
+ 0050ef50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050ef50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050ef50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050ef50 bytes 08290c91
+ 0050ef50 bytes 085d0e91
- 0050ef54 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0050ef54 bytes 09edfff0
+ 0050ef54 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0050ef54 bytes 09edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75c7ec393061dff103024734723c7db2"></a>

### [`0050ef84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050ef84.md) → [`0050ef84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ef84.md) FUN_0050ef84

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0051bf98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d7fc.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0051bf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d7fc.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "0050efdc",
      "DATA",
      [
        "storage",
        "00bebb10",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050efc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050ef84.md#insn-0050efc4)
- 新版 [`0050efc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ef84.md#insn-0050efc4)

~~~diff
- 0050efc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
- 0050efc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050efc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
+ 0050efc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050efc4 bytes 087141f9
+ 0050efc4 bytes 08c941f9
~~~


