# v15.7.4 → v16.0.0 · 最優先の変更候補 (3)

[一覧の目次](README.md)

<a id="compare-0bf206da3014e02b831a71f681156d4f"></a>

### [`00438788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438788.md) → [`0045b620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b620.md) FUN_0045b620

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045b638",
      "incomplete_value": false,
      "site": "0045b644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004387a0",
      "incomplete_value": false,
      "site": "004387ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "0045b644",
      "DATA",
      [
        "storage",
        "00be6a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045b644",
      "DATA",
      [
        "storage",
        "00c635f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043879c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438788.md#insn-0043879c) · [`004387a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438788.md#insn-004387a0) · [`004387d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438788.md#insn-004387d0)
- 新版 [`0045b634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b620.md#insn-0045b634) · [`0045b638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b620.md#insn-0045b638) · [`0045b668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b620.md#insn-0045b668)

~~~diff
- 0043879c ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045b634 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043879c bytes 683d00d0
+ 0045b634 bytes 48400090
- 004387a0 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 004387a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004387a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004387a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045b638 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 0045b638 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b638 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b638 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004387a0 bytes 08c12891
+ 0045b638 bytes 08c11791
- 004387d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004387d0 ["INT_ADD", "register:40f0:8", ["const:4387d0:8", "const:4:8"]]
- 004387d0 ["CALLIND", null, ["register:0:8"]]
+ 0045b668 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045b668 ["INT_ADD", "register:40f0:8", ["const:45b668:8", "const:4:8"]]
+ 0045b668 ["CALLIND", null, ["register:0:8"]]
- 004387d0 bytes 00013fd6
+ 0045b668 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f8cdd63153c5817d7d365ed4b9693df"></a>

### [`00438874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438874.md) → [`0045b70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b70c.md) FUN_0045b70c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045b724",
      "incomplete_value": false,
      "site": "0045b730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043888c",
      "incomplete_value": false,
      "site": "00438898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "0045b730",
      "DATA",
      [
        "storage",
        "00be6a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045b730",
      "DATA",
      [
        "storage",
        "00c635f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438874.md#insn-00438888) · [`0043888c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438874.md#insn-0043888c) · [`004388bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438874.md#insn-004388bc)
- 新版 [`0045b720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b70c.md#insn-0045b720) · [`0045b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b70c.md#insn-0045b724) · [`0045b754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b70c.md#insn-0045b754)

~~~diff
- 00438888 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045b720 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00438888 bytes 683d00d0
+ 0045b720 bytes 48400090
- 0043888c ["COPY", "tmp:0:8", ["const:a30:8"]]
- 0043888c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043888c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043888c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045b724 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 0045b724 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b724 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b724 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043888c bytes 08c12891
+ 0045b724 bytes 08c11791
- 004388bc ["COPY", "register:0:8", ["register:4040:8"]]
- 004388bc ["INT_ADD", "register:40f0:8", ["const:4388bc:8", "const:4:8"]]
- 004388bc ["CALLIND", null, ["register:0:8"]]
+ 0045b754 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045b754 ["INT_ADD", "register:40f0:8", ["const:45b754:8", "const:4:8"]]
+ 0045b754 ["CALLIND", null, ["register:0:8"]]
- 004388bc bytes 00013fd6
+ 0045b754 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43e93fd73140ac161530c8539a20b9cc"></a>

### [`0043895c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/0043895c.md) → [`0045b7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b7f4.md) FUN_0045b7f4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00438c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045babc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045babc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0045b818",
      "incomplete_value": false,
      "site": "0045b818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438980",
      "incomplete_value": false,
      "site": "00438980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "0045b818",
      "DATA",
      [
        "storage",
        "00be6a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045b818",
      "DATA",
      [
        "storage",
        "00c635f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/0043895c.md#insn-00438970) · [`00438978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/0043895c.md#insn-00438978) · [`0043897c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/0043895c.md#insn-0043897c)
- 新版 [`0045b808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b7f4.md#insn-0045b808) · [`0045b810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b7f4.md#insn-0045b810) · [`0045b814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b7f4.md#insn-0045b814)

~~~diff
- 00438970 ["INT_ADD", "register:40f0:8", ["const:438970:8", "const:4:8"]]
- 00438970 ["CALL", null, ["callee:00c57a90:8"]]
+ 0045b808 ["INT_ADD", "register:40f0:8", ["const:45b808:8", "const:4:8"]]
+ 0045b808 ["CALL", null, ["callee:00c57a90:8"]]
- 00438970 bytes b4891e94
+ 0045b808 bytes a2f01f94
- 00438978 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045b810 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00438978 bytes 683d00d0
+ 0045b810 bytes 48400090
- 0043897c ["COPY", "tmp:0:8", ["const:a30:8"]]
- 0043897c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043897c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043897c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045b814 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 0045b814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043897c bytes 08c12891
+ 0045b814 bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4d18045b9246720ca3a9ddb93670193"></a>

### [`004389b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/004389b0.md) → [`0045b848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b848.md) FUN_0045b848

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00438c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438c24.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045babc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045babc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045b854",
      "incomplete_value": false,
      "site": "0045b854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004389bc",
      "incomplete_value": false,
      "site": "004389bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "0045b854",
      "DATA",
      [
        "storage",
        "00be6a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045b854",
      "DATA",
      [
        "storage",
        "00c635f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004389b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/004389b0.md#insn-004389b4) · [`004389b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/004389b0.md#insn-004389b8)
- 新版 [`0045b84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b848.md#insn-0045b84c) · [`0045b850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b848.md#insn-0045b850)

~~~diff
- 004389b4 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0045b84c ["COPY", "register:4048:8", ["const:c63000:8"]]
- 004389b4 bytes 693d00d0
+ 0045b84c bytes 49400090
- 004389b8 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 004389b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004389b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004389b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045b850 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 0045b850 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045b850 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045b850 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004389b8 bytes 29c12891
+ 0045b850 bytes 29c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b156a80a5b784463435047e290a2ae35"></a>

### [`004389fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/004389fc.md) → [`0045b894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b894.md) FUN_0045b894

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md) [`0073eb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073eb44.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md) [`00768e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768e50.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.17% / 新版 94.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045b8d0",
      "value": [
        "leaf",
        "ram:768e50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00438a38",
      "value": [
        "leaf",
        "ram:73eb44:8"
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
      "site": "0045b948",
      "value": [
        "leaf",
        "ram:764344:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00438ab0",
      "value": [
        "leaf",
        "ram:73a038:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045b9fc",
      "incomplete_value": false,
      "site": "0045ba00",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438b64",
      "incomplete_value": false,
      "site": "00438b68",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045b8d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073eb44"
      ]
    ],
    [
      "0045b8dc",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045b948",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073a038"
      ]
    ]
  ],
  "added": [
    [
      "0045b8d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e50"
      ]
    ],
    [
      "0045b8dc",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045b948",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/004389fc.md#insn-00438a38) · [`00438ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/004389fc.md#insn-00438ab0) · [`00438b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/004389fc.md#insn-00438b68)
- 新版 [`0045b8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b894.md#insn-0045b8d0) · [`0045b948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b894.md#insn-0045b948) · [`0045ba00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b894.md#insn-0045ba00)

~~~diff
- 00438a38 ["INT_ADD", "register:40f0:8", ["const:438a38:8", "const:4:8"]]
- 00438a38 ["CALL", null, ["ram:73eb44:8"]]
+ 0045b8d0 ["INT_ADD", "register:40f0:8", ["const:45b8d0:8", "const:4:8"]]
+ 0045b8d0 ["CALL", null, ["ram:768e50:8"]]
- 00438a38 bytes 43180c94
+ 0045b8d0 bytes 60350c94
- 00438ab0 ["INT_ADD", "register:40f0:8", ["const:438ab0:8", "const:4:8"]]
- 00438ab0 ["CALL", null, ["ram:73a038:8"]]
+ 0045b948 ["INT_ADD", "register:40f0:8", ["const:45b948:8", "const:4:8"]]
+ 0045b948 ["CALL", null, ["ram:764344:8"]]
- 00438ab0 bytes 62050c94
+ 0045b948 bytes 7f220c94
- 00438b68 ["INT_ADD", "register:40f0:8", ["const:438b68:8", "const:4:8"]]
- 00438b68 ["CALL", null, ["callee:00c57a50:8"]]
+ 0045ba00 ["INT_ADD", "register:40f0:8", ["const:45ba00:8", "const:4:8"]]
+ 0045ba00 ["CALL", null, ["callee:00c57a50:8"]]
- 00438b68 bytes 26891e94
+ 0045ba00 bytes 14f01f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91bd8d49ee7dd05fc2fba952db1628e2"></a>

### [`00438f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f04.md) → [`0045bd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd9c.md) FUN_0045bd9c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00438f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f54.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045bdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdec.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045bdac",
      "incomplete_value": false,
      "site": "0045bdb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438f14",
      "incomplete_value": false,
      "site": "00438f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "0045bdb0",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045bdb0",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f04.md#insn-00438f10) · [`00438f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f04.md#insn-00438f14)
- 新版 [`0045bda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd9c.md#insn-0045bda8) · [`0045bdac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd9c.md#insn-0045bdac)

~~~diff
- 00438f10 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0045bda8 ["COPY", "register:4048:8", ["const:c63000:8"]]
- 00438f10 bytes 693d00d0
+ 0045bda8 bytes 49400090
- 00438f14 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00438f14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00438f14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00438f14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045bdac ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 0045bdac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045bdac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045bdac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00438f14 bytes 29812c91
+ 0045bdac bytes 29811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85165cb115883fdfe3cead537613e4c2"></a>

### [`00438f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f20.md) → [`0045bdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdb8.md) FUN_0045bdb8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) [`0073cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md) [`0076e98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e98c.md) [`00ad0260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad0260.md) · 呼出先 2件 [`00438f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f54.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 7件 [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) [`00798e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798e60.md) [`007abbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007abbe4.md) · 呼出先 2件 [`0045bdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0045bdd4",
      "incomplete_value": false,
      "site": "0045bdd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438f3c",
      "incomplete_value": false,
      "site": "00438f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "0045bdd4",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045bdd4",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f20.md#insn-00438f30) · [`00438f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f20.md#insn-00438f34) · [`00438f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f20.md#insn-00438f40)
- 新版 [`0045bdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdb8.md#insn-0045bdc8) · [`0045bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdb8.md#insn-0045bdcc) · [`0045bdd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdb8.md#insn-0045bdd8)

~~~diff
- 00438f30 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045bdc8 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00438f30 bytes 683d00d0
+ 0045bdc8 bytes 48400090
- 00438f34 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00438f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00438f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00438f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045bdcc ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 0045bdcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bdcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bdcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00438f34 bytes 08812c91
+ 0045bdcc bytes 08811b91
- 00438f40 ["INT_ADD", "register:40f0:8", ["const:438f40:8", "const:4:8"]]
- 00438f40 ["CALL", null, ["callee:0045bdec:8"]]
+ 0045bdd8 ["INT_ADD", "register:40f0:8", ["const:45bdd8:8", "const:4:8"]]
+ 0045bdd8 ["CALL", null, ["callee:0045bdec:8"]]
- 00438f40 bytes 05000094
+ 0045bdd8 bytes 05000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-452b84fd9715c1003dc2bc9d7e347fa5"></a>

### [`00438fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438fbc.md) → [`0045be54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045be54.md) FUN_0045be54

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045be60",
      "incomplete_value": false,
      "site": "0045be6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438fc8",
      "incomplete_value": false,
      "site": "00438fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b80:8"
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
      "0045be6c",
      "DATA",
      [
        "storage",
        "00be6b80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045be6c",
      "DATA",
      [
        "storage",
        "00c63740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438fbc.md#insn-00438fc4) · [`00438fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438fbc.md#insn-00438fc8)
- 新版 [`0045be5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045be54.md#insn-0045be5c) · [`0045be60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045be54.md#insn-0045be60)

~~~diff
- 00438fc4 ["COPY", "register:4050:8", ["const:be6000:8"]]
+ 0045be5c ["COPY", "register:4050:8", ["const:c63000:8"]]
- 00438fc4 bytes 6a3d00d0
+ 0045be5c bytes 4a400090
- 00438fc8 ["COPY", "tmp:0:8", ["const:b80:8"]]
- 00438fc8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00438fc8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00438fc8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045be60 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0045be60 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045be60 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045be60 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00438fc8 bytes 4a012e91
+ 0045be60 bytes 4a011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21781a0722c9890f985b3e6f5bcc0b9f"></a>

### [`00439000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439000.md) → [`0045be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045be98.md) FUN_0045be98

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0045beb0",
      "incomplete_value": false,
      "site": "0045bebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439018",
      "incomplete_value": false,
      "site": "00439024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b80:8"
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
      "0045bebc",
      "DATA",
      [
        "storage",
        "00be6b80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045bebc",
      "DATA",
      [
        "storage",
        "00c63740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439000.md#insn-00439014) · [`00439018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439000.md#insn-00439018) · [`00439048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439000.md#insn-00439048)
- 新版 [`0045beac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045be98.md#insn-0045beac) · [`0045beb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045be98.md#insn-0045beb0) · [`0045bee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045be98.md#insn-0045bee0)

~~~diff
- 00439014 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045beac ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00439014 bytes 683d00b0
+ 0045beac bytes 48400090
- 00439018 ["COPY", "tmp:0:8", ["const:b80:8"]]
- 00439018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045beb0 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0045beb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045beb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045beb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439018 bytes 08012e91
+ 0045beb0 bytes 08011d91
- 00439048 ["COPY", "register:0:8", ["register:4040:8"]]
- 00439048 ["INT_ADD", "register:40f0:8", ["const:439048:8", "const:4:8"]]
- 00439048 ["CALLIND", null, ["register:0:8"]]
+ 0045bee0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045bee0 ["INT_ADD", "register:40f0:8", ["const:45bee0:8", "const:4:8"]]
+ 0045bee0 ["CALLIND", null, ["register:0:8"]]
- 00439048 bytes 00013fd6
+ 0045bee0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91c922b5c4a72bf537323f1e59112c30"></a>

### [`0043905c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/0043905c.md) → [`0045bef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bef4.md) FUN_0045bef4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045bf20",
      "incomplete_value": false,
      "site": "0045bf20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439088",
      "incomplete_value": false,
      "site": "00439088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b80:8"
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
      "0045bf20",
      "DATA",
      [
        "storage",
        "00be6b80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045bf20",
      "DATA",
      [
        "storage",
        "00c63740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/0043905c.md#insn-00439070) · [`0043907c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/0043905c.md#insn-0043907c) · [`00439080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/0043905c.md#insn-00439080)
- 新版 [`0045bf08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bef4.md#insn-0045bf08) · [`0045bf14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bef4.md#insn-0045bf14) · [`0045bf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bef4.md#insn-0045bf18)

~~~diff
- 00439070 ["INT_ADD", "register:40f0:8", ["const:439070:8", "const:4:8"]]
- 00439070 ["CALL", null, ["callee:00c57a90:8"]]
+ 0045bf08 ["INT_ADD", "register:40f0:8", ["const:45bf08:8", "const:4:8"]]
+ 0045bf08 ["CALL", null, ["callee:00c57a90:8"]]
- 00439070 bytes f4871e94
+ 0045bf08 bytes e2ee1f94
- 0043907c ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045bf14 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043907c bytes 683d00b0
+ 0045bf14 bytes 48400090
- 00439080 ["COPY", "tmp:0:8", ["const:b80:8"]]
- 00439080 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439080 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439080 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045bf18 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0045bf18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bf18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bf18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439080 bytes 08012e91
+ 0045bf18 bytes 08011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c50be4b2ed99ec1ff7c21232cf37a87"></a>

### [`004390e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004390e4.md) → [`0045bf7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bf7c.md) FUN_0045bf7c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045bf98",
      "incomplete_value": false,
      "site": "0045bf98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439100",
      "incomplete_value": false,
      "site": "00439100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b80:8"
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
      "0045bf98",
      "DATA",
      [
        "storage",
        "00be6b80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045bf98",
      "DATA",
      [
        "storage",
        "00c63740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004390f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004390e4.md#insn-004390f8) · [`004390fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004390e4.md#insn-004390fc) · [`00439120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004390e4.md#insn-00439120)
- 新版 [`0045bf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bf7c.md#insn-0045bf90) · [`0045bf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bf7c.md#insn-0045bf94) · [`0045bfb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bf7c.md#insn-0045bfb8)

~~~diff
- 004390f8 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0045bf90 ["COPY", "register:4048:8", ["const:c63000:8"]]
- 004390f8 bytes 693d00b0
+ 0045bf90 bytes 49400090
- 004390fc ["COPY", "tmp:0:8", ["const:b80:8"]]
- 004390fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004390fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004390fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045bf94 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0045bf94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045bf94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045bf94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004390fc bytes 29012e91
+ 0045bf94 bytes 29011d91
- 00439120 ["COPY", "register:0:8", ["register:4048:8"]]
- 00439120 ["INT_ADD", "register:40f0:8", ["const:439120:8", "const:4:8"]]
- 00439120 ["CALLIND", null, ["register:0:8"]]
+ 0045bfb8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045bfb8 ["INT_ADD", "register:40f0:8", ["const:45bfb8:8", "const:4:8"]]
+ 0045bfb8 ["CALLIND", null, ["register:0:8"]]
- 00439120 bytes 20013fd6
+ 0045bfb8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64ea187e762203a27e5f218552545414"></a>

### [`004391e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004391e0.md) → [`0045c078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c078.md) FUN_0045c078

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045c0c0",
      "incomplete_value": true,
      "site": "0045c0c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:165:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439228",
      "incomplete_value": true,
      "site": "00439228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:674:8"
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
      "definition_site": "0045c244",
      "incomplete_value": true,
      "site": "0045c258",
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
                "const:d4e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004393ac",
      "incomplete_value": true,
      "site": "004393c0",
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
                "const:63e:8"
              ]
            ]
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
      "definition_site": "0045c324",
      "incomplete_value": true,
      "site": "0045c324",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:e60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043948c",
      "incomplete_value": true,
      "site": "0043948c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:290000:8"
              ],
              [
                "leaf",
                "const:91e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045c09c",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "0045c244",
      "READ",
      [
        "storage",
        "0029263e",
        null,
        "string"
      ]
    ],
    [
      "0045c310",
      "READ",
      [
        "storage",
        "0029091e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0045c09c",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "0045c244",
      "READ",
      [
        "storage",
        "002a1d4e",
        null,
        "string"
      ]
    ],
    [
      "0045c310",
      "READ",
      [
        "storage",
        "0029fe60",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004391f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004391e0.md#insn-004391f8) · [`004391fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004391e0.md#insn-004391fc) · [`00439238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004391e0.md#insn-00439238)
- 新版 [`0045c090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c078.md#insn-0045c090) · [`0045c094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c078.md#insn-0045c094) · [`0045c0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c078.md#insn-0045c0d0)

~~~diff
- 004391f8 ["COPY", "register:4050:8", ["const:2a6000:8"]]
+ 0045c090 ["COPY", "register:4050:8", ["const:2b7000:8"]]
- 004391f8 bytes 6af3ffb0
+ 0045c090 bytes caf2fff0
- 004391fc ["COPY", "tmp:0:8", ["const:674:8"]]
- 004391fc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004391fc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004391fc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045c094 ["COPY", "tmp:0:8", ["const:165:8"]]
+ 0045c094 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c094 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c094 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004391fc bytes 4ad11991
+ 0045c094 bytes 4a950591
- 00439238 ["INT_ADD", "register:40f0:8", ["const:439238:8", "const:4:8"]]
- 00439238 ["CALL", null, ["callee:0044104c:8"]]
+ 0045c0d0 ["INT_ADD", "register:40f0:8", ["const:45c0d0:8", "const:4:8"]]
+ 0045c0d0 ["CALL", null, ["callee:0044104c:8"]]
- 00439238 bytes c594ff97
+ 0045c0d0 bytes df93ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d711ac342c04382b67d36daf883a167"></a>

### [`0043980c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/0043980c.md) → [`0045c6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c6a4.md) FUN_0045c6a4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045c6b0",
      "incomplete_value": false,
      "site": "0045c6bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439818",
      "incomplete_value": false,
      "site": "00439824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "0045c6bc",
      "DATA",
      [
        "storage",
        "00be6c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c6bc",
      "DATA",
      [
        "storage",
        "00c637d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/0043980c.md#insn-00439814) · [`00439818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/0043980c.md#insn-00439818)
- 新版 [`0045c6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c6a4.md#insn-0045c6ac) · [`0045c6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c6a4.md#insn-0045c6b0)

~~~diff
- 00439814 ["COPY", "register:4050:8", ["const:be6000:8"]]
+ 0045c6ac ["COPY", "register:4050:8", ["const:c63000:8"]]
- 00439814 bytes 6a3d00b0
+ 0045c6ac bytes 2a4000f0
- 00439818 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 00439818 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00439818 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00439818 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045c6b0 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 0045c6b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c6b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c6b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00439818 bytes 4a413091
+ 0045c6b0 bytes 4a411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-518f38ea2553e1b12bbb070f1c5eb6eb"></a>

### [`00439850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439850.md) → [`0045c6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c6e8.md) FUN_0045c6e8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0045c700",
      "incomplete_value": false,
      "site": "0045c70c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439868",
      "incomplete_value": false,
      "site": "00439874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "0045c70c",
      "DATA",
      [
        "storage",
        "00be6c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c70c",
      "DATA",
      [
        "storage",
        "00c637d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439850.md#insn-00439864) · [`00439868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439850.md#insn-00439868) · [`00439898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439850.md#insn-00439898)
- 新版 [`0045c6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c6e8.md#insn-0045c6fc) · [`0045c700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c6e8.md#insn-0045c700) · [`0045c730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c6e8.md#insn-0045c730)

~~~diff
- 00439864 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045c6fc ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00439864 bytes 683d00b0
+ 0045c6fc bytes 284000f0
- 00439868 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 00439868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045c700 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 0045c700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439868 bytes 08413091
+ 0045c700 bytes 08411f91
- 00439898 ["COPY", "register:0:8", ["register:4040:8"]]
- 00439898 ["INT_ADD", "register:40f0:8", ["const:439898:8", "const:4:8"]]
- 00439898 ["CALLIND", null, ["register:0:8"]]
+ 0045c730 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045c730 ["INT_ADD", "register:40f0:8", ["const:45c730:8", "const:4:8"]]
+ 0045c730 ["CALLIND", null, ["register:0:8"]]
- 00439898 bytes 00013fd6
+ 0045c730 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3184278b410ea321fb79b3304da0eb9"></a>

### [`004398ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004398ac.md) → [`0045c744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c744.md) FUN_0045c744

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045c770",
      "incomplete_value": false,
      "site": "0045c770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004398d8",
      "incomplete_value": false,
      "site": "004398d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "0045c770",
      "DATA",
      [
        "storage",
        "00be6c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c770",
      "DATA",
      [
        "storage",
        "00c637d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004398c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004398ac.md#insn-004398c0) · [`004398cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004398ac.md#insn-004398cc) · [`004398d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004398ac.md#insn-004398d0)
- 新版 [`0045c758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c744.md#insn-0045c758) · [`0045c764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c744.md#insn-0045c764) · [`0045c768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c744.md#insn-0045c768)

~~~diff
- 004398c0 ["INT_ADD", "register:40f0:8", ["const:4398c0:8", "const:4:8"]]
- 004398c0 ["CALL", null, ["callee:00c57a90:8"]]
+ 0045c758 ["INT_ADD", "register:40f0:8", ["const:45c758:8", "const:4:8"]]
+ 0045c758 ["CALL", null, ["callee:00c57a90:8"]]
- 004398c0 bytes e0851e94
+ 0045c758 bytes ceec1f94
- 004398cc ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045c764 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 004398cc bytes 683d00b0
+ 0045c764 bytes 284000f0
- 004398d0 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 004398d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004398d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004398d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045c768 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 0045c768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004398d0 bytes 08413091
+ 0045c768 bytes 08411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d32ba8849249ff197d39f20970f78d59"></a>

### [`00439934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439934.md) → [`0045c7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c7cc.md) FUN_0045c7cc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045c7e8",
      "incomplete_value": false,
      "site": "0045c7e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439950",
      "incomplete_value": false,
      "site": "00439950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "0045c7e8",
      "DATA",
      [
        "storage",
        "00be6c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c7e8",
      "DATA",
      [
        "storage",
        "00c637d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439934.md#insn-00439948) · [`0043994c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439934.md#insn-0043994c) · [`00439970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439934.md#insn-00439970)
- 新版 [`0045c7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c7cc.md#insn-0045c7e0) · [`0045c7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c7cc.md#insn-0045c7e4) · [`0045c808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c7cc.md#insn-0045c808)

~~~diff
- 00439948 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0045c7e0 ["COPY", "register:4048:8", ["const:c63000:8"]]
- 00439948 bytes 693d00b0
+ 0045c7e0 bytes 294000f0
- 0043994c ["COPY", "tmp:0:8", ["const:c10:8"]]
- 0043994c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043994c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043994c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045c7e4 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 0045c7e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045c7e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045c7e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043994c bytes 29413091
+ 0045c7e4 bytes 29411f91
- 00439970 ["COPY", "register:0:8", ["register:4048:8"]]
- 00439970 ["INT_ADD", "register:40f0:8", ["const:439970:8", "const:4:8"]]
- 00439970 ["CALLIND", null, ["register:0:8"]]
+ 0045c808 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045c808 ["INT_ADD", "register:40f0:8", ["const:45c808:8", "const:4:8"]]
+ 0045c808 ["CALLIND", null, ["register:0:8"]]
- 00439970 bytes 20013fd6
+ 0045c808 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14e480e5d7d1909f40f8ff92226472df"></a>

### [`00439eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439eb4.md) → [`0045cd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cd4c.md) FUN_0045cd4c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00439bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439bc0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0045ca58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ca58.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0045cd5c",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00439ec4",
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
      "definition_site": "0045cd58",
      "incomplete_value": false,
      "site": "0045cd5c",
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
      "definition_site": "00439ec0",
      "incomplete_value": false,
      "site": "00439ec4",
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
      "0045cd58",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0045cd5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0045cd58",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0045cd5c",
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

- 旧版 [`00439ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439eb4.md#insn-00439ec4) · [`00439ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439eb4.md#insn-00439ebc) · [`00439ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439eb4.md#insn-00439ec0)
- 新版 [`0045cd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cd4c.md#insn-0045cd5c) · [`0045cd54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cd4c.md#insn-0045cd54) · [`0045cd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cd4c.md#insn-0045cd58)

~~~diff
- 00439ec4 ["INT_ADD", "register:40f0:8", ["const:439ec4:8", "const:4:8"]]
- 00439ec4 ["CALL", null, ["ram:418c38:8"]]
+ 0045cd5c ["INT_ADD", "register:40f0:8", ["const:45cd5c:8", "const:4:8"]]
+ 0045cd5c ["CALL", null, ["ram:43b738:8"]]
- 00439ec4 bytes 5d7bff97
+ 0045cd5c bytes 777aff97
- 00439ebc ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0045cd54 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00439ebc bytes 60f3ffd0
+ 0045cd54 bytes c0f2fff0
- 00439ec0 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00439ec0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00439ec0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00439ec0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0045cd58 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0045cd58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0045cd58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0045cd58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00439ec0 bytes 00740e91
+ 0045cd58 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7c5231ed34a7f73ee24bc6cc6fd4dac"></a>

### [`00439ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439ec8.md) → [`0045cd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cd60.md) FUN_0045cd60

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045cd6c",
      "incomplete_value": false,
      "site": "0045cd78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439ed4",
      "incomplete_value": false,
      "site": "00439ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "0045cd78",
      "DATA",
      [
        "storage",
        "00be6ca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045cd78",
      "DATA",
      [
        "storage",
        "00c63860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439ec8.md#insn-00439ed0) · [`00439ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439ec8.md#insn-00439ed4)
- 新版 [`0045cd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cd60.md#insn-0045cd68) · [`0045cd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cd60.md#insn-0045cd6c)

~~~diff
- 00439ed0 ["COPY", "register:4050:8", ["const:be6000:8"]]
+ 0045cd68 ["COPY", "register:4050:8", ["const:c63000:8"]]
- 00439ed0 bytes 6a3d00b0
+ 0045cd68 bytes 2a4000f0
- 00439ed4 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00439ed4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00439ed4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00439ed4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045cd6c ["COPY", "tmp:0:8", ["const:860:8"]]
+ 0045cd6c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045cd6c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045cd6c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00439ed4 bytes 4a813291
+ 0045cd6c bytes 4a812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f283c4d1912b0ac114d39738236a79dd"></a>

### [`00439f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439f0c.md) → [`0045cda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cda4.md) FUN_0045cda4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0045cdbc",
      "incomplete_value": false,
      "site": "0045cdc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439f24",
      "incomplete_value": false,
      "site": "00439f30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "0045cdc8",
      "DATA",
      [
        "storage",
        "00be6ca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045cdc8",
      "DATA",
      [
        "storage",
        "00c63860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439f0c.md#insn-00439f20) · [`00439f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439f0c.md#insn-00439f24) · [`00439f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439f0c.md#insn-00439f54)
- 新版 [`0045cdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cda4.md#insn-0045cdb8) · [`0045cdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cda4.md#insn-0045cdbc) · [`0045cdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cda4.md#insn-0045cdec)

~~~diff
- 00439f20 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045cdb8 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00439f20 bytes 683d00b0
+ 0045cdb8 bytes 284000f0
- 00439f24 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00439f24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439f24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439f24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045cdbc ["COPY", "tmp:0:8", ["const:860:8"]]
+ 0045cdbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045cdbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045cdbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439f24 bytes 08813291
+ 0045cdbc bytes 08812191
- 00439f54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00439f54 ["INT_ADD", "register:40f0:8", ["const:439f54:8", "const:4:8"]]
- 00439f54 ["CALLIND", null, ["register:0:8"]]
+ 0045cdec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045cdec ["INT_ADD", "register:40f0:8", ["const:45cdec:8", "const:4:8"]]
+ 0045cdec ["CALLIND", null, ["register:0:8"]]
- 00439f54 bytes 00013fd6
+ 0045cdec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b35be21cff7ebdebc85ac22b6815972"></a>

### [`00439f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439f68.md) → [`0045ce00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce00.md) FUN_0045ce00

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045ce2c",
      "incomplete_value": false,
      "site": "0045ce2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439f94",
      "incomplete_value": false,
      "site": "00439f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "0045ce2c",
      "DATA",
      [
        "storage",
        "00be6ca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ce2c",
      "DATA",
      [
        "storage",
        "00c63860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439f68.md#insn-00439f7c) · [`00439f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439f68.md#insn-00439f88) · [`00439f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439f68.md#insn-00439f8c)
- 新版 [`0045ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce00.md#insn-0045ce14) · [`0045ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce00.md#insn-0045ce20) · [`0045ce24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce00.md#insn-0045ce24)

~~~diff
- 00439f7c ["INT_ADD", "register:40f0:8", ["const:439f7c:8", "const:4:8"]]
- 00439f7c ["CALL", null, ["callee:00c57a90:8"]]
+ 0045ce14 ["INT_ADD", "register:40f0:8", ["const:45ce14:8", "const:4:8"]]
+ 0045ce14 ["CALL", null, ["callee:00c57a90:8"]]
- 00439f7c bytes 31841e94
+ 0045ce14 bytes 1feb1f94
- 00439f88 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045ce20 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00439f88 bytes 683d00b0
+ 0045ce20 bytes 284000f0
- 00439f8c ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00439f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045ce24 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 0045ce24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ce24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ce24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439f8c bytes 08813291
+ 0045ce24 bytes 08812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70649628733743e077de021f3ccade5c"></a>

### [`00439ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439ff0.md) → [`0045ce88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce88.md) FUN_0045ce88

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045cea4",
      "incomplete_value": false,
      "site": "0045cea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a00c",
      "incomplete_value": false,
      "site": "0043a00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "0045cea4",
      "DATA",
      [
        "storage",
        "00be6ca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045cea4",
      "DATA",
      [
        "storage",
        "00c63860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439ff0.md#insn-0043a004) · [`0043a008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439ff0.md#insn-0043a008) · [`0043a02c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439ff0.md#insn-0043a02c)
- 新版 [`0045ce9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce88.md#insn-0045ce9c) · [`0045cea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce88.md#insn-0045cea0) · [`0045cec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce88.md#insn-0045cec4)

~~~diff
- 0043a004 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0045ce9c ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0043a004 bytes 693d0090
+ 0045ce9c bytes 294000f0
- 0043a008 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 0043a008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043a008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043a008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045cea0 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 0045cea0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045cea0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045cea0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043a008 bytes 29813291
+ 0045cea0 bytes 29812191
- 0043a02c ["COPY", "register:0:8", ["register:4048:8"]]
- 0043a02c ["INT_ADD", "register:40f0:8", ["const:43a02c:8", "const:4:8"]]
- 0043a02c ["CALLIND", null, ["register:0:8"]]
+ 0045cec4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045cec4 ["INT_ADD", "register:40f0:8", ["const:45cec4:8", "const:4:8"]]
+ 0045cec4 ["CALLIND", null, ["register:0:8"]]
- 0043a02c bytes 20013fd6
+ 0045cec4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7096d278dac1e321420f390ae9e3d596"></a>

### [`0043a0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a0ec.md) → [`0045cf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cf84.md) FUN_0045cf84

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 2件, `store_destination` 6件, `store_value` 2件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045cfd8",
      "incomplete_value": true,
      "site": "0045cfd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:165:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a140",
      "incomplete_value": true,
      "site": "0043a140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:674:8"
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
      "definition_site": "0045d108",
      "incomplete_value": true,
      "site": "0045d11c",
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
                "const:d4e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a270",
      "incomplete_value": true,
      "site": "0043a284",
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
                "const:63e:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045d2dc",
      "incomplete_value": false,
      "site": "0045d2dc",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a444",
      "incomplete_value": false,
      "site": "0043a444",
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
            "const:c58:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045cfa4",
      "PARAM",
      [
        "storage",
        "00c24c20",
        null,
        null
      ]
    ],
    [
      "0045cfc4",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "0045d108",
      "READ",
      [
        "storage",
        "0029263e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0045cfa4",
      "PARAM",
      [
        "storage",
        "00ca46e0",
        null,
        null
      ]
    ],
    [
      "0045cfc4",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "0045d108",
      "READ",
      [
        "storage",
        "002a1d4e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a0ec.md#insn-0043a11c) · [`0043a444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a0ec.md#insn-0043a444) · [`0043a63c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a0ec.md#insn-0043a63c)
- 新版 [`0045cfb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cf84.md#insn-0045cfb4) · [`0045d2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cf84.md#insn-0045d2dc) · [`0045d4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cf84.md#insn-0045d4d4)

~~~diff
- 0043a11c ["INT_ADD", "register:40f0:8", ["const:43a11c:8", "const:4:8"]]
- 0043a11c ["CALL", null, ["callee:00c57ce0:8"]]
+ 0045cfb4 ["INT_ADD", "register:40f0:8", ["const:45cfb4:8", "const:4:8"]]
+ 0045cfb4 ["CALL", null, ["callee:00c57ce0:8"]]
- 0043a11c bytes 5d841e94
+ 0045cfb4 bytes 4beb1f94
- 0043a444 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c58:8"]]
- 0043a444 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 0045d2dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:718:8"]]
+ 0045d2dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 0043a444 bytes 142d06f9
+ 0045d2dc bytes 148d03f9
- 0043a63c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c58:8"]]
- 0043a63c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0045d4d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:718:8"]]
+ 0045d4d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0043a63c bytes 132d06f9
+ 0045d4d4 bytes 138d03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6d6848e43eb81c1ed64a5acfe1e8b39"></a>

### [`0043a8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a8b8.md) → [`0045d750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d750.md) FUN_0045d750

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045d75c",
      "incomplete_value": false,
      "site": "0045d768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a8c4",
      "incomplete_value": false,
      "site": "0043a8d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "0045d768",
      "DATA",
      [
        "storage",
        "00be6d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d768",
      "DATA",
      [
        "storage",
        "00c638e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a8b8.md#insn-0043a8c0) · [`0043a8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a8b8.md#insn-0043a8c4)
- 新版 [`0045d758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d750.md#insn-0045d758) · [`0045d75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d750.md#insn-0045d75c)

~~~diff
- 0043a8c0 ["COPY", "register:4050:8", ["const:be6000:8"]]
+ 0045d758 ["COPY", "register:4050:8", ["const:c63000:8"]]
- 0043a8c0 bytes 6a3d0090
+ 0045d758 bytes 2a4000d0
- 0043a8c4 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 0043a8c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043a8c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043a8c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045d75c ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 0045d75c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045d75c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045d75c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043a8c4 bytes 4a813491
+ 0045d75c bytes 4a812391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0c1fd52728af743ab074a641138a2f8"></a>

### [`0043a8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a8fc.md) → [`0045d794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d794.md) FUN_0045d794

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0045d7ac",
      "incomplete_value": false,
      "site": "0045d7b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a914",
      "incomplete_value": false,
      "site": "0043a920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "0045d7b8",
      "DATA",
      [
        "storage",
        "00be6d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d7b8",
      "DATA",
      [
        "storage",
        "00c638e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a8fc.md#insn-0043a910) · [`0043a914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a8fc.md#insn-0043a914) · [`0043a944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a8fc.md#insn-0043a944)
- 新版 [`0045d7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d794.md#insn-0045d7a8) · [`0045d7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d794.md#insn-0045d7ac) · [`0045d7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d794.md#insn-0045d7dc)

~~~diff
- 0043a910 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045d7a8 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043a910 bytes 683d0090
+ 0045d7a8 bytes 284000d0
- 0043a914 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 0043a914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043a914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043a914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045d7ac ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 0045d7ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d7ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d7ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043a914 bytes 08813491
+ 0045d7ac bytes 08812391
- 0043a944 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043a944 ["INT_ADD", "register:40f0:8", ["const:43a944:8", "const:4:8"]]
- 0043a944 ["CALLIND", null, ["register:0:8"]]
+ 0045d7dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045d7dc ["INT_ADD", "register:40f0:8", ["const:45d7dc:8", "const:4:8"]]
+ 0045d7dc ["CALLIND", null, ["register:0:8"]]
- 0043a944 bytes 00013fd6
+ 0045d7dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a25abe2daecc140a014abf41fb3c5b45"></a>

### [`0043a958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a958.md) → [`0045d7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d7f0.md) FUN_0045d7f0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045d81c",
      "incomplete_value": false,
      "site": "0045d81c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a984",
      "incomplete_value": false,
      "site": "0043a984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "0045d81c",
      "DATA",
      [
        "storage",
        "00be6d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d81c",
      "DATA",
      [
        "storage",
        "00c638e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a958.md#insn-0043a96c) · [`0043a978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a958.md#insn-0043a978) · [`0043a97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a958.md#insn-0043a97c)
- 新版 [`0045d804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d7f0.md#insn-0045d804) · [`0045d810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d7f0.md#insn-0045d810) · [`0045d814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d7f0.md#insn-0045d814)

~~~diff
- 0043a96c ["INT_ADD", "register:40f0:8", ["const:43a96c:8", "const:4:8"]]
- 0043a96c ["CALL", null, ["callee:00c57a90:8"]]
+ 0045d804 ["INT_ADD", "register:40f0:8", ["const:45d804:8", "const:4:8"]]
+ 0045d804 ["CALL", null, ["callee:00c57a90:8"]]
- 0043a96c bytes b5811e94
+ 0045d804 bytes a3e81f94
- 0043a978 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045d810 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043a978 bytes 683d0090
+ 0045d810 bytes 284000d0
- 0043a97c ["COPY", "tmp:0:8", ["const:d20:8"]]
- 0043a97c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043a97c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043a97c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045d814 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 0045d814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043a97c bytes 08813491
+ 0045d814 bytes 08812391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c833dccbcb14f7ab495d99d9de5610c5"></a>

### [`0043a9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a9e0.md) → [`0045d878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d878.md) FUN_0045d878

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045d894",
      "incomplete_value": false,
      "site": "0045d894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a9fc",
      "incomplete_value": false,
      "site": "0043a9fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "0045d894",
      "DATA",
      [
        "storage",
        "00be6d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d894",
      "DATA",
      [
        "storage",
        "00c638e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a9e0.md#insn-0043a9f4) · [`0043a9f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a9e0.md#insn-0043a9f8) · [`0043aa1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a9e0.md#insn-0043aa1c)
- 新版 [`0045d88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d878.md#insn-0045d88c) · [`0045d890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d878.md#insn-0045d890) · [`0045d8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d878.md#insn-0045d8b4)

~~~diff
- 0043a9f4 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0045d88c ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0043a9f4 bytes 693d0090
+ 0045d88c bytes 294000d0
- 0043a9f8 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 0043a9f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043a9f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043a9f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045d890 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 0045d890 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045d890 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045d890 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043a9f8 bytes 29813491
+ 0045d890 bytes 29812391
- 0043aa1c ["COPY", "register:0:8", ["register:4048:8"]]
- 0043aa1c ["INT_ADD", "register:40f0:8", ["const:43aa1c:8", "const:4:8"]]
- 0043aa1c ["CALLIND", null, ["register:0:8"]]
+ 0045d8b4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045d8b4 ["INT_ADD", "register:40f0:8", ["const:45d8b4:8", "const:4:8"]]
+ 0045d8b4 ["CALLIND", null, ["register:0:8"]]
- 0043aa1c bytes 20013fd6
+ 0045d8b4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89a57a625cf804e2cf2e34ad83228a7a"></a>

### [`0043aadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043aadc.md) → [`0045d974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d974.md) FUN_0045d974

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`009bd618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd618.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 91.95% / 新版 91.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045da88",
      "incomplete_value": false,
      "site": "0045da88",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043abf0",
      "incomplete_value": false,
      "site": "0043abf0",
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
            "const:c58:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045da8c",
      "incomplete_value": false,
      "site": "0045da8c",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043abf4",
      "incomplete_value": false,
      "site": "0043abf4",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0045d9d0",
      "incomplete_value": true,
      "site": "0045d9d0",
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
      "definition_site": "0043ab38",
      "incomplete_value": true,
      "site": "0043ab38",
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
      "0045d9c8",
      "READ",
      [
        "storage",
        "00c24c50",
        null,
        "undefined8"
      ]
    ],
    [
      "0045d9c8",
      "READ",
      [
        "storage",
        "00c24c58",
        null,
        "undefined8"
      ]
    ],
    [
      "0045da34",
      "READ",
      [
        "storage",
        "00c24c50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0045d9c8",
      "READ",
      [
        "storage",
        "00ca4710",
        null,
        "undefined8"
      ]
    ],
    [
      "0045d9c8",
      "READ",
      [
        "storage",
        "00ca4718",
        null,
        "undefined8"
      ]
    ],
    [
      "0045da34",
      "READ",
      [
        "storage",
        "00ca4710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043abf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043aadc.md#insn-0043abf0) · [`0043abf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043aadc.md#insn-0043abf4) · [`0043ab0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043aadc.md#insn-0043ab0c)
- 新版 [`0045da88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d974.md#insn-0045da88) · [`0045da8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d974.md#insn-0045da8c) · [`0045d9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d974.md#insn-0045d9a4)

~~~diff
- 0043abf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c58:8"]]
- 0043abf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0045da88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:718:8"]]
+ 0045da88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0043abf0 bytes 132d06f9
+ 0045da88 bytes 138d03f9
- 0043abf4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0043abf4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0043abf4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:c70:8"]]
- 0043abf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0045da8c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0045da8c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0045da8c ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:730:8"]]
+ 0045da8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0043abf4 bytes 3fc13139
+ 0045da8c bytes 3fc11c39
- 0043ab0c ["INT_ADD", "register:40f0:8", ["const:43ab0c:8", "const:4:8"]]
- 0043ab0c ["CALL", null, ["callee:008514b8:8"]]
+ 0045d9a4 ["INT_ADD", "register:40f0:8", ["const:45d9a4:8", "const:4:8"]]
+ 0045d9a4 ["CALL", null, ["callee:008514b8:8"]]
- 0043ab0c bytes 9d920f94
+ 0045d9a4 bytes c5ce0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66076501441af5a68dba729f3ca6ac5d"></a>

### [`0043af94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043af94.md) → [`0045de2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de2c.md) FUN_0045de2c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043aca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043aca0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0045db38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045db38.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0045de3c",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0043afa4",
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
      "definition_site": "0045de38",
      "incomplete_value": false,
      "site": "0045de3c",
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
      "definition_site": "0043afa0",
      "incomplete_value": false,
      "site": "0043afa4",
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
      "0045de38",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0045de3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0045de38",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0045de3c",
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

- 旧版 [`0043afa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043af94.md#insn-0043afa4) · [`0043af9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043af94.md#insn-0043af9c) · [`0043afa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043af94.md#insn-0043afa0)
- 新版 [`0045de3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de2c.md#insn-0045de3c) · [`0045de34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de2c.md#insn-0045de34) · [`0045de38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de2c.md#insn-0045de38)

~~~diff
- 0043afa4 ["INT_ADD", "register:40f0:8", ["const:43afa4:8", "const:4:8"]]
- 0043afa4 ["CALL", null, ["ram:418c38:8"]]
+ 0045de3c ["INT_ADD", "register:40f0:8", ["const:45de3c:8", "const:4:8"]]
+ 0045de3c ["CALL", null, ["ram:43b738:8"]]
- 0043afa4 bytes 2577ff97
+ 0045de3c bytes 3f76ff97
- 0043af9c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0045de34 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0043af9c bytes 60f3ffb0
+ 0045de34 bytes c0f2ffd0
- 0043afa0 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0043afa0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0043afa0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0043afa0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0045de38 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0045de38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0045de38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0045de38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0043afa0 bytes 00740e91
+ 0045de38 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-710b6f8ad58f2b2141aa1b43dc81284d"></a>

### [`0043afac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043afac.md) → [`0045de44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de44.md) FUN_0045de44

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0045de68",
      "incomplete_value": false,
      "site": "0045de68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043afd0",
      "incomplete_value": false,
      "site": "0043afd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "0045de68",
      "DATA",
      [
        "storage",
        "00be6db0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045de68",
      "DATA",
      [
        "storage",
        "00c63970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043afc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043afac.md#insn-0043afc0) · [`0043afc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043afac.md#insn-0043afc8) · [`0043afcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043afac.md#insn-0043afcc)
- 新版 [`0045de58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de44.md#insn-0045de58) · [`0045de60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de44.md#insn-0045de60) · [`0045de64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de44.md#insn-0045de64)

~~~diff
- 0043afc0 ["INT_ADD", "register:40f0:8", ["const:43afc0:8", "const:4:8"]]
- 0043afc0 ["CALL", null, ["callee:00c57a90:8"]]
+ 0045de58 ["INT_ADD", "register:40f0:8", ["const:45de58:8", "const:4:8"]]
+ 0045de58 ["CALL", null, ["callee:00c57a90:8"]]
- 0043afc0 bytes 20801e94
+ 0045de58 bytes 0ee71f94
- 0043afc8 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045de60 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043afc8 bytes 683d0090
+ 0045de60 bytes 284000d0
- 0043afcc ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0043afcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043afcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043afcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045de64 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 0045de64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045de64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045de64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043afcc bytes 08c13691
+ 0045de64 bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f41aa86bfe7e0239cb6a91a041b21e7a"></a>

### [`0043afe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043afe0.md) → [`0045de78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de78.md) FUN_0045de78

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0045de84",
      "incomplete_value": false,
      "site": "0045de84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043afec",
      "incomplete_value": false,
      "site": "0043afec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "0045de84",
      "DATA",
      [
        "storage",
        "00be6db0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045de84",
      "DATA",
      [
        "storage",
        "00c63970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043afe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043afe0.md#insn-0043afe4) · [`0043afe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043afe0.md#insn-0043afe8)
- 新版 [`0045de7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de78.md#insn-0045de7c) · [`0045de80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de78.md#insn-0045de80)

~~~diff
- 0043afe4 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0045de7c ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0043afe4 bytes 693d0090
+ 0045de7c bytes 294000d0
- 0043afe8 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0043afe8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043afe8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043afe8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045de80 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 0045de80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045de80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045de80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043afe8 bytes 29c13691
+ 0045de80 bytes 29c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f572c3d42a7e676ad0fff2611a54e02b"></a>

### [`0043b598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b598.md) → [`0045e430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e430.md) FUN_0045e430

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0045e454",
      "incomplete_value": false,
      "site": "0045e454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b5bc",
      "incomplete_value": false,
      "site": "0043b5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      "0045e454",
      "DATA",
      [
        "storage",
        "00be6e30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045e454",
      "DATA",
      [
        "storage",
        "00c639f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b598.md#insn-0043b5ac) · [`0043b5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b598.md#insn-0043b5b4) · [`0043b5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b598.md#insn-0043b5b8)
- 新版 [`0045e444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e430.md#insn-0045e444) · [`0045e44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e430.md#insn-0045e44c) · [`0045e450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e430.md#insn-0045e450)

~~~diff
- 0043b5ac ["INT_ADD", "register:40f0:8", ["const:43b5ac:8", "const:4:8"]]
- 0043b5ac ["CALL", null, ["callee:00c57a90:8"]]
+ 0045e444 ["INT_ADD", "register:40f0:8", ["const:45e444:8", "const:4:8"]]
+ 0045e444 ["CALL", null, ["callee:00c57a90:8"]]
- 0043b5ac bytes a57e1e94
+ 0045e444 bytes 93e51f94
- 0043b5b4 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045e44c ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043b5b4 bytes 483d00f0
+ 0045e44c bytes 284000b0
- 0043b5b8 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 0043b5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043b5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043b5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045e450 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0045e450 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045e450 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045e450 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043b5b8 bytes 08c13891
+ 0045e450 bytes 08c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44469002994233b99344c5eb1948e608"></a>

### [`0043b5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b5cc.md) → [`0045e464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e464.md) FUN_0045e464

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0045e470",
      "incomplete_value": false,
      "site": "0045e470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b5d8",
      "incomplete_value": false,
      "site": "0043b5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      "0045e470",
      "DATA",
      [
        "storage",
        "00be6e30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045e470",
      "DATA",
      [
        "storage",
        "00c639f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b5cc.md#insn-0043b5d0) · [`0043b5d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b5cc.md#insn-0043b5d4)
- 新版 [`0045e468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e464.md#insn-0045e468) · [`0045e46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e464.md#insn-0045e46c)

~~~diff
- 0043b5d0 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0045e468 ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0043b5d0 bytes 493d00f0
+ 0045e468 bytes 294000b0
- 0043b5d4 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 0043b5d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043b5d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043b5d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045e46c ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0045e46c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045e46c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045e46c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043b5d4 bytes 29c13891
+ 0045e46c bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78564e3411728f53497e1c992c79a313"></a>

### [`0043b5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b5e8.md) → [`0045e480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e480.md) FUN_0045e480

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0073e6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e6dc.md) [`0073ed78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ed78.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`007689e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007689e8.md) [`00769084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769084.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_value, call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 86.90% / 新版 86.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_target` 2件, `store_destination` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045e588",
      "incomplete_value": false,
      "site": "0045e588",
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
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b6f0",
      "incomplete_value": false,
      "site": "0043b6f0",
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
            "const:cb0:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045e58c",
      "incomplete_value": false,
      "site": "0045e58c",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b6f4",
      "incomplete_value": false,
      "site": "0043b6f4",
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
            "const:cc8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0045e4e8",
      "incomplete_value": true,
      "site": "0045e4e8",
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
      "definition_site": "0043b650",
      "incomplete_value": true,
      "site": "0043b650",
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
      "0045e4bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073e6dc"
      ]
    ],
    [
      "unmatched:0043b628",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "0045e4c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073ed78"
      ]
    ]
  ],
  "added": [
    [
      "0045e4bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007689e8"
      ]
    ],
    [
      "0045e4c0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "0045e4c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00769084"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b5e8.md#insn-0043b624) · [`0043b628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b5e8.md#insn-0043b628) · [`0043b62c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b5e8.md#insn-0043b62c)
- 新版 [`0045e4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e480.md#insn-0045e4bc) · [`0045e4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e480.md#insn-0045e4c4)

~~~diff
- 0043b624 ["INT_ADD", "register:40f0:8", ["const:43b624:8", "const:4:8"]]
- 0043b624 ["CALL", null, ["ram:73e6dc:8"]]
+ 0045e4bc ["INT_ADD", "register:40f0:8", ["const:45e4bc:8", "const:4:8"]]
+ 0045e4bc ["CALL", null, ["ram:7689e8:8"]]
- 0043b624 bytes 2e0c0c94
+ 0045e4bc bytes 4b290c94
- 0043b628 ["INT_ADD", "register:40f0:8", ["const:43b628:8", "const:4:8"]]
- 0043b628 ["CALL", null, ["callee:008514b8:8"]]
- 0043b628 bytes d68f0f94
- 0043b62c ["INT_ADD", "register:40f0:8", ["const:43b62c:8", "const:4:8"]]
- 0043b62c ["CALL", null, ["ram:73ed78:8"]]
+ 0045e4c4 ["INT_ADD", "register:40f0:8", ["const:45e4c4:8", "const:4:8"]]
+ 0045e4c4 ["CALL", null, ["ram:769084:8"]]
- 0043b62c bytes d30d0c94
+ 0045e4c4 bytes f02a0c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-571b14e879120383c59c9bcbe8fcec36"></a>

### [`0043b790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b790.md) → [`0045e628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e628.md) FUN_0045e628

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0043c490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c490.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0043bd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bd0c.md) [`00574ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0045f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f328.md) · 呼出先 6件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0045eba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eba4.md) [`00597e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e8c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045e6d4",
      "incomplete_value": true,
      "site": "0045e6e4",
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
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:e59:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b83c",
      "incomplete_value": true,
      "site": "0043b84c",
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
                "const:42b:8"
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
      "definition_site": "0045e74c",
      "incomplete_value": true,
      "site": "0045e74c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b8b4",
      "incomplete_value": true,
      "site": "0043b8b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c0:8"
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
      "definition_site": "0045e7e8",
      "incomplete_value": true,
      "site": "0045e800",
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
                "const:620:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b950",
      "incomplete_value": true,
      "site": "0043b968",
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045e6d4",
      "READ",
      [
        "storage",
        "002a542b",
        null,
        "string"
      ]
    ],
    [
      "0045e738",
      "READ",
      [
        "storage",
        "002918c0",
        null,
        "string"
      ]
    ],
    [
      "0045e7e8",
      "READ",
      [
        "storage",
        "002b1010",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0045e6d4",
      "READ",
      [
        "storage",
        "002b5e59",
        null,
        "string"
      ]
    ],
    [
      "0045e738",
      "READ",
      [
        "storage",
        "002a0ed9",
        null,
        "string"
      ]
    ],
    [
      "0045e7e8",
      "READ",
      [
        "storage",
        "002c2620",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b790.md#insn-0043b7f0) · [`0043b810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b790.md#insn-0043b810) · [`0043b824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b790.md#insn-0043b824)
- 新版 [`0045e688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e628.md#insn-0045e688) · [`0045e6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e628.md#insn-0045e6a8) · [`0045e6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e628.md#insn-0045e6bc)

~~~diff
- 0043b7f0 ["INT_ADD", "register:40f0:8", ["const:43b7f0:8", "const:4:8"]]
- 0043b7f0 ["CALL", null, ["callee:0044104c:8"]]
+ 0045e688 ["INT_ADD", "register:40f0:8", ["const:45e688:8", "const:4:8"]]
+ 0045e688 ["CALL", null, ["callee:0044104c:8"]]
- 0043b7f0 bytes 578bff97
+ 0045e688 bytes 718aff97
- 0043b810 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043b810 ["INT_ADD", "register:40f0:8", ["const:43b810:8", "const:4:8"]]
- 0043b810 ["CALLIND", null, ["register:0:8"]]
+ 0045e6a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045e6a8 ["INT_ADD", "register:40f0:8", ["const:45e6a8:8", "const:4:8"]]
+ 0045e6a8 ["CALLIND", null, ["register:0:8"]]
- 0043b810 bytes 00013fd6
+ 0045e6a8 bytes 00013fd6
- 0043b824 ["INT_ADD", "register:40f0:8", ["const:43b824:8", "const:4:8"]]
- 0043b824 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0045e6bc ["INT_ADD", "register:40f0:8", ["const:45e6bc:8", "const:4:8"]]
+ 0045e6bc ["CALL", null, ["callee:00c57ab0:8"]]
- 0043b824 bytes 0f7e1e94
+ 0045e6bc bytes fde41f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef3cc03755efacdfc0388e9aed43c438"></a>

### [`0043bd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bd0c.md) → [`0045eba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eba4.md) FUN_0045eba4

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0043b790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b790.md) · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00574ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0045e628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e628.md) · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00597e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e8c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.03% / 新版 82.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045ebf0",
      "incomplete_value": true,
      "site": "0045ebf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9fd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043bd58",
      "incomplete_value": true,
      "site": "0043bd58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c3f:8"
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
      "definition_site": "0045ebf4",
      "incomplete_value": true,
      "site": "0045ebf4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0043bd5c",
      "incomplete_value": true,
      "site": "0043bd5c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045ec5c",
      "incomplete_value": true,
      "site": "0045ec5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:e6b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043bdc4",
      "incomplete_value": true,
      "site": "0043bdc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:43d:8"
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
      "0045ebe0",
      "READ",
      [
        "storage",
        "00298c3f",
        null,
        "string"
      ]
    ],
    [
      "0045ebe4",
      "READ",
      [
        "storage",
        "00298c45",
        null,
        "string"
      ]
    ],
    [
      "0045ec48",
      "READ",
      [
        "storage",
        "002a543d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0045ebe0",
      "READ",
      [
        "storage",
        "002a89fd",
        null,
        "string"
      ]
    ],
    [
      "0045ebe4",
      "READ",
      [
        "storage",
        "002a8a03",
        null,
        "string"
      ]
    ],
    [
      "0045ec48",
      "READ",
      [
        "storage",
        "002b5e6b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043bd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bd0c.md#insn-0043bd3c) · [`0043bd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bd0c.md#insn-0043bd40) · [`0043bd44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bd0c.md#insn-0043bd44)
- 新版 [`0045ebd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eba4.md#insn-0045ebd4) · [`0045ebd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eba4.md#insn-0045ebd8)

~~~diff
- 0043bd3c ["COPY", "register:4048:8", ["const:298000:8"]]
+ 0045ebd4 ["COPY", "register:4048:8", ["const:2a8000:8"]]
- 0043bd3c bytes e9f2ffb0
+ 0045ebd4 bytes 49f2ffd0
- 0043bd40 ["COPY", "tmp:0:8", ["const:c3f:8"]]
- 0043bd40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043bd40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043bd40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045ebd8 ["COPY", "tmp:0:8", ["const:9fd:8"]]
+ 0045ebd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ebd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ebd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043bd40 bytes 29fd3091
+ 0045ebd8 bytes 29f52791
- 0043bd44 ["COPY", "register:40b0:8", ["register:4000:8"]]
- 0043bd44 bytes f60300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aad3c4d5435935124845c27570e3d7ee"></a>

### [`0043c03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c03c.md) → [`0045eed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eed4.md) FUN_0045eed4

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0043bf84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bf84.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377f0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)
- 新版 呼出元 1件 [`0045ee1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045ee1c.md) · 呼出先 12件 [`0045a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a688.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045ef78",
      "incomplete_value": true,
      "site": "0045ef7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c0e0",
      "incomplete_value": true,
      "site": "0043c0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045ef14",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0043c07c",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045ef54",
      "incomplete_value": true,
      "site": "0045ef5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:858:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c0bc",
      "incomplete_value": true,
      "site": "0043c0c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0045ef14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ],
    [
      "0045ef50",
      "PARAM",
      [
        "storage",
        "004377f0",
        null,
        null
      ]
    ],
    [
      "0045ef54",
      "READ",
      [
        "storage",
        "00c1ae68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045ef14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ],
    [
      "0045ef50",
      "PARAM",
      [
        "storage",
        "0045a688",
        null,
        null
      ]
    ],
    [
      "0045ef54",
      "READ",
      [
        "storage",
        "00c9a858",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c03c.md#insn-0043c07c) · [`0043c0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c03c.md#insn-0043c0c4) · [`0043c0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c03c.md#insn-0043c0d0)
- 新版 [`0045ef14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eed4.md#insn-0045ef14) · [`0045ef5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eed4.md#insn-0045ef5c) · [`0045ef68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eed4.md#insn-0045ef68)

~~~diff
- 0043c07c ["INT_ADD", "register:40f0:8", ["const:43c07c:8", "const:4:8"]]
- 0043c07c ["CALL", null, ["ram:bdb4a0:8"]]
+ 0045ef14 ["INT_ADD", "register:40f0:8", ["const:45ef14:8", "const:4:8"]]
+ 0045ef14 ["CALL", null, ["ram:c57ef0:8"]]
- 0043c07c bytes 097d1e94
+ 0045ef14 bytes f7e31f94
- 0043c0c4 ["INT_ADD", "register:40f0:8", ["const:43c0c4:8", "const:4:8"]]
- 0043c0c4 ["CALL", null, ["callee:00c57f30:8"]]
+ 0045ef5c ["INT_ADD", "register:40f0:8", ["const:45ef5c:8", "const:4:8"]]
+ 0045ef5c ["CALL", null, ["callee:00c57f30:8"]]
- 0043c0c4 bytes 077d1e94
+ 0045ef5c bytes f5e31f94
- 0043c0d0 ["INT_ADD", "register:40f0:8", ["const:43c0d0:8", "const:4:8"]]
- 0043c0d0 ["CALL", null, ["ram:bdb4f0:8"]]
+ 0045ef68 ["INT_ADD", "register:40f0:8", ["const:45ef68:8", "const:4:8"]]
+ 0045ef68 ["CALL", null, ["ram:c57f40:8"]]
- 0043c0d0 bytes 087d1e94
+ 0045ef68 bytes f6e31f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c7282c3b02cede0bac1e4c502a1b81c"></a>

### [`0043c164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c164.md) → [`0045effc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045effc.md) FUN_0045effc

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043cc04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cc04.md) · 呼出先 6件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)
- 新版 呼出元 1件 [`0045fa9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fa9c.md) · 呼出先 6件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.15% / 新版 98.15%

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
      "site": "0045f040",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0043c1a8",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
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
      "0045f040",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ]
  ],
  "added": [
    [
      "0045f040",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c1a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c164.md#insn-0043c1a8) · [`0043c190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c164.md#insn-0043c190) · [`0043c1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c164.md#insn-0043c1f0)
- 新版 [`0045f040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045effc.md#insn-0045f040) · [`0045f028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045effc.md#insn-0045f028) · [`0045f088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045effc.md#insn-0045f088)

~~~diff
- 0043c1a8 ["INT_ADD", "register:40f0:8", ["const:43c1a8:8", "const:4:8"]]
- 0043c1a8 ["CALL", null, ["ram:bdb4a0:8"]]
+ 0045f040 ["INT_ADD", "register:40f0:8", ["const:45f040:8", "const:4:8"]]
+ 0045f040 ["CALL", null, ["ram:c57ef0:8"]]
- 0043c1a8 bytes be7c1e94
+ 0045f040 bytes ace31f94
- 0043c190 ["INT_ADD", "register:40f0:8", ["const:43c190:8", "const:4:8"]]
- 0043c190 ["CALL", null, ["callee:00c57ce0:8"]]
+ 0045f028 ["INT_ADD", "register:40f0:8", ["const:45f028:8", "const:4:8"]]
+ 0045f028 ["CALL", null, ["callee:00c57ce0:8"]]
- 0043c190 bytes 407c1e94
+ 0045f028 bytes 2ee31f94
- 0043c1f0 ["INT_ADD", "register:40f0:8", ["const:43c1f0:8", "const:4:8"]]
- 0043c1f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0045f088 ["INT_ADD", "register:40f0:8", ["const:45f088:8", "const:4:8"]]
+ 0045f088 ["CALL", null, ["callee:00c57f80:8"]]
- 0043c1f0 bytes d07c1e94
+ 0045f088 bytes bee31f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a1a5f0cbb8338cd6e4a81b4ef3081b9"></a>

### [`0043c260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c260.md) → [`0045f0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f0f8.md) FUN_0045f0f8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045f104",
      "incomplete_value": false,
      "site": "0045f110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c26c",
      "incomplete_value": false,
      "site": "0043c278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "0045f110",
      "DATA",
      [
        "storage",
        "00be6f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f110",
      "DATA",
      [
        "storage",
        "00c63b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c260.md#insn-0043c268) · [`0043c26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c260.md#insn-0043c26c)
- 新版 [`0045f100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f0f8.md#insn-0045f100) · [`0045f104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f0f8.md#insn-0045f104)

~~~diff
- 0043c268 ["COPY", "register:4050:8", ["const:be6000:8"]]
+ 0045f100 ["COPY", "register:4050:8", ["const:c63000:8"]]
- 0043c268 bytes 4a3d00d0
+ 0045f100 bytes 2a400090
- 0043c26c ["COPY", "tmp:0:8", ["const:f58:8"]]
- 0043c26c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043c26c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043c26c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045f104 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 0045f104 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f104 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f104 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043c26c bytes 4a613d91
+ 0045f104 bytes 4a612c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e41ae0cd53cde58946531652f7f674a"></a>

### [`0043c2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c2a4.md) → [`0045f13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f13c.md) FUN_0045f13c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0045f154",
      "incomplete_value": false,
      "site": "0045f160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c2bc",
      "incomplete_value": false,
      "site": "0043c2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "0045f160",
      "DATA",
      [
        "storage",
        "00be6f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f160",
      "DATA",
      [
        "storage",
        "00c63b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c2a4.md#insn-0043c2b8) · [`0043c2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c2a4.md#insn-0043c2bc) · [`0043c2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c2a4.md#insn-0043c2ec)
- 新版 [`0045f150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f13c.md#insn-0045f150) · [`0045f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f13c.md#insn-0045f154) · [`0045f184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f13c.md#insn-0045f184)

~~~diff
- 0043c2b8 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045f150 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043c2b8 bytes 483d00d0
+ 0045f150 bytes 28400090
- 0043c2bc ["COPY", "tmp:0:8", ["const:f58:8"]]
- 0043c2bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c2bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c2bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f154 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 0045f154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c2bc bytes 08613d91
+ 0045f154 bytes 08612c91
- 0043c2ec ["COPY", "register:0:8", ["register:4040:8"]]
- 0043c2ec ["INT_ADD", "register:40f0:8", ["const:43c2ec:8", "const:4:8"]]
- 0043c2ec ["CALLIND", null, ["register:0:8"]]
+ 0045f184 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f184 ["INT_ADD", "register:40f0:8", ["const:45f184:8", "const:4:8"]]
+ 0045f184 ["CALLIND", null, ["register:0:8"]]
- 0043c2ec bytes 00013fd6
+ 0045f184 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-801d9b0f40fc6baae2ada2cb1deb626f"></a>

### [`0043c300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c300.md) → [`0045f198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f198.md) FUN_0045f198

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045f1c4",
      "incomplete_value": false,
      "site": "0045f1c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c32c",
      "incomplete_value": false,
      "site": "0043c32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "0045f1c4",
      "DATA",
      [
        "storage",
        "00be6f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f1c4",
      "DATA",
      [
        "storage",
        "00c63b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c300.md#insn-0043c314) · [`0043c320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c300.md#insn-0043c320) · [`0043c324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c300.md#insn-0043c324)
- 新版 [`0045f1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f198.md#insn-0045f1ac) · [`0045f1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f198.md#insn-0045f1b8) · [`0045f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f198.md#insn-0045f1bc)

~~~diff
- 0043c314 ["INT_ADD", "register:40f0:8", ["const:43c314:8", "const:4:8"]]
- 0043c314 ["CALL", null, ["callee:00c57a90:8"]]
+ 0045f1ac ["INT_ADD", "register:40f0:8", ["const:45f1ac:8", "const:4:8"]]
+ 0045f1ac ["CALL", null, ["callee:00c57a90:8"]]
- 0043c314 bytes 4b7b1e94
+ 0045f1ac bytes 39e21f94
- 0043c320 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045f1b8 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043c320 bytes 483d00d0
+ 0045f1b8 bytes 28400090
- 0043c324 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 0043c324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f1bc ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 0045f1bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f1bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f1bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c324 bytes 08613d91
+ 0045f1bc bytes 08612c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7521a3cbb1b931d779c66dcb76d0854"></a>

### [`0043c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c390.md) → [`0045f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f228.md) FUN_0045f228

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0045f248",
      "incomplete_value": false,
      "site": "0045f248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c3b0",
      "incomplete_value": false,
      "site": "0043c3b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "0045f248",
      "DATA",
      [
        "storage",
        "00be6f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f248",
      "DATA",
      [
        "storage",
        "00c63b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c390.md#insn-0043c3a8) · [`0043c3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c390.md#insn-0043c3ac) · [`0043c3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c390.md#insn-0043c3cc)
- 新版 [`0045f240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f228.md#insn-0045f240) · [`0045f244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f228.md#insn-0045f244) · [`0045f264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f228.md#insn-0045f264)

~~~diff
- 0043c3a8 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045f240 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043c3a8 bytes 483d00d0
+ 0045f240 bytes 28400090
- 0043c3ac ["COPY", "tmp:0:8", ["const:f58:8"]]
- 0043c3ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c3ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c3ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f244 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 0045f244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c3ac bytes 08613d91
+ 0045f244 bytes 08612c91
- 0043c3cc ["COPY", "register:0:8", ["register:4040:8"]]
- 0043c3cc ["INT_ADD", "register:40f0:8", ["const:43c3cc:8", "const:4:8"]]
- 0043c3cc ["CALLIND", null, ["register:0:8"]]
+ 0045f264 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f264 ["INT_ADD", "register:40f0:8", ["const:45f264:8", "const:4:8"]]
+ 0045f264 ["CALLIND", null, ["register:0:8"]]
- 0043c3cc bytes 00013fd6
+ 0045f264 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd68f0120524dd68a62652911c2ebc95"></a>

### [`0043c490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c490.md) → [`0045f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f328.md) FUN_0045f328

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0043b790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b790.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0045e628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e628.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045f3d4",
      "incomplete_value": true,
      "site": "0045f3d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d63:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c53c",
      "incomplete_value": true,
      "site": "0043c53c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:653:8"
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
      "0045f3c0",
      "READ",
      [
        "storage",
        "00292653",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0045f3c0",
      "READ",
      [
        "storage",
        "002a1d63",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c490.md#insn-0043c4e8) · [`0043c514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c490.md#insn-0043c514) · [`0043c51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c490.md#insn-0043c51c)
- 新版 [`0045f380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f328.md#insn-0045f380) · [`0045f3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f328.md#insn-0045f3ac) · [`0045f3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f328.md#insn-0045f3b4)

~~~diff
- 0043c4e8 ["INT_ADD", "register:40f0:8", ["const:43c4e8:8", "const:4:8"]]
- 0043c4e8 ["CALL", null, ["callee:0044104c:8"]]
+ 0045f380 ["INT_ADD", "register:40f0:8", ["const:45f380:8", "const:4:8"]]
+ 0045f380 ["CALL", null, ["callee:0044104c:8"]]
- 0043c4e8 bytes 1988ff97
+ 0045f380 bytes 3387ff97
- 0043c514 ["INT_ADD", "register:40f0:8", ["const:43c514:8", "const:4:8"]]
- 0043c514 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0045f3ac ["INT_ADD", "register:40f0:8", ["const:45f3ac:8", "const:4:8"]]
+ 0045f3ac ["CALL", null, ["callee:00c57ab0:8"]]
- 0043c514 bytes d37a1e94
+ 0045f3ac bytes c1e11f94
- 0043c51c ["COPY", "register:4048:8", ["const:292000:8"]]
+ 0045f3b4 ["COPY", "register:4048:8", ["const:2a1000:8"]]
- 0043c51c bytes a9f2ffd0
+ 0045f3b4 bytes 09f2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ab539758031eec553422932bb89f31a"></a>

### [`0043c754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c754.md) → [`0045f5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f5ec.md) FUN_0045f5ec

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045f5f8",
      "incomplete_value": false,
      "site": "0045f604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c760",
      "incomplete_value": false,
      "site": "0043c76c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
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
      "0045f604",
      "DATA",
      [
        "storage",
        "00be6fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f604",
      "DATA",
      [
        "storage",
        "00c63b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c75c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c754.md#insn-0043c75c) · [`0043c760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c754.md#insn-0043c760)
- 新版 [`0045f5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f5ec.md#insn-0045f5f4) · [`0045f5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f5ec.md#insn-0045f5f8)

~~~diff
- 0043c75c ["COPY", "register:4050:8", ["const:be6000:8"]]
+ 0045f5f4 ["COPY", "register:4050:8", ["const:c63000:8"]]
- 0043c75c bytes 4a3d00d0
+ 0045f5f4 bytes 2a400090
- 0043c760 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 0043c760 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043c760 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043c760 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045f5f8 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 0045f5f8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f5f8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f5f8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043c760 bytes 4a613f91
+ 0045f5f8 bytes 4a612e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0ddbb16274f2e220620d7b1f35cc5e6"></a>

### [`0043c798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c798.md) → [`0045f630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f630.md) FUN_0045f630

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0045f648",
      "incomplete_value": false,
      "site": "0045f654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c7b0",
      "incomplete_value": false,
      "site": "0043c7bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
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
      "0045f654",
      "DATA",
      [
        "storage",
        "00be6fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f654",
      "DATA",
      [
        "storage",
        "00c63b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c798.md#insn-0043c7ac) · [`0043c7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c798.md#insn-0043c7b0) · [`0043c7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c798.md#insn-0043c7e0)
- 新版 [`0045f644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f630.md#insn-0045f644) · [`0045f648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f630.md#insn-0045f648) · [`0045f678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f630.md#insn-0045f678)

~~~diff
- 0043c7ac ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045f644 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043c7ac bytes 483d00d0
+ 0045f644 bytes 28400090
- 0043c7b0 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 0043c7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f648 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 0045f648 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f648 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f648 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c7b0 bytes 08613f91
+ 0045f648 bytes 08612e91
- 0043c7e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043c7e0 ["INT_ADD", "register:40f0:8", ["const:43c7e0:8", "const:4:8"]]
- 0043c7e0 ["CALLIND", null, ["register:0:8"]]
+ 0045f678 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f678 ["INT_ADD", "register:40f0:8", ["const:45f678:8", "const:4:8"]]
+ 0045f678 ["CALLIND", null, ["register:0:8"]]
- 0043c7e0 bytes 00013fd6
+ 0045f678 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-215caa05e3a98fc29b1d0d72612687c6"></a>

### [`0043c7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c7f4.md) → [`0045f68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f68c.md) FUN_0045f68c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045f6b8",
      "incomplete_value": false,
      "site": "0045f6b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c820",
      "incomplete_value": false,
      "site": "0043c820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
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
      "0045f6b8",
      "DATA",
      [
        "storage",
        "00be6fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f6b8",
      "DATA",
      [
        "storage",
        "00c63b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c7f4.md#insn-0043c808) · [`0043c814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c7f4.md#insn-0043c814) · [`0043c818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c7f4.md#insn-0043c818)
- 新版 [`0045f6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f68c.md#insn-0045f6a0) · [`0045f6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f68c.md#insn-0045f6ac) · [`0045f6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f68c.md#insn-0045f6b0)

~~~diff
- 0043c808 ["INT_ADD", "register:40f0:8", ["const:43c808:8", "const:4:8"]]
- 0043c808 ["CALL", null, ["callee:00c57a90:8"]]
+ 0045f6a0 ["INT_ADD", "register:40f0:8", ["const:45f6a0:8", "const:4:8"]]
+ 0045f6a0 ["CALL", null, ["callee:00c57a90:8"]]
- 0043c808 bytes 0e7a1e94
+ 0045f6a0 bytes fce01f94
- 0043c814 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045f6ac ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043c814 bytes 483d00d0
+ 0045f6ac bytes 28400090
- 0043c818 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 0043c818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f6b0 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 0045f6b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f6b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f6b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c818 bytes 08613f91
+ 0045f6b0 bytes 08612e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30fd9cbdd373a7a29651a9190bade5e6"></a>

### [`0043c87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c87c.md) → [`0045f714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f714.md) FUN_0045f714

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045f730",
      "incomplete_value": false,
      "site": "0045f730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c898",
      "incomplete_value": false,
      "site": "0043c898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
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
      "0045f730",
      "DATA",
      [
        "storage",
        "00be6fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f730",
      "DATA",
      [
        "storage",
        "00c63b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c87c.md#insn-0043c890) · [`0043c894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c87c.md#insn-0043c894) · [`0043c8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c87c.md#insn-0043c8b8)
- 新版 [`0045f728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f714.md#insn-0045f728) · [`0045f72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f714.md#insn-0045f72c) · [`0045f750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f714.md#insn-0045f750)

~~~diff
- 0043c890 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0045f728 ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0043c890 bytes 493d00d0
+ 0045f728 bytes 29400090
- 0043c894 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 0043c894 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043c894 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043c894 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045f72c ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 0045f72c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045f72c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045f72c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043c894 bytes 29613f91
+ 0045f72c bytes 29612e91
- 0043c8b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0043c8b8 ["INT_ADD", "register:40f0:8", ["const:43c8b8:8", "const:4:8"]]
- 0043c8b8 ["CALLIND", null, ["register:0:8"]]
+ 0045f750 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045f750 ["INT_ADD", "register:40f0:8", ["const:45f750:8", "const:4:8"]]
+ 0045f750 ["CALLIND", null, ["register:0:8"]]
- 0043c8b8 bytes 20013fd6
+ 0045f750 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18ce162271bcb39e9d93d81b4ca043c9"></a>

### [`0043ca28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043ca28.md) → [`0045f8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f8c0.md) FUN_0045f8c0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "0045f8d4",
      "incomplete_value": false,
      "site": "0045f8d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ca3c",
      "incomplete_value": false,
      "site": "0043ca40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
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
      "0045f8d8",
      "DATA",
      [
        "storage",
        "00be7058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f8d8",
      "DATA",
      [
        "storage",
        "00c63c18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043ca38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043ca28.md#insn-0043ca38) · [`0043ca3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043ca28.md#insn-0043ca3c) · [`0043ca50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043ca28.md#insn-0043ca50)
- 新版 [`0045f8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f8c0.md#insn-0045f8d0) · [`0045f8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f8c0.md#insn-0045f8d4) · [`0045f8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f8c0.md#insn-0045f8e8)

~~~diff
- 0043ca38 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 0045f8d0 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043ca38 bytes 483d00f0
+ 0045f8d0 bytes 28400090
- 0043ca3c ["COPY", "tmp:0:8", ["const:58:8"]]
- 0043ca3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043ca3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043ca3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f8d4 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 0045f8d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f8d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f8d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043ca3c bytes 08610191
+ 0045f8d4 bytes 08613091
- 0043ca50 ["INT_ADD", "register:40f0:8", ["const:43ca50:8", "const:4:8"]]
- 0043ca50 ["CALL", null, ["callee:00c538e0:8"]]
+ 0045f8e8 ["INT_ADD", "register:40f0:8", ["const:45f8e8:8", "const:4:8"]]
+ 0045f8e8 ["CALL", null, ["callee:00c538e0:8"]]
- 0043ca50 bytes 10691e94
+ 0045f8e8 bytes fecf1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6f2c2f0707484032f337c716e5fb8d2"></a>

### [`0043ca84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043ca84.md) → [`0045f91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f91c.md) FUN_0045f91c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0045f934",
      "incomplete_value": false,
      "site": "0045f938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ca9c",
      "incomplete_value": false,
      "site": "0043caa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "0045f938",
      "DATA",
      [
        "storage",
        "00be7058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f938",
      "DATA",
      [
        "storage",
        "00c63c18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043ca98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043ca84.md#insn-0043ca98) · [`0043ca9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043ca84.md#insn-0043ca9c) · [`0043cab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043ca84.md#insn-0043cab0)
- 新版 [`0045f930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f91c.md#insn-0045f930) · [`0045f934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f91c.md#insn-0045f934) · [`0045f948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f91c.md#insn-0045f948)

~~~diff
- 0043ca98 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 0045f930 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043ca98 bytes 483d00f0
+ 0045f930 bytes 28400090
- 0043ca9c ["COPY", "tmp:0:8", ["const:58:8"]]
- 0043ca9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043ca9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043ca9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f934 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 0045f934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043ca9c bytes 08610191
+ 0045f934 bytes 08613091
- 0043cab0 ["INT_ADD", "register:40f0:8", ["const:43cab0:8", "const:4:8"]]
- 0043cab0 ["CALL", null, ["callee:00c538e0:8"]]
+ 0045f948 ["INT_ADD", "register:40f0:8", ["const:45f948:8", "const:4:8"]]
+ 0045f948 ["CALL", null, ["callee:00c538e0:8"]]
- 0043cab0 bytes f8681e94
+ 0045f948 bytes e6cf1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28e13709ffc03fcdfee6b077084e1cd6"></a>

### [`0043cae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cae0.md) → [`0045f978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f978.md) FUN_0045f978

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0045f99c",
      "incomplete_value": false,
      "site": "0045f99c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cb04",
      "incomplete_value": false,
      "site": "0043cb04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
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
      "0045f99c",
      "DATA",
      [
        "storage",
        "00be7058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f99c",
      "DATA",
      [
        "storage",
        "00c63c18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043caf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cae0.md#insn-0043caf4) · [`0043cafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cae0.md#insn-0043cafc) · [`0043cb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cae0.md#insn-0043cb00)
- 新版 [`0045f98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f978.md#insn-0045f98c) · [`0045f994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f978.md#insn-0045f994) · [`0045f998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f978.md#insn-0045f998)

~~~diff
- 0043caf4 ["INT_ADD", "register:40f0:8", ["const:43caf4:8", "const:4:8"]]
- 0043caf4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0045f98c ["INT_ADD", "register:40f0:8", ["const:45f98c:8", "const:4:8"]]
+ 0045f98c ["CALL", null, ["callee:00c57a90:8"]]
- 0043caf4 bytes 53791e94
+ 0045f98c bytes 41e01f94
- 0043cafc ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 0045f994 ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0043cafc bytes 493d00f0
+ 0045f994 bytes 29400090
- 0043cb00 ["COPY", "tmp:0:8", ["const:58:8"]]
- 0043cb00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043cb00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043cb00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045f998 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 0045f998 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045f998 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045f998 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043cb00 bytes 29610191
+ 0045f998 bytes 29613091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd29d53fc06d665b0d111ab2e7f760e3"></a>

### [`0043cb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cb30.md) → [`0045f9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f9c8.md) FUN_0045f9c8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

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
      "definition_site": "0045f9d4",
      "incomplete_value": false,
      "site": "0045f9d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cb3c",
      "incomplete_value": false,
      "site": "0043cb3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "0045f9d4",
      "DATA",
      [
        "storage",
        "00be7058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f9d4",
      "DATA",
      [
        "storage",
        "00c63c18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cb34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cb30.md#insn-0043cb34) · [`0043cb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cb30.md#insn-0043cb38) · [`0043cb58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cb30.md#insn-0043cb58)
- 新版 [`0045f9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f9c8.md#insn-0045f9cc) · [`0045f9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f9c8.md#insn-0045f9d0) · [`0045f9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f9c8.md#insn-0045f9f0)

~~~diff
- 0043cb34 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 0045f9cc ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0043cb34 bytes 493d00f0
+ 0045f9cc bytes 29400090
- 0043cb38 ["COPY", "tmp:0:8", ["const:58:8"]]
- 0043cb38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043cb38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043cb38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045f9d0 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 0045f9d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045f9d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045f9d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043cb38 bytes 29610191
+ 0045f9d0 bytes 29613091
- 0043cb58 ["INT_ADD", "register:40f0:8", ["const:43cb58:8", "const:4:8"]]
- 0043cb58 ["CALL", null, ["callee:00c538b0:8"]]
+ 0045f9f0 ["INT_ADD", "register:40f0:8", ["const:45f9f0:8", "const:4:8"]]
+ 0045f9f0 ["CALL", null, ["callee:00c538b0:8"]]
- 0043cb58 bytes c2681e94
+ 0045f9f0 bytes b0cf1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa9a8bc63c7d05c62e3cefddd7408034"></a>

### [`0043ccc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043ccc4.md) → [`0045fb5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fb5c.md) FUN_0045fb5c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045fb68",
      "incomplete_value": false,
      "site": "0045fb74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ccd0",
      "incomplete_value": false,
      "site": "0043ccdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "0045fb74",
      "DATA",
      [
        "storage",
        "00be70d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fb74",
      "DATA",
      [
        "storage",
        "00c63c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043ccc4.md#insn-0043cccc) · [`0043ccd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043ccc4.md#insn-0043ccd0)
- 新版 [`0045fb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fb5c.md#insn-0045fb64) · [`0045fb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fb5c.md#insn-0045fb68)

~~~diff
- 0043cccc ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 0045fb64 ["COPY", "register:4050:8", ["const:c63000:8"]]
- 0043cccc bytes 4a3d00f0
+ 0045fb64 bytes 2a400090
- 0043ccd0 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 0043ccd0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043ccd0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043ccd0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045fb68 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 0045fb68 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045fb68 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045fb68 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043ccd0 bytes 4a610391
+ 0045fb68 bytes 4a613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-702b6fe2e9a419eb539b383c091127b5"></a>

### [`0043cd08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cd08.md) → [`0045fba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fba0.md) FUN_0045fba0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0045fbb8",
      "incomplete_value": false,
      "site": "0045fbc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cd20",
      "incomplete_value": false,
      "site": "0043cd2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "0045fbc4",
      "DATA",
      [
        "storage",
        "00be70d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fbc4",
      "DATA",
      [
        "storage",
        "00c63c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cd08.md#insn-0043cd1c) · [`0043cd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cd08.md#insn-0043cd20) · [`0043cd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cd08.md#insn-0043cd50)
- 新版 [`0045fbb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fba0.md#insn-0045fbb4) · [`0045fbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fba0.md#insn-0045fbb8) · [`0045fbe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fba0.md#insn-0045fbe8)

~~~diff
- 0043cd1c ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 0045fbb4 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043cd1c bytes 483d00f0
+ 0045fbb4 bytes 28400090
- 0043cd20 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 0043cd20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043cd20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043cd20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045fbb8 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 0045fbb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fbb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fbb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043cd20 bytes 08610391
+ 0045fbb8 bytes 08613291
- 0043cd50 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043cd50 ["INT_ADD", "register:40f0:8", ["const:43cd50:8", "const:4:8"]]
- 0043cd50 ["CALLIND", null, ["register:0:8"]]
+ 0045fbe8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045fbe8 ["INT_ADD", "register:40f0:8", ["const:45fbe8:8", "const:4:8"]]
+ 0045fbe8 ["CALLIND", null, ["register:0:8"]]
- 0043cd50 bytes 00013fd6
+ 0045fbe8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-552771d1b59b9fcf9cf554f1bf0dd42a"></a>

### [`0043cd64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cd64.md) → [`0045fbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fbfc.md) FUN_0045fbfc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045fc28",
      "incomplete_value": false,
      "site": "0045fc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cd90",
      "incomplete_value": false,
      "site": "0043cd90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "0045fc28",
      "DATA",
      [
        "storage",
        "00be70d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fc28",
      "DATA",
      [
        "storage",
        "00c63c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cd78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cd64.md#insn-0043cd78) · [`0043cd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cd64.md#insn-0043cd84) · [`0043cd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cd64.md#insn-0043cd88)
- 新版 [`0045fc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fbfc.md#insn-0045fc10) · [`0045fc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fbfc.md#insn-0045fc1c) · [`0045fc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fbfc.md#insn-0045fc20)

~~~diff
- 0043cd78 ["INT_ADD", "register:40f0:8", ["const:43cd78:8", "const:4:8"]]
- 0043cd78 ["CALL", null, ["callee:00c57a90:8"]]
+ 0045fc10 ["INT_ADD", "register:40f0:8", ["const:45fc10:8", "const:4:8"]]
+ 0045fc10 ["CALL", null, ["callee:00c57a90:8"]]
- 0043cd78 bytes b2781e94
+ 0045fc10 bytes a0df1f94
- 0043cd84 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 0045fc1c ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043cd84 bytes 483d00f0
+ 0045fc1c bytes 28400090
- 0043cd88 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 0043cd88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043cd88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043cd88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045fc20 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 0045fc20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fc20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fc20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043cd88 bytes 08610391
+ 0045fc20 bytes 08613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-273a5c120e18b2d10caabf0aea5691d0"></a>

### [`0043cdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cdec.md) → [`0045fc84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fc84.md) FUN_0045fc84

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045fca0",
      "incomplete_value": false,
      "site": "0045fca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ce08",
      "incomplete_value": false,
      "site": "0043ce08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "0045fca0",
      "DATA",
      [
        "storage",
        "00be70d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fca0",
      "DATA",
      [
        "storage",
        "00c63c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043ce00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cdec.md#insn-0043ce00) · [`0043ce04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cdec.md#insn-0043ce04) · [`0043ce28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cdec.md#insn-0043ce28)
- 新版 [`0045fc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fc84.md#insn-0045fc98) · [`0045fc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fc84.md#insn-0045fc9c) · [`0045fcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fc84.md#insn-0045fcc0)

~~~diff
- 0043ce00 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 0045fc98 ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0043ce00 bytes 493d00f0
+ 0045fc98 bytes 29400090
- 0043ce04 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 0043ce04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043ce04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043ce04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045fc9c ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 0045fc9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fc9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fc9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043ce04 bytes 29610391
+ 0045fc9c bytes 29613291
- 0043ce28 ["COPY", "register:0:8", ["register:4048:8"]]
- 0043ce28 ["INT_ADD", "register:40f0:8", ["const:43ce28:8", "const:4:8"]]
- 0043ce28 ["CALLIND", null, ["register:0:8"]]
+ 0045fcc0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045fcc0 ["INT_ADD", "register:40f0:8", ["const:45fcc0:8", "const:4:8"]]
+ 0045fcc0 ["CALLIND", null, ["register:0:8"]]
- 0043ce28 bytes 20013fd6
+ 0045fcc0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e05c6b34364973f95a31aa59d0922adf"></a>

### [`0043cf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cf30.md) → [`0045fdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fdc8.md) FUN_0045fdc8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045fdd4",
      "incomplete_value": false,
      "site": "0045fde0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cf3c",
      "incomplete_value": false,
      "site": "0043cf48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "0045fde0",
      "DATA",
      [
        "storage",
        "00be7158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fde0",
      "DATA",
      [
        "storage",
        "00c63d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cf38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cf30.md#insn-0043cf38) · [`0043cf3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cf30.md#insn-0043cf3c)
- 新版 [`0045fdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fdc8.md#insn-0045fdd0) · [`0045fdd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fdc8.md#insn-0045fdd4)

~~~diff
- 0043cf38 ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 0045fdd0 ["COPY", "register:4050:8", ["const:c63000:8"]]
- 0043cf38 bytes 4a3d00f0
+ 0045fdd0 bytes 2a400090
- 0043cf3c ["COPY", "tmp:0:8", ["const:158:8"]]
- 0043cf3c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043cf3c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043cf3c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045fdd4 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 0045fdd4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045fdd4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045fdd4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043cf3c bytes 4a610591
+ 0045fdd4 bytes 4a613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e95f4481177c124e11a638b75821c13"></a>

### [`0043cf74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cf74.md) → [`0045fe0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe0c.md) FUN_0045fe0c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0045fe24",
      "incomplete_value": false,
      "site": "0045fe30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cf8c",
      "incomplete_value": false,
      "site": "0043cf98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "0045fe30",
      "DATA",
      [
        "storage",
        "00be7158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fe30",
      "DATA",
      [
        "storage",
        "00c63d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cf74.md#insn-0043cf88) · [`0043cf8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cf74.md#insn-0043cf8c) · [`0043cfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cf74.md#insn-0043cfbc)
- 新版 [`0045fe20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe0c.md#insn-0045fe20) · [`0045fe24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe0c.md#insn-0045fe24) · [`0045fe54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe0c.md#insn-0045fe54)

~~~diff
- 0043cf88 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 0045fe20 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043cf88 bytes 483d00f0
+ 0045fe20 bytes 28400090
- 0043cf8c ["COPY", "tmp:0:8", ["const:158:8"]]
- 0043cf8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043cf8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043cf8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045fe24 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 0045fe24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fe24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fe24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043cf8c bytes 08610591
+ 0045fe24 bytes 08613491
- 0043cfbc ["COPY", "register:0:8", ["register:4040:8"]]
- 0043cfbc ["INT_ADD", "register:40f0:8", ["const:43cfbc:8", "const:4:8"]]
- 0043cfbc ["CALLIND", null, ["register:0:8"]]
+ 0045fe54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045fe54 ["INT_ADD", "register:40f0:8", ["const:45fe54:8", "const:4:8"]]
+ 0045fe54 ["CALLIND", null, ["register:0:8"]]
- 0043cfbc bytes 00013fd6
+ 0045fe54 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-254125bc60b07c38ffa7e266b0b7804e"></a>

### [`0043cfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cfd0.md) → [`0045fe68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe68.md) FUN_0045fe68

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045fe94",
      "incomplete_value": false,
      "site": "0045fe94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cffc",
      "incomplete_value": false,
      "site": "0043cffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "0045fe94",
      "DATA",
      [
        "storage",
        "00be7158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fe94",
      "DATA",
      [
        "storage",
        "00c63d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cfe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cfd0.md#insn-0043cfe4) · [`0043cff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cfd0.md#insn-0043cff0) · [`0043cff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cfd0.md#insn-0043cff4)
- 新版 [`0045fe7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe68.md#insn-0045fe7c) · [`0045fe88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe68.md#insn-0045fe88) · [`0045fe8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe68.md#insn-0045fe8c)

~~~diff
- 0043cfe4 ["INT_ADD", "register:40f0:8", ["const:43cfe4:8", "const:4:8"]]
- 0043cfe4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0045fe7c ["INT_ADD", "register:40f0:8", ["const:45fe7c:8", "const:4:8"]]
+ 0045fe7c ["CALL", null, ["callee:00c57a90:8"]]
- 0043cfe4 bytes 17781e94
+ 0045fe7c bytes 05df1f94
- 0043cff0 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 0045fe88 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043cff0 bytes 483d00f0
+ 0045fe88 bytes 28400090
- 0043cff4 ["COPY", "tmp:0:8", ["const:158:8"]]
- 0043cff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043cff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043cff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045fe8c ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 0045fe8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fe8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fe8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043cff4 bytes 08610591
+ 0045fe8c bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-659d59f3a71687f30986ff0774c679a9"></a>

### [`0043d058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d058.md) → [`0045fef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fef0.md) FUN_0045fef0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045ff0c",
      "incomplete_value": false,
      "site": "0045ff0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d074",
      "incomplete_value": false,
      "site": "0043d074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "0045ff0c",
      "DATA",
      [
        "storage",
        "00be7158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ff0c",
      "DATA",
      [
        "storage",
        "00c63d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d058.md#insn-0043d06c) · [`0043d070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d058.md#insn-0043d070) · [`0043d094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d058.md#insn-0043d094)
- 新版 [`0045ff04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fef0.md#insn-0045ff04) · [`0045ff08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fef0.md#insn-0045ff08) · [`0045ff2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fef0.md#insn-0045ff2c)

~~~diff
- 0043d06c ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 0045ff04 ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0043d06c bytes 493d00d0
+ 0045ff04 bytes 29400090
- 0043d070 ["COPY", "tmp:0:8", ["const:158:8"]]
- 0043d070 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043d070 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043d070 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045ff08 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 0045ff08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ff08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ff08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043d070 bytes 29610591
+ 0045ff08 bytes 29613491
- 0043d094 ["COPY", "register:0:8", ["register:4048:8"]]
- 0043d094 ["INT_ADD", "register:40f0:8", ["const:43d094:8", "const:4:8"]]
- 0043d094 ["CALLIND", null, ["register:0:8"]]
+ 0045ff2c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045ff2c ["INT_ADD", "register:40f0:8", ["const:45ff2c:8", "const:4:8"]]
+ 0045ff2c ["CALLIND", null, ["register:0:8"]]
- 0043d094 bytes 20013fd6
+ 0045ff2c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcaf33e05aa2801d5bb97cf577da9448"></a>

### [`0043d1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d1f8.md) → [`00460090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460090.md) FUN_00460090

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "004600a4",
      "incomplete_value": false,
      "site": "004600a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d20c",
      "incomplete_value": false,
      "site": "0043d210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
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
      "004600a8",
      "DATA",
      [
        "storage",
        "00be71d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004600a8",
      "DATA",
      [
        "storage",
        "00c63d98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d1f8.md#insn-0043d204) · [`0043d208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d1f8.md#insn-0043d208) · [`0043d20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d1f8.md#insn-0043d20c)
- 新版 [`0046009c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460090.md#insn-0046009c) · [`004600a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460090.md#insn-004600a0) · [`004600a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460090.md#insn-004600a4)

~~~diff
- 0043d204 ["INT_ADD", "register:40f0:8", ["const:43d204:8", "const:4:8"]]
- 0043d204 ["CALL", null, ["callee:00c57a90:8"]]
+ 0046009c ["INT_ADD", "register:40f0:8", ["const:46009c:8", "const:4:8"]]
+ 0046009c ["CALL", null, ["callee:00c57a90:8"]]
- 0043d204 bytes 8f771e94
+ 0046009c bytes 7dde1f94
- 0043d208 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004600a0 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043d208 bytes 483d00d0
+ 004600a0 bytes 084000f0
- 0043d20c ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 0043d20c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043d20c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043d20c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004600a4 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 004600a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004600a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004600a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043d20c bytes 08610791
+ 004600a4 bytes 08613691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4646a0a91e898fee0dd7ac37c3d0ef87"></a>

### [`0043d21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d21c.md) → [`004600b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600b4.md) FUN_004600b4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004600b8",
      "incomplete_value": false,
      "site": "004600bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d220",
      "incomplete_value": false,
      "site": "0043d224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
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
      "004600bc",
      "DATA",
      [
        "storage",
        "00be71d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004600bc",
      "DATA",
      [
        "storage",
        "00c63d98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d21c.md#insn-0043d21c) · [`0043d220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d21c.md#insn-0043d220)
- 新版 [`004600b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600b4.md#insn-004600b4) · [`004600b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600b4.md#insn-004600b8)

~~~diff
- 0043d21c ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004600b4 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043d21c bytes 483d00d0
+ 004600b4 bytes 084000f0
- 0043d220 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 0043d220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043d220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043d220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004600b8 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 004600b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004600b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004600b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043d220 bytes 08610791
+ 004600b8 bytes 08613691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44c475d3affeb57d171b576673630f3c"></a>

### [`0043d234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d234.md) → [`004600cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600cc.md) FUN_004600cc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.77% / 新版 91.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004601f8",
      "incomplete_value": true,
      "site": "004601f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:e4f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d360",
      "incomplete_value": true,
      "site": "0043d360",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:421:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00460294",
      "incomplete_value": true,
      "site": "00460294",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0043d3fc",
      "incomplete_value": true,
      "site": "0043d3fc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00460284",
      "incomplete_value": true,
      "site": "00460294",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:698:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d3ec",
      "incomplete_value": true,
      "site": "0043d3fc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
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
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004601e8",
      "READ",
      [
        "storage",
        "002a5421",
        null,
        "string"
      ]
    ],
    [
      "00460230",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046023c",
      "READ",
      [
        "storage",
        "00c24bd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004601e8",
      "READ",
      [
        "storage",
        "002b5e4f",
        null,
        "string"
      ]
    ],
    [
      "00460230",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046023c",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d3fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d234.md#insn-0043d3fc) · [`0043d478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d234.md#insn-0043d478) · [`0043d524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d234.md#insn-0043d524)
- 新版 [`00460294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600cc.md#insn-00460294) · [`00460310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600cc.md#insn-00460310) · [`004603bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600cc.md#insn-004603bc)

~~~diff
- 0043d3fc ["COPY", "register:0:8", ["register:4040:8"]]
- 0043d3fc ["INT_ADD", "register:40f0:8", ["const:43d3fc:8", "const:4:8"]]
- 0043d3fc ["CALLIND", null, ["register:0:8"]]
+ 00460294 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00460294 ["INT_ADD", "register:40f0:8", ["const:460294:8", "const:4:8"]]
+ 00460294 ["CALLIND", null, ["register:0:8"]]
- 0043d3fc bytes 00013fd6
+ 00460294 bytes 00013fd6
- 0043d478 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043d478 ["INT_ADD", "register:40f0:8", ["const:43d478:8", "const:4:8"]]
- 0043d478 ["CALLIND", null, ["register:0:8"]]
+ 00460310 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00460310 ["INT_ADD", "register:40f0:8", ["const:460310:8", "const:4:8"]]
+ 00460310 ["CALLIND", null, ["register:0:8"]]
- 0043d478 bytes 00013fd6
+ 00460310 bytes 00013fd6
- 0043d524 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043d524 ["INT_ADD", "register:40f0:8", ["const:43d524:8", "const:4:8"]]
- 0043d524 ["CALLIND", null, ["register:0:8"]]
+ 004603bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004603bc ["INT_ADD", "register:40f0:8", ["const:4603bc:8", "const:4:8"]]
+ 004603bc ["CALLIND", null, ["register:0:8"]]
- 0043d524 bytes 00013fd6
+ 004603bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6389606ab03d2449f7471c35444ad520"></a>

### [`0043d694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d694.md) → [`0046052c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/0046052c.md) FUN_0046052c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00460538",
      "incomplete_value": false,
      "site": "00460544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d6a0",
      "incomplete_value": false,
      "site": "0043d6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
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
      "00460544",
      "DATA",
      [
        "storage",
        "00be7258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460544",
      "DATA",
      [
        "storage",
        "00c63e18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d69c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d694.md#insn-0043d69c) · [`0043d6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d694.md#insn-0043d6a0)
- 新版 [`00460534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/0046052c.md#insn-00460534) · [`00460538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/0046052c.md#insn-00460538)

~~~diff
- 0043d69c ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 00460534 ["COPY", "register:4050:8", ["const:c63000:8"]]
- 0043d69c bytes 4a3d00d0
+ 00460534 bytes 0a4000f0
- 0043d6a0 ["COPY", "tmp:0:8", ["const:258:8"]]
- 0043d6a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043d6a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043d6a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00460538 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 00460538 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00460538 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00460538 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043d6a0 bytes 4a610991
+ 00460538 bytes 4a613891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cede5bd6bb260ca87caff57c1680a4b0"></a>

### [`0043d6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d6d8.md) → [`00460570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460570.md) FUN_00460570

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00460588",
      "incomplete_value": false,
      "site": "00460594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d6f0",
      "incomplete_value": false,
      "site": "0043d6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
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
      "00460594",
      "DATA",
      [
        "storage",
        "00be7258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460594",
      "DATA",
      [
        "storage",
        "00c63e18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d6d8.md#insn-0043d6ec) · [`0043d6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d6d8.md#insn-0043d6f0) · [`0043d720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d6d8.md#insn-0043d720)
- 新版 [`00460584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460570.md#insn-00460584) · [`00460588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460570.md#insn-00460588) · [`004605b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460570.md#insn-004605b8)

~~~diff
- 0043d6ec ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00460584 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043d6ec bytes 483d00d0
+ 00460584 bytes 084000f0
- 0043d6f0 ["COPY", "tmp:0:8", ["const:258:8"]]
- 0043d6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043d6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043d6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00460588 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 00460588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00460588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00460588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043d6f0 bytes 08610991
+ 00460588 bytes 08613891
- 0043d720 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043d720 ["INT_ADD", "register:40f0:8", ["const:43d720:8", "const:4:8"]]
- 0043d720 ["CALLIND", null, ["register:0:8"]]
+ 004605b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004605b8 ["INT_ADD", "register:40f0:8", ["const:4605b8:8", "const:4:8"]]
+ 004605b8 ["CALLIND", null, ["register:0:8"]]
- 0043d720 bytes 00013fd6
+ 004605b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9fef4537c8854929a29bdfa516dde53"></a>

### [`0043d734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d734.md) → [`004605cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004605cc.md) FUN_004605cc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004605f8",
      "incomplete_value": false,
      "site": "004605f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d760",
      "incomplete_value": false,
      "site": "0043d760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:258:8"
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
      "004605f8",
      "DATA",
      [
        "storage",
        "00be7258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004605f8",
      "DATA",
      [
        "storage",
        "00c63e18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d734.md#insn-0043d748) · [`0043d754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d734.md#insn-0043d754) · [`0043d758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d734.md#insn-0043d758)
- 新版 [`004605e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004605cc.md#insn-004605e0) · [`004605ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004605cc.md#insn-004605ec) · [`004605f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004605cc.md#insn-004605f0)

~~~diff
- 0043d748 ["INT_ADD", "register:40f0:8", ["const:43d748:8", "const:4:8"]]
- 0043d748 ["CALL", null, ["callee:00c57a90:8"]]
+ 004605e0 ["INT_ADD", "register:40f0:8", ["const:4605e0:8", "const:4:8"]]
+ 004605e0 ["CALL", null, ["callee:00c57a90:8"]]
- 0043d748 bytes 3e761e94
+ 004605e0 bytes 2cdd1f94
- 0043d754 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004605ec ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043d754 bytes 483d00d0
+ 004605ec bytes 084000f0
- 0043d758 ["COPY", "tmp:0:8", ["const:258:8"]]
- 0043d758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043d758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043d758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004605f0 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 004605f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004605f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004605f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043d758 bytes 08610991
+ 004605f0 bytes 08613891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd23d8e2c4bd39e0a44e9934a2cc91c4"></a>

### [`0043d7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d7bc.md) → [`00460654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460654.md) FUN_00460654

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00460670",
      "incomplete_value": false,
      "site": "00460670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d7d8",
      "incomplete_value": false,
      "site": "0043d7d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
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
      "00460670",
      "DATA",
      [
        "storage",
        "00be7258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460670",
      "DATA",
      [
        "storage",
        "00c63e18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d7bc.md#insn-0043d7d0) · [`0043d7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d7bc.md#insn-0043d7d4) · [`0043d7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d7bc.md#insn-0043d7f8)
- 新版 [`00460668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460654.md#insn-00460668) · [`0046066c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460654.md#insn-0046066c) · [`00460690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460654.md#insn-00460690)

~~~diff
- 0043d7d0 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 00460668 ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0043d7d0 bytes 493d00d0
+ 00460668 bytes 094000f0
- 0043d7d4 ["COPY", "tmp:0:8", ["const:258:8"]]
- 0043d7d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043d7d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043d7d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0046066c ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 0046066c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0046066c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0046066c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043d7d4 bytes 29610991
+ 0046066c bytes 29613891
- 0043d7f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0043d7f8 ["INT_ADD", "register:40f0:8", ["const:43d7f8:8", "const:4:8"]]
- 0043d7f8 ["CALLIND", null, ["register:0:8"]]
+ 00460690 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00460690 ["INT_ADD", "register:40f0:8", ["const:460690:8", "const:4:8"]]
+ 00460690 ["CALLIND", null, ["register:0:8"]]
- 0043d7f8 bytes 20013fd6
+ 00460690 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76591a2c316fb576a74a80ca2e7e9074"></a>

### [`0043d8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d8b8.md) → [`00460750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460750.md) FUN_00460750

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0043e5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e5d8.md) [`0043e7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e7f8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00461470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461470.md) [`00461690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.41% / 新版 97.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004608d8",
      "incomplete_value": true,
      "site": "004608e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:931:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043da40",
      "incomplete_value": true,
      "site": "0043da4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:270:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00460a44",
      "incomplete_value": true,
      "site": "00460a54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:178:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043dbac",
      "incomplete_value": true,
      "site": "0043dbbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:687:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00460a58",
      "incomplete_value": true,
      "site": "00460a58",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043dbc0",
      "incomplete_value": true,
      "site": "0043dbc0",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004608d8",
      "READ",
      [
        "storage",
        "002a2270",
        null,
        "string"
      ]
    ],
    [
      "00460a44",
      "READ",
      [
        "storage",
        "002a6687",
        null,
        "string"
      ]
    ],
    [
      "00460a4c",
      "READ",
      [
        "storage",
        "002a668c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004608d8",
      "READ",
      [
        "storage",
        "002b2931",
        null,
        "string"
      ]
    ],
    [
      "00460a44",
      "READ",
      [
        "storage",
        "002b7178",
        null,
        "string"
      ]
    ],
    [
      "00460a4c",
      "READ",
      [
        "storage",
        "002b717d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d8b8.md#insn-0043d920) · [`0043d94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d8b8.md#insn-0043d94c) · [`0043d97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d8b8.md#insn-0043d97c)
- 新版 [`004607b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460750.md#insn-004607b8) · [`004607e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460750.md#insn-004607e4) · [`00460814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460750.md#insn-00460814)

~~~diff
- 0043d920 ["INT_ADD", "register:40f0:8", ["const:43d920:8", "const:4:8"]]
- 0043d920 ["CALL", null, ["callee:0044104c:8"]]
+ 004607b8 ["INT_ADD", "register:40f0:8", ["const:4607b8:8", "const:4:8"]]
+ 004607b8 ["CALL", null, ["callee:0044104c:8"]]
- 0043d920 bytes 0b83ff97
+ 004607b8 bytes 2582ff97
- 0043d94c ["INT_ADD", "register:40f0:8", ["const:43d94c:8", "const:4:8"]]
- 0043d94c ["CALL", null, ["callee:00c57ab0:8"]]
+ 004607e4 ["INT_ADD", "register:40f0:8", ["const:4607e4:8", "const:4:8"]]
+ 004607e4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0043d94c bytes c5751e94
+ 004607e4 bytes b3dc1f94
- 0043d97c ["INT_ADD", "register:40f0:8", ["const:43d97c:8", "const:4:8"]]
- 0043d97c ["CALL", null, ["callee:0044104c:8"]]
+ 00460814 ["INT_ADD", "register:40f0:8", ["const:460814:8", "const:4:8"]]
+ 00460814 ["CALL", null, ["callee:0044104c:8"]]
- 0043d97c bytes f482ff97
+ 00460814 bytes 0e82ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b44846164a330a565080f60434424917"></a>

### [`0043e788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e788.md) → [`00461620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461620.md) FUN_00461620

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0043e5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e5d8.md) [`0043eef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043eef0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00461470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461470.md) [`00461d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461d88.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00461630",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0043e798",
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
      "definition_site": "0046162c",
      "incomplete_value": false,
      "site": "00461630",
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
      "definition_site": "0043e794",
      "incomplete_value": false,
      "site": "0043e798",
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
      "0046162c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00461630",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0046162c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00461630",
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

- 旧版 [`0043e798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e788.md#insn-0043e798) · [`0043e790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e788.md#insn-0043e790) · [`0043e794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e788.md#insn-0043e794)
- 新版 [`00461630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461620.md#insn-00461630) · [`00461628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461620.md#insn-00461628) · [`0046162c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461620.md#insn-0046162c)

~~~diff
- 0043e798 ["INT_ADD", "register:40f0:8", ["const:43e798:8", "const:4:8"]]
- 0043e798 ["CALL", null, ["ram:418c38:8"]]
+ 00461630 ["INT_ADD", "register:40f0:8", ["const:461630:8", "const:4:8"]]
+ 00461630 ["CALL", null, ["ram:43b738:8"]]
- 0043e798 bytes 2869ff97
+ 00461630 bytes 4268ff97
- 0043e790 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00461628 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0043e790 bytes 40f3ffb0
+ 00461628 bytes a0f2ffd0
- 0043e794 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0043e794 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0043e794 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0043e794 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046162c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0046162c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046162c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046162c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0043e794 bytes 00740e91
+ 0046162c bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49ac98b00d526613144d7459191b6092"></a>

### [`0043eb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043eb40.md) → [`004619d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004619d8.md) FUN_004619d8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0043e940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e940.md) [`0043ec60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043ec60.md) [`00989584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989584.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`004617d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004617d8.md) [`00461af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461af8.md) [`009bf078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf078.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "004619e8",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0043eb50",
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
      "definition_site": "004619e4",
      "incomplete_value": false,
      "site": "004619e8",
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
      "definition_site": "0043eb4c",
      "incomplete_value": false,
      "site": "0043eb50",
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
      "004619e4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "004619e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "004619e4",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "004619e8",
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

- 旧版 [`0043eb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043eb40.md#insn-0043eb50) · [`0043eb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043eb40.md#insn-0043eb48) · [`0043eb4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043eb40.md#insn-0043eb4c)
- 新版 [`004619e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004619d8.md#insn-004619e8) · [`004619e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004619d8.md#insn-004619e0) · [`004619e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004619d8.md#insn-004619e4)

~~~diff
- 0043eb50 ["INT_ADD", "register:40f0:8", ["const:43eb50:8", "const:4:8"]]
- 0043eb50 ["CALL", null, ["ram:418c38:8"]]
+ 004619e8 ["INT_ADD", "register:40f0:8", ["const:4619e8:8", "const:4:8"]]
+ 004619e8 ["CALL", null, ["ram:43b738:8"]]
- 0043eb50 bytes 3a68ff97
+ 004619e8 bytes 5467ff97
- 0043eb48 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 004619e0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0043eb48 bytes 40f3ffb0
+ 004619e0 bytes a0f2ffd0
- 0043eb4c ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0043eb4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0043eb4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0043eb4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004619e4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 004619e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004619e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004619e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0043eb4c bytes 00740e91
+ 004619e4 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c9b96cabdcdcebb3ac3fc6fb27ab1e6"></a>

### [`0043f158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f158.md) → [`00461ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461ff0.md) FUN_00461ff0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00461ffc",
      "incomplete_value": false,
      "site": "00462008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f164",
      "incomplete_value": false,
      "site": "0043f170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
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
      "00462008",
      "DATA",
      [
        "storage",
        "00be72d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462008",
      "DATA",
      [
        "storage",
        "00c63e98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f158.md#insn-0043f160) · [`0043f164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f158.md#insn-0043f164)
- 新版 [`00461ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461ff0.md#insn-00461ff8) · [`00461ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461ff0.md#insn-00461ffc)

~~~diff
- 0043f160 ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 00461ff8 ["COPY", "register:4050:8", ["const:c63000:8"]]
- 0043f160 bytes 4a3d0090
+ 00461ff8 bytes 0a4000d0
- 0043f164 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0043f164 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043f164 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043f164 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00461ffc ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00461ffc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00461ffc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00461ffc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043f164 bytes 4a610b91
+ 00461ffc bytes 4a613a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bce113cca97a8a7b1571ce49805a218f"></a>

### [`0043f19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f19c.md) → [`00462034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462034.md) FUN_00462034

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0046204c",
      "incomplete_value": false,
      "site": "00462058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f1b4",
      "incomplete_value": false,
      "site": "0043f1c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
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
      "00462058",
      "DATA",
      [
        "storage",
        "00be72d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462058",
      "DATA",
      [
        "storage",
        "00c63e98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f19c.md#insn-0043f1b0) · [`0043f1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f19c.md#insn-0043f1b4) · [`0043f1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f19c.md#insn-0043f1e4)
- 新版 [`00462048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462034.md#insn-00462048) · [`0046204c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462034.md#insn-0046204c) · [`0046207c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462034.md#insn-0046207c)

~~~diff
- 0043f1b0 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00462048 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043f1b0 bytes 483d0090
+ 00462048 bytes 084000b0
- 0043f1b4 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0043f1b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f1b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f1b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046204c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0046204c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046204c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046204c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f1b4 bytes 08610b91
+ 0046204c bytes 08613a91
- 0043f1e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043f1e4 ["INT_ADD", "register:40f0:8", ["const:43f1e4:8", "const:4:8"]]
- 0043f1e4 ["CALLIND", null, ["register:0:8"]]
+ 0046207c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046207c ["INT_ADD", "register:40f0:8", ["const:46207c:8", "const:4:8"]]
+ 0046207c ["CALLIND", null, ["register:0:8"]]
- 0043f1e4 bytes 00013fd6
+ 0046207c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c46337decb50a5c6ccb5da6f7382e44"></a>

### [`0043f1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f1f8.md) → [`00462090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462090.md) FUN_00462090

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004620bc",
      "incomplete_value": false,
      "site": "004620bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f224",
      "incomplete_value": false,
      "site": "0043f224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
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
      "004620bc",
      "DATA",
      [
        "storage",
        "00be72d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004620bc",
      "DATA",
      [
        "storage",
        "00c63e98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f1f8.md#insn-0043f20c) · [`0043f218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f1f8.md#insn-0043f218) · [`0043f21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f1f8.md#insn-0043f21c)
- 新版 [`004620a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462090.md#insn-004620a4) · [`004620b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462090.md#insn-004620b0) · [`004620b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462090.md#insn-004620b4)

~~~diff
- 0043f20c ["INT_ADD", "register:40f0:8", ["const:43f20c:8", "const:4:8"]]
- 0043f20c ["CALL", null, ["callee:00c57a90:8"]]
+ 004620a4 ["INT_ADD", "register:40f0:8", ["const:4620a4:8", "const:4:8"]]
+ 004620a4 ["CALL", null, ["callee:00c57a90:8"]]
- 0043f20c bytes 8d6f1e94
+ 004620a4 bytes 7bd61f94
- 0043f218 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004620b0 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043f218 bytes 483d0090
+ 004620b0 bytes 084000b0
- 0043f21c ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0043f21c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f21c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f21c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004620b4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 004620b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004620b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004620b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f21c bytes 08610b91
+ 004620b4 bytes 08613a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-124318e025beab211e9b613d6c926a0b"></a>

### [`0043f280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f280.md) → [`00462118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462118.md) FUN_00462118

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00462134",
      "incomplete_value": false,
      "site": "00462134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f29c",
      "incomplete_value": false,
      "site": "0043f29c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
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
      "00462134",
      "DATA",
      [
        "storage",
        "00be72d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462134",
      "DATA",
      [
        "storage",
        "00c63e98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f280.md#insn-0043f294) · [`0043f298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f280.md#insn-0043f298) · [`0043f2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f280.md#insn-0043f2bc)
- 新版 [`0046212c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462118.md#insn-0046212c) · [`00462130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462118.md#insn-00462130) · [`00462154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462118.md#insn-00462154)

~~~diff
- 0043f294 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 0046212c ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0043f294 bytes 493d0090
+ 0046212c bytes 094000b0
- 0043f298 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0043f298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043f298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043f298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462130 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00462130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043f298 bytes 29610b91
+ 00462130 bytes 29613a91
- 0043f2bc ["COPY", "register:0:8", ["register:4048:8"]]
- 0043f2bc ["INT_ADD", "register:40f0:8", ["const:43f2bc:8", "const:4:8"]]
- 0043f2bc ["CALLIND", null, ["register:0:8"]]
+ 00462154 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00462154 ["INT_ADD", "register:40f0:8", ["const:462154:8", "const:4:8"]]
+ 00462154 ["CALLIND", null, ["register:0:8"]]
- 0043f2bc bytes 20013fd6
+ 00462154 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80b80fbbdee3bd8b686d177a1ec4fa6f"></a>

### [`0043f4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f4e8.md) → [`00462380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462380.md) FUN_00462380

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046238c",
      "incomplete_value": false,
      "site": "00462398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f4f4",
      "incomplete_value": false,
      "site": "0043f500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:358:8"
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
      "00462398",
      "DATA",
      [
        "storage",
        "00be7358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462398",
      "DATA",
      [
        "storage",
        "00c63f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f4e8.md#insn-0043f4f0) · [`0043f4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f4e8.md#insn-0043f4f4)
- 新版 [`00462388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462380.md#insn-00462388) · [`0046238c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462380.md#insn-0046238c)

~~~diff
- 0043f4f0 ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 00462388 ["COPY", "register:4050:8", ["const:c63000:8"]]
- 0043f4f0 bytes 4a3d0090
+ 00462388 bytes 0a4000b0
- 0043f4f4 ["COPY", "tmp:0:8", ["const:358:8"]]
- 0043f4f4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043f4f4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043f4f4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046238c ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 0046238c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046238c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046238c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043f4f4 bytes 4a610d91
+ 0046238c bytes 4a613c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de6f4bb5c96ab124fc45fb7f9cc5a5ec"></a>

### [`0043f52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f52c.md) → [`004623c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004623c4.md) FUN_004623c4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "004623dc",
      "incomplete_value": false,
      "site": "004623e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f544",
      "incomplete_value": false,
      "site": "0043f550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:358:8"
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
      "004623e8",
      "DATA",
      [
        "storage",
        "00be7358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004623e8",
      "DATA",
      [
        "storage",
        "00c63f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f52c.md#insn-0043f540) · [`0043f544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f52c.md#insn-0043f544) · [`0043f574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f52c.md#insn-0043f574)
- 新版 [`004623d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004623c4.md#insn-004623d8) · [`004623dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004623c4.md#insn-004623dc) · [`0046240c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004623c4.md#insn-0046240c)

~~~diff
- 0043f540 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004623d8 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043f540 bytes 483d0090
+ 004623d8 bytes 084000b0
- 0043f544 ["COPY", "tmp:0:8", ["const:358:8"]]
- 0043f544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004623dc ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 004623dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004623dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004623dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f544 bytes 08610d91
+ 004623dc bytes 08613c91
- 0043f574 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043f574 ["INT_ADD", "register:40f0:8", ["const:43f574:8", "const:4:8"]]
- 0043f574 ["CALLIND", null, ["register:0:8"]]
+ 0046240c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046240c ["INT_ADD", "register:40f0:8", ["const:46240c:8", "const:4:8"]]
+ 0046240c ["CALLIND", null, ["register:0:8"]]
- 0043f574 bytes 00013fd6
+ 0046240c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59031fe8febb1978c3d815615d4a6e8d"></a>

### [`0043f588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f588.md) → [`00462420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462420.md) FUN_00462420

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046244c",
      "incomplete_value": false,
      "site": "0046244c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f5b4",
      "incomplete_value": false,
      "site": "0043f5b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:358:8"
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
      "0046244c",
      "DATA",
      [
        "storage",
        "00be7358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046244c",
      "DATA",
      [
        "storage",
        "00c63f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f588.md#insn-0043f59c) · [`0043f5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f588.md#insn-0043f5a8) · [`0043f5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f588.md#insn-0043f5ac)
- 新版 [`00462434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462420.md#insn-00462434) · [`00462440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462420.md#insn-00462440) · [`00462444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462420.md#insn-00462444)

~~~diff
- 0043f59c ["INT_ADD", "register:40f0:8", ["const:43f59c:8", "const:4:8"]]
- 0043f59c ["CALL", null, ["callee:00c57a90:8"]]
+ 00462434 ["INT_ADD", "register:40f0:8", ["const:462434:8", "const:4:8"]]
+ 00462434 ["CALL", null, ["callee:00c57a90:8"]]
- 0043f59c bytes a96e1e94
+ 00462434 bytes 97d51f94
- 0043f5a8 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00462440 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043f5a8 bytes 483d0090
+ 00462440 bytes 084000b0
- 0043f5ac ["COPY", "tmp:0:8", ["const:358:8"]]
- 0043f5ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f5ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f5ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462444 ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 00462444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f5ac bytes 08610d91
+ 00462444 bytes 08613c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6867b1c0db020381323db44626158e6a"></a>

### [`0043f610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f610.md) → [`004624a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004624a8.md) FUN_004624a8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004624c4",
      "incomplete_value": false,
      "site": "004624c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f62c",
      "incomplete_value": false,
      "site": "0043f62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:358:8"
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
      "004624c4",
      "DATA",
      [
        "storage",
        "00be7358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004624c4",
      "DATA",
      [
        "storage",
        "00c63f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f610.md#insn-0043f624) · [`0043f628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f610.md#insn-0043f628) · [`0043f64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f610.md#insn-0043f64c)
- 新版 [`004624bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004624a8.md#insn-004624bc) · [`004624c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004624a8.md#insn-004624c0) · [`004624e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004624a8.md#insn-004624e4)

~~~diff
- 0043f624 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 004624bc ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0043f624 bytes 493d0090
+ 004624bc bytes 094000b0
- 0043f628 ["COPY", "tmp:0:8", ["const:358:8"]]
- 0043f628 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043f628 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043f628 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004624c0 ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 004624c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004624c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004624c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043f628 bytes 29610d91
+ 004624c0 bytes 29613c91
- 0043f64c ["COPY", "register:0:8", ["register:4048:8"]]
- 0043f64c ["INT_ADD", "register:40f0:8", ["const:43f64c:8", "const:4:8"]]
- 0043f64c ["CALLIND", null, ["register:0:8"]]
+ 004624e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004624e4 ["INT_ADD", "register:40f0:8", ["const:4624e4:8", "const:4:8"]]
+ 004624e4 ["CALLIND", null, ["register:0:8"]]
- 0043f64c bytes 20013fd6
+ 004624e4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d763f2fce164b1c1c968202f6fb3857"></a>

### [`0043f7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f7a8.md) → [`00462640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462640.md) FUN_00462640

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046264c",
      "incomplete_value": false,
      "site": "00462658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f7b4",
      "incomplete_value": false,
      "site": "0043f7c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "00462658",
      "DATA",
      [
        "storage",
        "00be73d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462658",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f7a8.md#insn-0043f7b0) · [`0043f7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f7a8.md#insn-0043f7b4)
- 新版 [`00462648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462640.md#insn-00462648) · [`0046264c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462640.md#insn-0046264c)

~~~diff
- 0043f7b0 ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 00462648 ["COPY", "register:4050:8", ["const:c63000:8"]]
- 0043f7b0 bytes 4a3d0090
+ 00462648 bytes 0a4000b0
- 0043f7b4 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 0043f7b4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043f7b4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043f7b4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046264c ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 0046264c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046264c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046264c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043f7b4 bytes 4a610f91
+ 0046264c bytes 4a613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64f2639a1352489a38b262f2ee453363"></a>

### [`0043f7ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f7ec.md) → [`00462684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462684.md) FUN_00462684

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0046269c",
      "incomplete_value": false,
      "site": "004626a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f804",
      "incomplete_value": false,
      "site": "0043f810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "004626a8",
      "DATA",
      [
        "storage",
        "00be73d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004626a8",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f7ec.md#insn-0043f800) · [`0043f804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f7ec.md#insn-0043f804) · [`0043f834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f7ec.md#insn-0043f834)
- 新版 [`00462698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462684.md#insn-00462698) · [`0046269c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462684.md#insn-0046269c) · [`004626cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462684.md#insn-004626cc)

~~~diff
- 0043f800 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00462698 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043f800 bytes 483d0090
+ 00462698 bytes 084000b0
- 0043f804 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 0043f804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046269c ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 0046269c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046269c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046269c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f804 bytes 08610f91
+ 0046269c bytes 08613e91
- 0043f834 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043f834 ["INT_ADD", "register:40f0:8", ["const:43f834:8", "const:4:8"]]
- 0043f834 ["CALLIND", null, ["register:0:8"]]
+ 004626cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004626cc ["INT_ADD", "register:40f0:8", ["const:4626cc:8", "const:4:8"]]
+ 004626cc ["CALLIND", null, ["register:0:8"]]
- 0043f834 bytes 00013fd6
+ 004626cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-434d3fd0998b3110d8d0c9d443259b41"></a>

### [`0043f848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f848.md) → [`004626e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004626e0.md) FUN_004626e0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046270c",
      "incomplete_value": false,
      "site": "0046270c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f874",
      "incomplete_value": false,
      "site": "0043f874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "0046270c",
      "DATA",
      [
        "storage",
        "00be73d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046270c",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f848.md#insn-0043f85c) · [`0043f868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f848.md#insn-0043f868) · [`0043f86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f848.md#insn-0043f86c)
- 新版 [`004626f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004626e0.md#insn-004626f4) · [`00462700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004626e0.md#insn-00462700) · [`00462704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004626e0.md#insn-00462704)

~~~diff
- 0043f85c ["INT_ADD", "register:40f0:8", ["const:43f85c:8", "const:4:8"]]
- 0043f85c ["CALL", null, ["callee:00c57a90:8"]]
+ 004626f4 ["INT_ADD", "register:40f0:8", ["const:4626f4:8", "const:4:8"]]
+ 004626f4 ["CALL", null, ["callee:00c57a90:8"]]
- 0043f85c bytes f96d1e94
+ 004626f4 bytes e7d41f94
- 0043f868 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00462700 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043f868 bytes 483d0090
+ 00462700 bytes 084000b0
- 0043f86c ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 0043f86c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f86c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f86c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462704 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00462704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f86c bytes 08610f91
+ 00462704 bytes 08613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-289630ea468388f1351fe139a92a3d6b"></a>

### [`0043f8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f8d0.md) → [`00462768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462768.md) FUN_00462768

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00462784",
      "incomplete_value": false,
      "site": "00462784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f8ec",
      "incomplete_value": false,
      "site": "0043f8ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "00462784",
      "DATA",
      [
        "storage",
        "00be73d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462784",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f8e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f8d0.md#insn-0043f8e4) · [`0043f8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f8d0.md#insn-0043f8e8) · [`0043f90c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f8d0.md#insn-0043f90c)
- 新版 [`0046277c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462768.md#insn-0046277c) · [`00462780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462768.md#insn-00462780) · [`004627a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462768.md#insn-004627a4)

~~~diff
- 0043f8e4 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 0046277c ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0043f8e4 bytes 493d0090
+ 0046277c bytes 094000b0
- 0043f8e8 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 0043f8e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043f8e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043f8e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462780 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00462780 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462780 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462780 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043f8e8 bytes 29610f91
+ 00462780 bytes 29613e91
- 0043f90c ["COPY", "register:0:8", ["register:4048:8"]]
- 0043f90c ["INT_ADD", "register:40f0:8", ["const:43f90c:8", "const:4:8"]]
- 0043f90c ["CALLIND", null, ["register:0:8"]]
+ 004627a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004627a4 ["INT_ADD", "register:40f0:8", ["const:4627a4:8", "const:4:8"]]
+ 004627a4 ["CALLIND", null, ["register:0:8"]]
- 0043f90c bytes 20013fd6
+ 004627a4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e32814065971df4ce15d25509f1fa7b"></a>

### [`0043fa68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fa68.md) → [`00462900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462900.md) FUN_00462900

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046290c",
      "incomplete_value": false,
      "site": "00462918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fa74",
      "incomplete_value": false,
      "site": "0043fa80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "00462918",
      "DATA",
      [
        "storage",
        "00be7458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462918",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043fa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fa68.md#insn-0043fa70) · [`0043fa74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fa68.md#insn-0043fa74)
- 新版 [`00462908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462900.md#insn-00462908) · [`0046290c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462900.md#insn-0046290c)

~~~diff
- 0043fa70 ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 00462908 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 0043fa70 bytes 4a3d0090
+ 00462908 bytes 0a4000d0
- 0043fa74 ["COPY", "tmp:0:8", ["const:458:8"]]
- 0043fa74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043fa74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043fa74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046290c ["COPY", "tmp:0:8", ["const:18:8"]]
+ 0046290c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046290c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046290c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043fa74 bytes 4a611191
+ 0046290c bytes 4a610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e525af7981970ada3c2031a12ccb0aea"></a>

### [`0043faac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043faac.md) → [`00462944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462944.md) FUN_00462944

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0046295c",
      "incomplete_value": false,
      "site": "00462968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fac4",
      "incomplete_value": false,
      "site": "0043fad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "00462968",
      "DATA",
      [
        "storage",
        "00be7458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462968",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043fac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043faac.md#insn-0043fac0) · [`0043fac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043faac.md#insn-0043fac4) · [`0043faf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043faac.md#insn-0043faf4)
- 新版 [`00462958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462944.md#insn-00462958) · [`0046295c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462944.md#insn-0046295c) · [`0046298c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462944.md#insn-0046298c)

~~~diff
- 0043fac0 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00462958 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0043fac0 bytes 483d0090
+ 00462958 bytes 084000d0
- 0043fac4 ["COPY", "tmp:0:8", ["const:458:8"]]
- 0043fac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043fac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043fac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046295c ["COPY", "tmp:0:8", ["const:18:8"]]
+ 0046295c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046295c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046295c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043fac4 bytes 08611191
+ 0046295c bytes 08610091
- 0043faf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043faf4 ["INT_ADD", "register:40f0:8", ["const:43faf4:8", "const:4:8"]]
- 0043faf4 ["CALLIND", null, ["register:0:8"]]
+ 0046298c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046298c ["INT_ADD", "register:40f0:8", ["const:46298c:8", "const:4:8"]]
+ 0046298c ["CALLIND", null, ["register:0:8"]]
- 0043faf4 bytes 00013fd6
+ 0046298c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93dfe6e8e58562529b83acbe38831371"></a>

### [`0043fb08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fb08.md) → [`004629a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004629a0.md) FUN_004629a0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004629cc",
      "incomplete_value": false,
      "site": "004629cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fb34",
      "incomplete_value": false,
      "site": "0043fb34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "004629cc",
      "DATA",
      [
        "storage",
        "00be7458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004629cc",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043fb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fb08.md#insn-0043fb1c) · [`0043fb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fb08.md#insn-0043fb28) · [`0043fb2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fb08.md#insn-0043fb2c)
- 新版 [`004629b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004629a0.md#insn-004629b4) · [`004629c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004629a0.md#insn-004629c0) · [`004629c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004629a0.md#insn-004629c4)

~~~diff
- 0043fb1c ["INT_ADD", "register:40f0:8", ["const:43fb1c:8", "const:4:8"]]
- 0043fb1c ["CALL", null, ["callee:00c57a90:8"]]
+ 004629b4 ["INT_ADD", "register:40f0:8", ["const:4629b4:8", "const:4:8"]]
+ 004629b4 ["CALL", null, ["callee:00c57a90:8"]]
- 0043fb1c bytes 496d1e94
+ 004629b4 bytes 37d41f94
- 0043fb28 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004629c0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0043fb28 bytes 483d0090
+ 004629c0 bytes 084000d0
- 0043fb2c ["COPY", "tmp:0:8", ["const:458:8"]]
- 0043fb2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043fb2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043fb2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004629c4 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 004629c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004629c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004629c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043fb2c bytes 08611191
+ 004629c4 bytes 08610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f98df919da69ebb87a9e3d6ff31658e4"></a>

### [`0043fb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fb90.md) → [`00462a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462a28.md) FUN_00462a28

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00462a44",
      "incomplete_value": false,
      "site": "00462a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fbac",
      "incomplete_value": false,
      "site": "0043fbac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "00462a44",
      "DATA",
      [
        "storage",
        "00be7458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462a44",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043fba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fb90.md#insn-0043fba4) · [`0043fba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fb90.md#insn-0043fba8) · [`0043fbcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fb90.md#insn-0043fbcc)
- 新版 [`00462a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462a28.md#insn-00462a3c) · [`00462a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462a28.md#insn-00462a40) · [`00462a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462a28.md#insn-00462a64)

~~~diff
- 0043fba4 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 00462a3c ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0043fba4 bytes 493d0090
+ 00462a3c bytes 094000d0
- 0043fba8 ["COPY", "tmp:0:8", ["const:458:8"]]
- 0043fba8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043fba8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043fba8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462a40 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00462a40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462a40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462a40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043fba8 bytes 29611191
+ 00462a40 bytes 29610091
- 0043fbcc ["COPY", "register:0:8", ["register:4048:8"]]
- 0043fbcc ["INT_ADD", "register:40f0:8", ["const:43fbcc:8", "const:4:8"]]
- 0043fbcc ["CALLIND", null, ["register:0:8"]]
+ 00462a64 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00462a64 ["INT_ADD", "register:40f0:8", ["const:462a64:8", "const:4:8"]]
+ 00462a64 ["CALLIND", null, ["register:0:8"]]
- 0043fbcc bytes 20013fd6
+ 00462a64 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75ea0a99fba418e42255d03d2e15d49e"></a>

### [`0043fee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fee4.md) → [`00462d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462d7c.md) FUN_00462d7c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00462d88",
      "incomplete_value": false,
      "site": "00462d94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fef0",
      "incomplete_value": false,
      "site": "0043fefc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
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
      "00462d94",
      "DATA",
      [
        "storage",
        "00be74d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462d94",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043feec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fee4.md#insn-0043feec) · [`0043fef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fee4.md#insn-0043fef0)
- 新版 [`00462d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462d7c.md#insn-00462d84) · [`00462d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462d7c.md#insn-00462d88)

~~~diff
- 0043feec ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 00462d84 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 0043feec bytes 4a3d0090
+ 00462d84 bytes 0a4000d0
- 0043fef0 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 0043fef0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043fef0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043fef0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00462d88 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00462d88 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00462d88 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00462d88 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043fef0 bytes 4a611391
+ 00462d88 bytes 4a610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f86e78baa9e934031f54cedf64ea2f47"></a>

### [`0043ff28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043ff28.md) → [`00462dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462dc0.md) FUN_00462dc0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00462dd8",
      "incomplete_value": false,
      "site": "00462de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ff40",
      "incomplete_value": false,
      "site": "0043ff4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "00462de4",
      "DATA",
      [
        "storage",
        "00be74d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462de4",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043ff3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043ff28.md#insn-0043ff3c) · [`0043ff40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043ff28.md#insn-0043ff40) · [`0043ff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043ff28.md#insn-0043ff70)
- 新版 [`00462dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462dc0.md#insn-00462dd4) · [`00462dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462dc0.md#insn-00462dd8) · [`00462e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462dc0.md#insn-00462e08)

~~~diff
- 0043ff3c ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00462dd4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0043ff3c bytes 483d0090
+ 00462dd4 bytes 084000d0
- 0043ff40 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 0043ff40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043ff40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043ff40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462dd8 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00462dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043ff40 bytes 08611391
+ 00462dd8 bytes 08610291
- 0043ff70 ["COPY", "register:0:8", ["register:4040:8"]]
- 0043ff70 ["INT_ADD", "register:40f0:8", ["const:43ff70:8", "const:4:8"]]
- 0043ff70 ["CALLIND", null, ["register:0:8"]]
+ 00462e08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462e08 ["INT_ADD", "register:40f0:8", ["const:462e08:8", "const:4:8"]]
+ 00462e08 ["CALLIND", null, ["register:0:8"]]
- 0043ff70 bytes 00013fd6
+ 00462e08 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c92d14bde5c28c737531fc75ac878c0"></a>

### [`0043ff84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043ff84.md) → [`00462e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462e1c.md) FUN_00462e1c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00462e48",
      "incomplete_value": false,
      "site": "00462e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ffb0",
      "incomplete_value": false,
      "site": "0043ffb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "00462e48",
      "DATA",
      [
        "storage",
        "00be74d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462e48",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043ff98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043ff84.md#insn-0043ff98) · [`0043ffa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043ff84.md#insn-0043ffa4) · [`0043ffa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043ff84.md#insn-0043ffa8)
- 新版 [`00462e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462e1c.md#insn-00462e30) · [`00462e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462e1c.md#insn-00462e3c) · [`00462e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462e1c.md#insn-00462e40)

~~~diff
- 0043ff98 ["INT_ADD", "register:40f0:8", ["const:43ff98:8", "const:4:8"]]
- 0043ff98 ["CALL", null, ["callee:00c57a90:8"]]
+ 00462e30 ["INT_ADD", "register:40f0:8", ["const:462e30:8", "const:4:8"]]
+ 00462e30 ["CALL", null, ["callee:00c57a90:8"]]
- 0043ff98 bytes 2a6c1e94
+ 00462e30 bytes 18d31f94
- 0043ffa4 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00462e3c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0043ffa4 bytes 483d0090
+ 00462e3c bytes 084000d0
- 0043ffa8 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 0043ffa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043ffa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043ffa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462e40 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00462e40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462e40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462e40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043ffa8 bytes 08611391
+ 00462e40 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d84342bdca7c8a870da202a7dc65b62"></a>

### [`0044000c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/0044000c.md) → [`00462ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462ea4.md) FUN_00462ea4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00462ec0",
      "incomplete_value": false,
      "site": "00462ec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00440028",
      "incomplete_value": false,
      "site": "00440028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "00462ec0",
      "DATA",
      [
        "storage",
        "00be74d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462ec0",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/0044000c.md#insn-00440020) · [`00440024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/0044000c.md#insn-00440024) · [`00440048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/0044000c.md#insn-00440048)
- 新版 [`00462eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462ea4.md#insn-00462eb8) · [`00462ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462ea4.md#insn-00462ebc) · [`00462ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462ea4.md#insn-00462ee0)

~~~diff
- 00440020 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 00462eb8 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00440020 bytes 293d00f0
+ 00462eb8 bytes 094000d0
- 00440024 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 00440024 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00440024 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00440024 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462ebc ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00462ebc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462ebc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462ebc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00440024 bytes 29611391
+ 00462ebc bytes 29610291
- 00440048 ["COPY", "register:0:8", ["register:4048:8"]]
- 00440048 ["INT_ADD", "register:40f0:8", ["const:440048:8", "const:4:8"]]
- 00440048 ["CALLIND", null, ["register:0:8"]]
+ 00462ee0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00462ee0 ["INT_ADD", "register:40f0:8", ["const:462ee0:8", "const:4:8"]]
+ 00462ee0 ["CALLIND", null, ["register:0:8"]]
- 00440048 bytes 20013fd6
+ 00462ee0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b07878b8a11c753f596df553a3901529"></a>

### [`004401ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004401ac.md) → [`00463044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463044.md) FUN_00463044

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463050",
      "incomplete_value": false,
      "site": "0046305c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004401b8",
      "incomplete_value": false,
      "site": "004401c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:558:8"
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
      "0046305c",
      "DATA",
      [
        "storage",
        "00be7558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046305c",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004401b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004401ac.md#insn-004401b4) · [`004401b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004401ac.md#insn-004401b8)
- 新版 [`0046304c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463044.md#insn-0046304c) · [`00463050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463044.md#insn-00463050)

~~~diff
- 004401b4 ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 0046304c ["COPY", "register:4050:8", ["const:c64000:8"]]
- 004401b4 bytes 2a3d00f0
+ 0046304c bytes 0a4000b0
- 004401b8 ["COPY", "tmp:0:8", ["const:558:8"]]
- 004401b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004401b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004401b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00463050 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 00463050 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00463050 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00463050 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004401b8 bytes 4a611591
+ 00463050 bytes 4a610491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b7839fa7689c078508b476a47c805fa"></a>

### [`004401f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004401f0.md) → [`00463088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463088.md) FUN_00463088

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "004630a0",
      "incomplete_value": false,
      "site": "004630ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00440208",
      "incomplete_value": false,
      "site": "00440214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:558:8"
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
      "004630ac",
      "DATA",
      [
        "storage",
        "00be7558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004630ac",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004401f0.md#insn-00440204) · [`00440208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004401f0.md#insn-00440208) · [`00440238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004401f0.md#insn-00440238)
- 新版 [`0046309c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463088.md#insn-0046309c) · [`004630a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463088.md#insn-004630a0) · [`004630d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463088.md#insn-004630d0)

~~~diff
- 00440204 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 0046309c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00440204 bytes 283d00f0
+ 0046309c bytes 084000b0
- 00440208 ["COPY", "tmp:0:8", ["const:558:8"]]
- 00440208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00440208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00440208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004630a0 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 004630a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004630a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004630a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00440208 bytes 08611591
+ 004630a0 bytes 08610491
- 00440238 ["COPY", "register:0:8", ["register:4040:8"]]
- 00440238 ["INT_ADD", "register:40f0:8", ["const:440238:8", "const:4:8"]]
- 00440238 ["CALLIND", null, ["register:0:8"]]
+ 004630d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004630d0 ["INT_ADD", "register:40f0:8", ["const:4630d0:8", "const:4:8"]]
+ 004630d0 ["CALLIND", null, ["register:0:8"]]
- 00440238 bytes 00013fd6
+ 004630d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a750310c303d4e697b7bcceb425e9742"></a>

### [`0044024c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/0044024c.md) → [`004630e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004630e4.md) FUN_004630e4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463110",
      "incomplete_value": false,
      "site": "00463110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00440278",
      "incomplete_value": false,
      "site": "00440278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:558:8"
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
      "00463110",
      "DATA",
      [
        "storage",
        "00be7558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463110",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/0044024c.md#insn-00440260) · [`0044026c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/0044024c.md#insn-0044026c) · [`00440270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/0044024c.md#insn-00440270)
- 新版 [`004630f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004630e4.md#insn-004630f8) · [`00463104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004630e4.md#insn-00463104) · [`00463108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004630e4.md#insn-00463108)

~~~diff
- 00440260 ["INT_ADD", "register:40f0:8", ["const:440260:8", "const:4:8"]]
- 00440260 ["CALL", null, ["callee:00c57a90:8"]]
+ 004630f8 ["INT_ADD", "register:40f0:8", ["const:4630f8:8", "const:4:8"]]
+ 004630f8 ["CALL", null, ["callee:00c57a90:8"]]
- 00440260 bytes 786b1e94
+ 004630f8 bytes 66d21f94
- 0044026c ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00463104 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0044026c bytes 283d00f0
+ 00463104 bytes 084000b0
- 00440270 ["COPY", "tmp:0:8", ["const:558:8"]]
- 00440270 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00440270 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00440270 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463108 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 00463108 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463108 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463108 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00440270 bytes 08611591
+ 00463108 bytes 08610491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ca45a9b926237377c39b0323bdb0bc3"></a>

### [`004402d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004402d4.md) → [`0046316c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046316c.md) FUN_0046316c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463188",
      "incomplete_value": false,
      "site": "00463188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004402f0",
      "incomplete_value": false,
      "site": "004402f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:558:8"
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
      "00463188",
      "DATA",
      [
        "storage",
        "00be7558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463188",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004402e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004402d4.md#insn-004402e8) · [`004402ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004402d4.md#insn-004402ec) · [`00440310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004402d4.md#insn-00440310)
- 新版 [`00463180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046316c.md#insn-00463180) · [`00463184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046316c.md#insn-00463184) · [`004631a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046316c.md#insn-004631a8)

~~~diff
- 004402e8 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 00463180 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 004402e8 bytes 293d00f0
+ 00463180 bytes 094000b0
- 004402ec ["COPY", "tmp:0:8", ["const:558:8"]]
- 004402ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004402ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004402ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00463184 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 00463184 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00463184 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00463184 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004402ec bytes 29611591
+ 00463184 bytes 29610491
- 00440310 ["COPY", "register:0:8", ["register:4048:8"]]
- 00440310 ["INT_ADD", "register:40f0:8", ["const:440310:8", "const:4:8"]]
- 00440310 ["CALLIND", null, ["register:0:8"]]
+ 004631a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004631a8 ["INT_ADD", "register:40f0:8", ["const:4631a8:8", "const:4:8"]]
+ 004631a8 ["CALLIND", null, ["register:0:8"]]
- 00440310 bytes 20013fd6
+ 004631a8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ec1667b96af3ffa6da8ef8c55d3b839"></a>

### [`004403d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004403d0.md) → [`00463268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463268.md) FUN_00463268

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.79% / 新版 97.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046330c",
      "incomplete_value": true,
      "site": "0046330c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ece:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00440474",
      "incomplete_value": true,
      "site": "00440474",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b5:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004632fc",
      "READ",
      [
        "storage",
        "002918b5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004632fc",
      "READ",
      [
        "storage",
        "002a0ece",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004403d0.md#insn-00440424) · [`00440450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004403d0.md#insn-00440450) · [`00440458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004403d0.md#insn-00440458)
- 新版 [`004632bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463268.md#insn-004632bc) · [`004632e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463268.md#insn-004632e8) · [`004632f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463268.md#insn-004632f0)

~~~diff
- 00440424 ["INT_ADD", "register:40f0:8", ["const:440424:8", "const:4:8"]]
- 00440424 ["CALL", null, ["callee:0044104c:8"]]
+ 004632bc ["INT_ADD", "register:40f0:8", ["const:4632bc:8", "const:4:8"]]
+ 004632bc ["CALL", null, ["callee:0044104c:8"]]
- 00440424 bytes 4a78ff97
+ 004632bc bytes 6477ff97
- 00440450 ["INT_ADD", "register:40f0:8", ["const:440450:8", "const:4:8"]]
- 00440450 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004632e8 ["INT_ADD", "register:40f0:8", ["const:4632e8:8", "const:4:8"]]
+ 004632e8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00440450 bytes 046b1e94
+ 004632e8 bytes f2d11f94
- 00440458 ["COPY", "register:4048:8", ["const:291000:8"]]
+ 004632f0 ["COPY", "register:4048:8", ["const:2a0000:8"]]
- 00440458 bytes 89f2ffb0
+ 004632f0 bytes e9f1ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1990b97b0c19cfc039afd4738b88f69e"></a>

### [`00440694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440694.md) → [`0046352c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046352c.md) FUN_0046352c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463538",
      "incomplete_value": false,
      "site": "00463544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004406a0",
      "incomplete_value": false,
      "site": "004406ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "00463544",
      "DATA",
      [
        "storage",
        "00be75d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463544",
      "DATA",
      [
        "storage",
        "00c64198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044069c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440694.md#insn-0044069c) · [`004406a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440694.md#insn-004406a0)
- 新版 [`00463534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046352c.md#insn-00463534) · [`00463538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046352c.md#insn-00463538)

~~~diff
- 0044069c ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 00463534 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 0044069c bytes 2a3d00f0
+ 00463534 bytes 0a4000b0
- 004406a0 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 004406a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004406a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004406a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00463538 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00463538 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00463538 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00463538 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004406a0 bytes 4a611791
+ 00463538 bytes 4a610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34b6967e6f5de61c9598500a5b1e9305"></a>

### [`004406d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004406d8.md) → [`00463570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463570.md) FUN_00463570

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00463588",
      "incomplete_value": false,
      "site": "00463594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004406f0",
      "incomplete_value": false,
      "site": "004406fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "00463594",
      "DATA",
      [
        "storage",
        "00be75d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463594",
      "DATA",
      [
        "storage",
        "00c64198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004406ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004406d8.md#insn-004406ec) · [`004406f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004406d8.md#insn-004406f0) · [`00440720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004406d8.md#insn-00440720)
- 新版 [`00463584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463570.md#insn-00463584) · [`00463588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463570.md#insn-00463588) · [`004635b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463570.md#insn-004635b8)

~~~diff
- 004406ec ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00463584 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004406ec bytes 283d00f0
+ 00463584 bytes 084000b0
- 004406f0 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 004406f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004406f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004406f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463588 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00463588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004406f0 bytes 08611791
+ 00463588 bytes 08610691
- 00440720 ["COPY", "register:0:8", ["register:4040:8"]]
- 00440720 ["INT_ADD", "register:40f0:8", ["const:440720:8", "const:4:8"]]
- 00440720 ["CALLIND", null, ["register:0:8"]]
+ 004635b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004635b8 ["INT_ADD", "register:40f0:8", ["const:4635b8:8", "const:4:8"]]
+ 004635b8 ["CALLIND", null, ["register:0:8"]]
- 00440720 bytes 00013fd6
+ 004635b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56386aa9808f1f112ffd9dd2dd49d44f"></a>

### [`00440734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440734.md) → [`004635cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004635cc.md) FUN_004635cc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004635f8",
      "incomplete_value": false,
      "site": "004635f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00440760",
      "incomplete_value": false,
      "site": "00440760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "004635f8",
      "DATA",
      [
        "storage",
        "00be75d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004635f8",
      "DATA",
      [
        "storage",
        "00c64198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440734.md#insn-00440748) · [`00440754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440734.md#insn-00440754) · [`00440758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440734.md#insn-00440758)
- 新版 [`004635e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004635cc.md#insn-004635e0) · [`004635ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004635cc.md#insn-004635ec) · [`004635f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004635cc.md#insn-004635f0)

~~~diff
- 00440748 ["INT_ADD", "register:40f0:8", ["const:440748:8", "const:4:8"]]
- 00440748 ["CALL", null, ["callee:00c57a90:8"]]
+ 004635e0 ["INT_ADD", "register:40f0:8", ["const:4635e0:8", "const:4:8"]]
+ 004635e0 ["CALL", null, ["callee:00c57a90:8"]]
- 00440748 bytes 3e6a1e94
+ 004635e0 bytes 2cd11f94
- 00440754 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004635ec ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00440754 bytes 283d00f0
+ 004635ec bytes 084000b0
- 00440758 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00440758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00440758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00440758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004635f0 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 004635f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004635f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004635f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00440758 bytes 08611791
+ 004635f0 bytes 08610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2819a2eac5e71f8fdfc38611db98a63"></a>

### [`004407bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004407bc.md) → [`00463654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463654.md) FUN_00463654

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463670",
      "incomplete_value": false,
      "site": "00463670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004407d8",
      "incomplete_value": false,
      "site": "004407d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "00463670",
      "DATA",
      [
        "storage",
        "00be75d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463670",
      "DATA",
      [
        "storage",
        "00c64198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004407d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004407bc.md#insn-004407d0) · [`004407d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004407bc.md#insn-004407d4) · [`004407f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004407bc.md#insn-004407f8)
- 新版 [`00463668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463654.md#insn-00463668) · [`0046366c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463654.md#insn-0046366c) · [`00463690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463654.md#insn-00463690)

~~~diff
- 004407d0 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 00463668 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 004407d0 bytes 293d00f0
+ 00463668 bytes 094000b0
- 004407d4 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 004407d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004407d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004407d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0046366c ["COPY", "tmp:0:8", ["const:198:8"]]
+ 0046366c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0046366c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0046366c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004407d4 bytes 29611791
+ 0046366c bytes 29610691
- 004407f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004407f8 ["INT_ADD", "register:40f0:8", ["const:4407f8:8", "const:4:8"]]
- 004407f8 ["CALLIND", null, ["register:0:8"]]
+ 00463690 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00463690 ["INT_ADD", "register:40f0:8", ["const:463690:8", "const:4:8"]]
+ 00463690 ["CALLIND", null, ["register:0:8"]]
- 004407f8 bytes 20013fd6
+ 00463690 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00ff3bb6cd20fb1964cd522366e3a79b"></a>

### [`004409ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004409ac.md) → [`00463844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463844.md) FUN_00463844

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463850",
      "incomplete_value": false,
      "site": "0046385c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004409b8",
      "incomplete_value": false,
      "site": "004409c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "0046385c",
      "DATA",
      [
        "storage",
        "00be7658",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046385c",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004409b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004409ac.md#insn-004409b4) · [`004409b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004409ac.md#insn-004409b8)
- 新版 [`0046384c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463844.md#insn-0046384c) · [`00463850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463844.md#insn-00463850)

~~~diff
- 004409b4 ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 0046384c ["COPY", "register:4050:8", ["const:c64000:8"]]
- 004409b4 bytes 2a3d00f0
+ 0046384c bytes 0a4000b0
- 004409b8 ["COPY", "tmp:0:8", ["const:658:8"]]
- 004409b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004409b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004409b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00463850 ["COPY", "tmp:0:8", ["const:218:8"]]
+ 00463850 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00463850 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00463850 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004409b8 bytes 4a611991
+ 00463850 bytes 4a610891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f628847089ad9f64e7f2407e65877f1"></a>

### [`004409f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004409f0.md) → [`00463888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463888.md) FUN_00463888

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "004638a0",
      "incomplete_value": false,
      "site": "004638ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00440a08",
      "incomplete_value": false,
      "site": "00440a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "004638ac",
      "DATA",
      [
        "storage",
        "00be7658",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004638ac",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004409f0.md#insn-00440a04) · [`00440a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004409f0.md#insn-00440a08) · [`00440a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004409f0.md#insn-00440a38)
- 新版 [`0046389c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463888.md#insn-0046389c) · [`004638a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463888.md#insn-004638a0) · [`004638d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463888.md#insn-004638d0)

~~~diff
- 00440a04 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 0046389c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00440a04 bytes 283d00f0
+ 0046389c bytes 084000b0
- 00440a08 ["COPY", "tmp:0:8", ["const:658:8"]]
- 00440a08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00440a08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00440a08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004638a0 ["COPY", "tmp:0:8", ["const:218:8"]]
+ 004638a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004638a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004638a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00440a08 bytes 08611991
+ 004638a0 bytes 08610891
- 00440a38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00440a38 ["INT_ADD", "register:40f0:8", ["const:440a38:8", "const:4:8"]]
- 00440a38 ["CALLIND", null, ["register:0:8"]]
+ 004638d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004638d0 ["INT_ADD", "register:40f0:8", ["const:4638d0:8", "const:4:8"]]
+ 004638d0 ["CALLIND", null, ["register:0:8"]]
- 00440a38 bytes 00013fd6
+ 004638d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-750981c30feb325c1f70217ec0c2ccd4"></a>

### [`00440a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440a4c.md) → [`004638e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004638e4.md) FUN_004638e4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463910",
      "incomplete_value": false,
      "site": "00463910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00440a78",
      "incomplete_value": false,
      "site": "00440a78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "00463910",
      "DATA",
      [
        "storage",
        "00be7658",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463910",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440a4c.md#insn-00440a60) · [`00440a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440a4c.md#insn-00440a6c) · [`00440a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440a4c.md#insn-00440a70)
- 新版 [`004638f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004638e4.md#insn-004638f8) · [`00463904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004638e4.md#insn-00463904) · [`00463908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004638e4.md#insn-00463908)

~~~diff
- 00440a60 ["INT_ADD", "register:40f0:8", ["const:440a60:8", "const:4:8"]]
- 00440a60 ["CALL", null, ["callee:00c57a90:8"]]
+ 004638f8 ["INT_ADD", "register:40f0:8", ["const:4638f8:8", "const:4:8"]]
+ 004638f8 ["CALL", null, ["callee:00c57a90:8"]]
- 00440a60 bytes 78691e94
+ 004638f8 bytes 66d01f94
- 00440a6c ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00463904 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00440a6c bytes 283d00f0
+ 00463904 bytes 084000b0
- 00440a70 ["COPY", "tmp:0:8", ["const:658:8"]]
- 00440a70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00440a70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00440a70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463908 ["COPY", "tmp:0:8", ["const:218:8"]]
+ 00463908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00440a70 bytes 08611991
+ 00463908 bytes 08610891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

