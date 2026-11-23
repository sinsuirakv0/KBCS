# v15.7.3 → v15.7.4 · 最優先の変更候補 (42)

[一覧の目次](README.md)

<a id="compare-9540a3cc06f509238559b867ca95fc37"></a>

### [`00855e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855e44.md) → [`00855e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855e44.md) FUN_00855e44

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
      "definition_site": "00855e50",
      "incomplete_value": false,
      "site": "00855e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00855e50",
      "incomplete_value": false,
      "site": "00855e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
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
      "00855e50",
      "DATA",
      [
        "storage",
        "00c02fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00855e50",
      "DATA",
      [
        "storage",
        "00c03018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00855e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855e44.md#insn-00855e48) · [`00855e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855e44.md#insn-00855e4c)
- 新版 [`00855e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855e44.md#insn-00855e48) · [`00855e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855e44.md#insn-00855e4c)

~~~diff
- 00855e48 ["COPY", "register:4048:8", ["const:c02000:8"]]
+ 00855e48 ["COPY", "register:4048:8", ["const:c03000:8"]]
- 00855e48 bytes 691d00b0
+ 00855e48 bytes 691d00d0
- 00855e4c ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 00855e4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00855e4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00855e4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00855e4c ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00855e4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00855e4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00855e4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00855e4c bytes 29213f91
+ 00855e4c bytes 29610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b513642cb4927ed25bed9ed1bcee8982"></a>

### [`00856010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856010.md) → [`00856010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856010.md) FUN_00856010

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
      "definition_site": "00856034",
      "incomplete_value": false,
      "site": "00856034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856034",
      "incomplete_value": false,
      "site": "00856034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00856034",
      "DATA",
      [
        "storage",
        "00c03058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00856034",
      "DATA",
      [
        "storage",
        "00c030a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00856030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856010.md#insn-00856030)
- 新版 [`00856030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856010.md#insn-00856030)

~~~diff
- 00856030 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00856030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00856030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00856030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00856030 ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 00856030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00856030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00856030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00856030 bytes 08610191
+ 00856030 bytes 08a10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4ca8eba820c02206401a51c09752d3c"></a>

### [`00856204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856204.md) → [`00856204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856204.md) FUN_00856204

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
      "definition_site": "00856218",
      "incomplete_value": false,
      "site": "0085621c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856218",
      "incomplete_value": false,
      "site": "0085621c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "0085621c",
      "DATA",
      [
        "storage",
        "00c030e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085621c",
      "DATA",
      [
        "storage",
        "00c03138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00856218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856204.md#insn-00856218)
- 新版 [`00856218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856204.md#insn-00856218)

~~~diff
- 00856218 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00856218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00856218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00856218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00856218 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 00856218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00856218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00856218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00856218 bytes 08a10391
+ 00856218 bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-439fdf0f34cdbc1d4201252309391bcf"></a>

### [`00856228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856228.md) → [`00856228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856228.md) FUN_00856228

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
      "definition_site": "0085622c",
      "incomplete_value": false,
      "site": "00856230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085622c",
      "incomplete_value": false,
      "site": "00856230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "00856230",
      "DATA",
      [
        "storage",
        "00c030e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00856230",
      "DATA",
      [
        "storage",
        "00c03138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085622c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856228.md#insn-0085622c)
- 新版 [`0085622c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856228.md#insn-0085622c)

~~~diff
- 0085622c ["COPY", "tmp:0:8", ["const:e8:8"]]
- 0085622c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085622c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085622c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085622c ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0085622c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085622c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085622c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085622c bytes 08a10391
+ 0085622c bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c9e7d01e24421423ca30d9bbd536de5"></a>

### [`00856700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856700.md) → [`00856700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856700.md) FUN_00856700

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
      "definition_site": "00856724",
      "incomplete_value": false,
      "site": "00856724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856724",
      "incomplete_value": false,
      "site": "00856724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:168:8"
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
      "00856724",
      "DATA",
      [
        "storage",
        "00c03168",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00856724",
      "DATA",
      [
        "storage",
        "00c031b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00856720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856700.md#insn-00856720)
- 新版 [`00856720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856700.md#insn-00856720)

~~~diff
- 00856720 ["COPY", "tmp:0:8", ["const:168:8"]]
- 00856720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00856720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00856720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00856720 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 00856720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00856720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00856720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00856720 bytes 08a10591
+ 00856720 bytes 08e10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a34fe6ecbbdd99591fabb52fe8ad7bd"></a>

### [`00856bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bb0.md) → [`00856bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856bb0.md) FUN_00856bb0

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
      "definition_site": "00856bbc",
      "incomplete_value": false,
      "site": "00856bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856bbc",
      "incomplete_value": false,
      "site": "00856bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
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
      "00856bbc",
      "DATA",
      [
        "storage",
        "00c031e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00856bbc",
      "DATA",
      [
        "storage",
        "00c03238",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00856bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bb0.md#insn-00856bb8)
- 新版 [`00856bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856bb0.md#insn-00856bb8)

~~~diff
- 00856bb8 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00856bb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00856bb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00856bb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00856bb8 ["COPY", "tmp:0:8", ["const:238:8"]]
+ 00856bb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00856bb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00856bb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00856bb8 bytes 29a10791
+ 00856bb8 bytes 29e10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b17aeb73162b34f897db57ada0454742"></a>

### [`00856bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bcc.md) → [`00856bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856bcc.md) FUN_00856bcc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00856d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856d90.md) [`00856d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856d94.md) [`0085718c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/0085718c.md) [`00857190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857190.md) [`00ad7d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7d44.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00856d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856d90.md) [`00856d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856d94.md) [`0085718c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/0085718c.md) [`00857190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857190.md) [`00ad7d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7d88.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.57% / 新版 90.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00856c04",
      "incomplete_value": false,
      "site": "00856c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856c04",
      "incomplete_value": false,
      "site": "00856c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00856c10",
      "incomplete_value": false,
      "site": "00856c10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856c10",
      "incomplete_value": false,
      "site": "00856c10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
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
      "00856c04",
      "DATA",
      [
        "storage",
        "00c03258",
        null,
        "undefined *"
      ]
    ],
    [
      "00856c10",
      "DATA",
      [
        "storage",
        "00c032d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00856c44",
      "READ",
      [
        "storage",
        "00c032f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00856c04",
      "DATA",
      [
        "storage",
        "00c032a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00856c10",
      "DATA",
      [
        "storage",
        "00c03328",
        null,
        "undefined *"
      ]
    ],
    [
      "00856c44",
      "READ",
      [
        "storage",
        "00c03348",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00856be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bcc.md#insn-00856be4) · [`00856c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bcc.md#insn-00856c08)
- 新版 [`00856be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856bcc.md#insn-00856be4) · [`00856c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856bcc.md#insn-00856c08)

~~~diff
- 00856be4 ["COPY", "tmp:0:8", ["const:258:8"]]
- 00856be4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00856be4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00856be4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00856be4 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 00856be4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00856be4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00856be4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00856be4 bytes 29610991
+ 00856be4 bytes 29a10a91
- 00856c08 ["COPY", "register:4048:8", ["const:c03000:8"]]
- 00856c08 bytes 691d00b0
+ 00856c08 ["COPY", "register:4048:8", ["const:c03000:8"]]
+ 00856c08 bytes 691d00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5b450c2640263baac4fcb5b3290510d"></a>

### [`00856d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856d48.md) → [`00856d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856d48.md) FUN_00856d48

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
      "definition_site": "00856d6c",
      "incomplete_value": false,
      "site": "00856d6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856d6c",
      "incomplete_value": false,
      "site": "00856d6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:258:8"
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
      "00856d6c",
      "DATA",
      [
        "storage",
        "00c03258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00856d6c",
      "DATA",
      [
        "storage",
        "00c032a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00856d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856d48.md#insn-00856d68)
- 新版 [`00856d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856d48.md#insn-00856d68)

~~~diff
- 00856d68 ["COPY", "tmp:0:8", ["const:258:8"]]
- 00856d68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00856d68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00856d68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00856d68 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 00856d68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00856d68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00856d68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00856d68 bytes 08610991
+ 00856d68 bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee9641148ca5091a2b5af268202351d3"></a>

### [`00856d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856d7c.md) → [`00856d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856d7c.md) FUN_00856d7c

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
      "definition_site": "00856d88",
      "incomplete_value": false,
      "site": "00856d88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856d88",
      "incomplete_value": false,
      "site": "00856d88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:258:8"
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
      "00856d88",
      "DATA",
      [
        "storage",
        "00c03258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00856d88",
      "DATA",
      [
        "storage",
        "00c032a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00856d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856d7c.md#insn-00856d84)
- 新版 [`00856d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856d7c.md#insn-00856d84)

~~~diff
- 00856d84 ["COPY", "tmp:0:8", ["const:258:8"]]
- 00856d84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00856d84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00856d84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00856d84 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 00856d84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00856d84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00856d84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00856d84 bytes 29610991
+ 00856d84 bytes 29a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13657db8b0de25f2aab2b19bc580cc70"></a>

### [`00857144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857144.md) → [`00857144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857144.md) FUN_00857144

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
      "definition_site": "00857168",
      "incomplete_value": false,
      "site": "00857168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857168",
      "incomplete_value": false,
      "site": "00857168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
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
      "00857168",
      "DATA",
      [
        "storage",
        "00c032d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00857168",
      "DATA",
      [
        "storage",
        "00c03328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857144.md#insn-00857164)
- 新版 [`00857164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857144.md#insn-00857164)

~~~diff
- 00857164 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 00857164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857164 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00857164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857164 bytes 08610b91
+ 00857164 bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0eda259cd5d2b4f13d06b1ec98b5bb9"></a>

### [`00857178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857178.md) → [`00857178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857178.md) FUN_00857178

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
      "definition_site": "00857184",
      "incomplete_value": false,
      "site": "00857184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857184",
      "incomplete_value": false,
      "site": "00857184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
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
      "00857184",
      "DATA",
      [
        "storage",
        "00c032d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00857184",
      "DATA",
      [
        "storage",
        "00c03328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857178.md#insn-00857180)
- 新版 [`00857180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857178.md#insn-00857180)

~~~diff
- 00857180 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 00857180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00857180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00857180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00857180 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00857180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00857180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00857180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00857180 bytes 29610b91
+ 00857180 bytes 29a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54403d1a09298d34bcf85d8d5ccabf13"></a>

### [`00857194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857194.md) → [`00857194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857194.md) FUN_00857194

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00678b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c7f0.md) [`0067c9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c9c0.md) [`0067c9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c9c4.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00469f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f78.md) [`00678b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c7f0.md) [`0067c9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c9c0.md) [`0067c9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c9c4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.47% / 新版 97.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00857230",
      "incomplete_value": false,
      "site": "0085723c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857230",
      "incomplete_value": false,
      "site": "0085723c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:348:8"
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
      "0085723c",
      "DATA",
      [
        "storage",
        "00c03348",
        null,
        "undefined *"
      ]
    ],
    [
      "00857288",
      "READ",
      [
        "storage",
        "00c03368",
        null,
        "pointer"
      ]
    ],
    [
      "00857288",
      "READ",
      [
        "storage",
        "00c03370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085723c",
      "DATA",
      [
        "storage",
        "00c03398",
        null,
        "undefined *"
      ]
    ],
    [
      "00857288",
      "READ",
      [
        "storage",
        "00c033b8",
        null,
        "pointer"
      ]
    ],
    [
      "00857288",
      "READ",
      [
        "storage",
        "00c033c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857194.md#insn-00857230)
- 新版 [`00857230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857194.md#insn-00857230)

~~~diff
- 00857230 ["COPY", "tmp:0:8", ["const:348:8"]]
- 00857230 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857230 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857230 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857230 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 00857230 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857230 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857230 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857230 bytes 08210d91
+ 00857230 bytes 08610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2c1f427ed5e706bb664de7265fdeac2"></a>

### [`00857374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857374.md) → [`00857374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857374.md) FUN_00857374

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
      "definition_site": "00857388",
      "incomplete_value": false,
      "site": "0085738c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857388",
      "incomplete_value": false,
      "site": "0085738c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:348:8"
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
      "0085738c",
      "DATA",
      [
        "storage",
        "00c03348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085738c",
      "DATA",
      [
        "storage",
        "00c03398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857374.md#insn-00857388)
- 新版 [`00857388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857374.md#insn-00857388)

~~~diff
- 00857388 ["COPY", "tmp:0:8", ["const:348:8"]]
- 00857388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857388 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 00857388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857388 bytes 08210d91
+ 00857388 bytes 08610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b66222aa54bf18ce0d532b5fb6bd2be7"></a>

### [`00857398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857398.md) → [`00857398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857398.md) FUN_00857398

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
      "definition_site": "0085739c",
      "incomplete_value": false,
      "site": "008573a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085739c",
      "incomplete_value": false,
      "site": "008573a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:348:8"
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
      "008573a0",
      "DATA",
      [
        "storage",
        "00c03348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008573a0",
      "DATA",
      [
        "storage",
        "00c03398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085739c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857398.md#insn-0085739c)
- 新版 [`0085739c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857398.md#insn-0085739c)

~~~diff
- 0085739c ["COPY", "tmp:0:8", ["const:348:8"]]
- 0085739c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085739c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085739c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085739c ["COPY", "tmp:0:8", ["const:398:8"]]
+ 0085739c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085739c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085739c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085739c bytes 08210d91
+ 0085739c bytes 08610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb58780670b010b4601aa3228da1ed9d"></a>

### [`008577f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008577f8.md) → [`008577f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/008577f8.md) FUN_008577f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/008544a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00857830",
      "incomplete_value": false,
      "site": "0085783c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857830",
      "incomplete_value": false,
      "site": "0085783c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
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
      "definition_site": "00857850",
      "incomplete_value": false,
      "site": "00857854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857850",
      "incomplete_value": false,
      "site": "00857854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      "definition_site": "0085786c",
      "incomplete_value": false,
      "site": "00857874",
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
            "const:966:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085786c",
      "incomplete_value": false,
      "site": "00857874",
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
            "const:8db:8"
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
      "0085783c",
      "DATA",
      [
        "storage",
        "00c033e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00857854",
      "DATA",
      [
        "storage",
        "00c02e30",
        null,
        "pointer"
      ]
    ],
    [
      "0085786c",
      "PARAM",
      [
        "storage",
        "002a28db",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0085783c",
      "DATA",
      [
        "storage",
        "00c03438",
        null,
        "undefined *"
      ]
    ],
    [
      "00857854",
      "DATA",
      [
        "storage",
        "00c02e80",
        null,
        "pointer"
      ]
    ],
    [
      "0085786c",
      "PARAM",
      [
        "storage",
        "002a2966",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008577f8.md#insn-00857830) · [`00857850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008577f8.md#insn-00857850) · [`0085786c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008577f8.md#insn-0085786c)
- 新版 [`00857830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/008577f8.md#insn-00857830) · [`00857850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/008577f8.md#insn-00857850) · [`0085786c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/008577f8.md#insn-0085786c)

~~~diff
- 00857830 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 00857830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857830 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00857830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857830 bytes 08a10f91
+ 00857830 bytes 08e11091
- 00857850 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00857850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857850 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00857850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857850 bytes 08c13891
+ 00857850 bytes 08013a91
- 0085786c ["COPY", "tmp:0:8", ["const:8db:8"]]
- 0085786c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0085786c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0085786c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0085786c ["COPY", "tmp:0:8", ["const:966:8"]]
+ 0085786c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0085786c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0085786c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0085786c bytes 216c2391
+ 0085786c bytes 21982591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7bdbeb5a1fcd197c598f0d3c0697125"></a>

### [`008578cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008578cc.md) → [`008578cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/008578cc.md) FUN_008578cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "008578d0",
      "incomplete_value": false,
      "site": "008578d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008578d0",
      "incomplete_value": false,
      "site": "008578d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
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
      "008578d4",
      "DATA",
      [
        "storage",
        "00c033e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008578d4",
      "DATA",
      [
        "storage",
        "00c03438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008578d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008578cc.md#insn-008578d0)
- 新版 [`008578d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/008578cc.md#insn-008578d0)

~~~diff
- 008578d0 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 008578d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008578d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008578d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008578d0 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 008578d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008578d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008578d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008578d0 bytes 08a10f91
+ 008578d0 bytes 08e11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-928455fecbf392a62bced63ac14a0276"></a>

### [`008578dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008578dc.md) → [`008578dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/008578dc.md) FUN_008578dc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008578ec",
      "incomplete_value": false,
      "site": "008578f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008578ec",
      "incomplete_value": false,
      "site": "008578f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
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
      "008578f4",
      "DATA",
      [
        "storage",
        "00c033e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008578f4",
      "DATA",
      [
        "storage",
        "00c03438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008578ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008578dc.md#insn-008578ec)
- 新版 [`008578ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/008578dc.md#insn-008578ec)

~~~diff
- 008578ec ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 008578ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008578ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008578ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008578ec ["COPY", "tmp:0:8", ["const:438:8"]]
+ 008578ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008578ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008578ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008578ec bytes 08a10f91
+ 008578ec bytes 08e11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89a2f2157482e5acaf5264d01dc518c9"></a>

### [`00857d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857d90.md) → [`00857d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857d90.md) FUN_00857d90

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/008544a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.37% / 新版 88.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00857de8",
      "incomplete_value": false,
      "site": "00857dec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857de8",
      "incomplete_value": false,
      "site": "00857dec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "definition_site": "00857e08",
      "incomplete_value": false,
      "site": "00857e10",
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
            "const:121:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857e08",
      "incomplete_value": false,
      "site": "00857e10",
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
            "const:1ae:8"
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
      "definition_site": "00857e18",
      "incomplete_value": false,
      "site": "00857e20",
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
            "const:795:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857e18",
      "incomplete_value": false,
      "site": "00857e20",
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
            "const:6fb:8"
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
      "00857dd4",
      "DATA",
      [
        "storage",
        "00c03438",
        null,
        "undefined *"
      ]
    ],
    [
      "00857dec",
      "DATA",
      [
        "storage",
        "00c02e50",
        null,
        "pointer"
      ]
    ],
    [
      "00857e08",
      "PARAM",
      [
        "storage",
        "002981ae",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00857dd4",
      "DATA",
      [
        "storage",
        "00c03488",
        null,
        "undefined *"
      ]
    ],
    [
      "00857dec",
      "DATA",
      [
        "storage",
        "00c02ea0",
        null,
        "pointer"
      ]
    ],
    [
      "00857e08",
      "PARAM",
      [
        "storage",
        "00298121",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857d90.md#insn-00857dc8) · [`00857de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857d90.md#insn-00857de8) · [`00857e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857d90.md#insn-00857e08)
- 新版 [`00857dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857d90.md#insn-00857dc8) · [`00857de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857d90.md#insn-00857de8) · [`00857e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857d90.md#insn-00857e08)

~~~diff
- 00857dc8 ["COPY", "tmp:0:8", ["const:438:8"]]
- 00857dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857dc8 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00857dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857dc8 bytes 08e11091
+ 00857dc8 bytes 08211291
- 00857de8 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00857de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857de8 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00857de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857de8 bytes 08413991
+ 00857de8 bytes 08813a91
- 00857e08 ["COPY", "tmp:0:8", ["const:1ae:8"]]
- 00857e08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00857e08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00857e08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00857e08 ["COPY", "tmp:0:8", ["const:121:8"]]
+ 00857e08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00857e08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00857e08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00857e08 bytes 21b80691
+ 00857e08 bytes 21840491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e21bb2f33d18a6bf94c7b09a2fe03d87"></a>

### [`00857e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857e68.md) → [`00857e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857e68.md) FUN_00857e68

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00857e6c",
      "incomplete_value": false,
      "site": "00857e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857e6c",
      "incomplete_value": false,
      "site": "00857e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "00857e70",
      "DATA",
      [
        "storage",
        "00c03438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00857e70",
      "DATA",
      [
        "storage",
        "00c03488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857e68.md#insn-00857e6c)
- 新版 [`00857e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857e68.md#insn-00857e6c)

~~~diff
- 00857e6c ["COPY", "tmp:0:8", ["const:438:8"]]
- 00857e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857e6c ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00857e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857e6c bytes 08e11091
+ 00857e6c bytes 08211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42f9a09e8cfd0309bfe83297758a2414"></a>

### [`00857e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857e78.md) → [`00857e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857e78.md) FUN_00857e78

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00857e88",
      "incomplete_value": false,
      "site": "00857e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857e88",
      "incomplete_value": false,
      "site": "00857e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "00857e90",
      "DATA",
      [
        "storage",
        "00c03438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00857e90",
      "DATA",
      [
        "storage",
        "00c03488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857e78.md#insn-00857e88)
- 新版 [`00857e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857e78.md#insn-00857e88)

~~~diff
- 00857e88 ["COPY", "tmp:0:8", ["const:438:8"]]
- 00857e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857e88 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00857e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857e88 bytes 08e11091
+ 00857e88 bytes 08211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30015b5b9036e6dc4815f21ceef0ced9"></a>

### [`00857eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857eb4.md) → [`00857eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857eb4.md) FUN_00857eb4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/008544a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00857eec",
      "incomplete_value": false,
      "site": "00857ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857eec",
      "incomplete_value": false,
      "site": "00857ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "definition_site": "00857f0c",
      "incomplete_value": false,
      "site": "00857f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857f0c",
      "incomplete_value": false,
      "site": "00857f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
      "definition_site": "00857f2c",
      "incomplete_value": false,
      "site": "00857f34",
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
            "const:aaa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857f2c",
      "incomplete_value": false,
      "site": "00857f34",
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
            "const:a1f:8"
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
      "00857ef8",
      "DATA",
      [
        "storage",
        "00c03488",
        null,
        "undefined *"
      ]
    ],
    [
      "00857f10",
      "DATA",
      [
        "storage",
        "00c02e70",
        null,
        "pointer"
      ]
    ],
    [
      "00857f2c",
      "PARAM",
      [
        "storage",
        "002a3a1f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00857ef8",
      "DATA",
      [
        "storage",
        "00c034d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00857f10",
      "DATA",
      [
        "storage",
        "00c02ec0",
        null,
        "pointer"
      ]
    ],
    [
      "00857f2c",
      "PARAM",
      [
        "storage",
        "002a3aaa",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857eb4.md#insn-00857eec) · [`00857f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857eb4.md#insn-00857f0c) · [`00857f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857eb4.md#insn-00857f2c)
- 新版 [`00857eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857eb4.md#insn-00857eec) · [`00857f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857eb4.md#insn-00857f0c) · [`00857f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857eb4.md#insn-00857f2c)

~~~diff
- 00857eec ["COPY", "tmp:0:8", ["const:488:8"]]
- 00857eec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857eec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857eec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857eec ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 00857eec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857eec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857eec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857eec bytes 08211291
+ 00857eec bytes 08611391
- 00857f0c ["COPY", "tmp:0:8", ["const:e70:8"]]
- 00857f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857f0c ["COPY", "tmp:0:8", ["const:ec0:8"]]
+ 00857f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857f0c bytes 08c13991
+ 00857f0c bytes 08013b91
- 00857f2c ["COPY", "tmp:0:8", ["const:a1f:8"]]
- 00857f2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00857f2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00857f2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00857f2c ["COPY", "tmp:0:8", ["const:aaa:8"]]
+ 00857f2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00857f2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00857f2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00857f2c bytes 217c2891
+ 00857f2c bytes 21a82a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3eb864404f4ccde1d8401014e8723c1"></a>

### [`00857f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857f8c.md) → [`00857f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857f8c.md) FUN_00857f8c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00857f90",
      "incomplete_value": false,
      "site": "00857f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857f90",
      "incomplete_value": false,
      "site": "00857f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "00857f94",
      "DATA",
      [
        "storage",
        "00c03488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00857f94",
      "DATA",
      [
        "storage",
        "00c034d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857f8c.md#insn-00857f90)
- 新版 [`00857f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857f8c.md#insn-00857f90)

~~~diff
- 00857f90 ["COPY", "tmp:0:8", ["const:488:8"]]
- 00857f90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857f90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857f90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857f90 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 00857f90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857f90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857f90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857f90 bytes 08211291
+ 00857f90 bytes 08611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b3177c39686b99deda91fcedcff006"></a>

### [`00857f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857f9c.md) → [`00857f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857f9c.md) FUN_00857f9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00857fac",
      "incomplete_value": false,
      "site": "00857fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857fac",
      "incomplete_value": false,
      "site": "00857fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "00857fb4",
      "DATA",
      [
        "storage",
        "00c03488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00857fb4",
      "DATA",
      [
        "storage",
        "00c034d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857f9c.md#insn-00857fac)
- 新版 [`00857fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857f9c.md#insn-00857fac)

~~~diff
- 00857fac ["COPY", "tmp:0:8", ["const:488:8"]]
- 00857fac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857fac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857fac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857fac ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 00857fac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857fac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857fac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857fac bytes 08211291
+ 00857fac bytes 08611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b66756b2be7bfe67b4b1f6a4ec7def3"></a>

### [`00857fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857fd8.md) → [`00857fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857fd8.md) FUN_00857fd8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/008544a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858030",
      "incomplete_value": false,
      "site": "00858034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858030",
      "incomplete_value": false,
      "site": "00858034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00858058"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00858060",
      "incomplete_value": false,
      "site": "00858068",
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
            "const:ccc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858060",
      "incomplete_value": false,
      "site": "00858068",
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
            "const:c41:8"
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
      "0085801c",
      "DATA",
      [
        "storage",
        "00c034d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00858034",
      "DATA",
      [
        "storage",
        "00c02e90",
        null,
        "pointer"
      ]
    ],
    [
      "00858050",
      "PARAM",
      [
        "storage",
        "0029b9e2",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0085801c",
      "DATA",
      [
        "storage",
        "00c03528",
        null,
        "undefined *"
      ]
    ],
    [
      "00858034",
      "DATA",
      [
        "storage",
        "00c02ee0",
        null,
        "pointer"
      ]
    ],
    [
      "00858050",
      "PARAM",
      [
        "storage",
        "0029b9e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857fd8.md#insn-00858058) · [`00858010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857fd8.md#insn-00858010)
- 新版 [`00858058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857fd8.md#insn-00858058) · [`00858010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857fd8.md#insn-00858010)

~~~diff
- 00858058 ["INT_ADD", "register:40f0:8", ["const:858058:8", "const:4:8"]]
- 00858058 ["CALL", null, ["callee:00bdb340:8"]]
- 00858058 bytes a60c0e94
+ 00858058 ["INT_ADD", "register:40f0:8", ["const:858058:8", "const:4:8"]]
+ 00858058 ["CALL", null, ["callee:00bdb340:8"]]
+ 00858058 bytes ba0c0e94
- 00858010 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 00858010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858010 ["COPY", "tmp:0:8", ["const:528:8"]]
+ 00858010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858010 bytes 08611391
+ 00858010 bytes 08a11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e0750c477426c96353ca6d9132d9baf"></a>

### [`008580b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580b0.md) → [`008580b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008580b0.md) FUN_008580b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "008580b4",
      "incomplete_value": false,
      "site": "008580b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008580b4",
      "incomplete_value": false,
      "site": "008580b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "008580b8",
      "DATA",
      [
        "storage",
        "00c034d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008580b8",
      "DATA",
      [
        "storage",
        "00c03528",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008580b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580b0.md#insn-008580b4)
- 新版 [`008580b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008580b0.md#insn-008580b4)

~~~diff
- 008580b4 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 008580b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008580b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008580b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008580b4 ["COPY", "tmp:0:8", ["const:528:8"]]
+ 008580b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008580b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008580b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008580b4 bytes 08611391
+ 008580b4 bytes 08a11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1d92b3f1b21f248349bb6af974185b2"></a>

### [`008580fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580fc.md) → [`008580fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008580fc.md) FUN_008580fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/008544a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858134",
      "incomplete_value": false,
      "site": "00858140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858134",
      "incomplete_value": false,
      "site": "00858140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "definition_site": "00858154",
      "incomplete_value": false,
      "site": "00858158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858154",
      "incomplete_value": false,
      "site": "00858158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "00858170",
      "incomplete_value": false,
      "site": "00858178",
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
            "const:886:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858170",
      "incomplete_value": false,
      "site": "00858178",
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
            "const:7ec:8"
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
      "00858140",
      "DATA",
      [
        "storage",
        "00c03528",
        null,
        "undefined *"
      ]
    ],
    [
      "00858158",
      "DATA",
      [
        "storage",
        "00c02ed0",
        null,
        "pointer"
      ]
    ],
    [
      "00858170",
      "PARAM",
      [
        "storage",
        "002a87ec",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00858140",
      "DATA",
      [
        "storage",
        "00c03578",
        null,
        "undefined *"
      ]
    ],
    [
      "00858158",
      "DATA",
      [
        "storage",
        "00c02f20",
        null,
        "pointer"
      ]
    ],
    [
      "00858170",
      "PARAM",
      [
        "storage",
        "002a8886",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580fc.md#insn-00858134) · [`00858154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580fc.md#insn-00858154) · [`00858170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580fc.md#insn-00858170)
- 新版 [`00858134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008580fc.md#insn-00858134) · [`00858154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008580fc.md#insn-00858154) · [`00858170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008580fc.md#insn-00858170)

~~~diff
- 00858134 ["COPY", "tmp:0:8", ["const:528:8"]]
- 00858134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858134 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 00858134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858134 bytes 08a11491
+ 00858134 bytes 08e11591
- 00858154 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 00858154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858154 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00858154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858154 bytes 08413b91
+ 00858154 bytes 08813c91
- 00858170 ["COPY", "tmp:0:8", ["const:7ec:8"]]
- 00858170 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00858170 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00858170 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00858170 ["COPY", "tmp:0:8", ["const:886:8"]]
+ 00858170 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00858170 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00858170 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00858170 bytes 21b01f91
+ 00858170 bytes 21182291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faa2354aa4feabb7486a7ee9bf7dfa38"></a>

### [`008581d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008581d0.md) → [`008581d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008581d0.md) FUN_008581d0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "008581d4",
      "incomplete_value": false,
      "site": "008581d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008581d4",
      "incomplete_value": false,
      "site": "008581d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "008581d8",
      "DATA",
      [
        "storage",
        "00c03528",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008581d8",
      "DATA",
      [
        "storage",
        "00c03578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008581d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008581d0.md#insn-008581d4)
- 新版 [`008581d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008581d0.md#insn-008581d4)

~~~diff
- 008581d4 ["COPY", "tmp:0:8", ["const:528:8"]]
- 008581d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008581d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008581d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008581d4 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 008581d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008581d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008581d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008581d4 bytes 08a11491
+ 008581d4 bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b200fc1b962bc8bd7a8183f4c07cd75d"></a>

### [`008581e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008581e0.md) → [`008581e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008581e0.md) FUN_008581e0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008581f0",
      "incomplete_value": false,
      "site": "008581f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008581f0",
      "incomplete_value": false,
      "site": "008581f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "008581f8",
      "DATA",
      [
        "storage",
        "00c03528",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008581f8",
      "DATA",
      [
        "storage",
        "00c03578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008581f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008581e0.md#insn-008581f0)
- 新版 [`008581f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008581e0.md#insn-008581f0)

~~~diff
- 008581f0 ["COPY", "tmp:0:8", ["const:528:8"]]
- 008581f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008581f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008581f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008581f0 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 008581f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008581f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008581f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008581f0 bytes 08a11491
+ 008581f0 bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-608085cd1f6490fc5dc06055bdc225b2"></a>

### [`0085821c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085821c.md) → [`0085821c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/0085821c.md) FUN_0085821c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/008544a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858254",
      "incomplete_value": false,
      "site": "00858260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858254",
      "incomplete_value": false,
      "site": "00858260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "definition_site": "00858274",
      "incomplete_value": false,
      "site": "00858278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858274",
      "incomplete_value": false,
      "site": "00858278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "definition_site": "00858290",
      "incomplete_value": false,
      "site": "00858298",
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
            "const:a5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858290",
      "incomplete_value": false,
      "site": "00858298",
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
            "const:9c1:8"
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
      "00858260",
      "DATA",
      [
        "storage",
        "00c03578",
        null,
        "undefined *"
      ]
    ],
    [
      "00858278",
      "DATA",
      [
        "storage",
        "00c02eb0",
        null,
        "pointer"
      ]
    ],
    [
      "00858290",
      "PARAM",
      [
        "storage",
        "002a79c1",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00858260",
      "DATA",
      [
        "storage",
        "00c035c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00858278",
      "DATA",
      [
        "storage",
        "00c02f00",
        null,
        "pointer"
      ]
    ],
    [
      "00858290",
      "PARAM",
      [
        "storage",
        "002a7a5b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085821c.md#insn-00858254) · [`00858274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085821c.md#insn-00858274) · [`00858290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085821c.md#insn-00858290)
- 新版 [`00858254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/0085821c.md#insn-00858254) · [`00858274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/0085821c.md#insn-00858274) · [`00858290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/0085821c.md#insn-00858290)

~~~diff
- 00858254 ["COPY", "tmp:0:8", ["const:578:8"]]
- 00858254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858254 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 00858254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858254 bytes 08e11591
+ 00858254 bytes 08211791
- 00858274 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 00858274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858274 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 00858274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858274 bytes 08c13a91
+ 00858274 bytes 08013c91
- 00858290 ["COPY", "tmp:0:8", ["const:9c1:8"]]
- 00858290 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00858290 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00858290 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00858290 ["COPY", "tmp:0:8", ["const:a5b:8"]]
+ 00858290 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00858290 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00858290 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00858290 bytes 21042791
+ 00858290 bytes 216c2991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4de56668c2c95f12327e683eb6443fd8"></a>

### [`008582f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008582f0.md) → [`008582f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008582f0.md) FUN_008582f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "008582f4",
      "incomplete_value": false,
      "site": "008582f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008582f4",
      "incomplete_value": false,
      "site": "008582f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "008582f8",
      "DATA",
      [
        "storage",
        "00c03578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008582f8",
      "DATA",
      [
        "storage",
        "00c035c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008582f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008582f0.md#insn-008582f4)
- 新版 [`008582f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008582f0.md#insn-008582f4)

~~~diff
- 008582f4 ["COPY", "tmp:0:8", ["const:578:8"]]
- 008582f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008582f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008582f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008582f4 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 008582f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008582f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008582f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008582f4 bytes 08e11591
+ 008582f4 bytes 08211791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14fcb57f3a052feb9ee7c7702ef9dbf2"></a>

### [`00858300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858300.md) → [`00858300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858300.md) FUN_00858300

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858310",
      "incomplete_value": false,
      "site": "00858318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858310",
      "incomplete_value": false,
      "site": "00858318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "00858318",
      "DATA",
      [
        "storage",
        "00c03578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858318",
      "DATA",
      [
        "storage",
        "00c035c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858300.md#insn-00858310)
- 新版 [`00858310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858300.md#insn-00858310)

~~~diff
- 00858310 ["COPY", "tmp:0:8", ["const:578:8"]]
- 00858310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858310 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 00858310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858310 bytes 08e11591
+ 00858310 bytes 08211791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dca92800725e3ed4ef623b70b1d2ceb"></a>

### [`0085833c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085833c.md) → [`0085833c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/0085833c.md) FUN_0085833c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`0085790c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/0085790c.md) [`00857ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857ea8.md) [`00857fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857fcc.md) [`008580f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580f0.md) [`00858210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858210.md) · 呼出先 3件 [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 7件 [`0085790c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/0085790c.md) [`00857ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857ea8.md) [`00857fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857fcc.md) [`008580f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008580f0.md) [`00858210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858210.md) · 呼出先 3件 [`00574ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858360",
      "incomplete_value": false,
      "site": "00858364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858360",
      "incomplete_value": false,
      "site": "00858364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e10:8"
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
      "00858364",
      "DATA",
      [
        "storage",
        "00c02e10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00858364",
      "DATA",
      [
        "storage",
        "00c02e60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085833c.md#insn-00858360)
- 新版 [`00858360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/0085833c.md#insn-00858360)

~~~diff
- 00858360 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 00858360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858360 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 00858360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858360 bytes 08413891
+ 00858360 bytes 08813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fefafbf93940093d67d32a66cc9ccb0"></a>

### [`008584c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008584c0.md) → [`008584c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008584c0.md) FUN_008584c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/008544a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858528",
      "incomplete_value": false,
      "site": "00858530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858528",
      "incomplete_value": false,
      "site": "00858530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
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
      "definition_site": "0085854c",
      "incomplete_value": false,
      "site": "00858554",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085854c",
      "incomplete_value": false,
      "site": "00858554",
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
            "const:9ce:8"
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
      "00858518",
      "DATA",
      [
        "storage",
        "00c035c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00858530",
      "DATA",
      [
        "storage",
        "00c02ef0",
        null,
        "pointer"
      ]
    ],
    [
      "0085854c",
      "PARAM",
      [
        "storage",
        "002a79ce",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00858518",
      "DATA",
      [
        "storage",
        "00c03618",
        null,
        "undefined *"
      ]
    ],
    [
      "00858530",
      "DATA",
      [
        "storage",
        "00c02f40",
        null,
        "pointer"
      ]
    ],
    [
      "0085854c",
      "PARAM",
      [
        "storage",
        "002a7a68",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085850c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008584c0.md#insn-0085850c) · [`00858528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008584c0.md#insn-00858528) · [`0085854c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008584c0.md#insn-0085854c)
- 新版 [`0085850c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008584c0.md#insn-0085850c) · [`00858528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008584c0.md#insn-00858528) · [`0085854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008584c0.md#insn-0085854c)

~~~diff
- 0085850c ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 0085850c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085850c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085850c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085850c ["COPY", "tmp:0:8", ["const:618:8"]]
+ 0085850c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085850c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085850c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085850c bytes 08211791
+ 0085850c bytes 08611891
- 00858528 ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 00858528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858528 ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 00858528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858528 bytes 08c13b91
+ 00858528 bytes 08013d91
- 0085854c ["COPY", "tmp:0:8", ["const:9ce:8"]]
- 0085854c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0085854c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0085854c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0085854c ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 0085854c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0085854c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0085854c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0085854c bytes 21382791
+ 0085854c bytes 21a02991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da9498b51652e10fa5f4139a184cf16f"></a>

### [`008585b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008585b0.md) → [`008585b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008585b0.md) FUN_008585b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "008585b4",
      "incomplete_value": false,
      "site": "008585b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008585b4",
      "incomplete_value": false,
      "site": "008585b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "008585b8",
      "DATA",
      [
        "storage",
        "00c035c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008585b8",
      "DATA",
      [
        "storage",
        "00c03618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008585b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008585b0.md#insn-008585b4)
- 新版 [`008585b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008585b0.md#insn-008585b4)

~~~diff
- 008585b4 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 008585b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008585b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008585b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008585b4 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 008585b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008585b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008585b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008585b4 bytes 08211791
+ 008585b4 bytes 08611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35724f22744d627640b3c3c3f327b231"></a>

### [`008585c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008585c0.md) → [`008585c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008585c0.md) FUN_008585c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008585d0",
      "incomplete_value": false,
      "site": "008585d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008585d0",
      "incomplete_value": false,
      "site": "008585d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "008585d8",
      "DATA",
      [
        "storage",
        "00c035c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008585d8",
      "DATA",
      [
        "storage",
        "00c03618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008585d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008585c0.md#insn-008585d0)
- 新版 [`008585d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008585c0.md#insn-008585d0)

~~~diff
- 008585d0 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 008585d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008585d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008585d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008585d0 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 008585d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008585d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008585d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008585d0 bytes 08211791
+ 008585d0 bytes 08611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e69fdb6ea5cdf1a3ca90b2168bc8dfd0"></a>

### [`008585f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008585f0.md) → [`008585f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008585f0.md) FUN_008585f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md) [`0085833c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085833c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00574ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff4.md) [`0085833c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/0085833c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858618",
      "incomplete_value": false,
      "site": "00858618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858618",
      "incomplete_value": false,
      "site": "00858618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
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
      "00858618",
      "DATA",
      [
        "storage",
        "00c02ef0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00858618",
      "DATA",
      [
        "storage",
        "00c02f40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085860c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008585f0.md#insn-0085860c)
- 新版 [`0085860c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008585f0.md#insn-0085860c)

~~~diff
- 0085860c ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 0085860c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085860c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085860c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085860c ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 0085860c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085860c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085860c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085860c bytes 29c13b91
+ 0085860c bytes 29013d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fbd21252b480d9f8240b166a9d1b69d"></a>

### [`00858670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858670.md) → [`00858670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858670.md) FUN_00858670

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/008544a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008586a8",
      "incomplete_value": false,
      "site": "008586b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008586a8",
      "incomplete_value": false,
      "site": "008586b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "definition_site": "008586c8",
      "incomplete_value": false,
      "site": "008586cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008586c8",
      "incomplete_value": false,
      "site": "008586cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "008586e8",
      "incomplete_value": false,
      "site": "008586f0",
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
            "const:886:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008586e8",
      "incomplete_value": false,
      "site": "008586f0",
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
            "const:7ec:8"
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
      "008586b4",
      "DATA",
      [
        "storage",
        "00c03528",
        null,
        "undefined *"
      ]
    ],
    [
      "008586cc",
      "DATA",
      [
        "storage",
        "00c02ed0",
        null,
        "pointer"
      ]
    ],
    [
      "008586e8",
      "PARAM",
      [
        "storage",
        "002a87ec",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008586b4",
      "DATA",
      [
        "storage",
        "00c03578",
        null,
        "undefined *"
      ]
    ],
    [
      "008586cc",
      "DATA",
      [
        "storage",
        "00c02f20",
        null,
        "pointer"
      ]
    ],
    [
      "008586e8",
      "PARAM",
      [
        "storage",
        "002a8886",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008586a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858670.md#insn-008586a8) · [`008586c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858670.md#insn-008586c8) · [`008586e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858670.md#insn-008586e8)
- 新版 [`008586a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858670.md#insn-008586a8) · [`008586c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858670.md#insn-008586c8) · [`008586e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858670.md#insn-008586e8)

~~~diff
- 008586a8 ["COPY", "tmp:0:8", ["const:528:8"]]
- 008586a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008586a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008586a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008586a8 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 008586a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008586a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008586a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008586a8 bytes 08a11491
+ 008586a8 bytes 08e11591
- 008586c8 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 008586c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008586c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008586c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008586c8 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 008586c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008586c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008586c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008586c8 bytes 08413b91
+ 008586c8 bytes 08813c91
- 008586e8 ["COPY", "tmp:0:8", ["const:7ec:8"]]
- 008586e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008586e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008586e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008586e8 ["COPY", "tmp:0:8", ["const:886:8"]]
+ 008586e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008586e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008586e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008586e8 bytes 21b01f91
+ 008586e8 bytes 21182291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaa1e2d73ebf5c6cc27b804597ba272f"></a>

### [`00858748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858748.md) → [`00858748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858748.md) FUN_00858748

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/008544a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858780",
      "incomplete_value": false,
      "site": "0085878c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858780",
      "incomplete_value": false,
      "site": "0085878c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "definition_site": "008587a0",
      "incomplete_value": false,
      "site": "008587a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008587a0",
      "incomplete_value": false,
      "site": "008587a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "definition_site": "008587c0",
      "incomplete_value": false,
      "site": "008587c8",
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
            "const:a5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008587c0",
      "incomplete_value": false,
      "site": "008587c8",
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
            "const:9c1:8"
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
      "0085878c",
      "DATA",
      [
        "storage",
        "00c03578",
        null,
        "undefined *"
      ]
    ],
    [
      "008587a4",
      "DATA",
      [
        "storage",
        "00c02eb0",
        null,
        "pointer"
      ]
    ],
    [
      "008587c0",
      "PARAM",
      [
        "storage",
        "002a79c1",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0085878c",
      "DATA",
      [
        "storage",
        "00c035c8",
        null,
        "undefined *"
      ]
    ],
    [
      "008587a4",
      "DATA",
      [
        "storage",
        "00c02f00",
        null,
        "pointer"
      ]
    ],
    [
      "008587c0",
      "PARAM",
      [
        "storage",
        "002a7a5b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858748.md#insn-00858780) · [`008587a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858748.md#insn-008587a0) · [`008587c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858748.md#insn-008587c0)
- 新版 [`00858780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858748.md#insn-00858780) · [`008587a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858748.md#insn-008587a0) · [`008587c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858748.md#insn-008587c0)

~~~diff
- 00858780 ["COPY", "tmp:0:8", ["const:578:8"]]
- 00858780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858780 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 00858780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858780 bytes 08e11591
+ 00858780 bytes 08211791
- 008587a0 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 008587a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008587a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008587a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008587a0 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 008587a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008587a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008587a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008587a0 bytes 08c13a91
+ 008587a0 bytes 08013c91
- 008587c0 ["COPY", "tmp:0:8", ["const:9c1:8"]]
- 008587c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008587c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008587c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008587c0 ["COPY", "tmp:0:8", ["const:a5b:8"]]
+ 008587c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008587c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008587c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008587c0 bytes 21042791
+ 008587c0 bytes 216c2991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fee1640c07768e10bc16a215e682a83a"></a>

### [`00858820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858820.md) → [`00858820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858820.md) FUN_00858820

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/008544a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.80% / 新版 89.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085886c",
      "incomplete_value": false,
      "site": "00858878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085886c",
      "incomplete_value": false,
      "site": "00858878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858888",
      "incomplete_value": false,
      "site": "00858890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858888",
      "incomplete_value": false,
      "site": "00858890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
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
      "definition_site": "008588ac",
      "incomplete_value": false,
      "site": "008588b4",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008588ac",
      "incomplete_value": false,
      "site": "008588b4",
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
            "const:9ce:8"
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
      "00858878",
      "DATA",
      [
        "storage",
        "00c035c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00858890",
      "DATA",
      [
        "storage",
        "00c02ef0",
        null,
        "pointer"
      ]
    ],
    [
      "008588ac",
      "PARAM",
      [
        "storage",
        "002a79ce",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00858878",
      "DATA",
      [
        "storage",
        "00c03618",
        null,
        "undefined *"
      ]
    ],
    [
      "00858890",
      "DATA",
      [
        "storage",
        "00c02f40",
        null,
        "pointer"
      ]
    ],
    [
      "008588ac",
      "PARAM",
      [
        "storage",
        "002a7a68",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085886c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858820.md#insn-0085886c) · [`00858888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858820.md#insn-00858888) · [`008588ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858820.md#insn-008588ac)
- 新版 [`0085886c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858820.md#insn-0085886c) · [`00858888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858820.md#insn-00858888) · [`008588ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858820.md#insn-008588ac)

~~~diff
- 0085886c ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 0085886c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085886c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085886c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085886c ["COPY", "tmp:0:8", ["const:618:8"]]
+ 0085886c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085886c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085886c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085886c bytes 08211791
+ 0085886c bytes 08611891
- 00858888 ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 00858888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858888 ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 00858888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858888 bytes 08c13b91
+ 00858888 bytes 08013d91
- 008588ac ["COPY", "tmp:0:8", ["const:9ce:8"]]
- 008588ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008588ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008588ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008588ac ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 008588ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008588ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008588ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008588ac bytes 21382791
+ 008588ac bytes 21a02991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d1070d61f717de7f2775a84ce864c01"></a>

### [`00858918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858918.md) → [`00858918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858918.md) FUN_00858918

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
      "definition_site": "0085893c",
      "incomplete_value": false,
      "site": "0085893c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085893c",
      "incomplete_value": false,
      "site": "0085893c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:618:8"
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
      "0085893c",
      "DATA",
      [
        "storage",
        "00c03618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085893c",
      "DATA",
      [
        "storage",
        "00c03668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858918.md#insn-00858938)
- 新版 [`00858938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858918.md#insn-00858938)

~~~diff
- 00858938 ["COPY", "tmp:0:8", ["const:618:8"]]
- 00858938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858938 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 00858938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858938 bytes 08611891
+ 00858938 bytes 08a11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c912787253146d53fdb43df02d033fb"></a>

### [`0085894c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085894c.md) → [`0085894c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/0085894c.md) FUN_0085894c

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
      "definition_site": "00858958",
      "incomplete_value": false,
      "site": "00858958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858958",
      "incomplete_value": false,
      "site": "00858958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:618:8"
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
      "00858958",
      "DATA",
      [
        "storage",
        "00c03618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858958",
      "DATA",
      [
        "storage",
        "00c03668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085894c.md#insn-00858954)
- 新版 [`00858954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/0085894c.md#insn-00858954)

~~~diff
- 00858954 ["COPY", "tmp:0:8", ["const:618:8"]]
- 00858954 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00858954 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00858954 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00858954 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 00858954 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00858954 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00858954 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00858954 bytes 29611891
+ 00858954 bytes 29a11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc4df0ecb9f954f36084d20ed59b46ea"></a>

### [`00858a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858a28.md) → [`00858a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858a28.md) FUN_00858a28

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
      "definition_site": "00858a4c",
      "incomplete_value": false,
      "site": "00858a4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858a4c",
      "incomplete_value": false,
      "site": "00858a4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "00858a4c",
      "DATA",
      [
        "storage",
        "00c03698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858a4c",
      "DATA",
      [
        "storage",
        "00c036e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858a28.md#insn-00858a48)
- 新版 [`00858a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858a28.md#insn-00858a48)

~~~diff
- 00858a48 ["COPY", "tmp:0:8", ["const:698:8"]]
- 00858a48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858a48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858a48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858a48 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 00858a48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858a48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858a48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858a48 bytes 08611a91
+ 00858a48 bytes 08a11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a781e06e5d36b2884614b8e31ae56d0f"></a>

### [`00858a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858a5c.md) → [`00858a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858a5c.md) FUN_00858a5c

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
      "definition_site": "00858a68",
      "incomplete_value": false,
      "site": "00858a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858a68",
      "incomplete_value": false,
      "site": "00858a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "00858a68",
      "DATA",
      [
        "storage",
        "00c03698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858a68",
      "DATA",
      [
        "storage",
        "00c036e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858a5c.md#insn-00858a64)
- 新版 [`00858a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858a5c.md#insn-00858a64)

~~~diff
- 00858a64 ["COPY", "tmp:0:8", ["const:698:8"]]
- 00858a64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00858a64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00858a64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00858a64 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 00858a64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00858a64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00858a64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00858a64 bytes 29611a91
+ 00858a64 bytes 29a11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fb30a50def41a870720d2056139f827"></a>

### [`00858b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858b20.md) → [`00858b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858b20.md) FUN_00858b20

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
      "definition_site": "00858b44",
      "incomplete_value": false,
      "site": "00858b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858b44",
      "incomplete_value": false,
      "site": "00858b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "00858b44",
      "DATA",
      [
        "storage",
        "00c03718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858b44",
      "DATA",
      [
        "storage",
        "00c03768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858b20.md#insn-00858b40)
- 新版 [`00858b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858b20.md#insn-00858b40)

~~~diff
- 00858b40 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00858b40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858b40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858b40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858b40 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 00858b40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858b40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858b40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858b40 bytes 08611c91
+ 00858b40 bytes 08a11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce34a8a947399f2047c748bf85e6b25c"></a>

### [`00858b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858b54.md) → [`00858b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858b54.md) FUN_00858b54

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
      "definition_site": "00858b60",
      "incomplete_value": false,
      "site": "00858b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858b60",
      "incomplete_value": false,
      "site": "00858b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "00858b60",
      "DATA",
      [
        "storage",
        "00c03718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858b60",
      "DATA",
      [
        "storage",
        "00c03768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858b54.md#insn-00858b5c)
- 新版 [`00858b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858b54.md#insn-00858b5c)

~~~diff
- 00858b5c ["COPY", "tmp:0:8", ["const:718:8"]]
- 00858b5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00858b5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00858b5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00858b5c ["COPY", "tmp:0:8", ["const:768:8"]]
+ 00858b5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00858b5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00858b5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00858b5c bytes 29611c91
+ 00858b5c bytes 29a11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-515b6770400a7dbfae5343287b8c7da0"></a>

### [`00858bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858bc4.md) → [`00858bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858bc4.md) FUN_00858bc4

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
      "definition_site": "00858be8",
      "incomplete_value": false,
      "site": "00858be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858be8",
      "incomplete_value": false,
      "site": "00858be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "00858be8",
      "DATA",
      [
        "storage",
        "00c03798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858be8",
      "DATA",
      [
        "storage",
        "00c037e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858bc4.md#insn-00858be4)
- 新版 [`00858be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858bc4.md#insn-00858be4)

~~~diff
- 00858be4 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00858be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858be4 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00858be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858be4 bytes 08611e91
+ 00858be4 bytes 08a11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b3e4ca593ebdd75323a20f3255c4926"></a>

### [`00858bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858bf8.md) → [`00858bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858bf8.md) FUN_00858bf8

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
      "definition_site": "00858c04",
      "incomplete_value": false,
      "site": "00858c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858c04",
      "incomplete_value": false,
      "site": "00858c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "00858c04",
      "DATA",
      [
        "storage",
        "00c03798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858c04",
      "DATA",
      [
        "storage",
        "00c037e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858bf8.md#insn-00858c00)
- 新版 [`00858c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858bf8.md#insn-00858c00)

~~~diff
- 00858c00 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00858c00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00858c00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00858c00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00858c00 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00858c00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00858c00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00858c00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00858c00 bytes 29611e91
+ 00858c00 bytes 29a11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8677a5fb2b76ba074267129cd49315e8"></a>

### [`00858db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858db8.md) → [`00858db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858db8.md) _INIT_160

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00858fe0",
      "incomplete_value": false,
      "site": "00858fec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109e000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858fe0",
      "incomplete_value": false,
      "site": "00858fec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109e000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
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
      "definition_site": "00858fe8",
      "incomplete_value": false,
      "site": "00858fec",
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
      "definition_site": "00858fe8",
      "incomplete_value": false,
      "site": "00858fec",
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
      "00858df4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00858e18",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00858e38",
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
      "00858df4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00858e18",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00858e38",
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

- 旧版 [`00858de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858db8.md#insn-00858de4) · [`00858dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858db8.md#insn-00858dec)
- 新版 [`00858de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858db8.md#insn-00858de4) · [`00858dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858db8.md#insn-00858dec)

~~~diff
- 00858de4 ["COPY", "tmp:0:8", ["const:5e8:8"]]
- 00858de4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00858de4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00858de4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00858de4 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 00858de4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00858de4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00858de4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00858de4 bytes 73a21791
+ 00858de4 bytes 73a21891
- 00858dec ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00858dec bytes 69d2fff0
+ 00858dec ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00858dec bytes 69d2fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-490d4183121e7bb498938043e90edc7e"></a>

### [`00859148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859148.md) → [`00859148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859148.md) FUN_00859148

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`0044fc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044f/0044fc20.md) [`0044fcd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044f/0044fcd4.md) [`0044fce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044f/0044fce4.md) [`0044fecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044f/0044fecc.md) [`004508a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/004508a4.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0044fc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fc20.md) [`0044fcd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fcd4.md) [`0044fce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fce4.md) [`0044fecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fecc.md) [`004508a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.79% / 新版 96.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00859290",
      "incomplete_value": false,
      "site": "00859298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00859290",
      "incomplete_value": false,
      "site": "00859298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "definition_site": "0085935c",
      "incomplete_value": true,
      "site": "0085935c",
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
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085935c",
      "incomplete_value": true,
      "site": "0085935c",
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
            "const:860:8"
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
      "definition_site": "008593a8",
      "incomplete_value": false,
      "site": "008593a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008593a8",
      "incomplete_value": false,
      "site": "008593a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "00859298",
      "DATA",
      [
        "storage",
        "00c03970",
        null,
        "undefined *"
      ]
    ],
    [
      "008592d0",
      "READ",
      [
        "storage",
        "00c03990",
        null,
        "pointer"
      ]
    ],
    [
      "008592d0",
      "READ",
      [
        "storage",
        "00c03998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00859298",
      "DATA",
      [
        "storage",
        "00c039c0",
        null,
        "undefined *"
      ]
    ],
    [
      "008592d0",
      "READ",
      [
        "storage",
        "00c039e0",
        null,
        "pointer"
      ]
    ],
    [
      "008592d0",
      "READ",
      [
        "storage",
        "00c039e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00859290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859148.md#insn-00859290) · [`00859350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859148.md#insn-00859350) · [`008593a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859148.md#insn-008593a4)
- 新版 [`00859290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859148.md#insn-00859290) · [`00859350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859148.md#insn-00859350) · [`008593a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859148.md#insn-008593a4)

~~~diff
- 00859290 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00859290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00859290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00859290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00859290 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00859290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00859290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00859290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00859290 bytes 08c12591
+ 00859290 bytes 08012791
- 00859350 ["COPY", "tmp:0:8", ["const:860:8"]]
- 00859350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00859350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00859350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00859350 ["COPY", "tmp:0:8", ["const:8b0:8"]]
+ 00859350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00859350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00859350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00859350 bytes 08812191
+ 00859350 bytes 08c12291
- 008593a4 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 008593a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008593a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008593a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008593a4 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 008593a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008593a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008593a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008593a4 bytes 08c12391
+ 008593a4 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a4696ea65f5aad690be66fa8a64b0cd"></a>

### [`008594d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/008594d4.md) → [`008594d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/008594d4.md) FUN_008594d4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00859148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859148.md) [`0085c4c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c4c4.md) [`0085c698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c698.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00429a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429a14.md) [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md)
- 新版 呼出元 3件 [`00859148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859148.md) [`0085c4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c4c4.md) [`0085c698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c698.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00429a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429a14.md) [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00859564",
      "incomplete_value": true,
      "site": "00859570",
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
                "const:71f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00859564",
      "incomplete_value": true,
      "site": "00859570",
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
                "const:685:8"
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
      "definition_site": "008595f4",
      "incomplete_value": true,
      "site": "008595f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e67:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008595f4",
      "incomplete_value": true,
      "site": "008595f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef4:8"
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
      "definition_site": "008595f8",
      "incomplete_value": true,
      "site": "008595f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008595f8",
      "incomplete_value": true,
      "site": "008595f8",
      "value": [
        "LOAD",
        "8",
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
      "00859518",
      "READ",
      [
        "storage",
        "00c25250",
        null,
        "undefined1"
      ]
    ],
    [
      "00859520",
      "READ",
      [
        "storage",
        "00c25250",
        null,
        "undefined1"
      ]
    ],
    [
      "00859524",
      "READ",
      [
        "storage",
        "00c25260",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00859518",
      "READ",
      [
        "storage",
        "00c25290",
        null,
        "undefined1"
      ]
    ],
    [
      "00859520",
      "READ",
      [
        "storage",
        "00c25290",
        null,
        "undefined1"
      ]
    ],
    [
      "00859524",
      "READ",
      [
        "storage",
        "00c252a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00859514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/008594d4.md#insn-00859514) · [`0085954c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/008594d4.md#insn-0085954c) · [`00859558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/008594d4.md#insn-00859558)
- 新版 [`00859514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/008594d4.md#insn-00859514) · [`0085954c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/008594d4.md#insn-0085954c) · [`00859558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/008594d4.md#insn-00859558)

~~~diff
- 00859514 ["COPY", "tmp:0:8", ["const:250:8"]]
- 00859514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00859514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00859514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00859514 ["COPY", "tmp:0:8", ["const:290:8"]]
+ 00859514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00859514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00859514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00859514 bytes 08410991
+ 00859514 bytes 08410a91
- 0085954c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 0085954c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0085954c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec0:8"]]
+ 0085954c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0085954c bytes 083947f9
+ 0085954c bytes 086147f9
- 00859558 ["COPY", "tmp:0:8", ["const:685:8"]]
- 00859558 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00859558 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00859558 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00859558 ["COPY", "tmp:0:8", ["const:71f:8"]]
+ 00859558 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00859558 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00859558 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00859558 bytes 29151a91
+ 00859558 bytes 297d1c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0f941f876756e40a41c98c899ecdf2d"></a>

### [`00859898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md) → [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) FUN_00859898

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 93件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md)
- 新版 呼出元 0件  · 呼出先 93件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.65% / 新版 98.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00859d38",
      "incomplete_value": false,
      "site": "00859d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00859d38",
      "incomplete_value": false,
      "site": "00859d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00859fe0",
      "incomplete_value": true,
      "site": "00859ff0",
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
                "const:d7e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00859fe0",
      "incomplete_value": true,
      "site": "00859ff0",
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
                "const:e0b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 72,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085b4b0",
      "incomplete_value": true,
      "site": "0085b4c4",
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
                "const:d7e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085b4b0",
      "incomplete_value": true,
      "site": "0085b4c4",
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
                "const:e0b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 123,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00859910",
      "READ",
      [
        "storage",
        "00296034",
        null,
        "string"
      ]
    ],
    [
      "00859c34",
      "PARAM",
      [
        "storage",
        "00292e1c",
        null,
        "string"
      ]
    ],
    [
      "00859d38",
      "DATA",
      [
        "storage",
        "00c03a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00859910",
      "READ",
      [
        "storage",
        "00295fa7",
        null,
        "string"
      ]
    ],
    [
      "00859c34",
      "PARAM",
      [
        "storage",
        "00292d8f",
        null,
        "string"
      ]
    ],
    [
      "00859d38",
      "DATA",
      [
        "storage",
        "00c03ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00859904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md#insn-00859904) · [`00859908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md#insn-00859908) · [`00859c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md#insn-00859c34)
- 新版 [`00859904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md#insn-00859904) · [`00859908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md#insn-00859908) · [`00859c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md#insn-00859c34)

~~~diff
- 00859904 ["COPY", "register:4048:8", ["const:296000:8"]]
+ 00859904 ["COPY", "register:4048:8", ["const:295000:8"]]
- 00859904 bytes e9d1ffb0
+ 00859904 bytes e9d1ff90
- 00859908 ["COPY", "tmp:0:8", ["const:34:8"]]
- 00859908 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00859908 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00859908 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00859908 ["COPY", "tmp:0:8", ["const:fa7:8"]]
+ 00859908 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00859908 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00859908 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00859908 bytes 29d10091
+ 00859908 bytes 299d3e91
- 00859c34 ["COPY", "tmp:0:8", ["const:e1c:8"]]
- 00859c34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00859c34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00859c34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00859c34 ["COPY", "tmp:0:8", ["const:d8f:8"]]
+ 00859c34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00859c34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00859c34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00859c34 bytes 21703891
+ 00859c34 bytes 213c3691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f748679cab3355e177e00b6396bba27c"></a>

### [`0085c46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c46c.md) → [`0085c46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c46c.md) FUN_0085c46c

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
      "definition_site": "0085c48c",
      "incomplete_value": false,
      "site": "0085c490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c48c",
      "incomplete_value": false,
      "site": "0085c490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "0085c490",
      "DATA",
      [
        "storage",
        "00c03860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085c490",
      "DATA",
      [
        "storage",
        "00c038b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085c48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c46c.md#insn-0085c48c)
- 新版 [`0085c48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c46c.md#insn-0085c48c)

~~~diff
- 0085c48c ["COPY", "tmp:0:8", ["const:860:8"]]
- 0085c48c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085c48c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085c48c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085c48c ["COPY", "tmp:0:8", ["const:8b0:8"]]
+ 0085c48c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c48c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c48c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085c48c bytes 08812191
+ 0085c48c bytes 08c12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33cc336d9a8081bc3c61db714594d46d"></a>

### [`0085c4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c4a4.md) → [`0085c4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c4a4.md) FUN_0085c4a4

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
      "definition_site": "0085c4a8",
      "incomplete_value": false,
      "site": "0085c4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c4a8",
      "incomplete_value": false,
      "site": "0085c4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "0085c4ac",
      "DATA",
      [
        "storage",
        "00c03860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085c4ac",
      "DATA",
      [
        "storage",
        "00c038b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085c4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c4a4.md#insn-0085c4a8)
- 新版 [`0085c4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c4a4.md#insn-0085c4a8)

~~~diff
- 0085c4a8 ["COPY", "tmp:0:8", ["const:860:8"]]
- 0085c4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085c4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085c4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085c4a8 ["COPY", "tmp:0:8", ["const:8b0:8"]]
+ 0085c4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085c4a8 bytes 08812191
+ 0085c4a8 bytes 08c12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94ab3c4d66976334412260d6b312e3fb"></a>

### [`0085c648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c648.md) → [`0085c648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c648.md) FUN_0085c648

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
      "definition_site": "0085c66c",
      "incomplete_value": false,
      "site": "0085c66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c66c",
      "incomplete_value": false,
      "site": "0085c66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "0085c66c",
      "DATA",
      [
        "storage",
        "00c038f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085c66c",
      "DATA",
      [
        "storage",
        "00c03940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085c668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c648.md#insn-0085c668)
- 新版 [`0085c668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c648.md#insn-0085c668)

~~~diff
- 0085c668 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 0085c668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085c668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085c668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085c668 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 0085c668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085c668 bytes 08c12391
+ 0085c668 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9f856b50f9034a833d934f81651e6fb"></a>

### [`0085c67c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c67c.md) → [`0085c67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c67c.md) FUN_0085c67c

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
      "definition_site": "0085c688",
      "incomplete_value": false,
      "site": "0085c688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c688",
      "incomplete_value": false,
      "site": "0085c688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "0085c688",
      "DATA",
      [
        "storage",
        "00c038f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085c688",
      "DATA",
      [
        "storage",
        "00c03940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085c684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c67c.md#insn-0085c684)
- 新版 [`0085c684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c67c.md#insn-0085c684)

~~~diff
- 0085c684 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 0085c684 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085c684 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085c684 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085c684 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 0085c684 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085c684 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085c684 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085c684 bytes 29c12391
+ 0085c684 bytes 29012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-822d025a287c555d95c921d37317ad76"></a>

### [`0085c6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c6c8.md) → [`0085c6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c6c8.md) FUN_0085c6c8

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
      "definition_site": "0085c6dc",
      "incomplete_value": false,
      "site": "0085c6e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c6dc",
      "incomplete_value": false,
      "site": "0085c6e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "0085c6e0",
      "DATA",
      [
        "storage",
        "00c03970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085c6e0",
      "DATA",
      [
        "storage",
        "00c039c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085c6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c6c8.md#insn-0085c6dc)
- 新版 [`0085c6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c6c8.md#insn-0085c6dc)

~~~diff
- 0085c6dc ["COPY", "tmp:0:8", ["const:970:8"]]
- 0085c6dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085c6dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085c6dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085c6dc ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 0085c6dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c6dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c6dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085c6dc bytes 08c12591
+ 0085c6dc bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c68bf8fcaab055bd2b6ebeeed9f47b5b"></a>

### [`0085c6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c6ec.md) → [`0085c6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c6ec.md) FUN_0085c6ec

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
      "definition_site": "0085c6f0",
      "incomplete_value": false,
      "site": "0085c6f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c6f0",
      "incomplete_value": false,
      "site": "0085c6f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "0085c6f4",
      "DATA",
      [
        "storage",
        "00c03970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085c6f4",
      "DATA",
      [
        "storage",
        "00c039c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085c6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c6ec.md#insn-0085c6f0)
- 新版 [`0085c6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c6ec.md#insn-0085c6f0)

~~~diff
- 0085c6f0 ["COPY", "tmp:0:8", ["const:970:8"]]
- 0085c6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085c6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085c6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085c6f0 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 0085c6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085c6f0 bytes 08c12591
+ 0085c6f0 bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15927608305fc5eca775d0b51f91a747"></a>

### [`0085c704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c704.md) → [`0085c704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c704.md) FUN_0085c704

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0052db3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db3c.md) [`0085cc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cc88.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0052db3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db3c.md) [`0085cc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cc88.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.27% / 新版 95.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085c738",
      "incomplete_value": true,
      "site": "0085c748",
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
                "const:cdd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c738",
      "incomplete_value": true,
      "site": "0085c748",
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
                "const:d6a:8"
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
      "definition_site": "0085c74c",
      "incomplete_value": true,
      "site": "0085c74c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0085c74c",
      "incomplete_value": true,
      "site": "0085c74c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085c888",
      "incomplete_value": false,
      "site": "0085c888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c888",
      "incomplete_value": false,
      "site": "0085c888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "0085c738",
      "READ",
      [
        "storage",
        "00294d6a",
        null,
        "string"
      ]
    ],
    [
      "0085c73c",
      "READ",
      [
        "storage",
        "00294d79",
        null,
        "string"
      ]
    ],
    [
      "0085c888",
      "DATA",
      [
        "storage",
        "00c039e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085c738",
      "READ",
      [
        "storage",
        "00294cdd",
        null,
        "string"
      ]
    ],
    [
      "0085c73c",
      "READ",
      [
        "storage",
        "00294cec",
        null,
        "string"
      ]
    ],
    [
      "0085c888",
      "DATA",
      [
        "storage",
        "00c03a30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085c730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c704.md#insn-0085c730) · [`0085c734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c704.md#insn-0085c734)
- 新版 [`0085c730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c704.md#insn-0085c730) · [`0085c734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c704.md#insn-0085c734)

~~~diff
- 0085c730 ["COPY", "tmp:0:8", ["const:d6a:8"]]
- 0085c730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085c730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085c730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085c730 ["COPY", "tmp:0:8", ["const:cdd:8"]]
+ 0085c730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085c730 bytes 08a93591
+ 0085c730 bytes 08753391
- 0085c734 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0085c734 bytes a9d2ff90
+ 0085c734 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0085c734 bytes a9d2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4559b676cc0c75e1de1bccca6f0bb0ba"></a>

### [`0085cb4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cb4c.md) → [`0085cb4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cb4c.md) FUN_0085cb4c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085cb60",
      "incomplete_value": false,
      "site": "0085cb64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cb60",
      "incomplete_value": false,
      "site": "0085cb64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "0085cb64",
      "DATA",
      [
        "storage",
        "00c039e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085cb64",
      "DATA",
      [
        "storage",
        "00c03a30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085cb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cb4c.md#insn-0085cb60)
- 新版 [`0085cb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cb4c.md#insn-0085cb60)

~~~diff
- 0085cb60 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 0085cb60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085cb60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085cb60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085cb60 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 0085cb60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cb60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cb60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085cb60 bytes 08812791
+ 0085cb60 bytes 08c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a75f4bbc9d9f0abee244b1a67e73c4d3"></a>

### [`0085cba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cba8.md) → [`0085cba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cba8.md) FUN_0085cba8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085cbc0",
      "incomplete_value": false,
      "site": "0085cbc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cbc0",
      "incomplete_value": false,
      "site": "0085cbc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "0085cbc4",
      "DATA",
      [
        "storage",
        "00c039e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085cbc4",
      "DATA",
      [
        "storage",
        "00c03a30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085cbc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cba8.md#insn-0085cbc0)
- 新版 [`0085cbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cba8.md#insn-0085cbc0)

~~~diff
- 0085cbc0 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 0085cbc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085cbc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085cbc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085cbc0 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 0085cbc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cbc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cbc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085cbc0 bytes 08812791
+ 0085cbc0 bytes 08c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56eb943fdfd1ad18649e957b03141fc3"></a>

### [`0085cc04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cc04.md) → [`0085cc04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cc04.md) FUN_0085cc04

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085cc28",
      "incomplete_value": false,
      "site": "0085cc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cc28",
      "incomplete_value": false,
      "site": "0085cc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "0085cc28",
      "DATA",
      [
        "storage",
        "00c039e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085cc28",
      "DATA",
      [
        "storage",
        "00c03a30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085cc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cc04.md#insn-0085cc24)
- 新版 [`0085cc24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cc04.md#insn-0085cc24)

~~~diff
- 0085cc24 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 0085cc24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085cc24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085cc24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085cc24 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 0085cc24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085cc24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085cc24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085cc24 bytes 29812791
+ 0085cc24 bytes 29c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10f327c5919274f0d3e54f18376d1815"></a>

### [`0085cc54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cc54.md) → [`0085cc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cc54.md) FUN_0085cc54

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "0085cc60",
      "incomplete_value": false,
      "site": "0085cc60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cc60",
      "incomplete_value": false,
      "site": "0085cc60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "0085cc60",
      "DATA",
      [
        "storage",
        "00c039e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085cc60",
      "DATA",
      [
        "storage",
        "00c03a30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085cc5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cc54.md#insn-0085cc5c)
- 新版 [`0085cc5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cc54.md#insn-0085cc5c)

~~~diff
- 0085cc5c ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 0085cc5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085cc5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085cc5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085cc5c ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 0085cc5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085cc5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085cc5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085cc5c bytes 29812791
+ 0085cc5c bytes 29c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb0e04161e9b1cb53163af668959171e"></a>

### [`0085cd84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cd84.md) → [`0085cd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cd84.md) FUN_0085cd84

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
      "definition_site": "0085cd98",
      "incomplete_value": false,
      "site": "0085cd9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cd98",
      "incomplete_value": false,
      "site": "0085cd9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "0085cd9c",
      "DATA",
      [
        "storage",
        "00c03a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085cd9c",
      "DATA",
      [
        "storage",
        "00c03ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085cd98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cd84.md#insn-0085cd98)
- 新版 [`0085cd98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cd84.md#insn-0085cd98)

~~~diff
- 0085cd98 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 0085cd98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085cd98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085cd98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085cd98 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 0085cd98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cd98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cd98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085cd98 bytes 08c12991
+ 0085cd98 bytes 08012b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7d8a999e55e9442b453aed3e4f45a2b"></a>

### [`0085cda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cda8.md) → [`0085cda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cda8.md) FUN_0085cda8

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
      "definition_site": "0085cdac",
      "incomplete_value": false,
      "site": "0085cdb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cdac",
      "incomplete_value": false,
      "site": "0085cdb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "0085cdb0",
      "DATA",
      [
        "storage",
        "00c03a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085cdb0",
      "DATA",
      [
        "storage",
        "00c03ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085cdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cda8.md#insn-0085cdac)
- 新版 [`0085cdac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cda8.md#insn-0085cdac)

~~~diff
- 0085cdac ["COPY", "tmp:0:8", ["const:a70:8"]]
- 0085cdac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085cdac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085cdac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085cdac ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 0085cdac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cdac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085cdac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085cdac bytes 08c12991
+ 0085cdac bytes 08012b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f759b7ae7ff5f43d823384fa3922512"></a>

### [`0085cdc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cdc0.md) → [`0085cdc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cdc0.md) FUN_0085cdc0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0052db3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db3c.md) [`0085d1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d1d8.md) [`0085d228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d228.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0052db3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db3c.md) [`0085d1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d1d8.md) [`0085d228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d228.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.40% / 新版 93.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085cdf8",
      "incomplete_value": true,
      "site": "0085cdf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:daf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cdf8",
      "incomplete_value": true,
      "site": "0085cdf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d15:8"
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
      "definition_site": "0085cdf0",
      "incomplete_value": true,
      "site": "0085cdfc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0085cdf0",
      "incomplete_value": true,
      "site": "0085cdfc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085ce8c",
      "incomplete_value": false,
      "site": "0085ce8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085ce8c",
      "incomplete_value": false,
      "site": "0085ce8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "0085cde4",
      "READ",
      [
        "storage",
        "002a6d15",
        null,
        "string"
      ]
    ],
    [
      "0085cdf0",
      "READ",
      [
        "storage",
        "002a6d1c",
        null,
        "string"
      ]
    ],
    [
      "0085ce8c",
      "DATA",
      [
        "storage",
        "00c03ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085cde4",
      "READ",
      [
        "storage",
        "002a6daf",
        null,
        "string"
      ]
    ],
    [
      "0085cdf0",
      "READ",
      [
        "storage",
        "002a6db6",
        null,
        "string"
      ]
    ],
    [
      "0085ce8c",
      "DATA",
      [
        "storage",
        "00c03b30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085cddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cdc0.md#insn-0085cddc) · [`0085ce84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085cdc0.md#insn-0085ce84)
- 新版 [`0085cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cdc0.md#insn-0085cddc) · [`0085ce84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cdc0.md#insn-0085ce84)

~~~diff
- 0085cddc ["COPY", "tmp:0:8", ["const:d15:8"]]
- 0085cddc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085cddc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085cddc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085cddc ["COPY", "tmp:0:8", ["const:daf:8"]]
+ 0085cddc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085cddc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085cddc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085cddc bytes 29553491
+ 0085cddc bytes 29bd3691
- 0085ce84 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0085ce84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085ce84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085ce84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085ce84 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 0085ce84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085ce84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085ce84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085ce84 bytes 08812b91
+ 0085ce84 bytes 08c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c68f1a24d309c7378324f7ef99179a05"></a>

### [`0085d09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d09c.md) → [`0085d09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d09c.md) FUN_0085d09c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085d0b0",
      "incomplete_value": false,
      "site": "0085d0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d0b0",
      "incomplete_value": false,
      "site": "0085d0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "0085d0b4",
      "DATA",
      [
        "storage",
        "00c03ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085d0b4",
      "DATA",
      [
        "storage",
        "00c03b30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085d0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d09c.md#insn-0085d0b0)
- 新版 [`0085d0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d09c.md#insn-0085d0b0)

~~~diff
- 0085d0b0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0085d0b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085d0b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085d0b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085d0b0 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 0085d0b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085d0b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085d0b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085d0b0 bytes 08812b91
+ 0085d0b0 bytes 08c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82fa34d979ffddef55dcb0e5a3e01387"></a>

### [`0085d0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d0f8.md) → [`0085d0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d0f8.md) FUN_0085d0f8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085d110",
      "incomplete_value": false,
      "site": "0085d114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d110",
      "incomplete_value": false,
      "site": "0085d114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "0085d114",
      "DATA",
      [
        "storage",
        "00c03ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085d114",
      "DATA",
      [
        "storage",
        "00c03b30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085d110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d0f8.md#insn-0085d110)
- 新版 [`0085d110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d0f8.md#insn-0085d110)

~~~diff
- 0085d110 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0085d110 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085d110 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085d110 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085d110 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 0085d110 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085d110 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085d110 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085d110 bytes 08812b91
+ 0085d110 bytes 08c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac744919c8b6099072d259fe52c4ffc9"></a>

### [`0085d154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d154.md) → [`0085d154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d154.md) FUN_0085d154

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085d178",
      "incomplete_value": false,
      "site": "0085d178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d178",
      "incomplete_value": false,
      "site": "0085d178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "0085d178",
      "DATA",
      [
        "storage",
        "00c03ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085d178",
      "DATA",
      [
        "storage",
        "00c03b30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085d174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d154.md#insn-0085d174)
- 新版 [`0085d174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d154.md#insn-0085d174)

~~~diff
- 0085d174 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0085d174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085d174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085d174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085d174 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 0085d174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085d174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085d174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085d174 bytes 29812b91
+ 0085d174 bytes 29c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a4631bc2f926ae9ad3797c5724b1156"></a>

### [`0085d1a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d1a4.md) → [`0085d1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d1a4.md) FUN_0085d1a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "0085d1b0",
      "incomplete_value": false,
      "site": "0085d1b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d1b0",
      "incomplete_value": false,
      "site": "0085d1b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "0085d1b0",
      "DATA",
      [
        "storage",
        "00c03ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085d1b0",
      "DATA",
      [
        "storage",
        "00c03b30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085d1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d1a4.md#insn-0085d1ac)
- 新版 [`0085d1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d1a4.md#insn-0085d1ac)

~~~diff
- 0085d1ac ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0085d1ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085d1ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085d1ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085d1ac ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 0085d1ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085d1ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085d1ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085d1ac bytes 29812b91
+ 0085d1ac bytes 29c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0e928668bef3d23dec8115e03398cb7"></a>

### [`0085d2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d2a4.md) → [`0085d2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d2a4.md) _INIT_161

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085d2e0",
      "incomplete_value": true,
      "site": "0085d2fc",
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d2e0",
      "incomplete_value": true,
      "site": "0085d2fc",
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
                "const:2dd:8"
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
      "definition_site": "0085d304",
      "incomplete_value": true,
      "site": "0085d320",
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d304",
      "incomplete_value": true,
      "site": "0085d320",
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
                "const:2f0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0085d324",
      "incomplete_value": true,
      "site": "0085d340",
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d324",
      "incomplete_value": true,
      "site": "0085d340",
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
                "const:46:8"
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
      "0085d2e0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0085d304",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0085d324",
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
      "0085d2e0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0085d304",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0085d324",
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

- 旧版 [`0085d2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d2a4.md#insn-0085d2d0) · [`0085d2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d2a4.md#insn-0085d2d8)
- 新版 [`0085d2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d2a4.md#insn-0085d2d0) · [`0085d2d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d2a4.md#insn-0085d2d8)

~~~diff
- 0085d2d0 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0085d2d0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0085d2d0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0085d2d0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0085d2d0 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 0085d2d0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0085d2d0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0085d2d0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0085d2d0 bytes 73021891
+ 0085d2d0 bytes 73021991
- 0085d2d8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0085d2d8 bytes 49d2ffd0
+ 0085d2d8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0085d2d8 bytes 49d2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a32078b6db59a568a8d9d15a353b108"></a>

### [`0085e130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e130.md) → [`0085e130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e130.md) FUN_0085e130

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 14件 [`006fd890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd890.md) [`0085e2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e2f8.md) [`0085fc14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fc14.md) [`0085fc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fc18.md) [`00ad90d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad90d4.md)
- 新版 呼出元 2件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 14件 [`006fd890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd890.md) [`0085e2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e2f8.md) [`0085fc14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc14.md) [`0085fc18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc18.md) [`00ad9118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9118.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.82% / 新版 75.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 2件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085e1ac",
      "incomplete_value": true,
      "site": "0085e1b8",
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
      "definition_site": "0085e1ac",
      "incomplete_value": true,
      "site": "0085e1b8",
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
      "definition_site": "0085e1a8",
      "incomplete_value": true,
      "site": "0085e1bc",
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
                "const:afb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085e1a8",
      "incomplete_value": true,
      "site": "0085e1bc",
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
                "const:a70:8"
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
      "definition_site": "0085e1a8",
      "incomplete_value": true,
      "site": "0085e1bc",
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
      "definition_site": "0085e1a8",
      "incomplete_value": true,
      "site": "0085e1bc",
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
      "0085e154",
      "READ",
      [
        "storage",
        "0109e660",
        null,
        "undefined1"
      ]
    ],
    [
      "0085e180",
      "PARAM",
      [
        "storage",
        "0109e630",
        null,
        "undefined8"
      ]
    ],
    [
      "0085e1a8",
      "READ",
      [
        "storage",
        "0029ca70",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0085e154",
      "READ",
      [
        "storage",
        "0109e6a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0085e180",
      "PARAM",
      [
        "storage",
        "0109e670",
        null,
        "undefined8"
      ]
    ],
    [
      "0085e1a8",
      "READ",
      [
        "storage",
        "0029cafb",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085e150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e130.md#insn-0085e150) · [`0085e180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e130.md#insn-0085e180) · [`0085e1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e130.md#insn-0085e1a0)
- 新版 [`0085e150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e130.md#insn-0085e150) · [`0085e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e130.md#insn-0085e180) · [`0085e1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e130.md#insn-0085e1a0)

~~~diff
- 0085e150 ["COPY", "tmp:0:8", ["const:660:8"]]
- 0085e150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085e150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085e150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085e150 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 0085e150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085e150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085e150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085e150 bytes 08811991
+ 0085e150 bytes 08811a91
- 0085e180 ["COPY", "tmp:0:8", ["const:630:8"]]
- 0085e180 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0085e180 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0085e180 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0085e180 ["COPY", "tmp:0:8", ["const:670:8"]]
+ 0085e180 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0085e180 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0085e180 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0085e180 bytes 00c01891
+ 0085e180 bytes 00c01991
- 0085e1a0 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 0085e1a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085e1a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085e1a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085e1a0 ["COPY", "tmp:0:8", ["const:afb:8"]]
+ 0085e1a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085e1a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085e1a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085e1a0 bytes 08c12991
+ 0085e1a0 bytes 08ed2b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-664ba6a633573b29c5e63268c13ce6d4"></a>

### [`0085e328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e328.md) → [`0085e328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e328.md) FUN_0085e328

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0085ef84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085ef84.md) · 呼出先 23件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`0085ef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085ef84.md) · 呼出先 23件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085e66c",
      "incomplete_value": false,
      "site": "0085e66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085e66c",
      "incomplete_value": false,
      "site": "0085e66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085e72c",
      "incomplete_value": false,
      "site": "0085e72c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085e72c",
      "incomplete_value": false,
      "site": "0085e72c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085e73c",
      "incomplete_value": false,
      "site": "0085e73c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085e73c",
      "incomplete_value": false,
      "site": "0085e73c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "0085e66c",
      "DATA",
      [
        "storage",
        "00c03e00",
        null,
        "undefined *"
      ]
    ],
    [
      "0085e6ec",
      "READ",
      [
        "storage",
        "00c03e28",
        null,
        "undefined *"
      ]
    ],
    [
      "0085e72c",
      "DATA",
      [
        "storage",
        "00c03e80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085e66c",
      "DATA",
      [
        "storage",
        "00c03e50",
        null,
        "undefined *"
      ]
    ],
    [
      "0085e6ec",
      "READ",
      [
        "storage",
        "00c03e78",
        null,
        "undefined *"
      ]
    ],
    [
      "0085e72c",
      "DATA",
      [
        "storage",
        "00c03ed0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085e668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e328.md#insn-0085e668) · [`0085e720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e328.md#insn-0085e720) · [`0085e734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e328.md#insn-0085e734)
- 新版 [`0085e668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e328.md#insn-0085e668) · [`0085e720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e328.md#insn-0085e720)

~~~diff
- 0085e668 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 0085e668 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0085e668 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0085e668 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0085e668 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 0085e668 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0085e668 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0085e668 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0085e668 bytes 4a013891
+ 0085e668 bytes 4a413991
- 0085e720 ["COPY", "tmp:0:8", ["const:e80:8"]]
- 0085e720 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0085e720 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0085e720 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0085e720 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 0085e720 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0085e720 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0085e720 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0085e720 bytes 4a013a91
+ 0085e720 bytes 4a413b91
- 0085e734 ["COPY", "register:4048:8", ["const:c03000:8"]]
- 0085e734 bytes 291d00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1eab09a2e12a5719260abcfdfde45e8a"></a>

### [`0085eb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085eb90.md) → [`0085eb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085eb90.md) FUN_0085eb90

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0085ef84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085ef84.md) [`0085f460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f460.md) [`00860170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860170.md) [`008602c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008602c0.md) · 呼出先 9件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0085fcb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fcb4.md) [`0085fcb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fcb8.md) [`008865b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md)
- 新版 呼出元 4件 [`0085ef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085ef84.md) [`0085f460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f460.md) [`00860170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860170.md) [`008602c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008602c0.md) · 呼出先 9件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0085fcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fcb4.md) [`0085fcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fcb8.md) [`008865b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/008865b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.07% / 新版 87.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085ebdc",
      "incomplete_value": true,
      "site": "0085ebec",
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
                "const:fb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085ebdc",
      "incomplete_value": true,
      "site": "0085ebec",
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
                "const:45:8"
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
      "definition_site": "0085ebe0",
      "incomplete_value": true,
      "site": "0085ebf0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0085ebe0",
      "incomplete_value": true,
      "site": "0085ebf0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085ec54",
      "incomplete_value": true,
      "site": "0085ec64",
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
                "const:fb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085ec54",
      "incomplete_value": true,
      "site": "0085ec64",
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
                "const:45:8"
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
      "0085ebdc",
      "READ",
      [
        "storage",
        "00296045",
        null,
        "string"
      ]
    ],
    [
      "0085ebe0",
      "READ",
      [
        "storage",
        "00296055",
        null,
        "string"
      ]
    ],
    [
      "0085ec54",
      "READ",
      [
        "storage",
        "00296045",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0085ebdc",
      "READ",
      [
        "storage",
        "00295fb8",
        null,
        "string"
      ]
    ],
    [
      "0085ebe0",
      "READ",
      [
        "storage",
        "00295fc8",
        null,
        "string"
      ]
    ],
    [
      "0085ec54",
      "READ",
      [
        "storage",
        "00295fb8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085ebd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085eb90.md#insn-0085ebd0) · [`0085ebd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085eb90.md#insn-0085ebd4) · [`0085ebd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085eb90.md#insn-0085ebd8)
- 新版 [`0085ebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085eb90.md#insn-0085ebd0) · [`0085ebd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085eb90.md#insn-0085ebd4)

~~~diff
- 0085ebd0 ["COPY", "register:4040:8", ["const:296000:8"]]
+ 0085ebd0 ["COPY", "register:4040:8", ["const:295000:8"]]
- 0085ebd0 bytes c8d1ff90
+ 0085ebd0 bytes a8d1fff0
- 0085ebd4 ["COPY", "tmp:0:8", ["const:45:8"]]
- 0085ebd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085ebd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085ebd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085ebd4 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0085ebd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085ebd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085ebd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085ebd4 bytes 08150191
+ 0085ebd4 bytes 08e13e91
- 0085ebd8 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0085ebd8 bytes 89d2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43ffe581b9989111f1400cda12985788"></a>

### [`0085ef84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085ef84.md) → [`0085ef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085ef84.md) FUN_0085ef84

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0085fed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fed0.md) [`00860de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860de0.md) [`0086a350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086a/0086a350.md) · 呼出先 16件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459f48.md) [`00459f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459f50.md) [`0056c55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c55c.md)
- 新版 呼出元 3件 [`0085fed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fed0.md) [`00860de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860de0.md) [`0086a350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086a/0086a350.md) · 呼出先 16件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f48.md) [`00459f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f50.md) [`0056c55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c55c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.52% / 新版 98.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085f2b4",
      "incomplete_value": false,
      "site": "0085f2bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f2b4",
      "incomplete_value": false,
      "site": "0085f2bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "0085f2bc",
      "DATA",
      [
        "storage",
        "00c04000",
        null,
        "undefined *"
      ]
    ],
    [
      "0085f2c8",
      "DATA",
      [
        "storage",
        "00c04080",
        null,
        "undefined *"
      ]
    ],
    [
      "0085f314",
      "READ",
      [
        "storage",
        "00c040a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0085f2bc",
      "DATA",
      [
        "storage",
        "00c04050",
        null,
        "undefined *"
      ]
    ],
    [
      "0085f2c8",
      "DATA",
      [
        "storage",
        "00c040d0",
        null,
        "undefined *"
      ]
    ],
    [
      "0085f314",
      "READ",
      [
        "storage",
        "00c040f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085f2b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085ef84.md#insn-0085f2b4) · [`0085f2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085ef84.md#insn-0085f2c0)
- 新版 [`0085f2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085ef84.md#insn-0085f2b4) · [`0085f2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085ef84.md#insn-0085f2c0)

~~~diff
- 0085f2b4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0085f2b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085f2b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085f2b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085f2b4 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 0085f2b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f2b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f2b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085f2b4 bytes 08010091
+ 0085f2b4 bytes 08410191
- 0085f2c0 ["COPY", "register:4040:8", ["const:c04000:8"]]
- 0085f2c0 bytes 281d00b0
+ 0085f2c0 ["COPY", "register:4040:8", ["const:c04000:8"]]
+ 0085f2c0 bytes 281d00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba51fbf14da908928523f0f7e4be03a5"></a>

### [`0085f5e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f5e8.md) → [`0085f5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f5e8.md) FUN_0085f5e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0085d778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085d/0085d778.md) [`0085e328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e328.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0085d778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d778.md) [`0085e328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e328.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0085f5f4",
      "incomplete_value": false,
      "site": "0085f5f8",
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
      "definition_site": "0085f5f4",
      "incomplete_value": false,
      "site": "0085f5f8",
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
      "0085f5f4",
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
      "0085f5f4",
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

- 旧版 [`0085f5f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f5e8.md#insn-0085f5f4)
- 新版 [`0085f5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f5e8.md#insn-0085f5f4)

~~~diff
- 0085f5f4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0085f5f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0085f5f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0085f5f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0085f5f4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0085f5f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0085f5f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0085f5f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0085f5f4 bytes 000c0c91
+ 0085f5f4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8664dad422bbd00528a07b06ec0cd700"></a>

### [`0085f600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f600.md) → [`0085f600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f600.md) FUN_0085f600

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
      "definition_site": "0085f614",
      "incomplete_value": false,
      "site": "0085f618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f614",
      "incomplete_value": false,
      "site": "0085f618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "0085f618",
      "DATA",
      [
        "storage",
        "00c03b70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085f618",
      "DATA",
      [
        "storage",
        "00c03bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085f614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f600.md#insn-0085f614)
- 新版 [`0085f614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f600.md#insn-0085f614)

~~~diff
- 0085f614 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 0085f614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085f614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085f614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085f614 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 0085f614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085f614 bytes 08c12d91
+ 0085f614 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d89c1d18fff6647dd1e1467b1fe665dc"></a>

### [`0085f624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f624.md) → [`0085f624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f624.md) FUN_0085f624

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
      "definition_site": "0085f628",
      "incomplete_value": false,
      "site": "0085f62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f628",
      "incomplete_value": false,
      "site": "0085f62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "0085f62c",
      "DATA",
      [
        "storage",
        "00c03b70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085f62c",
      "DATA",
      [
        "storage",
        "00c03bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085f628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f624.md#insn-0085f628)
- 新版 [`0085f628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f624.md#insn-0085f628)

~~~diff
- 0085f628 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 0085f628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085f628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085f628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085f628 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 0085f628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085f628 bytes 08c12d91
+ 0085f628 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f30bc3bea54bf1250e73a2c6fcf5e54"></a>

### [`0085f74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f74c.md) → [`0085f74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f74c.md) FUN_0085f74c

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
      "definition_site": "0085f760",
      "incomplete_value": false,
      "site": "0085f764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f760",
      "incomplete_value": false,
      "site": "0085f764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
      "0085f764",
      "DATA",
      [
        "storage",
        "00c03bf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085f764",
      "DATA",
      [
        "storage",
        "00c03c40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085f760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f74c.md#insn-0085f760)
- 新版 [`0085f760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f74c.md#insn-0085f760)

~~~diff
- 0085f760 ["COPY", "tmp:0:8", ["const:bf0:8"]]
- 0085f760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085f760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085f760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085f760 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 0085f760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085f760 bytes 08c12f91
+ 0085f760 bytes 08013191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddf6675bcfa69b1b4a8dbca98d6fa8e8"></a>

### [`0085f770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f770.md) → [`0085f770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f770.md) FUN_0085f770

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
      "definition_site": "0085f774",
      "incomplete_value": false,
      "site": "0085f778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f774",
      "incomplete_value": false,
      "site": "0085f778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
      "0085f778",
      "DATA",
      [
        "storage",
        "00c03bf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085f778",
      "DATA",
      [
        "storage",
        "00c03c40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085f774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f770.md#insn-0085f774)
- 新版 [`0085f774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f770.md#insn-0085f774)

~~~diff
- 0085f774 ["COPY", "tmp:0:8", ["const:bf0:8"]]
- 0085f774 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085f774 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085f774 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085f774 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 0085f774 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f774 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f774 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085f774 bytes 08c12f91
+ 0085f774 bytes 08013191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7bf0a3452941c6bfce9f1fac72f6724"></a>

### [`0085f788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f788.md) → [`0085f788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f788.md) FUN_0085f788

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f23b4.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.39% / 新版 97.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085f7f8",
      "incomplete_value": true,
      "site": "0085f808",
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
                "const:293000:8"
              ],
              [
                "leaf",
                "const:b96:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085f7f8",
      "incomplete_value": true,
      "site": "0085f808",
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
                "const:293000:8"
              ],
              [
                "leaf",
                "const:c23:8"
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
      "0085f7f8",
      "READ",
      [
        "storage",
        "00293c23",
        null,
        "string"
      ]
    ],
    [
      "0085f8d0",
      "DATA",
      [
        "storage",
        "00c03c60",
        null,
        "undefined *"
      ]
    ],
    [
      "0085f928",
      "READ",
      [
        "storage",
        "00c03c80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0085f7f8",
      "READ",
      [
        "storage",
        "00293b96",
        null,
        "string"
      ]
    ],
    [
      "0085f8d0",
      "DATA",
      [
        "storage",
        "00c03cb0",
        null,
        "undefined *"
      ]
    ],
    [
      "0085f928",
      "READ",
      [
        "storage",
        "00c03cd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085f7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f788.md#insn-0085f7f0) · [`0085f8c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f788.md#insn-0085f8c8)
- 新版 [`0085f7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f788.md#insn-0085f7f0) · [`0085f8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f788.md#insn-0085f8c8)

~~~diff
- 0085f7f0 ["COPY", "tmp:0:8", ["const:c23:8"]]
- 0085f7f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085f7f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085f7f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085f7f0 ["COPY", "tmp:0:8", ["const:b96:8"]]
+ 0085f7f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085f7f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085f7f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085f7f0 bytes 298d3091
+ 0085f7f0 bytes 29592e91
- 0085f8c8 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 0085f8c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085f8c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085f8c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085f8c8 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 0085f8c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f8c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085f8c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085f8c8 bytes 08813191
+ 0085f8c8 bytes 08c13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54a41b6c1d70d038c767232f12d37c8f"></a>

### [`0085fb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fb30.md) → [`0085fb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fb30.md) FUN_0085fb30

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
      "definition_site": "0085fb44",
      "incomplete_value": false,
      "site": "0085fb48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fb44",
      "incomplete_value": false,
      "site": "0085fb48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "0085fb48",
      "DATA",
      [
        "storage",
        "00c03c60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fb48",
      "DATA",
      [
        "storage",
        "00c03cb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fb30.md#insn-0085fb44)
- 新版 [`0085fb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fb30.md#insn-0085fb44)

~~~diff
- 0085fb44 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 0085fb44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085fb44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085fb44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085fb44 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 0085fb44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fb44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fb44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085fb44 bytes 08813191
+ 0085fb44 bytes 08c13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24ed42b309bf8c8eff2be598407f911e"></a>

### [`0085fb54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fb54.md) → [`0085fb54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fb54.md) FUN_0085fb54

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
      "definition_site": "0085fb58",
      "incomplete_value": false,
      "site": "0085fb5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fb58",
      "incomplete_value": false,
      "site": "0085fb5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "0085fb5c",
      "DATA",
      [
        "storage",
        "00c03c60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fb5c",
      "DATA",
      [
        "storage",
        "00c03cb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fb58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fb54.md#insn-0085fb58)
- 新版 [`0085fb58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fb54.md#insn-0085fb58)

~~~diff
- 0085fb58 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 0085fb58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085fb58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085fb58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085fb58 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 0085fb58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fb58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fb58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085fb58 bytes 08813191
+ 0085fb58 bytes 08c13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7594e7f6a281b9081b43de0768239fbc"></a>

### [`0085fbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fbe0.md) → [`0085fbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fbe0.md) FUN_0085fbe0

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
      "definition_site": "0085fbf4",
      "incomplete_value": false,
      "site": "0085fbf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fbf4",
      "incomplete_value": false,
      "site": "0085fbf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d00:8"
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
      "0085fbf8",
      "DATA",
      [
        "storage",
        "00c03d00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fbf8",
      "DATA",
      [
        "storage",
        "00c03d50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fbf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fbe0.md#insn-0085fbf4)
- 新版 [`0085fbf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fbe0.md#insn-0085fbf4)

~~~diff
- 0085fbf4 ["COPY", "tmp:0:8", ["const:d00:8"]]
- 0085fbf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085fbf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085fbf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085fbf4 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 0085fbf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fbf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fbf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085fbf4 bytes 08013491
+ 0085fbf4 bytes 08413591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed92fba3f5e9f18a0c83b40b85a68efe"></a>

### [`0085fc04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fc04.md) → [`0085fc04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc04.md) FUN_0085fc04

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
      "definition_site": "0085fc08",
      "incomplete_value": false,
      "site": "0085fc0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fc08",
      "incomplete_value": false,
      "site": "0085fc0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d00:8"
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
      "0085fc0c",
      "DATA",
      [
        "storage",
        "00c03d00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fc0c",
      "DATA",
      [
        "storage",
        "00c03d50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fc04.md#insn-0085fc08)
- 新版 [`0085fc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc04.md#insn-0085fc08)

~~~diff
- 0085fc08 ["COPY", "tmp:0:8", ["const:d00:8"]]
- 0085fc08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085fc08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085fc08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085fc08 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 0085fc08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fc08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fc08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085fc08 bytes 08013491
+ 0085fc08 bytes 08413591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a40409776e62e03a12a7975cac73b9b"></a>

### [`0085fc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fc80.md) → [`0085fc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc80.md) FUN_0085fc80

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
      "definition_site": "0085fc94",
      "incomplete_value": false,
      "site": "0085fc98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fc94",
      "incomplete_value": false,
      "site": "0085fc98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
      "0085fc98",
      "DATA",
      [
        "storage",
        "00c03d80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fc98",
      "DATA",
      [
        "storage",
        "00c03dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fc80.md#insn-0085fc94)
- 新版 [`0085fc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc80.md#insn-0085fc94)

~~~diff
- 0085fc94 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 0085fc94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085fc94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085fc94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085fc94 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 0085fc94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fc94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fc94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085fc94 bytes 08013691
+ 0085fc94 bytes 08413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-525a83b57e538cfad207b89a4c9c7ec9"></a>

### [`0085fca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fca4.md) → [`0085fca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fca4.md) FUN_0085fca4

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
      "definition_site": "0085fca8",
      "incomplete_value": false,
      "site": "0085fcac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fca8",
      "incomplete_value": false,
      "site": "0085fcac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
      "0085fcac",
      "DATA",
      [
        "storage",
        "00c03d80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fcac",
      "DATA",
      [
        "storage",
        "00c03dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fca4.md#insn-0085fca8)
- 新版 [`0085fca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fca4.md#insn-0085fca8)

~~~diff
- 0085fca8 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 0085fca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085fca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085fca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085fca8 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 0085fca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085fca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085fca8 bytes 08013691
+ 0085fca8 bytes 08413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a7f01cf9329cfc75087dd3439a33bd7"></a>

### [`0085fd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fd2c.md) → [`0085fd2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd2c.md) FUN_0085fd2c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0085e328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085e328.md) [`0085ef84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085e/0085ef84.md) [`0085fed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fed0.md) [`00860170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860170.md) [`008602c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008602c0.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 7件 [`0085e328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e328.md) [`0085ef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085ef84.md) [`0085fed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fed0.md) [`00860170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860170.md) [`008602c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008602c0.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "0085fd38",
      "incomplete_value": false,
      "site": "0085fd3c",
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
      "definition_site": "0085fd38",
      "incomplete_value": false,
      "site": "0085fd3c",
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
      "0085fd38",
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
      "0085fd38",
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

- 旧版 [`0085fd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fd2c.md#insn-0085fd38)
- 新版 [`0085fd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd2c.md#insn-0085fd38)

~~~diff
- 0085fd38 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0085fd38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0085fd38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0085fd38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0085fd38 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0085fd38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0085fd38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0085fd38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0085fd38 bytes 000c0c91
+ 0085fd38 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09f95aca3a9876606703d2e419c74c46"></a>

### [`0085fd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fd40.md) → [`0085fd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd40.md) FUN_0085fd40

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085fd48",
      "incomplete_value": false,
      "site": "0085fd4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fd48",
      "incomplete_value": false,
      "site": "0085fd4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "0085fd4c",
      "DATA",
      [
        "storage",
        "00c03e00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fd4c",
      "DATA",
      [
        "storage",
        "00c03e50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fd48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fd40.md#insn-0085fd48)
- 新版 [`0085fd48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd40.md#insn-0085fd48)

~~~diff
- 0085fd48 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 0085fd48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085fd48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085fd48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085fd48 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 0085fd48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085fd48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085fd48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085fd48 bytes 29013891
+ 0085fd48 bytes 29413991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b74b2a6686308b6a043fe2055fab033d"></a>

### [`0085fd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fd60.md) → [`0085fd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd60.md) FUN_0085fd60

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085fd68",
      "incomplete_value": false,
      "site": "0085fd6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fd68",
      "incomplete_value": false,
      "site": "0085fd6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "0085fd6c",
      "DATA",
      [
        "storage",
        "00c03e00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fd6c",
      "DATA",
      [
        "storage",
        "00c03e50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fd68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fd60.md#insn-0085fd68)
- 新版 [`0085fd68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd60.md#insn-0085fd68)

~~~diff
- 0085fd68 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 0085fd68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085fd68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085fd68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085fd68 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 0085fd68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085fd68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085fd68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085fd68 bytes 29013891
+ 0085fd68 bytes 29413991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dcf180b22f7ae06707ab3373a10f319"></a>

### [`0085fda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fda0.md) → [`0085fda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fda0.md) FUN_0085fda0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085fdd0",
      "incomplete_value": false,
      "site": "0085fdd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fdd0",
      "incomplete_value": false,
      "site": "0085fdd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "0085fdd0",
      "DATA",
      [
        "storage",
        "00c03e00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fdd0",
      "DATA",
      [
        "storage",
        "00c03e50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fdc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fda0.md#insn-0085fdc4)
- 新版 [`0085fdc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fda0.md#insn-0085fdc4)

~~~diff
- 0085fdc4 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 0085fdc4 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 0085fdc4 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 0085fdc4 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 0085fdc4 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 0085fdc4 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 0085fdc4 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 0085fdc4 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 0085fdc4 bytes 6b013891
+ 0085fdc4 bytes 6b413991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eef73c2b9e734f23d1232cd439abc09f"></a>

### [`0085fe24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fe24.md) → [`0085fe24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fe24.md) FUN_0085fe24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085fe44",
      "incomplete_value": false,
      "site": "0085fe44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085fe44",
      "incomplete_value": false,
      "site": "0085fe44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "0085fe44",
      "DATA",
      [
        "storage",
        "00c03e00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085fe44",
      "DATA",
      [
        "storage",
        "00c03e50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085fe38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fe24.md#insn-0085fe38) · [`0085fe40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085fe24.md#insn-0085fe40)
- 新版 [`0085fe38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fe24.md#insn-0085fe38) · [`0085fe40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fe24.md#insn-0085fe40)

~~~diff
- 0085fe38 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 0085fe38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085fe38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085fe38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085fe38 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 0085fe38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085fe38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085fe38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085fe38 bytes 29013891
+ 0085fe38 bytes 29413991
- 0085fe40 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 0085fe40 bytes f40300aa
+ 0085fe40 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 0085fe40 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a94389ecf401b7df94b8acc4244483d"></a>

### [`00860118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860118.md) → [`00860118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860118.md) FUN_00860118

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
      "definition_site": "00860138",
      "incomplete_value": false,
      "site": "0086013c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860138",
      "incomplete_value": false,
      "site": "0086013c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e80:8"
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
      "0086013c",
      "DATA",
      [
        "storage",
        "00c03e80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086013c",
      "DATA",
      [
        "storage",
        "00c03ed0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00860138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860118.md#insn-00860138)
- 新版 [`00860138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860118.md#insn-00860138)

~~~diff
- 00860138 ["COPY", "tmp:0:8", ["const:e80:8"]]
- 00860138 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00860138 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00860138 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00860138 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 00860138 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00860138 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00860138 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00860138 bytes 08013a91
+ 00860138 bytes 08413b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71f500198182e7ed86cb3e6712104335"></a>

### [`00860150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860150.md) → [`00860150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860150.md) FUN_00860150

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
      "definition_site": "00860154",
      "incomplete_value": false,
      "site": "00860158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860154",
      "incomplete_value": false,
      "site": "00860158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
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
      "00860158",
      "DATA",
      [
        "storage",
        "00c03e80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00860158",
      "DATA",
      [
        "storage",
        "00c03ed0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00860154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860150.md#insn-00860154)
- 新版 [`00860154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860150.md#insn-00860154)

~~~diff
- 00860154 ["COPY", "tmp:0:8", ["const:e80:8"]]
- 00860154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00860154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00860154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00860154 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 00860154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00860154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00860154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00860154 bytes 08013a91
+ 00860154 bytes 08413b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5594dd8111d885face125ff0434bd8cc"></a>

### [`008602a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008602a0.md) → [`008602a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008602a0.md) FUN_008602a0

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
      "definition_site": "008602a4",
      "incomplete_value": false,
      "site": "008602a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008602a4",
      "incomplete_value": false,
      "site": "008602a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "008602a8",
      "DATA",
      [
        "storage",
        "00c03f00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008602a8",
      "DATA",
      [
        "storage",
        "00c03f50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008602a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008602a0.md#insn-008602a4)
- 新版 [`008602a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008602a0.md#insn-008602a4)

~~~diff
- 008602a4 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 008602a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008602a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008602a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008602a4 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 008602a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008602a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008602a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008602a4 bytes 08013c91
+ 008602a4 bytes 08413d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dbaba24359dad7b76a7a632f3d65315"></a>

### [`008603b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008603b4.md) → [`008603b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008603b4.md) FUN_008603b4

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
      "definition_site": "008603d4",
      "incomplete_value": false,
      "site": "008603d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008603d4",
      "incomplete_value": false,
      "site": "008603d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
      "008603d8",
      "DATA",
      [
        "storage",
        "00c03f80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008603d8",
      "DATA",
      [
        "storage",
        "00c03fd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008603d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008603b4.md#insn-008603d4)
- 新版 [`008603d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008603b4.md#insn-008603d4)

~~~diff
- 008603d4 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 008603d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008603d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008603d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008603d4 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 008603d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008603d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008603d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008603d4 bytes 08013e91
+ 008603d4 bytes 08413f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ebe1408112efe91b57dca020f71c8a2"></a>

### [`008603ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008603ec.md) → [`008603ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008603ec.md) FUN_008603ec

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
      "definition_site": "008603f0",
      "incomplete_value": false,
      "site": "008603f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008603f0",
      "incomplete_value": false,
      "site": "008603f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
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
      "008603f4",
      "DATA",
      [
        "storage",
        "00c03f80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008603f4",
      "DATA",
      [
        "storage",
        "00c03fd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008603f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008603ec.md#insn-008603f0)
- 新版 [`008603f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008603ec.md#insn-008603f0)

~~~diff
- 008603f0 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 008603f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008603f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008603f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008603f0 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 008603f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008603f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008603f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008603f0 bytes 08013e91
+ 008603f0 bytes 08413f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cef2dc1f84afe5816f2425aa6d1f370"></a>

### [`008604b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008604b0.md) → [`008604b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008604b0.md) FUN_008604b0

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
      "definition_site": "008604c4",
      "incomplete_value": false,
      "site": "008604c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008604c4",
      "incomplete_value": false,
      "site": "008604c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "008604c8",
      "DATA",
      [
        "storage",
        "00c04000",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008604c8",
      "DATA",
      [
        "storage",
        "00c04050",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008604c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008604b0.md#insn-008604c4)
- 新版 [`008604c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008604b0.md#insn-008604c4)

~~~diff
- 008604c4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 008604c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008604c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008604c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008604c4 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 008604c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008604c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008604c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008604c4 bytes 08010091
+ 008604c4 bytes 08410191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6cc64d77dbdcd08fad82880471fb714"></a>

### [`008604d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008604d4.md) → [`008604d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008604d4.md) FUN_008604d4

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
      "definition_site": "008604d8",
      "incomplete_value": false,
      "site": "008604dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008604d8",
      "incomplete_value": false,
      "site": "008604dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "008604dc",
      "DATA",
      [
        "storage",
        "00c04000",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008604dc",
      "DATA",
      [
        "storage",
        "00c04050",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008604d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008604d4.md#insn-008604d8)
- 新版 [`008604d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008604d4.md#insn-008604d8)

~~~diff
- 008604d8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 008604d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008604d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008604d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008604d8 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 008604d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008604d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008604d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008604d8 bytes 08010091
+ 008604d8 bytes 08410191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-044f27fe53fbc65bb6309aed15845400"></a>

### [`0086051c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/0086051c.md) → [`0086051c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/0086051c.md) FUN_0086051c

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
      "definition_site": "0086053c",
      "incomplete_value": false,
      "site": "00860540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086053c",
      "incomplete_value": false,
      "site": "00860540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:80:8"
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
      "00860540",
      "DATA",
      [
        "storage",
        "00c04080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00860540",
      "DATA",
      [
        "storage",
        "00c040d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086053c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/0086051c.md#insn-0086053c)
- 新版 [`0086053c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/0086051c.md#insn-0086053c)

~~~diff
- 0086053c ["COPY", "tmp:0:8", ["const:80:8"]]
- 0086053c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0086053c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0086053c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086053c ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 0086053c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086053c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086053c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0086053c bytes 08010291
+ 0086053c bytes 08410391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f28586e03c4ff36dc3202f2dfb303107"></a>

### [`00860554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860554.md) → [`00860554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860554.md) FUN_00860554

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
      "definition_site": "00860558",
      "incomplete_value": false,
      "site": "0086055c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00860558",
      "incomplete_value": false,
      "site": "0086055c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:80:8"
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
      "0086055c",
      "DATA",
      [
        "storage",
        "00c04080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086055c",
      "DATA",
      [
        "storage",
        "00c040d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00860558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860554.md#insn-00860558)
- 新版 [`00860558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860554.md#insn-00860558)

~~~diff
- 00860558 ["COPY", "tmp:0:8", ["const:80:8"]]
- 00860558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00860558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00860558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00860558 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 00860558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00860558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00860558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00860558 bytes 08010291
+ 00860558 bytes 08410391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

