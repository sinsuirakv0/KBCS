# v15.7.2 → v15.7.3 · 最優先の変更候補 (75)

[一覧の目次](README.md)

<a id="compare-30e72d6268c8f32d248e1455b5f88a9f"></a>

### [`00b7d530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d530.md) → [`00b7d5f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d5f8.md) _ZNSt6__ndk121recursive_timed_mutexD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdaf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf10.md) [`00bdb180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb180.md) [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)

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
    "old": {
      "definition_site": "00b7d574",
      "incomplete_value": false,
      "site": "00b7d578",
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
            "const:ffa:8"
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
      "00b7d63c",
      "PARAM",
      [
        "storage",
        "002a0ffa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d63c",
      "PARAM",
      [
        "storage",
        "002a1087",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d530.md#insn-00b7d578) · [`00b7d544`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d530.md#insn-00b7d544) · [`00b7d550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d530.md#insn-00b7d550)
- 新版 `00b7d640`（命令位置の公開資料なし） · `00b7d60c`（命令位置の公開資料なし） · `00b7d618`（命令位置の公開資料なし）

~~~diff
- 00b7d578 ["INT_ADD", "register:40f0:8", ["const:b7d578:8", "const:4:8"]]
- 00b7d578 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7d640 ["INT_ADD", "register:40f0:8", ["const:b7d640:8", "const:4:8"]]
+ 00b7d640 ["CALL", null, ["callee:00bdb280:8"]]
- 00b7d578 bytes 16770194
+ 00b7d640 bytes 10770194
- 00b7d544 ["INT_ADD", "register:40f0:8", ["const:b7d544:8", "const:4:8"]]
- 00b7d544 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00b7d60c ["INT_ADD", "register:40f0:8", ["const:b7d60c:8", "const:4:8"]]
+ 00b7d60c ["CALL", null, ["callee:00bde7d0:8"]]
- 00b7d544 bytes 77840194
+ 00b7d60c bytes 71840194
- 00b7d550 ["INT_ADD", "register:40f0:8", ["const:b7d550:8", "const:4:8"]]
- 00b7d550 ["CALL", null, ["callee:00bde7e0:8"]]
+ 00b7d618 ["INT_ADD", "register:40f0:8", ["const:b7d618:8", "const:4:8"]]
+ 00b7d618 ["CALL", null, ["callee:00bde7e0:8"]]
- 00b7d550 bytes 78840194
+ 00b7d618 bytes 72840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eda85fd88ac1ee401337208d936a8489"></a>

### [`00b7d584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d584.md) → [`00b7d64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d64c.md) _ZNSt6__ndk121recursive_timed_mutex4lockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00bdb530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb530.md) [`00bdb6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6d0.md) [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdb5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5e0.md) [`00bdb780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb780.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)

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
    "old": {
      "definition_site": "00b7d630",
      "incomplete_value": false,
      "site": "00b7d634",
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
            "const:ffa:8"
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
    "old": {
      "definition_site": "00b7d63c",
      "incomplete_value": false,
      "site": "00b7d644",
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
      "00b7d6f8",
      "PARAM",
      [
        "storage",
        "002a0ffa",
        null,
        "string"
      ]
    ],
    [
      "00b7d704",
      "PARAM",
      [
        "storage",
        "002943e4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d6f8",
      "PARAM",
      [
        "storage",
        "002a1087",
        null,
        "string"
      ]
    ],
    [
      "00b7d704",
      "PARAM",
      [
        "storage",
        "00294471",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d584.md#insn-00b7d634) · [`00b7d644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d584.md#insn-00b7d644) · [`00b7d59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d584.md#insn-00b7d59c)
- 新版 `00b7d6fc`（命令位置の公開資料なし） · `00b7d70c`（命令位置の公開資料なし） · `00b7d664`（命令位置の公開資料なし）

~~~diff
- 00b7d634 ["INT_ADD", "register:40f0:8", ["const:b7d634:8", "const:4:8"]]
- 00b7d634 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7d6fc ["INT_ADD", "register:40f0:8", ["const:b7d6fc:8", "const:4:8"]]
+ 00b7d6fc ["CALL", null, ["callee:00bdb280:8"]]
- 00b7d634 bytes e7760194
+ 00b7d6fc bytes e1760194
- 00b7d644 ["INT_ADD", "register:40f0:8", ["const:b7d644:8", "const:4:8"]]
- 00b7d644 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7d70c ["INT_ADD", "register:40f0:8", ["const:b7d70c:8", "const:4:8"]]
+ 00b7d70c ["CALL", null, ["callee:00bdb280:8"]]
- 00b7d644 bytes e3760194
+ 00b7d70c bytes dd760194
- 00b7d59c ["INT_ADD", "register:40f0:8", ["const:b7d59c:8", "const:4:8"]]
- 00b7d59c ["CALL", null, ["callee:00bdb780:8"]]
+ 00b7d664 ["INT_ADD", "register:40f0:8", ["const:b7d664:8", "const:4:8"]]
+ 00b7d664 ["CALL", null, ["callee:00bdb780:8"]]
- 00b7d59c bytes 4d780194
+ 00b7d664 bytes 47780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e9f7290b4648a8d67a3618983478882"></a>

### [`00b7d6ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d6ec.md) → [`00b7d7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d7b4.md) _ZNSt6__ndk121recursive_timed_mutex6unlockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00bdc1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc1c0.md) [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdc270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc270.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)

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
    "old": {
      "definition_site": "00b7d754",
      "incomplete_value": false,
      "site": "00b7d758",
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
            "const:ffa:8"
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
      "00b7d81c",
      "PARAM",
      [
        "storage",
        "002a0ffa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d81c",
      "PARAM",
      [
        "storage",
        "002a1087",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d6ec.md#insn-00b7d758) · [`00b7d700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d6ec.md#insn-00b7d700) · [`00b7d71c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d6ec.md#insn-00b7d71c)
- 新版 `00b7d820`（命令位置の公開資料なし） · `00b7d7c8`（命令位置の公開資料なし） · `00b7d7e4`（命令位置の公開資料なし）

~~~diff
- 00b7d758 ["INT_ADD", "register:40f0:8", ["const:b7d758:8", "const:4:8"]]
- 00b7d758 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7d820 ["INT_ADD", "register:40f0:8", ["const:b7d820:8", "const:4:8"]]
+ 00b7d820 ["CALL", null, ["callee:00bdb280:8"]]
- 00b7d758 bytes 9e760194
+ 00b7d820 bytes 98760194
- 00b7d700 ["INT_ADD", "register:40f0:8", ["const:b7d700:8", "const:4:8"]]
- 00b7d700 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00b7d7c8 ["INT_ADD", "register:40f0:8", ["const:b7d7c8:8", "const:4:8"]]
+ 00b7d7c8 ["CALL", null, ["callee:00bde7d0:8"]]
- 00b7d700 bytes 08840194
+ 00b7d7c8 bytes 02840194
- 00b7d71c ["INT_ADD", "register:40f0:8", ["const:b7d71c:8", "const:4:8"]]
- 00b7d71c ["CALL", null, ["callee:00bde7e0:8"]]
+ 00b7d7e4 ["INT_ADD", "register:40f0:8", ["const:b7d7e4:8", "const:4:8"]]
+ 00b7d7e4 ["CALL", null, ["callee:00bde7e0:8"]]
- 00b7d71c bytes 05840194
+ 00b7d7e4 bytes ff830194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a91d394629a17c76642358d3184b692"></a>

### [`00b7d788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d788.md) → [`00b7d850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d850.md) _ZNSt6__ndk16thread4joinEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb220.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00be0560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0560.md)
- 新版 呼出元 1件 [`00bdb2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2d0.md) · 呼出先 2件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00be0610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0610.md)

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
    "old": {
      "definition_site": "00b7d7cc",
      "incomplete_value": false,
      "site": "00b7d7d0",
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
      "00b7d894",
      "PARAM",
      [
        "storage",
        "002966d6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d894",
      "PARAM",
      [
        "storage",
        "00296763",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d788.md#insn-00b7d7d0) · [`00b7d7a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d788.md#insn-00b7d7a8) · [`00b7d7cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d788.md#insn-00b7d7cc)
- 新版 `00b7d898`（命令位置の公開資料なし） · `00b7d870`（命令位置の公開資料なし） · `00b7d894`（命令位置の公開資料なし）

~~~diff
- 00b7d7d0 ["INT_ADD", "register:40f0:8", ["const:b7d7d0:8", "const:4:8"]]
- 00b7d7d0 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7d898 ["INT_ADD", "register:40f0:8", ["const:b7d898:8", "const:4:8"]]
+ 00b7d898 ["CALL", null, ["callee:00bdb280:8"]]
- 00b7d7d0 bytes 80760194
+ 00b7d898 bytes 7a760194
- 00b7d7a8 ["INT_ADD", "register:40f0:8", ["const:b7d7a8:8", "const:4:8"]]
- 00b7d7a8 ["CALL", null, ["callee:00be0610:8"]]
+ 00b7d870 ["INT_ADD", "register:40f0:8", ["const:b7d870:8", "const:4:8"]]
+ 00b7d870 ["CALL", null, ["callee:00be0610:8"]]
- 00b7d7a8 bytes 6e8b0194
+ 00b7d870 bytes 688b0194
- 00b7d7cc ["COPY", "tmp:0:8", ["const:6d6:8"]]
- 00b7d7cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b7d7cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b7d7cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b7d894 ["COPY", "tmp:0:8", ["const:763:8"]]
+ 00b7d894 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7d894 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7d894 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b7d7cc bytes 21581b91
+ 00b7d894 bytes 218c1d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0f7123ea6adebaaa464fd9f983d1aae"></a>

### [`00b7d7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d7d4.md) → [`00b7d89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d89c.md) _ZNSt6__ndk16thread6detachEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5c0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00be1180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1180.md)
- 新版 呼出元 1件 [`00bdb670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb670.md) · 呼出先 2件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00be1230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1230.md)

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
    "old": {
      "definition_site": "00b7d814",
      "incomplete_value": false,
      "site": "00b7d818",
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
            "const:6e:8"
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
      "00b7d8dc",
      "PARAM",
      [
        "storage",
        "0029e06e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d8dc",
      "PARAM",
      [
        "storage",
        "0029e0fb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d7d4.md#insn-00b7d818) · [`00b7d7f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d7d4.md#insn-00b7d7f0) · [`00b7d814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d7d4.md#insn-00b7d814)
- 新版 `00b7d8e0`（命令位置の公開資料なし） · `00b7d8b8`（命令位置の公開資料なし） · `00b7d8dc`（命令位置の公開資料なし）

~~~diff
- 00b7d818 ["INT_ADD", "register:40f0:8", ["const:b7d818:8", "const:4:8"]]
- 00b7d818 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7d8e0 ["INT_ADD", "register:40f0:8", ["const:b7d8e0:8", "const:4:8"]]
+ 00b7d8e0 ["CALL", null, ["callee:00bdb280:8"]]
- 00b7d818 bytes 6e760194
+ 00b7d8e0 bytes 68760194
- 00b7d7f0 ["INT_ADD", "register:40f0:8", ["const:b7d7f0:8", "const:4:8"]]
- 00b7d7f0 ["CALL", null, ["callee:00be1230:8"]]
+ 00b7d8b8 ["INT_ADD", "register:40f0:8", ["const:b7d8b8:8", "const:4:8"]]
+ 00b7d8b8 ["CALL", null, ["callee:00be1230:8"]]
- 00b7d7f0 bytes 648e0194
+ 00b7d8b8 bytes 5e8e0194
- 00b7d814 ["COPY", "tmp:0:8", ["const:6e:8"]]
- 00b7d814 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b7d814 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b7d814 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b7d8dc ["COPY", "tmp:0:8", ["const:fb:8"]]
+ 00b7d8dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7d8dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7d8dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b7d814 bytes 21b80191
+ 00b7d8dc bytes 21ec0391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ea94560011b44bb352d3df3d2f5fa5b"></a>

### [`00b7d8c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d8c8.md) → [`00b7d990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d990.md) _ZNSt6__ndk119__thread_local_dataEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdb1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1e0.md) · 呼出先 3件 [`00b7d94c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d94c.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`00bdb290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb290.md) · 呼出先 3件 [`00b7da14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da14.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

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
    "old": {
      "definition_site": "00b7d928",
      "incomplete_value": true,
      "site": "00b7d928",
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
            "const:f78:8"
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
    "old": {
      "definition_site": "00b7d904",
      "incomplete_value": false,
      "site": "00b7d908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
    "old": {
      "definition_site": "00b7d918",
      "incomplete_value": false,
      "site": "00b7d91c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:f70:8"
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
      "00b7d9ac",
      "READ",
      [
        "storage",
        "010a1f80",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7d9b4",
      "READ",
      [
        "storage",
        "010a1f78",
        null,
        "undefined8"
      ]
    ],
    [
      "00b7d9b4",
      "DATA",
      [
        "storage",
        "010a1f70",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b7d9ac",
      "READ",
      [
        "storage",
        "010a2040",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7d9b4",
      "READ",
      [
        "storage",
        "010a2038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b7d9b4",
      "DATA",
      [
        "storage",
        "010a2030",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d8c8.md#insn-00b7d908) · [`00b7d91c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d8c8.md#insn-00b7d91c) · [`00b7d928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d8c8.md#insn-00b7d928)
- 新版 `00b7d9d0`（命令位置の公開資料なし） · `00b7d9e4`（命令位置の公開資料なし） · `00b7d9f0`（命令位置の公開資料なし）

~~~diff
- 00b7d908 ["INT_ADD", "register:40f0:8", ["const:b7d908:8", "const:4:8"]]
- 00b7d908 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00b7d9d0 ["INT_ADD", "register:40f0:8", ["const:b7d9d0:8", "const:4:8"]]
+ 00b7d9d0 ["CALL", null, ["callee:00bdafb0:8"]]
- 00b7d908 bytes 7e750194
+ 00b7d9d0 bytes 78750194
- 00b7d91c ["INT_ADD", "register:40f0:8", ["const:b7d91c:8", "const:4:8"]]
- 00b7d91c ["CALL", null, ["callee:00b7da14:8"]]
+ 00b7d9e4 ["INT_ADD", "register:40f0:8", ["const:b7d9e4:8", "const:4:8"]]
+ 00b7d9e4 ["CALL", null, ["callee:00b7da14:8"]]
- 00b7d91c bytes 0c000094
+ 00b7d9e4 bytes 0c000094
- 00b7d928 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f78:8"]]
- 00b7d928 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00b7d9f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:38:8"]]
+ 00b7d9f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b7d928 bytes 93be07f9
+ 00b7d9f0 bytes 931e00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bad304d58e66f5879a54a18c00eee85"></a>

### [`00b7d94c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d94c.md) → [`00b7da14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da14.md) FUN_00b7da14

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b7d8c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d8c8.md) · 呼出先 3件 [`00b7dd00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dd00.md) [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00bdd3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3b0.md)
- 新版 呼出元 1件 [`00b7d990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d990.md) · 呼出先 3件 [`00b7ddc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7ddc8.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdd460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd460.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7da24",
      "incomplete_value": false,
      "site": "00b7da28",
      "value": [
        "leaf",
        "const:b7ddc8:8"
      ]
    },
    "old": {
      "definition_site": "00b7d95c",
      "incomplete_value": false,
      "site": "00b7d960",
      "value": [
        "leaf",
        "const:b7dd00:8"
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
      "site": "00b7d97c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b7da44"
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
      "00b7da24",
      "PARAM",
      [
        "storage",
        "00b7dd00",
        null,
        null
      ]
    ],
    [
      "00b7da2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7d974"
      ]
    ],
    [
      "unmatched:00b7d978",
      "PARAM",
      [
        "storage",
        "0029440d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7da24",
      "PARAM",
      [
        "storage",
        "00b7ddc8",
        null,
        null
      ]
    ],
    [
      "00b7da2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7da3c"
      ]
    ],
    [
      "00b7da40",
      "PARAM",
      [
        "storage",
        "0029449a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d94c.md#insn-00b7d960) · [`00b7d970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d94c.md#insn-00b7d970) · [`00b7d97c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d94c.md#insn-00b7d97c)
- 新版 `00b7da28`（命令位置の公開資料なし）

~~~diff
- 00b7d960 ["INT_ADD", "register:40f0:8", ["const:b7d960:8", "const:4:8"]]
- 00b7d960 ["CALL", null, ["callee:00bdd460:8"]]
+ 00b7da28 ["INT_ADD", "register:40f0:8", ["const:b7da28:8", "const:4:8"]]
+ 00b7da28 ["CALL", null, ["callee:00bdd460:8"]]
- 00b7d960 bytes 947e0194
+ 00b7da28 bytes 8e7e0194
- 00b7d970 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b7d970 ["RETURN", null, ["register:0:8"]]
- 00b7d970 bytes c0035fd6
- 00b7d97c ["INT_ADD", "register:40f0:8", ["const:b7d97c:8", "const:4:8"]]
- 00b7d97c ["CALL", null, ["callee:00bdb280:8"]]
- 00b7d97c bytes 15760194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3893d53ce3799a435bc9c3acfd27f81"></a>

### [`00b7da4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7da4c.md) → [`00b7db14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7db14.md) FUN_00b7db14

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00b7dcb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dcb8.md) · 呼出先 4件 [`00b7dcd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dcd0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00b7dd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd80.md) · 呼出先 4件 [`00b7dd98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd98.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 76.92% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7da70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7da4c.md#insn-00b7da70) · [`00b7da7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7da4c.md#insn-00b7da7c) · [`00b7da94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7da4c.md#insn-00b7da94)
- 新版 `00b7db38`（命令位置の公開資料なし） · `00b7db44`（命令位置の公開資料なし） · `00b7db5c`（命令位置の公開資料なし）

~~~diff
- 00b7da70 ["CBRANCH", null, ["local:b3:8", "register:102:1"]]
+ 00b7db38 ["CBRANCH", null, ["local:b2:8", "register:102:1"]]
- 00b7da70 bytes 82000054
+ 00b7db38 bytes 82000054
- 00b7da7c ["BRANCH", null, ["local:b9:8"]]
+ 00b7db44 ["BRANCH", null, ["local:b8:8"]]
- 00b7da7c bytes 2a000014
+ 00b7db44 bytes 2a000014
- 00b7da94 ["INT_NOTEQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 00b7da94 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00b7db5c ["INT_NOTEQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
+ 00b7db5c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b7da94 bytes 6b0500b5
+ 00b7db5c bytes 6b0500b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3082b4b7749f94ee8afae260cb91da6"></a>

### [`00b7dd38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dd38.md) → [`00b7de00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7de00.md) _ZNSt6__ndk113random_deviceC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb450.md) · 呼出先 4件 [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00be0530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0530.md)
- 新版 呼出元 1件 [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) · 呼出先 4件 [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00be05e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be05e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dd40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dd40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dd44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7dd40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7dd44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7dd94",
      "PARAM",
      [
        "storage",
        "002a40d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7de08",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b7de0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b7de5c",
      "PARAM",
      [
        "storage",
        "002a40ca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7dd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dd38.md#insn-00b7dd40) · [`00b7dd44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dd38.md#insn-00b7dd44) · [`00b7dda4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dd38.md#insn-00b7dda4)
- 新版 `00b7de6c`（命令位置の公開資料なし）

~~~diff
- 00b7dd40 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7dd40 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7dd40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b7dd40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7dd40 bytes fd7b02a9
- 00b7dd44 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b7dd44 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b7dd44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b7dd44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7dd44 bytes f44f03a9
- 00b7dda4 ["INT_ADD", "register:40f0:8", ["const:b7dda4:8", "const:4:8"]]
- 00b7dda4 ["CALL", null, ["callee:00bdb210:8"]]
+ 00b7de6c ["INT_ADD", "register:40f0:8", ["const:b7de6c:8", "const:4:8"]]
+ 00b7de6c ["CALL", null, ["callee:00bdb210:8"]]
- 00b7dda4 bytes ef740194
+ 00b7de6c bytes e9740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad1a6ce6af30065a6e7825fba4289ef4"></a>

### [`00b7de00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7de00.md) → [`00b7dec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dec8.md) _ZNSt6__ndk113random_deviceclEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb460.md) · 呼出先 3件 [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00be0570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0570.md)
- 新版 呼出元 1件 [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md) · 呼出先 3件 [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00be0620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0620.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 83.78% / 新版 83.78%

CFGの説明率　旧版 61.54% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b7de7c",
      "incomplete_value": false,
      "site": "00b7de80",
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
            "const:5a:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7de90"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b7df58"
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
      "00b7df18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7de84"
      ]
    ],
    [
      "00b7df44",
      "PARAM",
      [
        "storage",
        "002a805a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b7de88",
      "PARAM",
      [
        "storage",
        "0029c1ba",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7df18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7df4c"
      ]
    ],
    [
      "00b7df44",
      "PARAM",
      [
        "storage",
        "002a7fc6",
        null,
        "string"
      ]
    ],
    [
      "00b7df50",
      "PARAM",
      [
        "storage",
        "0029c247",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7de74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7de00.md#insn-00b7de74) · [`00b7de80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7de00.md#insn-00b7de80) · [`00b7de90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7de00.md#insn-00b7de90)
- 新版 `00b7df48`（命令位置の公開資料なし）

~~~diff
- 00b7de74 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b7de74 ["RETURN", null, ["register:0:8"]]
- 00b7de74 bytes c0035fd6
- 00b7de80 ["INT_ADD", "register:40f0:8", ["const:b7de80:8", "const:4:8"]]
- 00b7de80 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7df48 ["INT_ADD", "register:40f0:8", ["const:b7df48:8", "const:4:8"]]
+ 00b7df48 ["CALL", null, ["callee:00bdb280:8"]]
- 00b7de80 bytes d4740194
+ 00b7df48 bytes ce740194
- 00b7de90 ["INT_ADD", "register:40f0:8", ["const:b7de90:8", "const:4:8"]]
- 00b7de90 ["CALL", null, ["callee:00bdb280:8"]]
- 00b7de90 bytes d0740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2398ceb62a57a2705b86cd45271c99b"></a>

### [`00b7df70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7df70.md) → [`00b7e038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e038.md) _ZNSt6__ndk117iostream_categoryEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

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
    "old": {
      "definition_site": "00b7dfa4",
      "incomplete_value": false,
      "site": "00b7dfa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
    "old": {
      "definition_site": "00b7dfb4",
      "incomplete_value": false,
      "site": "00b7dfb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "00b7e04c",
      "READ",
      [
        "storage",
        "010a1f88",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7e058",
      "DATA",
      [
        "storage",
        "00c24820",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e06c",
      "PARAM",
      [
        "storage",
        "010a1f88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b7e04c",
      "READ",
      [
        "storage",
        "010a2048",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7e058",
      "DATA",
      [
        "storage",
        "00c248d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e06c",
      "PARAM",
      [
        "storage",
        "010a2048",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7dfa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7df70.md#insn-00b7dfa8) · [`00b7dfb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7df70.md#insn-00b7dfb8) · [`00b7df7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7df70.md#insn-00b7df7c)
- 新版 `00b7e070`（命令位置の公開資料なし） · `00b7e080`（命令位置の公開資料なし） · `00b7e044`（命令位置の公開資料なし）

~~~diff
- 00b7dfa8 ["INT_ADD", "register:40f0:8", ["const:b7dfa8:8", "const:4:8"]]
- 00b7dfa8 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00b7e070 ["INT_ADD", "register:40f0:8", ["const:b7e070:8", "const:4:8"]]
+ 00b7e070 ["CALL", null, ["callee:00bdafb0:8"]]
- 00b7dfa8 bytes d6730194
+ 00b7e070 bytes d0730194
- 00b7dfb8 ["INT_ADD", "register:40f0:8", ["const:b7dfb8:8", "const:4:8"]]
- 00b7dfb8 ["CALL", null, ["callee:00bdafd0:8"]]
+ 00b7e080 ["INT_ADD", "register:40f0:8", ["const:b7e080:8", "const:4:8"]]
+ 00b7e080 ["CALL", null, ["callee:00bdafd0:8"]]
- 00b7dfb8 bytes da730194
+ 00b7e080 bytes d4730194
- 00b7df7c ["COPY", "register:4040:8", ["const:10a1000:8"]]
+ 00b7e044 ["COPY", "register:4040:8", ["const:10a2000:8"]]
- 00b7df7c bytes 28290090
+ 00b7e044 bytes 28290090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab0ac0f40f3947a85a44aa586db61fd7"></a>

### [`00b7dfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dfc0.md) → [`00b7e088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e088.md) _ZNSt6__ndk18ios_base7failureC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_10error_codeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1050.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1100.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7e0b0",
      "incomplete_value": true,
      "site": "00b7e0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7dfe8",
      "incomplete_value": true,
      "site": "00b7dfec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b7e0ac",
      "READ",
      [
        "storage",
        "00c1bbb8",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e0b4",
      "DATA",
      [
        "storage",
        "00c12ed8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b7e0ac",
      "READ",
      [
        "storage",
        "00c1bc68",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e0b4",
      "DATA",
      [
        "storage",
        "00c12f88",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7dfdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dfc0.md#insn-00b7dfdc) · [`00b7dfe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dfc0.md#insn-00b7dfe4)
- 新版 `00b7e0a4`（命令位置の公開資料なし） · `00b7e0ac`（命令位置の公開資料なし）

~~~diff
- 00b7dfdc ["INT_ADD", "register:40f0:8", ["const:b7dfdc:8", "const:4:8"]]
- 00b7dfdc ["CALL", null, ["callee:00be1100:8"]]
+ 00b7e0a4 ["INT_ADD", "register:40f0:8", ["const:b7e0a4:8", "const:4:8"]]
+ 00b7e0a4 ["CALL", null, ["callee:00be1100:8"]]
- 00b7dfdc bytes 1d8c0194
+ 00b7e0a4 bytes 178c0194
- 00b7dfe4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bb8:8"]]
- 00b7dfe4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7e0ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c68:8"]]
+ 00b7e0ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7dfe4 bytes 08dd45f9
+ 00b7e0ac bytes 083546f9
~~~


<a id="compare-f23793d332b1fcf7101f2739a8db8e9b"></a>

### [`00b7e048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e048.md) → [`00b7e110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e110.md) _ZNSt6__ndk18ios_base7failureD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be11c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1270.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e05c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e048.md#insn-00b7e05c)
- 新版 `00b7e124`（命令位置の公開資料なし）

~~~diff
- 00b7e05c ["INT_ADD", "register:40f0:8", ["const:b7e05c:8", "const:4:8"]]
- 00b7e05c ["CALL", null, ["callee:00be1270:8"]]
+ 00b7e124 ["INT_ADD", "register:40f0:8", ["const:b7e124:8", "const:4:8"]]
+ 00b7e124 ["CALL", null, ["callee:00be1270:8"]]
- 00b7e05c bytes 598c0194
+ 00b7e124 bytes 538c0194
~~~


<a id="compare-dd002864d74c5dcc616d1a8f6d9a05e0"></a>

### [`00b7e074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e074.md) → [`00b7e13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e13c.md) _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00be11d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11d0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be1280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1280.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e07c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e074.md#insn-00b7e07c) · [`00b7e0b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e074.md#insn-00b7e0b4) · [`00b7e0c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e074.md#insn-00b7e0c0)
- 新版 `00b7e144`（命令位置の公開資料なし） · `00b7e17c`（命令位置の公開資料なし） · `00b7e188`（命令位置の公開資料なし）

~~~diff
- 00b7e07c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b7e07c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b7e144 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b7e144 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b7e07c bytes c80200b4
+ 00b7e144 bytes c80200b4
- 00b7e0b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7e0b4 ["INT_ADD", "register:40f0:8", ["const:b7e0b4:8", "const:4:8"]]
- 00b7e0b4 ["CALLIND", null, ["register:0:8"]]
+ 00b7e17c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7e17c ["INT_ADD", "register:40f0:8", ["const:b7e17c:8", "const:4:8"]]
+ 00b7e17c ["CALLIND", null, ["register:0:8"]]
- 00b7e0b4 bytes 00013fd6
+ 00b7e17c bytes 00013fd6
- 00b7e0c0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b7e0c0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b7e188 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b7e188 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b7e0c0 bytes 01ffff54
+ 00b7e188 bytes 01ffff54
~~~


<a id="compare-2e472862b4d2f8f544f78b291254ead1"></a>

### [`00b7e178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e178.md) → [`00b7e240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e240.md) _ZNSt6__ndk18ios_base6xallocEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md)

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
    "old": {
      "definition_site": "00b7e18c",
      "incomplete_value": true,
      "site": "00b7e190",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
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
      "00b7e254",
      "READ",
      [
        "storage",
        "00c1bbc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e254",
      "PARAM",
      [
        "storage",
        "010a1f90",
        "_ZNSt6__ndk18ios_base9__xindex_E",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b7e254",
      "READ",
      [
        "storage",
        "00c1bc78",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e254",
      "PARAM",
      [
        "storage",
        "010a2050",
        "_ZNSt6__ndk18ios_base9__xindex_E",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e178.md#insn-00b7e190) · [`00b7e18c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e178.md#insn-00b7e18c)
- 新版 `00b7e258`（命令位置の公開資料なし） · `00b7e254`（命令位置の公開資料なし）

~~~diff
- 00b7e190 ["INT_ADD", "register:40f0:8", ["const:b7e190:8", "const:4:8"]]
- 00b7e190 ["CALL", null, ["callee:00bd6df0:8"]]
+ 00b7e258 ["INT_ADD", "register:40f0:8", ["const:b7e258:8", "const:4:8"]]
+ 00b7e258 ["CALL", null, ["callee:00bd6df0:8"]]
- 00b7e190 bytes e8620194
+ 00b7e258 bytes e6620194
- 00b7e18c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:bc8:8"]]
- 00b7e18c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7e254 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:c78:8"]]
+ 00b7e254 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7e18c bytes 21e445f9
+ 00b7e254 bytes 213c46f9
~~~


<a id="compare-1d97bc3d5717eb283be4d062b3f0db38"></a>

### [`00b7e3c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e3c8.md) → [`00b7e490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e490.md) _ZNSt6__ndk18ios_base17register_callbackEPFvNS0_5eventERS0_iEi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7e5c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e5c8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b7e690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e690.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md)

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
    "old": {
      "definition_site": "00b7e4a0",
      "incomplete_value": false,
      "site": "00b7e4a4",
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
      "00b7e568",
      "PARAM",
      [
        "storage",
        "0029781f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7e568",
      "PARAM",
      [
        "storage",
        "002978ac",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e4a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e3c8.md#insn-00b7e4a4) · [`00b7e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e3c8.md#insn-00b7e41c) · [`00b7e448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e3c8.md#insn-00b7e448)
- 新版 `00b7e56c`（命令位置の公開資料なし） · `00b7e4e4`（命令位置の公開資料なし） · `00b7e510`（命令位置の公開資料なし）

~~~diff
- 00b7e4a4 ["INT_ADD", "register:40f0:8", ["const:b7e4a4:8", "const:4:8"]]
- 00b7e4a4 ["CALL", null, ["callee:00b7e690:8"]]
+ 00b7e56c ["INT_ADD", "register:40f0:8", ["const:b7e56c:8", "const:4:8"]]
+ 00b7e56c ["CALL", null, ["callee:00b7e690:8"]]
- 00b7e4a4 bytes 49000094
+ 00b7e56c bytes 49000094
- 00b7e41c ["INT_ADD", "register:40f0:8", ["const:b7e41c:8", "const:4:8"]]
- 00b7e41c ["CALL", null, ["callee:00bdd200:8"]]
+ 00b7e4e4 ["INT_ADD", "register:40f0:8", ["const:b7e4e4:8", "const:4:8"]]
+ 00b7e4e4 ["CALL", null, ["callee:00bdd200:8"]]
- 00b7e41c bytes 4d7b0194
+ 00b7e4e4 bytes 477b0194
- 00b7e448 ["INT_ADD", "register:40f0:8", ["const:b7e448:8", "const:4:8"]]
- 00b7e448 ["CALL", null, ["callee:00bdd200:8"]]
+ 00b7e510 ["INT_ADD", "register:40f0:8", ["const:b7e510:8", "const:4:8"]]
+ 00b7e510 ["CALL", null, ["callee:00bdd200:8"]]
- 00b7e448 bytes 427b0194
+ 00b7e510 bytes 3c7b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01b6f286495bf522c17d115270d10e2c"></a>

### [`00b7e4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e4a8.md) → [`00b7e570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e570.md) _ZNSt6__ndk18ios_baseD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md) [`00be11f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11f0.md) · 呼出先 2件 [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md)
- 新版 呼出元 2件 [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md) [`00be12a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12a0.md) · 呼出先 2件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)

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
    "old": {
      "definition_site": "00b7e4cc",
      "incomplete_value": true,
      "site": "00b7e4d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b7e58c",
      "READ",
      [
        "storage",
        "00c1bbd0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e598",
      "DATA",
      [
        "storage",
        "00c12f00",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b7e58c",
      "READ",
      [
        "storage",
        "00c1bc80",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e598",
      "DATA",
      [
        "storage",
        "00c12fb0",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e4c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e4a8.md#insn-00b7e4c4) · [`00b7e4fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e4a8.md#insn-00b7e4fc) · [`00b7e510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e4a8.md#insn-00b7e510)
- 新版 `00b7e58c`（命令位置の公開資料なし） · `00b7e5c4`（命令位置の公開資料なし） · `00b7e5d8`（命令位置の公開資料なし）

~~~diff
- 00b7e4c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd0:8"]]
- 00b7e4c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7e58c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c80:8"]]
+ 00b7e58c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7e4c4 bytes 08e945f9
+ 00b7e58c bytes 084146f9
- 00b7e4fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7e4fc ["INT_ADD", "register:40f0:8", ["const:b7e4fc:8", "const:4:8"]]
- 00b7e4fc ["CALLIND", null, ["register:0:8"]]
+ 00b7e5c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7e5c4 ["INT_ADD", "register:40f0:8", ["const:b7e5c4:8", "const:4:8"]]
+ 00b7e5c4 ["CALLIND", null, ["register:0:8"]]
- 00b7e4fc bytes 00013fd6
+ 00b7e5c4 bytes 00013fd6
- 00b7e510 ["INT_ADD", "register:40f0:8", ["const:b7e510:8", "const:4:8"]]
- 00b7e510 ["CALL", null, ["callee:00bdb3f0:8"]]
+ 00b7e5d8 ["INT_ADD", "register:40f0:8", ["const:b7e5d8:8", "const:4:8"]]
+ 00b7e5d8 ["CALL", null, ["callee:00bdb3f0:8"]]
- 00b7e510 bytes 8c730194
+ 00b7e5d8 bytes 86730194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd2e613ff08cc25bac786ce982225e90"></a>

### [`00b7e588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e588.md) → [`00b7e650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e650.md) _ZNSt6__ndk18ios_base5clearEj

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) · 呼出先 1件 [`00b7e5c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e5c8.md)
- 新版 呼出元 1件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) · 呼出先 1件 [`00b7e690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e690.md)

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
    "old": {
      "definition_site": "00b7e5c0",
      "incomplete_value": false,
      "site": "00b7e5c4",
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
      "00b7e688",
      "PARAM",
      [
        "storage",
        "0029781f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7e688",
      "PARAM",
      [
        "storage",
        "002978ac",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e5c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e588.md#insn-00b7e5c4) · [`00b7e5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e588.md#insn-00b7e5c0)
- 新版 `00b7e68c`（命令位置の公開資料なし） · `00b7e688`（命令位置の公開資料なし）

~~~diff
- 00b7e5c4 ["INT_ADD", "register:40f0:8", ["const:b7e5c4:8", "const:4:8"]]
- 00b7e5c4 ["CALL", null, ["callee:00b7e690:8"]]
+ 00b7e68c ["INT_ADD", "register:40f0:8", ["const:b7e68c:8", "const:4:8"]]
+ 00b7e68c ["CALL", null, ["callee:00b7e690:8"]]
- 00b7e5c4 bytes 01000094
+ 00b7e68c bytes 01000094
- 00b7e5c0 ["COPY", "tmp:0:8", ["const:81f:8"]]
- 00b7e5c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b7e5c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b7e5c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b7e688 ["COPY", "tmp:0:8", ["const:8ac:8"]]
+ 00b7e688 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b7e688 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b7e688 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b7e5c0 bytes 007c2091
+ 00b7e688 bytes 00b02291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-386be5331832d1320f65a7214ed6c08e"></a>

### [`00b7e5c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e5c8.md) → [`00b7e690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e690.md) FUN_00b7e690

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00b7e1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e1a0.md) [`00b7e2b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e2b4.md) [`00b7e3c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e3c8.md) [`00b7e588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e588.md) · 呼出先 6件 [`00b7e040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e040.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 4件 [`00b7e268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e268.md) [`00b7e37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e37c.md) [`00b7e490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e490.md) [`00b7e650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e650.md) · 呼出先 6件 [`00b7e108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e108.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

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
      "definition_site": "00b7e6d0",
      "incomplete_value": false,
      "site": "00b7e6d0",
      "value": [
        "leaf",
        "const:c248d0:8"
      ]
    },
    "old": {
      "definition_site": "00b7e608",
      "incomplete_value": false,
      "site": "00b7e608",
      "value": [
        "leaf",
        "const:c24820:8"
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b7e628",
      "incomplete_value": true,
      "site": "00b7e630",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd8:8"
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
    "old": {
      "definition_site": "00b7e62c",
      "incomplete_value": true,
      "site": "00b7e630",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc0:8"
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
      "00b7e6bc",
      "READ",
      [
        "storage",
        "010a1f88",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7e6d0",
      "DATA",
      [
        "storage",
        "00c24820",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e6f0",
      "READ",
      [
        "storage",
        "00c1bbd8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b7e6bc",
      "READ",
      [
        "storage",
        "010a2048",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7e6d0",
      "DATA",
      [
        "storage",
        "00c248d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e6f0",
      "READ",
      [
        "storage",
        "00c1bc88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e5c8.md#insn-00b7e630) · [`00b7e63c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e5c8.md#insn-00b7e63c) · [`00b7e64c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e5c8.md#insn-00b7e64c)
- 新版 `00b7e6f8`（命令位置の公開資料なし） · `00b7e704`（命令位置の公開資料なし） · `00b7e714`（命令位置の公開資料なし）

~~~diff
- 00b7e630 ["INT_ADD", "register:40f0:8", ["const:b7e630:8", "const:4:8"]]
- 00b7e630 ["CALL", null, ["callee:00bdb070:8"]]
+ 00b7e6f8 ["INT_ADD", "register:40f0:8", ["const:b7e6f8:8", "const:4:8"]]
+ 00b7e6f8 ["CALL", null, ["callee:00bdb070:8"]]
- 00b7e630 bytes 64720194
+ 00b7e6f8 bytes 5e720194
- 00b7e63c ["INT_ADD", "register:40f0:8", ["const:b7e63c:8", "const:4:8"]]
- 00b7e63c ["CALL", null, ["callee:00bdafb0:8"]]
+ 00b7e704 ["INT_ADD", "register:40f0:8", ["const:b7e704:8", "const:4:8"]]
+ 00b7e704 ["CALL", null, ["callee:00bdafb0:8"]]
- 00b7e63c bytes 31720194
+ 00b7e704 bytes 2b720194
- 00b7e64c ["INT_ADD", "register:40f0:8", ["const:b7e64c:8", "const:4:8"]]
- 00b7e64c ["CALL", null, ["callee:00bdafd0:8"]]
+ 00b7e714 ["INT_ADD", "register:40f0:8", ["const:b7e714:8", "const:4:8"]]
+ 00b7e714 ["CALL", null, ["callee:00bdafd0:8"]]
- 00b7e64c bytes 35720194
+ 00b7e714 bytes 2f720194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fed119e1b0deb770d2582ed25bc10eca"></a>

### [`00b7eb84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7eb84.md) → [`00b7ec4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec4c.md) _ZNSt6__ndk18ios_base15sync_with_stdioEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "00b7eb94",
      "incomplete_value": false,
      "site": "00b7eb94",
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
            "const:828:8"
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
      "00b7ec58",
      "READ",
      [
        "storage",
        "00c24828",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7ec5c",
      "WRITE",
      [
        "storage",
        "00c24828",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b7ec58",
      "READ",
      [
        "storage",
        "00c248d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7ec5c",
      "WRITE",
      [
        "storage",
        "00c248d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7eb94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7eb84.md#insn-00b7eb94) · [`00b7eb90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7eb84.md#insn-00b7eb90)
- 新版 `00b7ec5c`（命令位置の公開資料なし） · `00b7ec58`（命令位置の公開資料なし）

~~~diff
- 00b7eb94 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b7eb94 ["INT_ADD", "tmp:1:8", ["register:4050:8", "const:828:8"]]
- 00b7eb94 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b7ec5c ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00b7ec5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "const:8d8:8"]]
+ 00b7ec5c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b7eb94 bytes 49a12039
+ 00b7ec5c bytes 49612339
- 00b7eb90 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:828:8"]]
- 00b7eb90 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b7eb90 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b7ec58 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:8d8:8"]]
+ 00b7ec58 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b7ec58 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b7eb90 bytes 48a16039
+ 00b7ec58 bytes 48616339
~~~


<a id="compare-c5a234529ed9ac97301a22315e092256"></a>

### [`00b7ef20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ef20.md) → [`00b7efe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7efe8.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2a0.md) · 呼出先 1件 [`00bdd850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd850.md)
- 新版 呼出元 1件 [`00bdb350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb350.md) · 呼出先 1件 [`00bdd900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd900.md)

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
    "old": {
      "definition_site": "00b7ef40",
      "incomplete_value": true,
      "site": "00b7ef40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b7f000",
      "READ",
      [
        "storage",
        "00c1b950",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f008",
      "DATA",
      [
        "storage",
        "00c11120",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00b7f000",
      "READ",
      [
        "storage",
        "00c1ba00",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f008",
      "DATA",
      [
        "storage",
        "00c111d0",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7ef38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ef20.md#insn-00b7ef38) · [`00b7ef44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ef20.md#insn-00b7ef44)
- 新版 `00b7f000`（命令位置の公開資料なし） · `00b7f00c`（命令位置の公開資料なし）

~~~diff
- 00b7ef38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
- 00b7ef38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7f000 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a00:8"]]
+ 00b7f000 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7ef38 bytes 08a944f9
+ 00b7f000 bytes 080145f9
- 00b7ef44 ["INT_ADD", "register:40f0:8", ["const:b7ef44:8", "const:4:8"]]
- 00b7ef44 ["CALL", null, ["callee:00bdd900:8"]]
+ 00b7f00c ["INT_ADD", "register:40f0:8", ["const:b7f00c:8", "const:4:8"]]
+ 00b7f00c ["CALL", null, ["callee:00bdd900:8"]]
- 00b7ef44 bytes 437a0194
+ 00b7f00c bytes 3d7a0194
~~~


<a id="compare-4de183e2832952c1621cc34360a903ad"></a>

### [`00b7ef64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ef64.md) → [`00b7f02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f02c.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC2ERKS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md)

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
    "old": {
      "definition_site": "00b7ef8c",
      "incomplete_value": true,
      "site": "00b7ef8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b7f048",
      "READ",
      [
        "storage",
        "00c1b950",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f054",
      "DATA",
      [
        "storage",
        "00c11120",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00b7f048",
      "READ",
      [
        "storage",
        "00c1ba00",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f054",
      "DATA",
      [
        "storage",
        "00c111d0",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7ef80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ef64.md#insn-00b7ef80) · [`00b7ef90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7ef64.md#insn-00b7ef90)
- 新版 `00b7f048`（命令位置の公開資料なし） · `00b7f058`（命令位置の公開資料なし）

~~~diff
- 00b7ef80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
- 00b7ef80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7f048 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a00:8"]]
+ 00b7f048 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7ef80 bytes 08a944f9
+ 00b7f048 bytes 080145f9
- 00b7ef90 ["INT_ADD", "register:40f0:8", ["const:b7ef90:8", "const:4:8"]]
- 00b7ef90 ["CALL", null, ["callee:00bdd930:8"]]
+ 00b7f058 ["INT_ADD", "register:40f0:8", ["const:b7f058:8", "const:4:8"]]
+ 00b7f058 ["CALL", null, ["callee:00bdd930:8"]]
- 00b7ef90 bytes 3c7a0194
+ 00b7f058 bytes 367a0194
~~~


<a id="compare-0eb2bbd30fd9c2470dee9ffd76bc1bee"></a>

### [`00b7f16c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f16c.md) → [`00b7f234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f234.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)

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
    "old": {
      "definition_site": "00b7f198",
      "incomplete_value": true,
      "site": "00b7f198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "old": {
      "definition_site": "00b7f19c",
      "incomplete_value": true,
      "site": "00b7f19c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b7f250",
      "READ",
      [
        "storage",
        "00c1b340",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f260",
      "DATA",
      [
        "storage",
        "00c12f90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f264",
      "DATA",
      [
        "storage",
        "00c12f68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b7f250",
      "READ",
      [
        "storage",
        "00c1b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f260",
      "DATA",
      [
        "storage",
        "00c13040",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f264",
      "DATA",
      [
        "storage",
        "00c13018",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f16c.md#insn-00b7f188) · [`00b7f1a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f16c.md#insn-00b7f1a4)
- 新版 `00b7f250`（命令位置の公開資料なし） · `00b7f26c`（命令位置の公開資料なし）

~~~diff
- 00b7f188 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:340:8"]]
- 00b7f188 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7f250 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3f0:8"]]
+ 00b7f250 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7f188 bytes 08a141f9
+ 00b7f250 bytes 08f941f9
- 00b7f1a4 ["INT_ADD", "register:40f0:8", ["const:b7f1a4:8", "const:4:8"]]
- 00b7f1a4 ["CALL", null, ["callee:00bdb340:8"]]
+ 00b7f26c ["INT_ADD", "register:40f0:8", ["const:b7f26c:8", "const:4:8"]]
+ 00b7f26c ["CALL", null, ["callee:00bdb340:8"]]
- 00b7f1a4 bytes 3b700194
+ 00b7f26c bytes 35700194
~~~


<a id="compare-be1658f4088a025a62f02162c8e82eda"></a>

### [`00b7f24c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f24c.md) → [`00b7f314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f314.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC2ERS3_b

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdbfa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbfa0.md)
- 新版 呼出元 1件 [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc050.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 82.50% / 新版 80.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b7f2d8",
      "incomplete_value": true,
      "site": "00b7f2e0",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b7f2dc",
      "incomplete_value": true,
      "site": "00b7f2e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "definition_site": "00b7f464",
      "incomplete_value": true,
      "site": "00b7f470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
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
    "old": null,
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7f2dc",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b7f2dc",
      "PARAM",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7f3a4",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f3a4",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f24c.md#insn-00b7f2e0) · [`00b7f3a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f24c.md#insn-00b7f3a8) · [`00b7f2ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f24c.md#insn-00b7f2ac)
- 新版 `00b7f3a8`（命令位置の公開資料なし） · `00b7f470`（命令位置の公開資料なし） · `00b7f374`（命令位置の公開資料なし）

~~~diff
- 00b7f2e0 ["INT_ADD", "register:40f0:8", ["const:b7f2e0:8", "const:4:8"]]
- 00b7f2e0 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b7f3a8 ["INT_ADD", "register:40f0:8", ["const:b7f3a8:8", "const:4:8"]]
+ 00b7f3a8 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b7f2e0 bytes 14700194
+ 00b7f3a8 bytes 0e700194
- 00b7f3a8 ["INT_ADD", "register:40f0:8", ["const:b7f3a8:8", "const:4:8"]]
- 00b7f3a8 ["CALL", null, ["callee:00bdb400:8"]]
+ 00b7f470 ["INT_ADD", "register:40f0:8", ["const:b7f470:8", "const:4:8"]]
+ 00b7f470 ["CALL", null, ["callee:00bdb400:8"]]
- 00b7f3a8 bytes ea6f0194
+ 00b7f470 bytes e46f0194
- 00b7f2ac ["INT_ADD", "register:40f0:8", ["const:b7f2ac:8", "const:4:8"]]
- 00b7f2ac ["CALL", null, ["callee:00bdc050:8"]]
+ 00b7f374 ["INT_ADD", "register:40f0:8", ["const:b7f374:8", "const:4:8"]]
+ 00b7f374 ["CALL", null, ["callee:00bdc050:8"]]
- 00b7f2ac bytes 3d730194
+ 00b7f374 bytes 37730194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-638fe433500d33f6b35b93d94bb1ab95"></a>

### [`00b7f65c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f65c.md) → [`00b7f724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f724.md) FUN_00b7f724

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7f654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f654.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00b7f71c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f71c.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

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
    "old": {
      "definition_site": "00b7f6b0",
      "incomplete_value": true,
      "site": "00b7f6b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
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
      "00b7f778",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f778",
      "PARAM",
      [
        "storage",
        "010a2770",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7f778",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f778",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f6b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f65c.md#insn-00b7f6b4) · [`00b7f688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f65c.md#insn-00b7f688) · [`00b7f6a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f65c.md#insn-00b7f6a4)
- 新版 `00b7f77c`（命令位置の公開資料なし） · `00b7f750`（命令位置の公開資料なし） · `00b7f76c`（命令位置の公開資料なし）

~~~diff
- 00b7f6b4 ["INT_ADD", "register:40f0:8", ["const:b7f6b4:8", "const:4:8"]]
- 00b7f6b4 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b7f77c ["INT_ADD", "register:40f0:8", ["const:b7f77c:8", "const:4:8"]]
+ 00b7f77c ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b7f6b4 bytes 1f6f0194
+ 00b7f77c bytes 196f0194
- 00b7f688 ["INT_ADD", "register:40f0:8", ["const:b7f688:8", "const:4:8"]]
- 00b7f688 ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b7f750 ["INT_ADD", "register:40f0:8", ["const:b7f750:8", "const:4:8"]]
+ 00b7f750 ["CALL", null, ["callee:00bdcf30:8"]]
- 00b7f688 bytes fe750194
+ 00b7f750 bytes f8750194
- 00b7f6a4 ["INT_ADD", "register:40f0:8", ["const:b7f6a4:8", "const:4:8"]]
- 00b7f6a4 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b7f76c ["INT_ADD", "register:40f0:8", ["const:b7f76c:8", "const:4:8"]]
+ 00b7f76c ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b7f6a4 bytes 1f6f0194
+ 00b7f76c bytes 196f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d41455d9e2ae16e0e520c8fde25cff41"></a>

### [`00b7f794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f794.md) → [`00b7f85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f85c.md) FUN_00b7f85c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7f78c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f78c.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00b7f854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f854.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

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
    "old": {
      "definition_site": "00b7f7e8",
      "incomplete_value": true,
      "site": "00b7f7ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
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
      "00b7f8b0",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f8b0",
      "PARAM",
      [
        "storage",
        "010a2770",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7f8b0",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f8b0",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f7ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f794.md#insn-00b7f7ec) · [`00b7f7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f794.md#insn-00b7f7c0) · [`00b7f7dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f794.md#insn-00b7f7dc)
- 新版 `00b7f8b4`（命令位置の公開資料なし） · `00b7f888`（命令位置の公開資料なし） · `00b7f8a4`（命令位置の公開資料なし）

~~~diff
- 00b7f7ec ["INT_ADD", "register:40f0:8", ["const:b7f7ec:8", "const:4:8"]]
- 00b7f7ec ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b7f8b4 ["INT_ADD", "register:40f0:8", ["const:b7f8b4:8", "const:4:8"]]
+ 00b7f8b4 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b7f7ec bytes d16e0194
+ 00b7f8b4 bytes cb6e0194
- 00b7f7c0 ["INT_ADD", "register:40f0:8", ["const:b7f7c0:8", "const:4:8"]]
- 00b7f7c0 ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b7f888 ["INT_ADD", "register:40f0:8", ["const:b7f888:8", "const:4:8"]]
+ 00b7f888 ["CALL", null, ["callee:00bdcf30:8"]]
- 00b7f7c0 bytes b0750194
+ 00b7f888 bytes aa750194
- 00b7f7dc ["INT_ADD", "register:40f0:8", ["const:b7f7dc:8", "const:4:8"]]
- 00b7f7dc ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b7f8a4 ["INT_ADD", "register:40f0:8", ["const:b7f8a4:8", "const:4:8"]]
+ 00b7f8a4 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b7f7dc bytes d16e0194
+ 00b7f8a4 bytes cb6e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3126b2292d41fea31b2206738692bc9"></a>

### [`00b7f90c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f90c.md) → [`00b7f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f9d4.md) FUN_00b7f9d4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7f904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f904.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00b7f9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f9cc.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

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
    "old": {
      "definition_site": "00b7f960",
      "incomplete_value": true,
      "site": "00b7f964",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
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
      "00b7fa28",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fa28",
      "PARAM",
      [
        "storage",
        "010a2770",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7fa28",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fa28",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f90c.md#insn-00b7f964) · [`00b7f938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f90c.md#insn-00b7f938) · [`00b7f954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7f90c.md#insn-00b7f954)
- 新版 `00b7fa2c`（命令位置の公開資料なし） · `00b7fa00`（命令位置の公開資料なし） · `00b7fa1c`（命令位置の公開資料なし）

~~~diff
- 00b7f964 ["INT_ADD", "register:40f0:8", ["const:b7f964:8", "const:4:8"]]
- 00b7f964 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b7fa2c ["INT_ADD", "register:40f0:8", ["const:b7fa2c:8", "const:4:8"]]
+ 00b7fa2c ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b7f964 bytes 736e0194
+ 00b7fa2c bytes 6d6e0194
- 00b7f938 ["INT_ADD", "register:40f0:8", ["const:b7f938:8", "const:4:8"]]
- 00b7f938 ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b7fa00 ["INT_ADD", "register:40f0:8", ["const:b7fa00:8", "const:4:8"]]
+ 00b7fa00 ["CALL", null, ["callee:00bdcf30:8"]]
- 00b7f938 bytes 52750194
+ 00b7fa00 bytes 4c750194
- 00b7f954 ["INT_ADD", "register:40f0:8", ["const:b7f954:8", "const:4:8"]]
- 00b7f954 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b7fa1c ["INT_ADD", "register:40f0:8", ["const:b7fa1c:8", "const:4:8"]]
+ 00b7fa1c ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b7f954 bytes 736e0194
+ 00b7fa1c bytes 6d6e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8be103d55188ba683d7777cfc9ebf3f1"></a>

### [`00b7fa44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fa44.md) → [`00b7fb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fb0c.md) FUN_00b7fb0c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7fa3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fa3c.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00b7fb04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fb04.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

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
    "old": {
      "definition_site": "00b7fa98",
      "incomplete_value": true,
      "site": "00b7fa9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
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
      "00b7fb60",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fb60",
      "PARAM",
      [
        "storage",
        "010a2770",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7fb60",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fb60",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7fa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fa44.md#insn-00b7fa9c) · [`00b7fa70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fa44.md#insn-00b7fa70) · [`00b7fa8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fa44.md#insn-00b7fa8c)
- 新版 `00b7fb64`（命令位置の公開資料なし） · `00b7fb38`（命令位置の公開資料なし） · `00b7fb54`（命令位置の公開資料なし）

~~~diff
- 00b7fa9c ["INT_ADD", "register:40f0:8", ["const:b7fa9c:8", "const:4:8"]]
- 00b7fa9c ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b7fb64 ["INT_ADD", "register:40f0:8", ["const:b7fb64:8", "const:4:8"]]
+ 00b7fb64 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b7fa9c bytes 256e0194
+ 00b7fb64 bytes 1f6e0194
- 00b7fa70 ["INT_ADD", "register:40f0:8", ["const:b7fa70:8", "const:4:8"]]
- 00b7fa70 ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b7fb38 ["INT_ADD", "register:40f0:8", ["const:b7fb38:8", "const:4:8"]]
+ 00b7fb38 ["CALL", null, ["callee:00bdcf30:8"]]
- 00b7fa70 bytes 04750194
+ 00b7fb38 bytes fe740194
- 00b7fa8c ["INT_ADD", "register:40f0:8", ["const:b7fa8c:8", "const:4:8"]]
- 00b7fa8c ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b7fb54 ["INT_ADD", "register:40f0:8", ["const:b7fb54:8", "const:4:8"]]
+ 00b7fb54 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b7fa8c bytes 256e0194
+ 00b7fb54 bytes 1f6e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f19e06fbd5366939128ac52a6dc0c2e5"></a>

### [`00b7fbc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fbc0.md) → [`00b7fc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fc88.md) FUN_00b7fc88

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7fbb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fbb8.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00b7fc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fc80.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

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
    "old": {
      "definition_site": "00b7fc14",
      "incomplete_value": true,
      "site": "00b7fc18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
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
      "00b7fcdc",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fcdc",
      "PARAM",
      [
        "storage",
        "010a2770",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7fcdc",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fcdc",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7fc18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fbc0.md#insn-00b7fc18) · [`00b7fbec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fbc0.md#insn-00b7fbec) · [`00b7fc08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fbc0.md#insn-00b7fc08)
- 新版 `00b7fce0`（命令位置の公開資料なし） · `00b7fcb4`（命令位置の公開資料なし） · `00b7fcd0`（命令位置の公開資料なし）

~~~diff
- 00b7fc18 ["INT_ADD", "register:40f0:8", ["const:b7fc18:8", "const:4:8"]]
- 00b7fc18 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b7fce0 ["INT_ADD", "register:40f0:8", ["const:b7fce0:8", "const:4:8"]]
+ 00b7fce0 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b7fc18 bytes c66d0194
+ 00b7fce0 bytes c06d0194
- 00b7fbec ["INT_ADD", "register:40f0:8", ["const:b7fbec:8", "const:4:8"]]
- 00b7fbec ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b7fcb4 ["INT_ADD", "register:40f0:8", ["const:b7fcb4:8", "const:4:8"]]
+ 00b7fcb4 ["CALL", null, ["callee:00bdcf30:8"]]
- 00b7fbec bytes a5740194
+ 00b7fcb4 bytes 9f740194
- 00b7fc08 ["INT_ADD", "register:40f0:8", ["const:b7fc08:8", "const:4:8"]]
- 00b7fc08 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b7fcd0 ["INT_ADD", "register:40f0:8", ["const:b7fcd0:8", "const:4:8"]]
+ 00b7fcd0 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b7fc08 bytes c66d0194
+ 00b7fcd0 bytes c06d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e54ef05b98650e451ad333373a6e7dcc"></a>

### [`00b7fcf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fcf8.md) → [`00b7fdc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fdc0.md) FUN_00b7fdc0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7fcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fcf0.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00b7fdb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fdb8.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

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
    "old": {
      "definition_site": "00b7fd4c",
      "incomplete_value": true,
      "site": "00b7fd50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
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
      "00b7fe14",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fe14",
      "PARAM",
      [
        "storage",
        "010a2770",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7fe14",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fe14",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7fd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fcf8.md#insn-00b7fd50) · [`00b7fd24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fcf8.md#insn-00b7fd24) · [`00b7fd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fcf8.md#insn-00b7fd40)
- 新版 `00b7fe18`（命令位置の公開資料なし） · `00b7fdec`（命令位置の公開資料なし） · `00b7fe08`（命令位置の公開資料なし）

~~~diff
- 00b7fd50 ["INT_ADD", "register:40f0:8", ["const:b7fd50:8", "const:4:8"]]
- 00b7fd50 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b7fe18 ["INT_ADD", "register:40f0:8", ["const:b7fe18:8", "const:4:8"]]
+ 00b7fe18 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b7fd50 bytes 786d0194
+ 00b7fe18 bytes 726d0194
- 00b7fd24 ["INT_ADD", "register:40f0:8", ["const:b7fd24:8", "const:4:8"]]
- 00b7fd24 ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b7fdec ["INT_ADD", "register:40f0:8", ["const:b7fdec:8", "const:4:8"]]
+ 00b7fdec ["CALL", null, ["callee:00bdcf30:8"]]
- 00b7fd24 bytes 57740194
+ 00b7fdec bytes 51740194
- 00b7fd40 ["INT_ADD", "register:40f0:8", ["const:b7fd40:8", "const:4:8"]]
- 00b7fd40 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b7fe08 ["INT_ADD", "register:40f0:8", ["const:b7fe08:8", "const:4:8"]]
+ 00b7fe08 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b7fd40 bytes 786d0194
+ 00b7fe08 bytes 726d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21bb981350a948b4756f2bd0b52f6c8a"></a>

### [`00b7fe30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fe30.md) → [`00b7fef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fef8.md) FUN_00b7fef8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b7fe28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fe28.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00b7fef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fef0.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b7fe84",
      "incomplete_value": true,
      "site": "00b7fe88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
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
      "unmatched:00b7fe84",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b7fe84",
      "PARAM",
      [
        "storage",
        "010a2770",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7ff4c",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ff4c",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7fe88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fe30.md#insn-00b7fe88) · [`00b7fe5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fe30.md#insn-00b7fe5c) · [`00b7fe64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7fe30.md#insn-00b7fe64)
- 新版 `00b7ff50`（命令位置の公開資料なし） · `00b7ff24`（命令位置の公開資料なし） · `00b7ff2c`（命令位置の公開資料なし）

~~~diff
- 00b7fe88 ["INT_ADD", "register:40f0:8", ["const:b7fe88:8", "const:4:8"]]
- 00b7fe88 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b7ff50 ["INT_ADD", "register:40f0:8", ["const:b7ff50:8", "const:4:8"]]
+ 00b7ff50 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b7fe88 bytes 2a6d0194
+ 00b7ff50 bytes 246d0194
- 00b7fe5c ["INT_ADD", "register:40f0:8", ["const:b7fe5c:8", "const:4:8"]]
- 00b7fe5c ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b7ff24 ["INT_ADD", "register:40f0:8", ["const:b7ff24:8", "const:4:8"]]
+ 00b7ff24 ["CALL", null, ["callee:00bdcf30:8"]]
- 00b7fe5c bytes 09740194
+ 00b7ff24 bytes 03740194
- 00b7fe64 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b7fe64 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b7ff2c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b7ff2c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b7fe64 bytes a8030034
+ 00b7ff2c bytes a8030034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcc77e0af6f432ef7801e91e9410f5b5"></a>

### [`00b7ff68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7ff68.md) → [`00b80030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80030.md) FUN_00b80030

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b7ff60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7ff60.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00b80028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80028.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 47.92% / 新版 47.92%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7ff90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b80058"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8004c",
      "incomplete_value": true,
      "site": "00b8005c",
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
    "old": {
      "definition_site": "00b7ff84",
      "incomplete_value": true,
      "site": "00b7ff94",
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
      "unmatched:00b7ff90",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7ffb0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb3d0"
      ]
    ],
    [
      "unmatched:00b7ffbc",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b80058",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ],
    [
      "00b80078",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb3d0"
      ]
    ],
    [
      "00b80084",
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

- 旧版 [`00b7ff90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7ff68.md#insn-00b7ff90) · [`00b7ff94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7ff68.md#insn-00b7ff94) · [`00b7ffb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7f/00b7ff68.md#insn-00b7ffb0)
- 新版 `00b8005c`（命令位置の公開資料なし）

~~~diff
- 00b7ff90 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b7ff90 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b7ff90 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:fffffffffffffffc:8"]]
- 00b7ff90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 00b7ff90 bytes bfc31fb8
- 00b7ff94 ["INT_ADD", "register:40f0:8", ["const:b7ff94:8", "const:4:8"]]
- 00b7ff94 ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b8005c ["INT_ADD", "register:40f0:8", ["const:b8005c:8", "const:4:8"]]
+ 00b8005c ["CALL", null, ["callee:00bdcf30:8"]]
- 00b7ff94 bytes bb730194
+ 00b8005c bytes b5730194
- 00b7ffb0 ["INT_ADD", "register:40f0:8", ["const:b7ffb0:8", "const:4:8"]]
- 00b7ffb0 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b7ffb0 bytes dc6c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b85df1312b7144102d750c0e1e7a1f8"></a>

### [`00b800a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b800a0.md) → [`00b80168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80168.md) FUN_00b80168

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b80098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80098.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00b80160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80160.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 12.50% / 新版 5.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b800a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b800a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b800ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b800a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b800ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b800c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b80170",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b80174",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b80190",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b800a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b800a0.md#insn-00b800a8) · [`00b800ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b800a0.md#insn-00b800ac) · [`00b800c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b800a0.md#insn-00b800c8)

~~~diff
- 00b800a8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b800a8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b800a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b800a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b800a8 bytes fd7b01a9
- 00b800ac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b800ac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b800ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b800ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b800ac bytes f44f02a9
- 00b800c8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b800c8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b800c8 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:fffffffffffffffc:8"]]
- 00b800c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 00b800c8 bytes bfc31fb8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d03a7231a97171d1d820c02fbc258544"></a>

### [`00b801d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b801d8.md) → [`00b802a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b802a0.md) FUN_00b802a0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b801d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b801d0.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00b80298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80298.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b801e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b801e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b801e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b801e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b801e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b80200",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b802a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b802ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b802c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b801e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b801d8.md#insn-00b801e0) · [`00b801e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b801d8.md#insn-00b801e4) · [`00b80200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b801d8.md#insn-00b80200)

~~~diff
- 00b801e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b801e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b801e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b801e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b801e0 bytes fd7b01a9
- 00b801e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b801e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b801e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b801e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b801e4 bytes f44f02a9
- 00b80200 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b80200 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b80200 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:fffffffffffffffc:8"]]
- 00b80200 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 00b80200 bytes bfc31fb8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8484009db01b9dd6ab1ad81304c542f2"></a>

### [`00b80308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80308.md) → [`00b803d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b803d0.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsERd

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b80310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80310.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b803d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b803d8.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8030c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b803d8"
      ]
    ]
  ],
  "added": [
    [
      "00b803d4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b803d8"
      ]
    ]
  ]
}
~~~


<a id="compare-5cdb5499dc5755f053f686acae8e16b7"></a>

### [`00b80310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80310.md) → [`00b803d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b803d8.md) FUN_00b803d8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b80308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80308.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00b803d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b803d0.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_call_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b8032c",
      "incomplete_value": true,
      "site": "00b8033c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b80330",
      "incomplete_value": true,
      "site": "00b8033c",
      "value": [
        "live",
        "register:4000:8"
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
      "definition_site": "00b80334",
      "incomplete_value": false,
      "site": "00b8033c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "leaf",
            "const:0:4"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b80358",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb3d0"
      ]
    ],
    [
      "unmatched:00b80364",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b80364",
      "PARAM",
      [
        "storage",
        "010a2770",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b80420",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb3d0"
      ]
    ],
    [
      "00b8042c",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b8042c",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8033c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80310.md#insn-00b8033c) · [`00b80358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80310.md#insn-00b80358) · [`00b80368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80310.md#insn-00b80368)
- 新版 `00b80404`（命令位置の公開資料なし） · `00b80430`（命令位置の公開資料なし）

~~~diff
- 00b8033c ["INT_ADD", "register:40f0:8", ["const:b8033c:8", "const:4:8"]]
- 00b8033c ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b80404 ["INT_ADD", "register:40f0:8", ["const:b80404:8", "const:4:8"]]
+ 00b80404 ["CALL", null, ["callee:00bdcf30:8"]]
- 00b8033c bytes d1720194
+ 00b80404 bytes cb720194
- 00b80358 ["INT_ADD", "register:40f0:8", ["const:b80358:8", "const:4:8"]]
- 00b80358 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b80358 bytes f26b0194
- 00b80368 ["INT_ADD", "register:40f0:8", ["const:b80368:8", "const:4:8"]]
- 00b80368 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b80430 ["INT_ADD", "register:40f0:8", ["const:b80430:8", "const:4:8"]]
+ 00b80430 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b80368 bytes f26b0194
+ 00b80430 bytes ec6b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9754f33b0532747be9684a4ff39508b6"></a>

### [`00b80448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80448.md) → [`00b80510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80510.md) FUN_00b80510

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b80440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80440.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00b80508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80508.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 39.58% / 新版 39.58%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b80470"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b80538"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8052c",
      "incomplete_value": true,
      "site": "00b8053c",
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
    "old": null,
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
      "unmatched:00b80470",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b80490",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb3d0"
      ]
    ],
    [
      "unmatched:00b8049c",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b80538",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ],
    [
      "00b80558",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb3d0"
      ]
    ],
    [
      "00b80564",
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

- 旧版 [`00b80470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80448.md#insn-00b80470) · [`00b80474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80448.md#insn-00b80474) · [`00b80490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80448.md#insn-00b80490)
- 新版 `00b8053c`（命令位置の公開資料なし）

~~~diff
- 00b80470 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b80470 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b80470 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:fffffffffffffffc:8"]]
- 00b80470 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 00b80470 bytes bfc31fb8
- 00b80474 ["INT_ADD", "register:40f0:8", ["const:b80474:8", "const:4:8"]]
- 00b80474 ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b8053c ["INT_ADD", "register:40f0:8", ["const:b8053c:8", "const:4:8"]]
+ 00b8053c ["CALL", null, ["callee:00bdcf30:8"]]
- 00b80474 bytes 83720194
+ 00b8053c bytes 7d720194
- 00b80490 ["INT_ADD", "register:40f0:8", ["const:b80490:8", "const:4:8"]]
- 00b80490 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b80490 bytes a46b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-972b472caf9077b496d261b036e41e5f"></a>

### [`00b80580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80580.md) → [`00b80648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80648.md) FUN_00b80648

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b80578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80578.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00b80640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80640.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 85.42% / 新版 85.42%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b805d4",
      "incomplete_value": true,
      "site": "00b805d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b80600"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b806c8"
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
      "unmatched:00b805d4",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b805d4",
      "PARAM",
      [
        "storage",
        "010a2770",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b80600",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b8069c",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b8069c",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b806c8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b805d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80580.md#insn-00b805d8) · [`00b80600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80580.md#insn-00b80600)
- 新版 `00b806a0`（命令位置の公開資料なし） · `00b806c8`（命令位置の公開資料なし）

~~~diff
- 00b805d8 ["INT_ADD", "register:40f0:8", ["const:b805d8:8", "const:4:8"]]
- 00b805d8 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b806a0 ["INT_ADD", "register:40f0:8", ["const:b806a0:8", "const:4:8"]]
+ 00b806a0 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b805d8 bytes 566b0194
+ 00b806a0 bytes 506b0194
- 00b80600 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80600 ["INT_ADD", "register:40f0:8", ["const:b80600:8", "const:4:8"]]
- 00b80600 ["CALLIND", null, ["register:0:8"]]
- 00b80600 bytes 00013fd6
+ 00b806c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b806c8 ["INT_ADD", "register:40f0:8", ["const:b806c8:8", "const:4:8"]]
+ 00b806c8 ["CALLIND", null, ["register:0:8"]]
+ 00b806c8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ff449a9daa652a47aba1dcd363b11f0"></a>

### [`00b806b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b806b0.md) → [`00b80778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80778.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00be1260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1260.md) · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00be1310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1310.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 75.00% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b806d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b806b0.md#insn-00b806d8) · [`00b806e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b806b0.md#insn-00b806e0) · [`00b806fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b806b0.md#insn-00b806fc)
- 新版 `00b807a0`（命令位置の公開資料なし） · `00b807a8`（命令位置の公開資料なし） · `00b807c4`（命令位置の公開資料なし）

~~~diff
- 00b806d8 ["INT_ADD", "register:40f0:8", ["const:b806d8:8", "const:4:8"]]
- 00b806d8 ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b807a0 ["INT_ADD", "register:40f0:8", ["const:b807a0:8", "const:4:8"]]
+ 00b807a0 ["CALL", null, ["callee:00bdcf30:8"]]
- 00b806d8 bytes ea710194
+ 00b807a0 bytes e4710194
- 00b806e0 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b806e0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b807a8 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b807a8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b806e0 bytes 88010034
+ 00b807a8 bytes 88010034
- 00b806fc ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00b807c4 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b806fc bytes e0000054
+ 00b807c4 bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cacadd3a74ed8d1706b46c0518806a99"></a>

### [`00b80804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80804.md) → [`00b808cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b808cc.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEPcl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00be1270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1270.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be1320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1320.md)

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
    "old": {
      "definition_site": "00b80844",
      "incomplete_value": true,
      "site": "00b80848",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "00b8090c",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00b8090c",
      "PARAM",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b8090c",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b8090c",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80804.md#insn-00b80848) · [`00b80838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80804.md#insn-00b80838) · [`00b80844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80804.md#insn-00b80844)
- 新版 `00b80910`（命令位置の公開資料なし） · `00b80900`（命令位置の公開資料なし） · `00b8090c`（命令位置の公開資料なし）

~~~diff
- 00b80848 ["INT_ADD", "register:40f0:8", ["const:b80848:8", "const:4:8"]]
- 00b80848 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b80910 ["INT_ADD", "register:40f0:8", ["const:b80910:8", "const:4:8"]]
+ 00b80910 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b80848 bytes ba6a0194
+ 00b80910 bytes b46a0194
- 00b80838 ["INT_ADD", "register:40f0:8", ["const:b80838:8", "const:4:8"]]
- 00b80838 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b80900 ["INT_ADD", "register:40f0:8", ["const:b80900:8", "const:4:8"]]
+ 00b80900 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b80838 bytes ba6a0194
+ 00b80900 bytes b46a0194
- 00b80844 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d40:8"]]
- 00b80844 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b8090c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
+ 00b8090c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b80844 bytes 21a046f9
+ 00b8090c bytes 21f846f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cd8b2f05112277c5e66e1304193c2b5"></a>

### [`00b80a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80a7c.md) → [`00b80b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80b44.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00be1280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1280.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be1330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1330.md)

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
    "old": {
      "definition_site": "00b80ab4",
      "incomplete_value": true,
      "site": "00b80ab8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "00b80b7c",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00b80b7c",
      "PARAM",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b80b7c",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b80b7c",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80ab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80a7c.md#insn-00b80ab8) · [`00b80aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80a7c.md#insn-00b80aa8) · [`00b80ab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80a7c.md#insn-00b80ab4)
- 新版 `00b80b80`（命令位置の公開資料なし） · `00b80b70`（命令位置の公開資料なし） · `00b80b7c`（命令位置の公開資料なし）

~~~diff
- 00b80ab8 ["INT_ADD", "register:40f0:8", ["const:b80ab8:8", "const:4:8"]]
- 00b80ab8 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b80b80 ["INT_ADD", "register:40f0:8", ["const:b80b80:8", "const:4:8"]]
+ 00b80b80 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b80ab8 bytes 1e6a0194
+ 00b80b80 bytes 186a0194
- 00b80aa8 ["INT_ADD", "register:40f0:8", ["const:b80aa8:8", "const:4:8"]]
- 00b80aa8 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b80b70 ["INT_ADD", "register:40f0:8", ["const:b80b70:8", "const:4:8"]]
+ 00b80b70 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b80aa8 bytes 1e6a0194
+ 00b80b70 bytes 186a0194
- 00b80ab4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d40:8"]]
- 00b80ab4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b80b7c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
+ 00b80b7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b80ab4 bytes 21a046f9
+ 00b80b7c bytes 21f846f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23308068ed27c7885a59ea7c644a9646"></a>

### [`00b80c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80c80.md) → [`00b80d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80d48.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPcl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00be1290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1290.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be1340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1340.md)

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
    "old": {
      "definition_site": "00b80cc0",
      "incomplete_value": true,
      "site": "00b80cc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "00b80d88",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00b80d88",
      "PARAM",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b80d88",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b80d88",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80c80.md#insn-00b80cc4) · [`00b80cb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80c80.md#insn-00b80cb4) · [`00b80cc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b80/00b80c80.md#insn-00b80cc0)
- 新版 `00b80d8c`（命令位置の公開資料なし） · `00b80d7c`（命令位置の公開資料なし） · `00b80d88`（命令位置の公開資料なし）

~~~diff
- 00b80cc4 ["INT_ADD", "register:40f0:8", ["const:b80cc4:8", "const:4:8"]]
- 00b80cc4 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b80d8c ["INT_ADD", "register:40f0:8", ["const:b80d8c:8", "const:4:8"]]
+ 00b80d8c ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b80cc4 bytes 9b690194
+ 00b80d8c bytes 95690194
- 00b80cb4 ["INT_ADD", "register:40f0:8", ["const:b80cb4:8", "const:4:8"]]
- 00b80cb4 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b80d7c ["INT_ADD", "register:40f0:8", ["const:b80d7c:8", "const:4:8"]]
+ 00b80d7c ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b80cb4 bytes 9b690194
+ 00b80d7c bytes 95690194
- 00b80cc0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d40:8"]]
- 00b80cc0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b80d88 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
+ 00b80d88 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b80cc0 bytes 21a046f9
+ 00b80d88 bytes 21f846f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75949ab76edad6dc250d5f9a85fcdd64"></a>

### [`00b81124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81124.md) → [`00b811ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b811ec.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4peekEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.74% / 新版 76.74%

CFGの説明率　旧版 33.33% / 新版 23.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8112c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8112c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81130"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8112c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b81130",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8118c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b811f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b811f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b81254",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8112c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81124.md#insn-00b8112c) · [`00b81130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81124.md#insn-00b81130) · [`00b8113c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81124.md#insn-00b8113c)

~~~diff
- 00b8112c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b8112c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b8112c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b8112c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8112c bytes fd7b01a9
- 00b81130 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b81130 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b81130 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b81130 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b81130 bytes f44f02a9
- 00b8113c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00b8113c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b8113c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b8113c bytes 1f0400f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69e3228fdaac4866a1b3756690ff0824"></a>

### [`00b81224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81224.md) → [`00b812ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b812ec.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4readEPcl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdc180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc180.md) · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00bdc230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc230.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8128c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b81354"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81290"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b81280",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b81348",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81254`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81224.md#insn-00b81254) · [`00b81280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81224.md#insn-00b81280) · [`00b8128c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81224.md#insn-00b8128c)
- 新版 `00b8131c`（命令位置の公開資料なし）

~~~diff
- 00b81254 ["INT_ADD", "register:40f0:8", ["const:b81254:8", "const:4:8"]]
- 00b81254 ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b8131c ["INT_ADD", "register:40f0:8", ["const:b8131c:8", "const:4:8"]]
+ 00b8131c ["CALL", null, ["callee:00bdcf30:8"]]
- 00b81254 bytes 0b6f0194
+ 00b8131c bytes 056f0194
- 00b81280 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b81280 ["INT_ADD", "register:40f0:8", ["const:b81280:8", "const:4:8"]]
- 00b81280 ["CALLIND", null, ["register:0:8"]]
- 00b81280 bytes 00013fd6
- 00b8128c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00b8128c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b8128c bytes 600600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a86eb1e036599557262ce2743b9127f6"></a>

### [`00b8131c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b8131c.md) → [`00b813e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b813e4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE8readsomeEPcl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 22.22% / 新版 23.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b813e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b814b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b81408",
      "incomplete_value": true,
      "site": "00b81414",
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
            "const:1c:8"
          ]
        ]
      ]
    },
    "old": null,
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
      "00b81448",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b813ec"
      ]
    ],
    [
      "00b81468",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b813ec"
      ]
    ],
    [
      "00b81470",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b813ec"
      ]
    ]
  ],
  "added": [
    [
      "00b81448",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b814b4"
      ]
    ],
    [
      "00b81468",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b814b4"
      ]
    ],
    [
      "00b81470",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b814b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8134c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b8131c.md#insn-00b8134c) · [`00b813e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b8131c.md#insn-00b813e8) · [`00b81400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b8131c.md#insn-00b81400)
- 新版 `00b81414`（命令位置の公開資料なし） · `00b814c8`（命令位置の公開資料なし）

~~~diff
- 00b8134c ["INT_ADD", "register:40f0:8", ["const:b8134c:8", "const:4:8"]]
- 00b8134c ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b81414 ["INT_ADD", "register:40f0:8", ["const:b81414:8", "const:4:8"]]
+ 00b81414 ["CALL", null, ["callee:00bdcf30:8"]]
- 00b8134c bytes cd6e0194
+ 00b81414 bytes c76e0194
- 00b813e8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b813e8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b813e8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b813e8 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b813e8 bytes e803881a
- 00b81400 ["INT_ADD", "register:40f0:8", ["const:b81400:8", "const:4:8"]]
- 00b81400 ["CALL", null, ["callee:00bdb400:8"]]
+ 00b814c8 ["INT_ADD", "register:40f0:8", ["const:b814c8:8", "const:4:8"]]
+ 00b814c8 ["CALL", null, ["callee:00bdb400:8"]]
- 00b81400 bytes d4670194
+ 00b814c8 bytes ce670194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c6c9475c952a21127e9c4fd02054b8a"></a>

### [`00b8146c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b8146c.md) → [`00b81534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81534.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7putbackEc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.72% / 新版 87.72%

CFGの説明率　旧版 26.67% / 新版 23.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81490"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b81558"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b81568",
      "incomplete_value": true,
      "site": "00b81574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
    "old": null,
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
      "unmatched:00b81510",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b815d8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b8146c.md#insn-00b81490) · [`00b814ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b8146c.md#insn-00b814ac) · [`00b81510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b8146c.md#insn-00b81510)
- 新版 `00b81574`（命令位置の公開資料なし）

~~~diff
- 00b81490 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00b81490 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b81490 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b81490 bytes 1f0400f9
- 00b814ac ["INT_ADD", "register:40f0:8", ["const:b814ac:8", "const:4:8"]]
- 00b814ac ["CALL", null, ["callee:00bdb400:8"]]
+ 00b81574 ["INT_ADD", "register:40f0:8", ["const:b81574:8", "const:4:8"]]
+ 00b81574 ["CALL", null, ["callee:00bdb400:8"]]
- 00b814ac bytes a9670194
+ 00b81574 bytes a3670194
- 00b81510 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b81510 ["INT_ADD", "register:40f0:8", ["const:b81510:8", "const:4:8"]]
- 00b81510 ["CALLIND", null, ["register:0:8"]]
- 00b81510 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc91f8c5673bc13603c05c01bd3ebca2"></a>

### [`00b815a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b815a0.md) → [`00b81668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81668.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5ungetEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, unresolved_branch_alignment

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 18.75% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81614"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b816dc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b81698",
      "incomplete_value": true,
      "site": "00b816a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
    "old": null,
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
      "unmatched:00b81614",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b816f4"
      ]
    ]
  ],
  "added": [
    [
      "00b816dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b816f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b815dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b815a0.md#insn-00b815dc) · [`00b81614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b815a0.md#insn-00b81614) · [`00b8165c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b815a0.md#insn-00b8165c)
- 新版 `00b816a4`（命令位置の公開資料なし） · `00b81724`（命令位置の公開資料なし）

~~~diff
- 00b815dc ["INT_ADD", "register:40f0:8", ["const:b815dc:8", "const:4:8"]]
- 00b815dc ["CALL", null, ["callee:00bdb400:8"]]
+ 00b816a4 ["INT_ADD", "register:40f0:8", ["const:b816a4:8", "const:4:8"]]
+ 00b816a4 ["CALL", null, ["callee:00bdb400:8"]]
- 00b815dc bytes 5d670194
+ 00b816a4 bytes 57670194
- 00b81614 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00b81614 bytes c0000054
- 00b8165c ["INT_ADD", "register:40f0:8", ["const:b8165c:8", "const:4:8"]]
- 00b8165c ["CALL", null, ["callee:00bdb400:8"]]
+ 00b81724 ["INT_ADD", "register:40f0:8", ["const:b81724:8", "const:4:8"]]
+ 00b81724 ["CALL", null, ["callee:00bdb400:8"]]
- 00b8165c bytes 3d670194
+ 00b81724 bytes 37670194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-194258095593dd0c94251532aae5b915"></a>

### [`00b816c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b816c8.md) → [`00b81790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81790.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4syncEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 30.00% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81700"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b817c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00b8174c",
      "incomplete_value": true,
      "site": "00b81760",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a0:4"
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
      "unmatched:00b81700",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b81808"
      ]
    ]
  ],
  "added": [
    [
      "00b817c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b81808"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b816c8.md#insn-00b81700) · [`00b816ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b816c8.md#insn-00b816ec)
- 新版 `00b817c8`（命令位置の公開資料なし） · `00b817b4`（命令位置の公開資料なし）

~~~diff
- 00b81700 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b81700 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b81700 bytes 000200b4
+ 00b817c8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b817c8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b817c8 bytes 000200b4
- 00b816ec ["INT_ADD", "register:40f0:8", ["const:b816ec:8", "const:4:8"]]
- 00b816ec ["CALL", null, ["callee:00bdcf30:8"]]
+ 00b817b4 ["INT_ADD", "register:40f0:8", ["const:b817b4:8", "const:4:8"]]
+ 00b817b4 ["CALL", null, ["callee:00bdcf30:8"]]
- 00b816ec bytes e56d0194
+ 00b817b4 bytes df6d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d964584c8503c028bdbd0807318e188"></a>

### [`00b817b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b817b8.md) → [`00b81880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81880.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5seekgENS_4fposI9mbstate_tEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdc8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc8b0.md) · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce80.md)
- 新版 呼出元 1件 [`00bdc960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc960.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.58% / 新版 64.58%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b817c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b817c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b817c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b817c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b817c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b817c8",
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
      "00b81888",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b8188c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b81890",
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

- 旧版 [`00b817c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b817b8.md#insn-00b817c0) · [`00b817c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b817b8.md#insn-00b817c4) · [`00b817c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b817b8.md#insn-00b817c8)

~~~diff
- 00b817c0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b817c0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b817c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b817c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b817c0 bytes fd7b01a9
- 00b817c4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b817c4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b817c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b817c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b817c4 bytes f65702a9
- 00b817c8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b817c8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b817c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b817c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b817c8 bytes f44f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af35036d483d9a18cd315ac183ed887f"></a>

### [`00b818c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b818c8.md) → [`00b81990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81990.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b818cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b818cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b818d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b818cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b818d0",
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
      "00b81994",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b81998",
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

- 旧版 [`00b818cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b818c8.md#insn-00b818cc) · [`00b818d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b818c8.md#insn-00b818d0) · [`00b818dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b818c8.md#insn-00b818dc)

~~~diff
- 00b818cc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b818cc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b818cc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b818cc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b818cc bytes fd7bbea9
- 00b818d0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b818d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b818d0 bytes f30b00f9
- 00b818dc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b818dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b818dc bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20e1d5e943d19500654d99c382d7592a"></a>

### [`00b819f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b819f8.md) → [`00b81ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81ac0.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb310.md) · 呼出先 1件 [`00bdbfa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbfa0.md)
- 新版 呼出元 1件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) · 呼出先 1件 [`00bdc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc050.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 3件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81a14"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81a20"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b81adc"
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
      "unmatched:00b81a14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b81a1c"
      ]
    ],
    [
      "unmatched:00b81a20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b81b18"
      ]
    ]
  ],
  "added": [
    [
      "00b81adc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b81ae4"
      ]
    ],
    [
      "00b81ae8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b81b18"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b819f8.md#insn-00b81a14) · [`00b81a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b819f8.md#insn-00b81a20) · [`00b81a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b819f8.md#insn-00b81a3c)
- 新版 `00b81b04`（命令位置の公開資料なし）

~~~diff
- 00b81a14 ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b81a14 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b81a14 bytes 49000034
- 00b81a20 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b81a20 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b81a20 bytes 880100b4
- 00b81a3c ["INT_ADD", "register:40f0:8", ["const:b81a3c:8", "const:4:8"]]
- 00b81a3c ["CALL", null, ["callee:00bdc050:8"]]
+ 00b81b04 ["INT_ADD", "register:40f0:8", ["const:b81b04:8", "const:4:8"]]
+ 00b81b04 ["CALL", null, ["callee:00bdc050:8"]]
- 00b81a3c bytes 59690194
+ 00b81b04 bytes 53690194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c70d433a1aba35e59afc678d99a4e41"></a>

### [`00b81a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81a5c.md) → [`00b81b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81b24.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb360.md) · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be00f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00f0.md)
- 新版 呼出元 1件 [`00bdb410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb410.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be01a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 68.42% / 新版 68.42%

CFGの説明率　旧版 33.33% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81a80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81ac4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b81b48"
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
      "unmatched:00b81a80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b81bac"
      ]
    ],
    [
      "unmatched:00b81ac4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b81bac"
      ]
    ],
    [
      "unmatched:00b81abc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b81b48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b81bac"
      ]
    ],
    [
      "00b81b8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b81bac"
      ]
    ],
    [
      "00b81b84",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81a5c.md#insn-00b81a80) · [`00b81abc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81a5c.md#insn-00b81abc) · [`00b81ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81a5c.md#insn-00b81ac4)

~~~diff
- 00b81a80 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b81a80 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b81a80 bytes 290300b4
- 00b81abc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b81abc ["INT_ADD", "register:40f0:8", ["const:b81abc:8", "const:4:8"]]
- 00b81abc ["CALLIND", null, ["register:0:8"]]
- 00b81abc bytes 00013fd6
- 00b81ac4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b81ac4 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b81ac4 bytes 01010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-495218d84741b80677cba39e812e848f"></a>

### [`00b81b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81b80.md) → [`00b81c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81c48.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb310.md) [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md)

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
    "old": {
      "definition_site": "00b81bd4",
      "incomplete_value": true,
      "site": "00b81bd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
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
    "old": {
      "definition_site": "00b81c1c",
      "incomplete_value": true,
      "site": "00b81c20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "00b81c9c",
      "READ",
      [
        "storage",
        "00c1b940",
        null,
        "pointer"
      ]
    ],
    [
      "00b81c9c",
      "PARAM",
      [
        "storage",
        "010a2790",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b81ce4",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b81c9c",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b81c9c",
      "PARAM",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b81ce4",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81b80.md#insn-00b81bd8) · [`00b81c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81b80.md#insn-00b81c20) · [`00b81bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81b80.md#insn-00b81bac)
- 新版 `00b81ca0`（命令位置の公開資料なし） · `00b81ce8`（命令位置の公開資料なし） · `00b81c74`（命令位置の公開資料なし）

~~~diff
- 00b81bd8 ["INT_ADD", "register:40f0:8", ["const:b81bd8:8", "const:4:8"]]
- 00b81bd8 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b81ca0 ["INT_ADD", "register:40f0:8", ["const:b81ca0:8", "const:4:8"]]
+ 00b81ca0 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b81bd8 bytes d6650194
+ 00b81ca0 bytes d0650194
- 00b81c20 ["INT_ADD", "register:40f0:8", ["const:b81c20:8", "const:4:8"]]
- 00b81c20 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b81ce8 ["INT_ADD", "register:40f0:8", ["const:b81ce8:8", "const:4:8"]]
+ 00b81ce8 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b81c20 bytes c4650194
+ 00b81ce8 bytes be650194
- 00b81bac ["INT_ADD", "register:40f0:8", ["const:b81bac:8", "const:4:8"]]
- 00b81bac ["CALL", null, ["callee:00bdb3c0:8"]]
+ 00b81c74 ["INT_ADD", "register:40f0:8", ["const:b81c74:8", "const:4:8"]]
+ 00b81c74 ["CALL", null, ["callee:00bdb3c0:8"]]
- 00b81bac bytes d9650194
+ 00b81c74 bytes d3650194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7563097a16afbd1a5a2b2860be722d8"></a>

### [`00b81d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81d10.md) → [`00b81dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81dd8.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEx

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb310.md) [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 11.11% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b81d64",
      "incomplete_value": true,
      "site": "00b81d68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
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
    "old": {
      "definition_site": "00b81dac",
      "incomplete_value": true,
      "site": "00b81db0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "unmatched:00b81d64",
      "READ",
      [
        "storage",
        "00c1b940",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b81d64",
      "PARAM",
      [
        "storage",
        "010a2790",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b81dac",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b81e2c",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b81e2c",
      "PARAM",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b81e74",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81d68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81d10.md#insn-00b81d68) · [`00b81db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81d10.md#insn-00b81db0) · [`00b81d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81d10.md#insn-00b81d3c)
- 新版 `00b81e30`（命令位置の公開資料なし） · `00b81e78`（命令位置の公開資料なし） · `00b81e04`（命令位置の公開資料なし）

~~~diff
- 00b81d68 ["INT_ADD", "register:40f0:8", ["const:b81d68:8", "const:4:8"]]
- 00b81d68 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b81e30 ["INT_ADD", "register:40f0:8", ["const:b81e30:8", "const:4:8"]]
+ 00b81e30 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b81d68 bytes 72650194
+ 00b81e30 bytes 6c650194
- 00b81db0 ["INT_ADD", "register:40f0:8", ["const:b81db0:8", "const:4:8"]]
- 00b81db0 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b81e78 ["INT_ADD", "register:40f0:8", ["const:b81e78:8", "const:4:8"]]
+ 00b81e78 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b81db0 bytes 60650194
+ 00b81e78 bytes 5a650194
- 00b81d3c ["INT_ADD", "register:40f0:8", ["const:b81d3c:8", "const:4:8"]]
- 00b81d3c ["CALL", null, ["callee:00bdb3c0:8"]]
+ 00b81e04 ["INT_ADD", "register:40f0:8", ["const:b81e04:8", "const:4:8"]]
+ 00b81e04 ["CALL", null, ["callee:00bdb3c0:8"]]
- 00b81d3c bytes 75650194
+ 00b81e04 bytes 6f650194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85386a9f05200a56fa7cb0a0d9eef0b2"></a>

### [`00b81ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81ea0.md) → [`00b81f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81f68.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEy

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb310.md) [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 12.50% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b81ef4",
      "incomplete_value": true,
      "site": "00b81ef8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
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
    "old": {
      "definition_site": "00b81f3c",
      "incomplete_value": true,
      "site": "00b81f40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "unmatched:00b81ef4",
      "READ",
      [
        "storage",
        "00c1b940",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b81ef4",
      "PARAM",
      [
        "storage",
        "010a2790",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b81f3c",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b81fbc",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b81fbc",
      "PARAM",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b82004",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81ef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81ea0.md#insn-00b81ef8) · [`00b81f40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81ea0.md#insn-00b81f40) · [`00b81ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81ea0.md#insn-00b81ecc)
- 新版 `00b81fc0`（命令位置の公開資料なし） · `00b82008`（命令位置の公開資料なし） · `00b81f94`（命令位置の公開資料なし）

~~~diff
- 00b81ef8 ["INT_ADD", "register:40f0:8", ["const:b81ef8:8", "const:4:8"]]
- 00b81ef8 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b81fc0 ["INT_ADD", "register:40f0:8", ["const:b81fc0:8", "const:4:8"]]
+ 00b81fc0 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b81ef8 bytes 0e650194
+ 00b81fc0 bytes 08650194
- 00b81f40 ["INT_ADD", "register:40f0:8", ["const:b81f40:8", "const:4:8"]]
- 00b81f40 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b82008 ["INT_ADD", "register:40f0:8", ["const:b82008:8", "const:4:8"]]
+ 00b82008 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b81f40 bytes fc640194
+ 00b82008 bytes f6640194
- 00b81ecc ["INT_ADD", "register:40f0:8", ["const:b81ecc:8", "const:4:8"]]
- 00b81ecc ["CALL", null, ["callee:00bdb3c0:8"]]
+ 00b81f94 ["INT_ADD", "register:40f0:8", ["const:b81f94:8", "const:4:8"]]
+ 00b81f94 ["CALL", null, ["callee:00bdb3c0:8"]]
- 00b81ecc bytes 11650194
+ 00b81f94 bytes 0b650194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbec0eced5b4fa7a300745f444d99b06"></a>

### [`00b82030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82030.md) → [`00b820f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b820f8.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEf

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb310.md) [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.62% / 新版 76.62%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82038"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8203c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8203c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b82038",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8203c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b82040",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b82100",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b82104",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b82108",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82030.md#insn-00b82038) · [`00b8203c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82030.md#insn-00b8203c) · [`00b82040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82030.md#insn-00b82040)

~~~diff
- 00b82038 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b82038 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 00b82038 bytes e81300fd
- 00b8203c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b8203c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b8203c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:28:8"]]
- 00b8203c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8203c bytes fdfb02a9
- 00b82040 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b82040 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b82040 bytes f71f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecc9c64d71aa98ffad68b750cd630086"></a>

### [`00b821c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b821c8.md) → [`00b82290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82290.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEe

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb310.md) [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.67% / 新版 94.67%

CFGの説明率　旧版 11.11% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b8221c",
      "incomplete_value": true,
      "site": "00b82220",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
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
    "new": null,
    "old": {
      "definition_site": "00b82228",
      "incomplete_value": true,
      "site": "00b8222c",
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
            "const:18:8"
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
    "old": {
      "definition_site": "00b82264",
      "incomplete_value": true,
      "site": "00b82268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "unmatched:00b8221c",
      "READ",
      [
        "storage",
        "00c1b940",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b8221c",
      "PARAM",
      [
        "storage",
        "010a2790",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b82264",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b822e4",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b822e4",
      "PARAM",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b8232c",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b821c8.md#insn-00b82220) · [`00b8222c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b821c8.md#insn-00b8222c) · [`00b82268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b821c8.md#insn-00b82268)
- 新版 `00b822e8`（命令位置の公開資料なし） · `00b822f4`（命令位置の公開資料なし） · `00b82330`（命令位置の公開資料なし）

~~~diff
- 00b82220 ["INT_ADD", "register:40f0:8", ["const:b82220:8", "const:4:8"]]
- 00b82220 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b822e8 ["INT_ADD", "register:40f0:8", ["const:b822e8:8", "const:4:8"]]
+ 00b822e8 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b82220 bytes 44640194
+ 00b822e8 bytes 3e640194
- 00b8222c ["INT_ADD", "register:40f0:8", ["const:b8222c:8", "const:4:8"]]
- 00b8222c ["CALL", null, ["callee:00bdb3f0:8"]]
+ 00b822f4 ["INT_ADD", "register:40f0:8", ["const:b822f4:8", "const:4:8"]]
+ 00b822f4 ["CALL", null, ["callee:00bdb3f0:8"]]
- 00b8222c bytes 45640194
+ 00b822f4 bytes 3f640194
- 00b82268 ["INT_ADD", "register:40f0:8", ["const:b82268:8", "const:4:8"]]
- 00b82268 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b82330 ["INT_ADD", "register:40f0:8", ["const:b82330:8", "const:4:8"]]
+ 00b82330 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b82268 bytes 32640194
+ 00b82330 bytes 2c640194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b171c72a52cd1dc84a7a28900c192687"></a>

### [`00b82358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82358.md) → [`00b82420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82420.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPKv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb310.md) [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 44.44% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b823a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b823ac",
      "incomplete_value": true,
      "site": "00b823b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
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
    "old": {
      "definition_site": "00b823f4",
      "incomplete_value": true,
      "site": "00b823f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "unmatched:00b823a0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb3d0"
      ]
    ],
    [
      "unmatched:00b823ac",
      "READ",
      [
        "storage",
        "00c1b940",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b823ac",
      "PARAM",
      [
        "storage",
        "010a2790",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b82468",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb3d0"
      ]
    ],
    [
      "00b82474",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b82474",
      "PARAM",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b823a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82358.md#insn-00b823a0) · [`00b823b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82358.md#insn-00b823b0) · [`00b823f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82358.md#insn-00b823f8)
- 新版 `00b82478`（命令位置の公開資料なし） · `00b824c0`（命令位置の公開資料なし）

~~~diff
- 00b823a0 ["INT_ADD", "register:40f0:8", ["const:b823a0:8", "const:4:8"]]
- 00b823a0 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b823a0 bytes e0630194
- 00b823b0 ["INT_ADD", "register:40f0:8", ["const:b823b0:8", "const:4:8"]]
- 00b823b0 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b82478 ["INT_ADD", "register:40f0:8", ["const:b82478:8", "const:4:8"]]
+ 00b82478 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b823b0 bytes e0630194
+ 00b82478 bytes da630194
- 00b823f8 ["INT_ADD", "register:40f0:8", ["const:b823f8:8", "const:4:8"]]
- 00b823f8 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b824c0 ["INT_ADD", "register:40f0:8", ["const:b824c0:8", "const:4:8"]]
+ 00b824c0 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b823f8 bytes ce630194
+ 00b824c0 bytes c8630194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-841bd0c43f5130fc68b64d57adab6100"></a>

### [`00b82640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82640.md) → [`00b82708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82708.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5seekpENS_4fposI9mbstate_tEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb310.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdb360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb360.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdb410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb410.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 14.29% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b82780",
      "incomplete_value": true,
      "site": "00b8278c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
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
      "definition_site": "00b826b8",
      "incomplete_value": true,
      "site": "00b826c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "live",
            "register:4040:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b826c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82640.md#insn-00b826c4) · [`00b8266c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82640.md#insn-00b8266c) · [`00b82688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82640.md#insn-00b82688)
- 新版 `00b8278c`（命令位置の公開資料なし） · `00b82734`（命令位置の公開資料なし） · `00b82750`（命令位置の公開資料なし）

~~~diff
- 00b826c4 ["INT_ADD", "register:40f0:8", ["const:b826c4:8", "const:4:8"]]
- 00b826c4 ["CALL", null, ["callee:00bdb400:8"]]
+ 00b8278c ["INT_ADD", "register:40f0:8", ["const:b8278c:8", "const:4:8"]]
+ 00b8278c ["CALL", null, ["callee:00bdb400:8"]]
- 00b826c4 bytes 23630194
+ 00b8278c bytes 1d630194
- 00b8266c ["INT_ADD", "register:40f0:8", ["const:b8266c:8", "const:4:8"]]
- 00b8266c ["CALL", null, ["callee:00bdb3c0:8"]]
+ 00b82734 ["INT_ADD", "register:40f0:8", ["const:b82734:8", "const:4:8"]]
+ 00b82734 ["CALL", null, ["callee:00bdb3c0:8"]]
- 00b8266c bytes 29630194
+ 00b82734 bytes 23630194
- 00b82688 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b82688 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b82750 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b82750 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b82688 bytes 01020054
+ 00b82750 bytes 01020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fd28faad0d98dd8c0c1f25e2cf0d279"></a>

### [`00b82868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82868.md) → [`00b82930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82930.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)

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
    "old": {
      "definition_site": "00b82894",
      "incomplete_value": true,
      "site": "00b82894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "old": {
      "definition_site": "00b82898",
      "incomplete_value": true,
      "site": "00b82898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "old": {
      "definition_site": "00b828b8",
      "incomplete_value": true,
      "site": "00b828c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b8294c",
      "READ",
      [
        "storage",
        "00c1bbf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b8295c",
      "DATA",
      [
        "storage",
        "00c134b0",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00b82960",
      "DATA",
      [
        "storage",
        "00c13488",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00b8294c",
      "READ",
      [
        "storage",
        "00c1bca0",
        null,
        "pointer"
      ]
    ],
    [
      "00b8295c",
      "DATA",
      [
        "storage",
        "00c13560",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00b82960",
      "DATA",
      [
        "storage",
        "00c13538",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82868.md#insn-00b82884) · [`00b828a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82868.md#insn-00b828a0) · [`00b828ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82868.md#insn-00b828ac)
- 新版 `00b8294c`（命令位置の公開資料なし） · `00b82968`（命令位置の公開資料なし） · `00b82974`（命令位置の公開資料なし）

~~~diff
- 00b82884 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bf0:8"]]
- 00b82884 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b8294c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ca0:8"]]
+ 00b8294c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b82884 bytes 08f945f9
+ 00b8294c bytes 085146f9
- 00b828a0 ["INT_ADD", "register:40f0:8", ["const:b828a0:8", "const:4:8"]]
- 00b828a0 ["CALL", null, ["callee:00bdb340:8"]]
+ 00b82968 ["INT_ADD", "register:40f0:8", ["const:b82968:8", "const:4:8"]]
+ 00b82968 ["CALL", null, ["callee:00bdb340:8"]]
- 00b828a0 bytes 7c620194
+ 00b82968 bytes 76620194
- 00b828ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bf8:8"]]
- 00b828ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b82974 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ca8:8"]]
+ 00b82974 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b828ac bytes 08fd45f9
+ 00b82974 bytes 085546f9
~~~


<a id="compare-c173de0e00dd41c866b919b584ef4b72"></a>

### [`00b82928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82928.md) → [`00b829f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b829f0.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82928.md#insn-00b82940)
- 新版 `00b82a08`（命令位置の公開資料なし）

~~~diff
- 00b82940 ["INT_ADD", "register:40f0:8", ["const:b82940:8", "const:4:8"]]
- 00b82940 ["CALL", null, ["callee:00be0190:8"]]
+ 00b82a08 ["INT_ADD", "register:40f0:8", ["const:b82a08:8", "const:4:8"]]
+ 00b82a08 ["CALL", null, ["callee:00be0190:8"]]
- 00b82940 bytes e8750194
+ 00b82a08 bytes e2750194
~~~


<a id="compare-121820c7b16d48ca70b16fc496b10987"></a>

### [`00b829c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b829c0.md) → [`00b82a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82a88.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1220.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.37% / 新版 70.37%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b829d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b829dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b82aa0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b829d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b829c0.md#insn-00b829d8) · [`00b829dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b829c0.md#insn-00b829dc) · [`00b829f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b829c0.md#insn-00b829f8)
- 新版 `00b82ac0`（命令位置の公開資料なし）

~~~diff
- 00b829d8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00b829d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b829d8 bytes 080400f9
- 00b829dc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00b829dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b829dc bytes 290400f9
- 00b829f8 ["INT_ADD", "register:40f0:8", ["const:b829f8:8", "const:4:8"]]
- 00b829f8 ["CALL", null, ["callee:00be12d0:8"]]
+ 00b82ac0 ["INT_ADD", "register:40f0:8", ["const:b82ac0:8", "const:4:8"]]
+ 00b82ac0 ["CALL", null, ["callee:00be12d0:8"]]
- 00b829f8 bytes 0a7a0194
+ 00b82ac0 bytes 047a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44771ce03ebe5554a194f8dac72ced68"></a>

### [`00b82adc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82adc.md) → [`00b82ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82ba4.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 2件 [`00be12c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be12c0.md) [`00be12d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be12d0.md) · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 2件 [`00be1370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1370.md) [`00be1380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1380.md) · 呼出先 1件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b82bb4",
      "incomplete_value": true,
      "site": "00b82bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b82aec",
      "incomplete_value": true,
      "site": "00b82aec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b82bac",
      "READ",
      [
        "storage",
        "00c1bc00",
        null,
        "pointer"
      ]
    ],
    [
      "00b82bb4",
      "DATA",
      [
        "storage",
        "00c130d0",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00b82bac",
      "READ",
      [
        "storage",
        "00c1bcb0",
        null,
        "pointer"
      ]
    ],
    [
      "00b82bb4",
      "DATA",
      [
        "storage",
        "00c13180",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82adc.md#insn-00b82ae4)
- 新版 `00b82bac`（命令位置の公開資料なし）

~~~diff
- 00b82ae4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c00:8"]]
- 00b82ae4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b82bac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb0:8"]]
+ 00b82bac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b82ae4 bytes 080146f9
+ 00b82bac bytes 085946f9
~~~


<a id="compare-2fe906c28c3a99db0396fdb1c4ad3ec4"></a>

### [`00b82af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82af4.md) → [`00b82bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82bbc.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be12d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be12d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1380.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82af4.md#insn-00b82b08)
- 新版 `00b82bd0`（命令位置の公開資料なし）

~~~diff
- 00b82b08 ["INT_ADD", "register:40f0:8", ["const:b82b08:8", "const:4:8"]]
- 00b82b08 ["CALL", null, ["callee:00be1380:8"]]
+ 00b82bd0 ["INT_ADD", "register:40f0:8", ["const:b82bd0:8", "const:4:8"]]
+ 00b82bd0 ["CALL", null, ["callee:00be1380:8"]]
- 00b82b08 bytes f2790194
+ 00b82bd0 bytes ec790194
~~~


<a id="compare-0a2ba81bb74dfc0edb25d028ff887f4d"></a>

### [`00b82d8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82d8c.md) → [`00b82e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82e54.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEC1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be12e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be12e0.md) · 呼出先 1件 [`00bdd850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd850.md)
- 新版 呼出元 1件 [`00be1390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1390.md) · 呼出先 1件 [`00bdd900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd900.md)

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
    "old": {
      "definition_site": "00b82dac",
      "incomplete_value": true,
      "site": "00b82dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b82e6c",
      "READ",
      [
        "storage",
        "00c1bc00",
        null,
        "pointer"
      ]
    ],
    [
      "00b82e74",
      "DATA",
      [
        "storage",
        "00c130d0",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00b82e6c",
      "READ",
      [
        "storage",
        "00c1bcb0",
        null,
        "pointer"
      ]
    ],
    [
      "00b82e74",
      "DATA",
      [
        "storage",
        "00c13180",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82d8c.md#insn-00b82da4) · [`00b82db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82d8c.md#insn-00b82db0)
- 新版 `00b82e6c`（命令位置の公開資料なし） · `00b82e78`（命令位置の公開資料なし）

~~~diff
- 00b82da4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c00:8"]]
- 00b82da4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b82e6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb0:8"]]
+ 00b82e6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b82da4 bytes 080146f9
+ 00b82e6c bytes 085946f9
- 00b82db0 ["INT_ADD", "register:40f0:8", ["const:b82db0:8", "const:4:8"]]
- 00b82db0 ["CALL", null, ["callee:00bdd900:8"]]
+ 00b82e78 ["INT_ADD", "register:40f0:8", ["const:b82e78:8", "const:4:8"]]
+ 00b82e78 ["CALL", null, ["callee:00bdd900:8"]]
- 00b82db0 bytes a86a0194
+ 00b82e78 bytes a26a0194
~~~


<a id="compare-f977466b02389f357eb476ec8a8528be"></a>

### [`00b82dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82dd0.md) → [`00b82e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82e98.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEC2ERKS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82df8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b82ec0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b82de8",
      "incomplete_value": true,
      "site": "00b82dfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "unmatched:00b82dec",
      "READ",
      [
        "storage",
        "00c1bc00",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b82df8",
      "DATA",
      [
        "storage",
        "00c130d0",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00b82eb4",
      "READ",
      [
        "storage",
        "00c1bcb0",
        null,
        "pointer"
      ]
    ],
    [
      "00b82ec0",
      "DATA",
      [
        "storage",
        "00c13180",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82dd0.md#insn-00b82df8) · [`00b82dfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82dd0.md#insn-00b82dfc)
- 新版 `00b82ec4`（命令位置の公開資料なし） · `00b82ec0`（命令位置の公開資料なし）

~~~diff
- 00b82df8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b82df8 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b82df8 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00b82df8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b82df8 bytes 088400f8
- 00b82dfc ["INT_ADD", "register:40f0:8", ["const:b82dfc:8", "const:4:8"]]
- 00b82dfc ["CALL", null, ["callee:00bdd930:8"]]
+ 00b82ec4 ["INT_ADD", "register:40f0:8", ["const:b82ec4:8", "const:4:8"]]
+ 00b82ec4 ["CALL", null, ["callee:00bdd930:8"]]
- 00b82dfc bytes a16a0194
+ 00b82ec4 bytes 9b6a0194
+ 00b82ec0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b82ec0 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00b82ec0 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
+ 00b82ec0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00b82ec0 bytes 088400f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92f15900a88c1d9b83ce241681f1db13"></a>

### [`00b82e78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82e78.md) → [`00b82f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82f40.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md) [`00be11e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82e78.md#insn-00b82e9c) · [`00b82ea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82e78.md#insn-00b82ea8) · [`00b82eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82e78.md#insn-00b82eb4)
- 新版 `00b82f64`（命令位置の公開資料なし） · `00b82f70`（命令位置の公開資料なし） · `00b82f7c`（命令位置の公開資料なし）

~~~diff
- 00b82e9c ["INT_ADD", "register:40f0:8", ["const:b82e9c:8", "const:4:8"]]
- 00b82e9c ["CALL", null, ["callee:00bdd930:8"]]
+ 00b82f64 ["INT_ADD", "register:40f0:8", ["const:b82f64:8", "const:4:8"]]
+ 00b82f64 ["CALL", null, ["callee:00bdd930:8"]]
- 00b82e9c bytes 796a0194
+ 00b82f64 bytes 736a0194
- 00b82ea8 ["INT_ADD", "register:40f0:8", ["const:b82ea8:8", "const:4:8"]]
- 00b82ea8 ["CALL", null, ["callee:00be1290:8"]]
+ 00b82f70 ["INT_ADD", "register:40f0:8", ["const:b82f70:8", "const:4:8"]]
+ 00b82f70 ["CALL", null, ["callee:00be1290:8"]]
- 00b82ea8 bytes ce780194
+ 00b82f70 bytes c8780194
- 00b82eb4 ["INT_ADD", "register:40f0:8", ["const:b82eb4:8", "const:4:8"]]
- 00b82eb4 ["CALL", null, ["callee:00be1290:8"]]
+ 00b82f7c ["INT_ADD", "register:40f0:8", ["const:b82f7c:8", "const:4:8"]]
+ 00b82f7c ["CALL", null, ["callee:00be1290:8"]]
- 00b82eb4 bytes cb780194
+ 00b82f7c bytes c5780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61321b451a67297bf151e7837004e71c"></a>

### [`00b83234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83234.md) → [`00b832fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b832fc.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEEC1EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)

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
    "old": {
      "definition_site": "00b83260",
      "incomplete_value": true,
      "site": "00b83260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "old": {
      "definition_site": "00b83264",
      "incomplete_value": true,
      "site": "00b83264",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b83318",
      "READ",
      [
        "storage",
        "00c1bc08",
        null,
        "pointer"
      ]
    ],
    [
      "00b83328",
      "DATA",
      [
        "storage",
        "00c13180",
        null,
        "pointer"
      ]
    ],
    [
      "00b8332c",
      "DATA",
      [
        "storage",
        "00c13158",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b83318",
      "READ",
      [
        "storage",
        "00c1bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00b83328",
      "DATA",
      [
        "storage",
        "00c13230",
        null,
        "pointer"
      ]
    ],
    [
      "00b8332c",
      "DATA",
      [
        "storage",
        "00c13208",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83234.md#insn-00b83250) · [`00b8326c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83234.md#insn-00b8326c)
- 新版 `00b83318`（命令位置の公開資料なし） · `00b83334`（命令位置の公開資料なし）

~~~diff
- 00b83250 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c08:8"]]
- 00b83250 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b83318 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb8:8"]]
+ 00b83318 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b83250 bytes 080546f9
+ 00b83318 bytes 085d46f9
- 00b8326c ["INT_ADD", "register:40f0:8", ["const:b8326c:8", "const:4:8"]]
- 00b8326c ["CALL", null, ["callee:00bdb340:8"]]
+ 00b83334 ["INT_ADD", "register:40f0:8", ["const:b83334:8", "const:4:8"]]
+ 00b83334 ["CALL", null, ["callee:00bdb340:8"]]
- 00b8326c bytes 09600194
+ 00b83334 bytes 03600194
~~~


<a id="compare-d92dfb2225c95b4af075eb45cc2274a3"></a>

### [`00b833a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b833a0.md) → [`00b83468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83468.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE6sentryC1ERS3_b

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be12f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be12f0.md)
- 新版 呼出元 1件 [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13a0.md)

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
    "old": {
      "definition_site": "00b83430",
      "incomplete_value": true,
      "site": "00b83434",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "00b834f8",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00b834f8",
      "PARAM",
      [
        "storage",
        "010a2a00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b834f8",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b834f8",
      "PARAM",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b833a0.md#insn-00b83434) · [`00b83400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b833a0.md#insn-00b83400) · [`00b83424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b833a0.md#insn-00b83424)
- 新版 `00b834fc`（命令位置の公開資料なし） · `00b834c8`（命令位置の公開資料なし） · `00b834ec`（命令位置の公開資料なし）

~~~diff
- 00b83434 ["INT_ADD", "register:40f0:8", ["const:b83434:8", "const:4:8"]]
- 00b83434 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b834fc ["INT_ADD", "register:40f0:8", ["const:b834fc:8", "const:4:8"]]
+ 00b834fc ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b83434 bytes bf5f0194
+ 00b834fc bytes b95f0194
- 00b83400 ["INT_ADD", "register:40f0:8", ["const:b83400:8", "const:4:8"]]
- 00b83400 ["CALL", null, ["callee:00be13a0:8"]]
+ 00b834c8 ["INT_ADD", "register:40f0:8", ["const:b834c8:8", "const:4:8"]]
+ 00b834c8 ["CALL", null, ["callee:00be13a0:8"]]
- 00b83400 bytes bc770194
+ 00b834c8 bytes b6770194
- 00b83424 ["INT_ADD", "register:40f0:8", ["const:b83424:8", "const:4:8"]]
- 00b83424 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b834ec ["INT_ADD", "register:40f0:8", ["const:b834ec:8", "const:4:8"]]
+ 00b834ec ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b83424 bytes bf5f0194
+ 00b834ec bytes b95f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3216af357d311eddd316b3115e0f56eb"></a>

### [`00b838a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b838a8.md) → [`00b83970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83970.md) FUN_00b83970

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b838a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b838a0.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00b83968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83968.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

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
    "old": {
      "definition_site": "00b838fc",
      "incomplete_value": true,
      "site": "00b83900",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "00b839c4",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b839c4",
      "PARAM",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b839c4",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b839c4",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b838a8.md#insn-00b83900) · [`00b838d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b838a8.md#insn-00b838d4) · [`00b838f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b838a8.md#insn-00b838f0)
- 新版 `00b839c8`（命令位置の公開資料なし） · `00b8399c`（命令位置の公開資料なし） · `00b839b8`（命令位置の公開資料なし）

~~~diff
- 00b83900 ["INT_ADD", "register:40f0:8", ["const:b83900:8", "const:4:8"]]
- 00b83900 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b839c8 ["INT_ADD", "register:40f0:8", ["const:b839c8:8", "const:4:8"]]
+ 00b839c8 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b83900 bytes 8c5e0194
+ 00b839c8 bytes 865e0194
- 00b838d4 ["INT_ADD", "register:40f0:8", ["const:b838d4:8", "const:4:8"]]
- 00b838d4 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b8399c ["INT_ADD", "register:40f0:8", ["const:b8399c:8", "const:4:8"]]
+ 00b8399c ["CALL", null, ["callee:00be13d0:8"]]
- 00b838d4 bytes 93760194
+ 00b8399c bytes 8d760194
- 00b838f0 ["INT_ADD", "register:40f0:8", ["const:b838f0:8", "const:4:8"]]
- 00b838f0 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b839b8 ["INT_ADD", "register:40f0:8", ["const:b839b8:8", "const:4:8"]]
+ 00b839b8 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b838f0 bytes 8c5e0194
+ 00b839b8 bytes 865e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84aee299cbdb5888e5d7a28eab710af2"></a>

### [`00b839e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b839e0.md) → [`00b83aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83aa8.md) FUN_00b83aa8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b839d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b839d8.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00b83aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83aa0.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

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
    "old": {
      "definition_site": "00b83a34",
      "incomplete_value": true,
      "site": "00b83a38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "00b83afc",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b83afc",
      "PARAM",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b83afc",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b83afc",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83a38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b839e0.md#insn-00b83a38) · [`00b83a0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b839e0.md#insn-00b83a0c) · [`00b83a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b839e0.md#insn-00b83a28)
- 新版 `00b83b00`（命令位置の公開資料なし） · `00b83ad4`（命令位置の公開資料なし） · `00b83af0`（命令位置の公開資料なし）

~~~diff
- 00b83a38 ["INT_ADD", "register:40f0:8", ["const:b83a38:8", "const:4:8"]]
- 00b83a38 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b83b00 ["INT_ADD", "register:40f0:8", ["const:b83b00:8", "const:4:8"]]
+ 00b83b00 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b83a38 bytes 3e5e0194
+ 00b83b00 bytes 385e0194
- 00b83a0c ["INT_ADD", "register:40f0:8", ["const:b83a0c:8", "const:4:8"]]
- 00b83a0c ["CALL", null, ["callee:00be13d0:8"]]
+ 00b83ad4 ["INT_ADD", "register:40f0:8", ["const:b83ad4:8", "const:4:8"]]
+ 00b83ad4 ["CALL", null, ["callee:00be13d0:8"]]
- 00b83a0c bytes 45760194
+ 00b83ad4 bytes 3f760194
- 00b83a28 ["INT_ADD", "register:40f0:8", ["const:b83a28:8", "const:4:8"]]
- 00b83a28 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b83af0 ["INT_ADD", "register:40f0:8", ["const:b83af0:8", "const:4:8"]]
+ 00b83af0 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b83a28 bytes 3e5e0194
+ 00b83af0 bytes 385e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f06a09280120c9a7e45d1c3dd18abc8"></a>

### [`00b83b58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83b58.md) → [`00b83c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83c20.md) FUN_00b83c20

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b83b50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83b50.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00b83c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83c18.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

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
    "old": {
      "definition_site": "00b83bac",
      "incomplete_value": true,
      "site": "00b83bb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "00b83c74",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b83c74",
      "PARAM",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b83c74",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b83c74",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83b58.md#insn-00b83bb0) · [`00b83b84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83b58.md#insn-00b83b84) · [`00b83ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83b58.md#insn-00b83ba0)
- 新版 `00b83c78`（命令位置の公開資料なし） · `00b83c4c`（命令位置の公開資料なし） · `00b83c68`（命令位置の公開資料なし）

~~~diff
- 00b83bb0 ["INT_ADD", "register:40f0:8", ["const:b83bb0:8", "const:4:8"]]
- 00b83bb0 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b83c78 ["INT_ADD", "register:40f0:8", ["const:b83c78:8", "const:4:8"]]
+ 00b83c78 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b83bb0 bytes e05d0194
+ 00b83c78 bytes da5d0194
- 00b83b84 ["INT_ADD", "register:40f0:8", ["const:b83b84:8", "const:4:8"]]
- 00b83b84 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b83c4c ["INT_ADD", "register:40f0:8", ["const:b83c4c:8", "const:4:8"]]
+ 00b83c4c ["CALL", null, ["callee:00be13d0:8"]]
- 00b83b84 bytes e7750194
+ 00b83c4c bytes e1750194
- 00b83ba0 ["INT_ADD", "register:40f0:8", ["const:b83ba0:8", "const:4:8"]]
- 00b83ba0 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b83c68 ["INT_ADD", "register:40f0:8", ["const:b83c68:8", "const:4:8"]]
+ 00b83c68 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b83ba0 bytes e05d0194
+ 00b83c68 bytes da5d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bf33ef019f0223b8b6807115f669d21"></a>

### [`00b83c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83c90.md) → [`00b83d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83d58.md) FUN_00b83d58

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b83c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83c88.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00b83d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83d50.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

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
    "old": {
      "definition_site": "00b83ce4",
      "incomplete_value": true,
      "site": "00b83ce8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "00b83dac",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b83dac",
      "PARAM",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b83dac",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b83dac",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83ce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83c90.md#insn-00b83ce8) · [`00b83cbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83c90.md#insn-00b83cbc) · [`00b83cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83c90.md#insn-00b83cd8)
- 新版 `00b83db0`（命令位置の公開資料なし） · `00b83d84`（命令位置の公開資料なし） · `00b83da0`（命令位置の公開資料なし）

~~~diff
- 00b83ce8 ["INT_ADD", "register:40f0:8", ["const:b83ce8:8", "const:4:8"]]
- 00b83ce8 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b83db0 ["INT_ADD", "register:40f0:8", ["const:b83db0:8", "const:4:8"]]
+ 00b83db0 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b83ce8 bytes 925d0194
+ 00b83db0 bytes 8c5d0194
- 00b83cbc ["INT_ADD", "register:40f0:8", ["const:b83cbc:8", "const:4:8"]]
- 00b83cbc ["CALL", null, ["callee:00be13d0:8"]]
+ 00b83d84 ["INT_ADD", "register:40f0:8", ["const:b83d84:8", "const:4:8"]]
+ 00b83d84 ["CALL", null, ["callee:00be13d0:8"]]
- 00b83cbc bytes 99750194
+ 00b83d84 bytes 93750194
- 00b83cd8 ["INT_ADD", "register:40f0:8", ["const:b83cd8:8", "const:4:8"]]
- 00b83cd8 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b83da0 ["INT_ADD", "register:40f0:8", ["const:b83da0:8", "const:4:8"]]
+ 00b83da0 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b83cd8 bytes 925d0194
+ 00b83da0 bytes 8c5d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-055cfebcc02aaef20074382c68128d15"></a>

### [`00b83e0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83e0c.md) → [`00b83ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83ed4.md) FUN_00b83ed4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b83e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83e04.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00b83ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83ecc.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

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
    "old": {
      "definition_site": "00b83e60",
      "incomplete_value": true,
      "site": "00b83e64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "00b83f28",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b83f28",
      "PARAM",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b83f28",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b83f28",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83e64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83e0c.md#insn-00b83e64) · [`00b83e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83e0c.md#insn-00b83e38) · [`00b83e54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83e0c.md#insn-00b83e54)
- 新版 `00b83f2c`（命令位置の公開資料なし） · `00b83f00`（命令位置の公開資料なし） · `00b83f1c`（命令位置の公開資料なし）

~~~diff
- 00b83e64 ["INT_ADD", "register:40f0:8", ["const:b83e64:8", "const:4:8"]]
- 00b83e64 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b83f2c ["INT_ADD", "register:40f0:8", ["const:b83f2c:8", "const:4:8"]]
+ 00b83f2c ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b83e64 bytes 335d0194
+ 00b83f2c bytes 2d5d0194
- 00b83e38 ["INT_ADD", "register:40f0:8", ["const:b83e38:8", "const:4:8"]]
- 00b83e38 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b83f00 ["INT_ADD", "register:40f0:8", ["const:b83f00:8", "const:4:8"]]
+ 00b83f00 ["CALL", null, ["callee:00be13d0:8"]]
- 00b83e38 bytes 3a750194
+ 00b83f00 bytes 34750194
- 00b83e54 ["INT_ADD", "register:40f0:8", ["const:b83e54:8", "const:4:8"]]
- 00b83e54 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b83f1c ["INT_ADD", "register:40f0:8", ["const:b83f1c:8", "const:4:8"]]
+ 00b83f1c ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b83e54 bytes 335d0194
+ 00b83f1c bytes 2d5d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dac035af51c3a8b210f6417c59618fcd"></a>

### [`00b83f44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83f44.md) → [`00b8400c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8400c.md) FUN_00b8400c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b83f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83f3c.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00b84004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84004.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

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
    "old": {
      "definition_site": "00b83f98",
      "incomplete_value": true,
      "site": "00b83f9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "00b84060",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b84060",
      "PARAM",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b84060",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b84060",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83f44.md#insn-00b83f9c) · [`00b83f70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83f44.md#insn-00b83f70) · [`00b83f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b83/00b83f44.md#insn-00b83f8c)
- 新版 `00b84064`（命令位置の公開資料なし） · `00b84038`（命令位置の公開資料なし） · `00b84054`（命令位置の公開資料なし）

~~~diff
- 00b83f9c ["INT_ADD", "register:40f0:8", ["const:b83f9c:8", "const:4:8"]]
- 00b83f9c ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b84064 ["INT_ADD", "register:40f0:8", ["const:b84064:8", "const:4:8"]]
+ 00b84064 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b83f9c bytes e55c0194
+ 00b84064 bytes df5c0194
- 00b83f70 ["INT_ADD", "register:40f0:8", ["const:b83f70:8", "const:4:8"]]
- 00b83f70 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b84038 ["INT_ADD", "register:40f0:8", ["const:b84038:8", "const:4:8"]]
+ 00b84038 ["CALL", null, ["callee:00be13d0:8"]]
- 00b83f70 bytes ec740194
+ 00b84038 bytes e6740194
- 00b83f8c ["INT_ADD", "register:40f0:8", ["const:b83f8c:8", "const:4:8"]]
- 00b83f8c ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b84054 ["INT_ADD", "register:40f0:8", ["const:b84054:8", "const:4:8"]]
+ 00b84054 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b83f8c bytes e55c0194
+ 00b84054 bytes df5c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd3879773820b3da614da3539e1d56b4"></a>

### [`00b8407c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b8407c.md) → [`00b84144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84144.md) FUN_00b84144

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b84074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84074.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00b8413c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8413c.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

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
    "old": {
      "definition_site": "00b840d0",
      "incomplete_value": true,
      "site": "00b840d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "00b84198",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b84198",
      "PARAM",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b84198",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b84198",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b840d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b8407c.md#insn-00b840d4) · [`00b840a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b8407c.md#insn-00b840a8) · [`00b840c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b8407c.md#insn-00b840c4)
- 新版 `00b8419c`（命令位置の公開資料なし） · `00b84170`（命令位置の公開資料なし） · `00b8418c`（命令位置の公開資料なし）

~~~diff
- 00b840d4 ["INT_ADD", "register:40f0:8", ["const:b840d4:8", "const:4:8"]]
- 00b840d4 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b8419c ["INT_ADD", "register:40f0:8", ["const:b8419c:8", "const:4:8"]]
+ 00b8419c ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b840d4 bytes 975c0194
+ 00b8419c bytes 915c0194
- 00b840a8 ["INT_ADD", "register:40f0:8", ["const:b840a8:8", "const:4:8"]]
- 00b840a8 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b84170 ["INT_ADD", "register:40f0:8", ["const:b84170:8", "const:4:8"]]
+ 00b84170 ["CALL", null, ["callee:00be13d0:8"]]
- 00b840a8 bytes 9e740194
+ 00b84170 bytes 98740194
- 00b840c4 ["INT_ADD", "register:40f0:8", ["const:b840c4:8", "const:4:8"]]
- 00b840c4 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b8418c ["INT_ADD", "register:40f0:8", ["const:b8418c:8", "const:4:8"]]
+ 00b8418c ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b840c4 bytes 975c0194
+ 00b8418c bytes 915c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07cc19ada013ca9db25702d51195dcb0"></a>

### [`00b841b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b841b4.md) → [`00b8427c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8427c.md) FUN_00b8427c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b841ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b841ac.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00b84274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84274.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

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
    "old": {
      "definition_site": "00b84208",
      "incomplete_value": true,
      "site": "00b8420c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "00b842d0",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b842d0",
      "PARAM",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b842d0",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b842d0",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8420c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b841b4.md#insn-00b8420c) · [`00b841e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b841b4.md#insn-00b841e0) · [`00b841fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b841b4.md#insn-00b841fc)
- 新版 `00b842d4`（命令位置の公開資料なし） · `00b842a8`（命令位置の公開資料なし） · `00b842c4`（命令位置の公開資料なし）

~~~diff
- 00b8420c ["INT_ADD", "register:40f0:8", ["const:b8420c:8", "const:4:8"]]
- 00b8420c ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b842d4 ["INT_ADD", "register:40f0:8", ["const:b842d4:8", "const:4:8"]]
+ 00b842d4 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b8420c bytes 495c0194
+ 00b842d4 bytes 435c0194
- 00b841e0 ["INT_ADD", "register:40f0:8", ["const:b841e0:8", "const:4:8"]]
- 00b841e0 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b842a8 ["INT_ADD", "register:40f0:8", ["const:b842a8:8", "const:4:8"]]
+ 00b842a8 ["CALL", null, ["callee:00be13d0:8"]]
- 00b841e0 bytes 50740194
+ 00b842a8 bytes 4a740194
- 00b841fc ["INT_ADD", "register:40f0:8", ["const:b841fc:8", "const:4:8"]]
- 00b841fc ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b842c4 ["INT_ADD", "register:40f0:8", ["const:b842c4:8", "const:4:8"]]
+ 00b842c4 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b841fc bytes 495c0194
+ 00b842c4 bytes 435c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dec5f43073f7e15f22ccccca0ca0d49"></a>

### [`00b842ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b842ec.md) → [`00b843b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b843b4.md) FUN_00b843b4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b842e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b842e4.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00b843ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b843ac.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

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
    "old": {
      "definition_site": "00b84340",
      "incomplete_value": true,
      "site": "00b84344",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "00b84408",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b84408",
      "PARAM",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b84408",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b84408",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b842ec.md#insn-00b84344) · [`00b84318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b842ec.md#insn-00b84318) · [`00b84334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b842ec.md#insn-00b84334)
- 新版 `00b8440c`（命令位置の公開資料なし） · `00b843e0`（命令位置の公開資料なし） · `00b843fc`（命令位置の公開資料なし）

~~~diff
- 00b84344 ["INT_ADD", "register:40f0:8", ["const:b84344:8", "const:4:8"]]
- 00b84344 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b8440c ["INT_ADD", "register:40f0:8", ["const:b8440c:8", "const:4:8"]]
+ 00b8440c ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b84344 bytes fb5b0194
+ 00b8440c bytes f55b0194
- 00b84318 ["INT_ADD", "register:40f0:8", ["const:b84318:8", "const:4:8"]]
- 00b84318 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b843e0 ["INT_ADD", "register:40f0:8", ["const:b843e0:8", "const:4:8"]]
+ 00b843e0 ["CALL", null, ["callee:00be13d0:8"]]
- 00b84318 bytes 02740194
+ 00b843e0 bytes fc730194
- 00b84334 ["INT_ADD", "register:40f0:8", ["const:b84334:8", "const:4:8"]]
- 00b84334 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b843fc ["INT_ADD", "register:40f0:8", ["const:b843fc:8", "const:4:8"]]
+ 00b843fc ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b84334 bytes fb5b0194
+ 00b843fc bytes f55b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37e526c9018d5f56ad58d5391cc49a01"></a>

### [`00b84424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84424.md) → [`00b844ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b844ec.md) FUN_00b844ec

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8441c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b8441c.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00b844e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b844e4.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

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
    "old": {
      "definition_site": "00b84478",
      "incomplete_value": true,
      "site": "00b8447c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "00b84540",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b84540",
      "PARAM",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b84540",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b84540",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8447c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84424.md#insn-00b8447c) · [`00b84450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84424.md#insn-00b84450) · [`00b8446c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84424.md#insn-00b8446c)
- 新版 `00b84544`（命令位置の公開資料なし） · `00b84518`（命令位置の公開資料なし） · `00b84534`（命令位置の公開資料なし）

~~~diff
- 00b8447c ["INT_ADD", "register:40f0:8", ["const:b8447c:8", "const:4:8"]]
- 00b8447c ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b84544 ["INT_ADD", "register:40f0:8", ["const:b84544:8", "const:4:8"]]
+ 00b84544 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b8447c bytes ad5b0194
+ 00b84544 bytes a75b0194
- 00b84450 ["INT_ADD", "register:40f0:8", ["const:b84450:8", "const:4:8"]]
- 00b84450 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b84518 ["INT_ADD", "register:40f0:8", ["const:b84518:8", "const:4:8"]]
+ 00b84518 ["CALL", null, ["callee:00be13d0:8"]]
- 00b84450 bytes b4730194
+ 00b84518 bytes ae730194
- 00b8446c ["INT_ADD", "register:40f0:8", ["const:b8446c:8", "const:4:8"]]
- 00b8446c ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b84534 ["INT_ADD", "register:40f0:8", ["const:b84534:8", "const:4:8"]]
+ 00b84534 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b8446c bytes ad5b0194
+ 00b84534 bytes a75b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-445b6177db11e805931938a6a00efd98"></a>

### [`00b8455c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b8455c.md) → [`00b84624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84624.md) FUN_00b84624

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b84554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84554.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00b8461c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8461c.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

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
    "old": {
      "definition_site": "00b845b0",
      "incomplete_value": true,
      "site": "00b845b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "unmatched:00b845b0",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b845b0",
      "PARAM",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b84678",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b84678",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b845b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b8455c.md#insn-00b845b4) · [`00b84588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b8455c.md#insn-00b84588) · [`00b845a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b8455c.md#insn-00b845a4)
- 新版 `00b8467c`（命令位置の公開資料なし） · `00b84650`（命令位置の公開資料なし） · `00b8466c`（命令位置の公開資料なし）

~~~diff
- 00b845b4 ["INT_ADD", "register:40f0:8", ["const:b845b4:8", "const:4:8"]]
- 00b845b4 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b8467c ["INT_ADD", "register:40f0:8", ["const:b8467c:8", "const:4:8"]]
+ 00b8467c ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b845b4 bytes 5f5b0194
+ 00b8467c bytes 595b0194
- 00b84588 ["INT_ADD", "register:40f0:8", ["const:b84588:8", "const:4:8"]]
- 00b84588 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b84650 ["INT_ADD", "register:40f0:8", ["const:b84650:8", "const:4:8"]]
+ 00b84650 ["CALL", null, ["callee:00be13d0:8"]]
- 00b84588 bytes 66730194
+ 00b84650 bytes 60730194
- 00b845a4 ["INT_ADD", "register:40f0:8", ["const:b845a4:8", "const:4:8"]]
- 00b845a4 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b8466c ["INT_ADD", "register:40f0:8", ["const:b8466c:8", "const:4:8"]]
+ 00b8466c ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b845a4 bytes 5f5b0194
+ 00b8466c bytes 595b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d603e9220dedaefe6c0542dd5d792213"></a>

### [`00b84694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84694.md) → [`00b8475c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8475c.md) FUN_00b8475c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8468c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b8468c.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00b84754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84754.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

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
    "old": {
      "definition_site": "00b846e8",
      "incomplete_value": true,
      "site": "00b846ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "00b847b0",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00b847b0",
      "PARAM",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b847b0",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b847b0",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b846ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84694.md#insn-00b846ec) · [`00b846c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84694.md#insn-00b846c0) · [`00b846dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84694.md#insn-00b846dc)
- 新版 `00b847b4`（命令位置の公開資料なし） · `00b84788`（命令位置の公開資料なし） · `00b847a4`（命令位置の公開資料なし）

~~~diff
- 00b846ec ["INT_ADD", "register:40f0:8", ["const:b846ec:8", "const:4:8"]]
- 00b846ec ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b847b4 ["INT_ADD", "register:40f0:8", ["const:b847b4:8", "const:4:8"]]
+ 00b847b4 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b846ec bytes 115b0194
+ 00b847b4 bytes 0b5b0194
- 00b846c0 ["INT_ADD", "register:40f0:8", ["const:b846c0:8", "const:4:8"]]
- 00b846c0 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b84788 ["INT_ADD", "register:40f0:8", ["const:b84788:8", "const:4:8"]]
+ 00b84788 ["CALL", null, ["callee:00be13d0:8"]]
- 00b846c0 bytes 18730194
+ 00b84788 bytes 12730194
- 00b846dc ["INT_ADD", "register:40f0:8", ["const:b846dc:8", "const:4:8"]]
- 00b846dc ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b847a4 ["INT_ADD", "register:40f0:8", ["const:b847a4:8", "const:4:8"]]
+ 00b847a4 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b846dc bytes 115b0194
+ 00b847a4 bytes 0b5b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4d374d941e63be4a7c23f93c6d99fdb"></a>

### [`00b847cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b847cc.md) → [`00b84894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84894.md) FUN_00b84894

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b847c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b847c4.md) · 呼出先 5件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00b8488c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8488c.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00b84820",
      "incomplete_value": true,
      "site": "00b84824",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "unmatched:00b84820",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b84820",
      "PARAM",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b848e8",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b848e8",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b847cc.md#insn-00b84824) · [`00b847f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b847cc.md#insn-00b847f8) · [`00b84800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b847cc.md#insn-00b84800)
- 新版 `00b848ec`（命令位置の公開資料なし） · `00b848c0`（命令位置の公開資料なし） · `00b848c8`（命令位置の公開資料なし）

~~~diff
- 00b84824 ["INT_ADD", "register:40f0:8", ["const:b84824:8", "const:4:8"]]
- 00b84824 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b848ec ["INT_ADD", "register:40f0:8", ["const:b848ec:8", "const:4:8"]]
+ 00b848ec ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b84824 bytes c35a0194
+ 00b848ec bytes bd5a0194
- 00b847f8 ["INT_ADD", "register:40f0:8", ["const:b847f8:8", "const:4:8"]]
- 00b847f8 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b848c0 ["INT_ADD", "register:40f0:8", ["const:b848c0:8", "const:4:8"]]
+ 00b848c0 ["CALL", null, ["callee:00be13d0:8"]]
- 00b847f8 bytes ca720194
+ 00b848c0 bytes c4720194
- 00b84800 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b84800 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b848c8 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b848c8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b84800 bytes a8030034
+ 00b848c8 bytes a8030034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75256dd26d4deb48ab72a3eaa86e2b20"></a>

### [`00b848fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b848fc.md) → [`00b849c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b849c4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00be1330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1330.md) · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00be13e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13e0.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 76.92% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b84924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b848fc.md#insn-00b84924) · [`00b84948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b848fc.md#insn-00b84948) · [`00b84958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b848fc.md#insn-00b84958)
- 新版 `00b849ec`（命令位置の公開資料なし） · `00b84a10`（命令位置の公開資料なし） · `00b84a20`（命令位置の公開資料なし）

~~~diff
- 00b84924 ["INT_ADD", "register:40f0:8", ["const:b84924:8", "const:4:8"]]
- 00b84924 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b849ec ["INT_ADD", "register:40f0:8", ["const:b849ec:8", "const:4:8"]]
+ 00b849ec ["CALL", null, ["callee:00be13d0:8"]]
- 00b84924 bytes 7f720194
+ 00b849ec bytes 79720194
- 00b84948 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00b84a10 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00b84948 bytes 60010054
+ 00b84a10 bytes 60010054
- 00b84958 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 00b84a20 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00b84958 bytes a0010054
+ 00b84a20 bytes a0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-607f5dc9bd7ef4dd70d07224f704c9cd"></a>

### [`00b84a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84a50.md) → [`00b84b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84b18.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEPwl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00be1340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1340.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be13f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13f0.md)

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
    "old": {
      "definition_site": "00b84a90",
      "incomplete_value": true,
      "site": "00b84a94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "00b84b58",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00b84b58",
      "PARAM",
      [
        "storage",
        "010a2a00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b84b58",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b84b58",
      "PARAM",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84a50.md#insn-00b84a94) · [`00b84a84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84a50.md#insn-00b84a84) · [`00b84a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84a50.md#insn-00b84a90)
- 新版 `00b84b5c`（命令位置の公開資料なし） · `00b84b4c`（命令位置の公開資料なし） · `00b84b58`（命令位置の公開資料なし）

~~~diff
- 00b84a94 ["INT_ADD", "register:40f0:8", ["const:b84a94:8", "const:4:8"]]
- 00b84a94 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b84b5c ["INT_ADD", "register:40f0:8", ["const:b84b5c:8", "const:4:8"]]
+ 00b84b5c ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b84a94 bytes 275a0194
+ 00b84b5c bytes 215a0194
- 00b84a84 ["INT_ADD", "register:40f0:8", ["const:b84a84:8", "const:4:8"]]
- 00b84a84 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b84b4c ["INT_ADD", "register:40f0:8", ["const:b84b4c:8", "const:4:8"]]
+ 00b84b4c ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b84a84 bytes 275a0194
+ 00b84b4c bytes 215a0194
- 00b84a90 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:c10:8"]]
- 00b84a90 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b84b58 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
+ 00b84b58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b84a90 bytes 210846f9
+ 00b84b58 bytes 216046f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80927eb235aba395e16fb6026b6a11e8"></a>

### [`00b84af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84af4.md) → [`00b84bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84bbc.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEPwlw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1340.md) · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00be13f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13f0.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.94% / 新版 98.94%

CFGの説明率　旧版 85.29% / 新版 85.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b84be8",
      "incomplete_value": true,
      "site": "00b84bf8",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "live",
            "register:40e8:8"
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84b20",
      "incomplete_value": true,
      "site": "00b84b30",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b84b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84af4.md#insn-00b84b30) · [`00b84b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84af4.md#insn-00b84b20) · [`00b84b54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84af4.md#insn-00b84b54)
- 新版 `00b84bf8`（命令位置の公開資料なし） · `00b84c1c`（命令位置の公開資料なし）

~~~diff
- 00b84b30 ["INT_ADD", "register:40f0:8", ["const:b84b30:8", "const:4:8"]]
- 00b84b30 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b84bf8 ["INT_ADD", "register:40f0:8", ["const:b84bf8:8", "const:4:8"]]
+ 00b84bf8 ["CALL", null, ["callee:00be13d0:8"]]
- 00b84b30 bytes fc710194
+ 00b84bf8 bytes f6710194
- 00b84b20 ["INT_SUB", "register:4000:8", ["register:40e8:8", "const:4:8"]]
- 00b84b20 bytes a01300d1
- 00b84b54 ["BRANCH", null, ["local:b6:8"]]
+ 00b84c1c ["BRANCH", null, ["local:b7:8"]]
- 00b84b54 bytes 0b000014
+ 00b84c1c bytes 0b000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6f940c0f588a26822026edb3db5bc1e"></a>

### [`00b84cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84cc4.md) → [`00b84d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84d8c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00be1350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1350.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be1400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1400.md)

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
    "old": {
      "definition_site": "00b84cfc",
      "incomplete_value": true,
      "site": "00b84d00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "00b84dc4",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00b84dc4",
      "PARAM",
      [
        "storage",
        "010a2a00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b84dc4",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b84dc4",
      "PARAM",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84cc4.md#insn-00b84d00) · [`00b84cf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84cc4.md#insn-00b84cf0) · [`00b84cfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84cc4.md#insn-00b84cfc)
- 新版 `00b84dc8`（命令位置の公開資料なし） · `00b84db8`（命令位置の公開資料なし） · `00b84dc4`（命令位置の公開資料なし）

~~~diff
- 00b84d00 ["INT_ADD", "register:40f0:8", ["const:b84d00:8", "const:4:8"]]
- 00b84d00 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b84dc8 ["INT_ADD", "register:40f0:8", ["const:b84dc8:8", "const:4:8"]]
+ 00b84dc8 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b84d00 bytes 8c590194
+ 00b84dc8 bytes 86590194
- 00b84cf0 ["INT_ADD", "register:40f0:8", ["const:b84cf0:8", "const:4:8"]]
- 00b84cf0 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b84db8 ["INT_ADD", "register:40f0:8", ["const:b84db8:8", "const:4:8"]]
+ 00b84db8 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b84cf0 bytes 8c590194
+ 00b84db8 bytes 86590194
- 00b84cfc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:c10:8"]]
- 00b84cfc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b84dc4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
+ 00b84dc4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b84cfc bytes 210846f9
+ 00b84dc4 bytes 216046f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d1e79ab26bb0ec0859d175f5b3c3713"></a>

### [`00b84ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84ebc.md) → [`00b84f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84f84.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7getlineEPwl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00be1360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1360.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be1410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1410.md)

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
    "old": {
      "definition_site": "00b84efc",
      "incomplete_value": true,
      "site": "00b84f00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "00b84fc4",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00b84fc4",
      "PARAM",
      [
        "storage",
        "010a2a00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b84fc4",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b84fc4",
      "PARAM",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84ebc.md#insn-00b84f00) · [`00b84ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84ebc.md#insn-00b84ef0) · [`00b84efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84ebc.md#insn-00b84efc)
- 新版 `00b84fc8`（命令位置の公開資料なし） · `00b84fb8`（命令位置の公開資料なし） · `00b84fc4`（命令位置の公開資料なし）

~~~diff
- 00b84f00 ["INT_ADD", "register:40f0:8", ["const:b84f00:8", "const:4:8"]]
- 00b84f00 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b84fc8 ["INT_ADD", "register:40f0:8", ["const:b84fc8:8", "const:4:8"]]
+ 00b84fc8 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b84f00 bytes 0c590194
+ 00b84fc8 bytes 06590194
- 00b84ef0 ["INT_ADD", "register:40f0:8", ["const:b84ef0:8", "const:4:8"]]
- 00b84ef0 ["CALL", null, ["callee:00bdb3d0:8"]]
+ 00b84fb8 ["INT_ADD", "register:40f0:8", ["const:b84fb8:8", "const:4:8"]]
+ 00b84fb8 ["CALL", null, ["callee:00bdb3d0:8"]]
- 00b84ef0 bytes 0c590194
+ 00b84fb8 bytes 06590194
- 00b84efc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:c10:8"]]
- 00b84efc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b84fc4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
+ 00b84fc4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b84efc bytes 210846f9
+ 00b84fc4 bytes 216046f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36c9ebfebe1f6f7dd817d6acf2bc66db"></a>

### [`00b84f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84f60.md) → [`00b85028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85028.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7getlineEPwlw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1360.md) · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 1件 [`00be1410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1410.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 98.26% / 新版 98.26%

CFGの説明率　旧版 77.50% / 新版 77.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b85050"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b85118"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b851d0",
      "incomplete_value": true,
      "site": "00b851f0",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
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
      "unmatched:00b85050",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b85098"
      ]
    ]
  ],
  "added": [
    [
      "00b85118",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b85098"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b85050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84f60.md#insn-00b85050) · [`00b84fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b84/00b84f60.md#insn-00b84fa0)
- 新版 `00b85118`（命令位置の公開資料なし） · `00b85068`（命令位置の公開資料なし）

~~~diff
- 00b85050 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b85050 bytes 00fcff54
+ 00b85118 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00b85118 bytes 00fcff54
- 00b84fa0 ["INT_ADD", "register:40f0:8", ["const:b84fa0:8", "const:4:8"]]
- 00b84fa0 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b85068 ["INT_ADD", "register:40f0:8", ["const:b85068:8", "const:4:8"]]
+ 00b85068 ["CALL", null, ["callee:00be13d0:8"]]
- 00b84fa0 bytes e0700194
+ 00b85068 bytes da700194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc7335b8a6cfef7061c4030fccd80174"></a>

### [`00b8519c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b8519c.md) → [`00b85264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85264.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE6ignoreElj

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 66.67% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b85228"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b85290"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b852f0"
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
      "00b852d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8521c"
      ]
    ],
    [
      "00b8533c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b85284"
      ]
    ],
    [
      "unmatched:00b85228",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b852d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b852e4"
      ]
    ],
    [
      "00b8533c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8534c"
      ]
    ],
    [
      "00b852f0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b85228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b8519c.md#insn-00b85228) · [`00b85290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b8519c.md#insn-00b85290)
- 新版 `00b852f0`（命令位置の公開資料なし）

~~~diff
- 00b85228 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b85228 ["INT_ADD", "register:40f0:8", ["const:b85228:8", "const:4:8"]]
- 00b85228 ["CALLIND", null, ["register:0:8"]]
- 00b85228 bytes 20013fd6
- 00b85290 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b85290 ["INT_ADD", "register:40f0:8", ["const:b85290:8", "const:4:8"]]
- 00b85290 ["CALLIND", null, ["register:0:8"]]
- 00b85290 bytes 20013fd6
+ 00b852f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b852f0 ["INT_ADD", "register:40f0:8", ["const:b852f0:8", "const:4:8"]]
+ 00b852f0 ["CALLIND", null, ["register:0:8"]]
+ 00b852f0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9bc0a47583ce52fb7c003467e438267"></a>

### [`00b85450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85450.md) → [`00b85518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85518.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4readEPwl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8553c",
      "incomplete_value": true,
      "site": "00b85548",
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
            "const:1c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b85474",
      "incomplete_value": true,
      "site": "00b85480",
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
            "const:1c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b85480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85450.md#insn-00b85480) · [`00b85460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85450.md#insn-00b85460) · [`00b85474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85450.md#insn-00b85474)
- 新版 `00b85548`（命令位置の公開資料なし）

~~~diff
- 00b85480 ["INT_ADD", "register:40f0:8", ["const:b85480:8", "const:4:8"]]
- 00b85480 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b85548 ["INT_ADD", "register:40f0:8", ["const:b85548:8", "const:4:8"]]
+ 00b85548 ["CALL", null, ["callee:00be13d0:8"]]
- 00b85480 bytes a86f0194
+ 00b85548 bytes a26f0194
- 00b85460 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00b85460 bytes fd030091
- 00b85474 ["COPY", "tmp:0:8", ["const:1c:8"]]
- 00b85474 ["INT_CARRY", "register:105:1", ["register:40e8:8", "tmp:0:8"]]
- 00b85474 ["INT_SCARRY", "register:106:1", ["register:40e8:8", "tmp:0:8"]]
- 00b85474 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "tmp:0:8"]]
- 00b85474 bytes a0730091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a4b5d316c344a43581b905a02675d38"></a>

### [`00b85910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85910.md) → [`00b859d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b859d8.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4syncEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85910.md#insn-00b85934) · [`00b85948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85910.md#insn-00b85948) · [`00b85950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85910.md#insn-00b85950)
- 新版 `00b859fc`（命令位置の公開資料なし） · `00b85a10`（命令位置の公開資料なし） · `00b85a18`（命令位置の公開資料なし）

~~~diff
- 00b85934 ["INT_ADD", "register:40f0:8", ["const:b85934:8", "const:4:8"]]
- 00b85934 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b859fc ["INT_ADD", "register:40f0:8", ["const:b859fc:8", "const:4:8"]]
+ 00b859fc ["CALL", null, ["callee:00be13d0:8"]]
- 00b85934 bytes 7b6e0194
+ 00b859fc bytes 756e0194
- 00b85948 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b85948 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b85a10 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b85a10 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b85948 bytes 000200b4
+ 00b85a10 bytes 000200b4
- 00b85950 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b85950 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b85a18 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b85a18 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b85950 bytes 08020034
+ 00b85a18 bytes 08020034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-291ec944fcff6c055b23413ba0d75ba0"></a>

### [`00b85a00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85a00.md) → [`00b85ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85ac8.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5tellgEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85a00.md#insn-00b85a24) · [`00b85a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85a00.md#insn-00b85a2c) · [`00b85a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85a00.md#insn-00b85a54)
- 新版 `00b85aec`（命令位置の公開資料なし） · `00b85af4`（命令位置の公開資料なし） · `00b85b1c`（命令位置の公開資料なし）

~~~diff
- 00b85a24 ["INT_ADD", "register:40f0:8", ["const:b85a24:8", "const:4:8"]]
- 00b85a24 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b85aec ["INT_ADD", "register:40f0:8", ["const:b85aec:8", "const:4:8"]]
+ 00b85aec ["CALL", null, ["callee:00be13d0:8"]]
- 00b85a24 bytes 3f6e0194
+ 00b85aec bytes 396e0194
- 00b85a2c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b85a2c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b85af4 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b85af4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b85a2c bytes a8020034
+ 00b85af4 bytes a8020034
- 00b85a54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85a54 ["INT_ADD", "register:40f0:8", ["const:b85a54:8", "const:4:8"]]
- 00b85a54 ["CALLIND", null, ["register:0:8"]]
+ 00b85b1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b85b1c ["INT_ADD", "register:40f0:8", ["const:b85b1c:8", "const:4:8"]]
+ 00b85b1c ["CALLIND", null, ["register:0:8"]]
- 00b85a54 bytes 00013fd6
+ 00b85b1c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7667511c6f65522f46145418660900e0"></a>

### [`00b85c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85c0c.md) → [`00b85cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85cd4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5seekgExNS_8ios_base7seekdirE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85c0c.md#insn-00b85c48) · [`00b85c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85c0c.md#insn-00b85c58) · [`00b85c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85c0c.md#insn-00b85c60)
- 新版 `00b85d10`（命令位置の公開資料なし） · `00b85d20`（命令位置の公開資料なし） · `00b85d28`（命令位置の公開資料なし）

~~~diff
- 00b85c48 ["INT_ADD", "register:40f0:8", ["const:b85c48:8", "const:4:8"]]
- 00b85c48 ["CALL", null, ["callee:00bdb400:8"]]
+ 00b85d10 ["INT_ADD", "register:40f0:8", ["const:b85d10:8", "const:4:8"]]
+ 00b85d10 ["CALL", null, ["callee:00bdb400:8"]]
- 00b85c48 bytes c2550194
+ 00b85d10 bytes bc550194
- 00b85c58 ["INT_ADD", "register:40f0:8", ["const:b85c58:8", "const:4:8"]]
- 00b85c58 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b85d20 ["INT_ADD", "register:40f0:8", ["const:b85d20:8", "const:4:8"]]
+ 00b85d20 ["CALL", null, ["callee:00be13d0:8"]]
- 00b85c58 bytes b26d0194
+ 00b85d20 bytes ac6d0194
- 00b85c60 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b85c60 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b85d28 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b85d28 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b85c60 bytes 88020034
+ 00b85d28 bytes 88020034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85df2e0f0eee2a8d3f96c301480c816a"></a>

### [`00b85d1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85d1c.md) → [`00b85de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85de4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEEC2EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85d1c.md#insn-00b85d54)
- 新版 `00b85e1c`（命令位置の公開資料なし）

~~~diff
- 00b85d54 ["INT_ADD", "register:40f0:8", ["const:b85d54:8", "const:4:8"]]
- 00b85d54 ["CALL", null, ["callee:00bdb340:8"]]
+ 00b85e1c ["INT_ADD", "register:40f0:8", ["const:b85e1c:8", "const:4:8"]]
+ 00b85e1c ["CALL", null, ["callee:00bdb340:8"]]
- 00b85d54 bytes 4f550194
+ 00b85e1c bytes 49550194
~~~


<a id="compare-4f39a33b80665a2b4ad921ad7b27c8df"></a>

### [`00b85d74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85d74.md) → [`00b85e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85e3c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEEC1EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)

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
    "old": {
      "definition_site": "00b85da0",
      "incomplete_value": true,
      "site": "00b85da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "old": {
      "definition_site": "00b85d9c",
      "incomplete_value": true,
      "site": "00b85da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b85e58",
      "READ",
      [
        "storage",
        "00c1bc20",
        null,
        "pointer"
      ]
    ],
    [
      "00b85e68",
      "DATA",
      [
        "storage",
        "00c131e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b85e6c",
      "DATA",
      [
        "storage",
        "00c131b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b85e58",
      "READ",
      [
        "storage",
        "00c1bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00b85e68",
      "DATA",
      [
        "storage",
        "00c13290",
        null,
        "pointer"
      ]
    ],
    [
      "00b85e6c",
      "DATA",
      [
        "storage",
        "00c13268",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b85d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85d74.md#insn-00b85d90) · [`00b85dac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85d74.md#insn-00b85dac)
- 新版 `00b85e58`（命令位置の公開資料なし） · `00b85e74`（命令位置の公開資料なし）

~~~diff
- 00b85d90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c20:8"]]
- 00b85d90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b85e58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
+ 00b85e58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b85d90 bytes 081146f9
+ 00b85e58 bytes 086946f9
- 00b85dac ["INT_ADD", "register:40f0:8", ["const:b85dac:8", "const:4:8"]]
- 00b85dac ["CALL", null, ["callee:00bdb340:8"]]
+ 00b85e74 ["INT_ADD", "register:40f0:8", ["const:b85e74:8", "const:4:8"]]
+ 00b85e74 ["CALL", null, ["callee:00bdb340:8"]]
- 00b85dac bytes 39550194
+ 00b85e74 bytes 33550194
~~~


<a id="compare-fabdc3864a9c0ca69ffc71c07e94f031"></a>

### [`00b85ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85ed8.md) → [`00b85fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85fa0.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE6sentryC1ERS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00be1300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1300.md) · 呼出先 1件 [`00be12f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be12f0.md)
- 新版 呼出元 1件 [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md) · 呼出先 1件 [`00be13a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85ed8.md#insn-00b85ef4) · [`00b85f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85ed8.md#insn-00b85f00) · [`00b85f1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85ed8.md#insn-00b85f1c)
- 新版 `00b85fbc`（命令位置の公開資料なし） · `00b85fc8`（命令位置の公開資料なし） · `00b85fe4`（命令位置の公開資料なし）

~~~diff
- 00b85ef4 ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b85ef4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b85fbc ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
+ 00b85fbc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b85ef4 bytes 49000034
+ 00b85fbc bytes 49000034
- 00b85f00 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b85f00 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b85fc8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b85fc8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b85f00 bytes 880100b4
+ 00b85fc8 bytes 880100b4
- 00b85f1c ["INT_ADD", "register:40f0:8", ["const:b85f1c:8", "const:4:8"]]
- 00b85f1c ["CALL", null, ["callee:00be13a0:8"]]
+ 00b85fe4 ["INT_ADD", "register:40f0:8", ["const:b85fe4:8", "const:4:8"]]
+ 00b85fe4 ["CALL", null, ["callee:00be13a0:8"]]
- 00b85f1c bytes f56c0194
+ 00b85fe4 bytes ef6c0194
~~~


<a id="compare-e5b0c1570f448e317619b34051bba6f0"></a>

### [`00b86060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b86060.md) → [`00b86128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86128.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1300.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)

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
    "old": {
      "definition_site": "00b860b4",
      "incomplete_value": true,
      "site": "00b860b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
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
    "old": {
      "definition_site": "00b860fc",
      "incomplete_value": true,
      "site": "00b86100",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "00b8617c",
      "READ",
      [
        "storage",
        "00c1bc28",
        null,
        "pointer"
      ]
    ],
    [
      "00b8617c",
      "PARAM",
      [
        "storage",
        "010a27a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b861c4",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b8617c",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b8617c",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b861c4",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b860b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b86060.md#insn-00b860b8) · [`00b86100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b86060.md#insn-00b86100) · [`00b8608c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b86060.md#insn-00b8608c)
- 新版 `00b86180`（命令位置の公開資料なし） · `00b861c8`（命令位置の公開資料なし） · `00b86154`（命令位置の公開資料なし）

~~~diff
- 00b860b8 ["INT_ADD", "register:40f0:8", ["const:b860b8:8", "const:4:8"]]
- 00b860b8 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b86180 ["INT_ADD", "register:40f0:8", ["const:b86180:8", "const:4:8"]]
+ 00b86180 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b860b8 bytes 9e540194
+ 00b86180 bytes 98540194
- 00b86100 ["INT_ADD", "register:40f0:8", ["const:b86100:8", "const:4:8"]]
- 00b86100 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b861c8 ["INT_ADD", "register:40f0:8", ["const:b861c8:8", "const:4:8"]]
+ 00b861c8 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b86100 bytes 8c540194
+ 00b861c8 bytes 86540194
- 00b8608c ["INT_ADD", "register:40f0:8", ["const:b8608c:8", "const:4:8"]]
- 00b8608c ["CALL", null, ["callee:00be13b0:8"]]
+ 00b86154 ["INT_ADD", "register:40f0:8", ["const:b86154:8", "const:4:8"]]
+ 00b86154 ["CALL", null, ["callee:00be13b0:8"]]
- 00b8608c bytes 9d6c0194
+ 00b86154 bytes 976c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed30857201a289f0fba98ae4a8aefe85"></a>

### [`00b861f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b861f0.md) → [`00b862b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b862b8.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEs

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1300.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b86314",
      "incomplete_value": true,
      "site": "00b86318",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b8624c",
      "incomplete_value": true,
      "site": "00b86250",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
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
      "definition_site": "00b8635c",
      "incomplete_value": true,
      "site": "00b86360",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b86294",
      "incomplete_value": true,
      "site": "00b86298",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "00b86314",
      "READ",
      [
        "storage",
        "00c1bc28",
        null,
        "pointer"
      ]
    ],
    [
      "00b86314",
      "PARAM",
      [
        "storage",
        "010a27a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b8635c",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b86314",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b86314",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b8635c",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b861f0.md#insn-00b86250) · [`00b86298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b861f0.md#insn-00b86298) · [`00b86220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b861f0.md#insn-00b86220)
- 新版 `00b86318`（命令位置の公開資料なし） · `00b86360`（命令位置の公開資料なし） · `00b862e8`（命令位置の公開資料なし）

~~~diff
- 00b86250 ["INT_ADD", "register:40f0:8", ["const:b86250:8", "const:4:8"]]
- 00b86250 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b86318 ["INT_ADD", "register:40f0:8", ["const:b86318:8", "const:4:8"]]
+ 00b86318 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b86250 bytes 38540194
+ 00b86318 bytes 32540194
- 00b86298 ["INT_ADD", "register:40f0:8", ["const:b86298:8", "const:4:8"]]
- 00b86298 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b86360 ["INT_ADD", "register:40f0:8", ["const:b86360:8", "const:4:8"]]
+ 00b86360 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b86298 bytes 26540194
+ 00b86360 bytes 20540194
- 00b86220 ["INT_ADD", "register:40f0:8", ["const:b86220:8", "const:4:8"]]
- 00b86220 ["CALL", null, ["callee:00be13b0:8"]]
+ 00b862e8 ["INT_ADD", "register:40f0:8", ["const:b862e8:8", "const:4:8"]]
+ 00b862e8 ["CALL", null, ["callee:00be13b0:8"]]
- 00b86220 bytes 386c0194
+ 00b862e8 bytes 326c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8672f4a497cc120d3a936b8ec646baf2"></a>

### [`00b863a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b863a8.md) → [`00b86470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86470.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEt

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1300.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.67% / 新版 90.67%

CFGの説明率　旧版 37.50% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b864c4",
      "incomplete_value": true,
      "site": "00b864c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b863fc",
      "incomplete_value": true,
      "site": "00b86400",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
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
      "definition_site": "00b8650c",
      "incomplete_value": true,
      "site": "00b86510",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b86444",
      "incomplete_value": true,
      "site": "00b86448",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86488"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b864c4",
      "READ",
      [
        "storage",
        "00c1bc28",
        null,
        "pointer"
      ]
    ],
    [
      "00b864c4",
      "PARAM",
      [
        "storage",
        "010a27a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b86444",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b864c4",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b864c4",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b8650c",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b863a8.md#insn-00b86400) · [`00b86448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b863a8.md#insn-00b86448) · [`00b86488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b863a8.md#insn-00b86488)
- 新版 `00b864c8`（命令位置の公開資料なし） · `00b86510`（命令位置の公開資料なし）

~~~diff
- 00b86400 ["INT_ADD", "register:40f0:8", ["const:b86400:8", "const:4:8"]]
- 00b86400 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b864c8 ["INT_ADD", "register:40f0:8", ["const:b864c8:8", "const:4:8"]]
+ 00b864c8 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b86400 bytes cc530194
+ 00b864c8 bytes c6530194
- 00b86448 ["INT_ADD", "register:40f0:8", ["const:b86448:8", "const:4:8"]]
- 00b86448 ["CALL", null, ["callee:00bdb3e0:8"]]
+ 00b86510 ["INT_ADD", "register:40f0:8", ["const:b86510:8", "const:4:8"]]
+ 00b86510 ["CALL", null, ["callee:00bdb3e0:8"]]
- 00b86448 bytes ba530194
+ 00b86510 bytes b4530194
- 00b86488 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b86488 ["INT_ADD", "register:40f0:8", ["const:b86488:8", "const:4:8"]]
- 00b86488 ["CALLIND", null, ["register:0:8"]]
- 00b86488 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f248bf94151c70a4b1edfae5c35d9f25"></a>

### [`00b86538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b86538.md) → [`00b86600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86600.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb320.md) [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1300.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86540"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86540"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86544"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b86540",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b86544",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b86548",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b86608",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b8660c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b86610",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b86538.md#insn-00b86540) · [`00b86544`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b86538.md#insn-00b86544) · [`00b86548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b86/00b86538.md#insn-00b86548)

~~~diff
- 00b86540 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b86540 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b86540 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b86540 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b86540 bytes fd7b01a9
- 00b86544 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b86544 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00b86544 bytes f91300f9
- 00b86548 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b86548 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b86548 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b86548 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b86548 bytes f85f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

