# v16.0.0 → v16.0.1 · 最優先の変更候補 (24)

[一覧の目次](README.md)

<a id="compare-be4d9fd3a56aebfc5922a011cdd7f455"></a>

### [`005b90ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b90ec.md) → [`005b912c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b912c.md) FUN_005b912c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b9138",
      "incomplete_value": false,
      "site": "005b9144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b90f8",
      "incomplete_value": false,
      "site": "005b9104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "005b9144",
      "DATA",
      [
        "storage",
        "00c70570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b9144",
      "DATA",
      [
        "storage",
        "00c70970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b90f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b90ec.md#insn-005b90f8)
- 新版 `005b9138`（命令位置の公開資料なし）

~~~diff
- 005b90f8 ["COPY", "tmp:0:8", ["const:570:8"]]
- 005b90f8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b90f8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b90f8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b9138 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 005b9138 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b9138 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b9138 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b90f8 bytes 4ac11591
+ 005b9138 bytes 4ac12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29e7cdff096a1b5d65bce33a34d57933"></a>

### [`005b9130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9130.md) → [`005b9170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9170.md) FUN_005b9170

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005b9188",
      "incomplete_value": false,
      "site": "005b9194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b9148",
      "incomplete_value": false,
      "site": "005b9154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "005b9194",
      "DATA",
      [
        "storage",
        "00c70570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b9194",
      "DATA",
      [
        "storage",
        "00c70970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b9148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9130.md#insn-005b9148) · [`005b9178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9130.md#insn-005b9178)
- 新版 `005b9188`（命令位置の公開資料なし） · `005b91b8`（命令位置の公開資料なし）

~~~diff
- 005b9148 ["COPY", "tmp:0:8", ["const:570:8"]]
- 005b9148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b9148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b9148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b9188 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 005b9188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b9188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b9188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b9148 bytes 08c11591
+ 005b9188 bytes 08c12591
- 005b9178 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b9178 ["INT_ADD", "register:40f0:8", ["const:5b9178:8", "const:4:8"]]
- 005b9178 ["CALLIND", null, ["register:0:8"]]
+ 005b91b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b91b8 ["INT_ADD", "register:40f0:8", ["const:5b91b8:8", "const:4:8"]]
+ 005b91b8 ["CALLIND", null, ["register:0:8"]]
- 005b9178 bytes 00013fd6
+ 005b91b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4161c696a41ee18d425b058b78cedfc2"></a>

### [`005b918c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b918c.md) → [`005b91cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b91cc.md) FUN_005b91cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005b91f8",
      "incomplete_value": false,
      "site": "005b91f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b91b8",
      "incomplete_value": false,
      "site": "005b91b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "005b91f8",
      "DATA",
      [
        "storage",
        "00c70570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b91f8",
      "DATA",
      [
        "storage",
        "00c70970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b91a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b918c.md#insn-005b91a0) · [`005b91b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b918c.md#insn-005b91b0) · [`005b91d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b918c.md#insn-005b91d4)
- 新版 `005b91e0`（命令位置の公開資料なし） · `005b91f0`（命令位置の公開資料なし） · `005b9214`（命令位置の公開資料なし）

~~~diff
- 005b91a0 ["INT_ADD", "register:40f0:8", ["const:5b91a0:8", "const:4:8"]]
- 005b91a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b91e0 ["INT_ADD", "register:40f0:8", ["const:5b91e0:8", "const:4:8"]]
+ 005b91e0 ["CALL", null, ["callee:00c57e90:8"]]
- 005b91a0 bytes 3c7a1a94
+ 005b91e0 bytes 2c7b1a94
- 005b91b0 ["COPY", "tmp:0:8", ["const:570:8"]]
- 005b91b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b91b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b91b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b91f0 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 005b91f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b91f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b91f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b91b0 bytes 08c11591
+ 005b91f0 bytes 08c12591
- 005b91d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b91d4 ["INT_ADD", "register:40f0:8", ["const:5b91d4:8", "const:4:8"]]
- 005b91d4 ["CALLIND", null, ["register:0:8"]]
+ 005b9214 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b9214 ["INT_ADD", "register:40f0:8", ["const:5b9214:8", "const:4:8"]]
+ 005b9214 ["CALLIND", null, ["register:0:8"]]
- 005b91d4 bytes 00013fd6
+ 005b9214 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-104e95b6e504a98ee96a65e9bb685206"></a>

### [`005b9214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9214.md) → [`005b9254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9254.md) FUN_005b9254

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b9270",
      "incomplete_value": false,
      "site": "005b9270",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b9230",
      "incomplete_value": false,
      "site": "005b9230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "005b9270",
      "DATA",
      [
        "storage",
        "00c70570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b9270",
      "DATA",
      [
        "storage",
        "00c70970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b922c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9214.md#insn-005b922c) · [`005b9250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9214.md#insn-005b9250)
- 新版 `005b926c`（命令位置の公開資料なし） · `005b9290`（命令位置の公開資料なし）

~~~diff
- 005b922c ["COPY", "tmp:0:8", ["const:570:8"]]
- 005b922c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b922c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b922c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b926c ["COPY", "tmp:0:8", ["const:970:8"]]
+ 005b926c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b926c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b926c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b922c bytes 29c11591
+ 005b926c bytes 29c12591
- 005b9250 ["COPY", "register:0:8", ["register:4048:8"]]
- 005b9250 ["INT_ADD", "register:40f0:8", ["const:5b9250:8", "const:4:8"]]
- 005b9250 ["CALLIND", null, ["register:0:8"]]
+ 005b9290 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b9290 ["INT_ADD", "register:40f0:8", ["const:5b9290:8", "const:4:8"]]
+ 005b9290 ["CALLIND", null, ["register:0:8"]]
- 005b9250 bytes 20013fd6
+ 005b9290 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-941a4c048eade64c0b7d20f88adedb51"></a>

### [`005b9628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9628.md) → [`005b9668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9668.md) _INIT_61

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b96a4",
      "incomplete_value": true,
      "site": "005b96c0",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b9664",
      "incomplete_value": true,
      "site": "005b9680",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:ee6:8"
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
      "definition_site": "005b96c8",
      "incomplete_value": true,
      "site": "005b96e4",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b9688",
      "incomplete_value": true,
      "site": "005b96a4",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:ef9:8"
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
      "definition_site": "005b96e8",
      "incomplete_value": true,
      "site": "005b9704",
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
                "const:dc2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b96a8",
      "incomplete_value": true,
      "site": "005b96c4",
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
                "const:d82:8"
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
      "005b96a4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005b96c8",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005b96e8",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005b96a4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005b96c8",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005b96e8",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b96a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9628.md#insn-005b96a0) · [`005b96c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9628.md#insn-005b96c0) · [`005b985c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9628.md#insn-005b985c)
- 新版 `005b96e0`（命令位置の公開資料なし） · `005b9700`（命令位置の公開資料なし） · `005b989c`（命令位置の公開資料なし）

~~~diff
- 005b96a0 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 005b96a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b96a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b96a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b96e0 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 005b96e0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b96e0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b96e0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b96a0 bytes 4a093691
+ 005b96e0 bytes 4a093791
- 005b96c0 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005b96c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b96c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b96c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b9700 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005b9700 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b9700 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b9700 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b96c0 bytes 4a553a91
+ 005b9700 bytes 4a893d91
- 005b985c ["INT_ADD", "register:40f0:8", ["const:5b985c:8", "const:4:8"]]
- 005b985c ["CALL", null, ["callee:00c57e30:8"]]
+ 005b989c ["INT_ADD", "register:40f0:8", ["const:5b989c:8", "const:4:8"]]
+ 005b989c ["CALL", null, ["callee:00c57e30:8"]]
- 005b985c bytes 75781a94
+ 005b989c bytes 65791a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb322194b1cf1938c9c125acbfa33945"></a>

### [`005b9a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a58.md) → [`005b9a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a98.md) FUN_005b9a98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) · 呼出先 2件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md)
- 新版 呼出元 1件 [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) · 呼出先 2件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "site": "005b9ab4",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b9a74",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "005b9ab4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "005b9ab4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b9a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a58.md#insn-005b9a74) · [`005b9a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a58.md#insn-005b9a78)
- 新版 `005b9ab4`（命令位置の公開資料なし） · `005b9ab8`（命令位置の公開資料なし）

~~~diff
- 005b9a74 ["INT_ADD", "register:40f0:8", ["const:5b9a74:8", "const:4:8"]]
- 005b9a74 ["CALL", null, ["ram:48ccb8:8"]]
+ 005b9ab4 ["INT_ADD", "register:40f0:8", ["const:5b9ab4:8", "const:4:8"]]
+ 005b9ab4 ["CALL", null, ["ram:48ccf8:8"]]
- 005b9a74 bytes 914cfb97
+ 005b9ab4 bytes 914cfb97
- 005b9a78 ["INT_ADD", "register:40f0:8", ["const:5b9a78:8", "const:4:8"]]
- 005b9a78 ["CALL", null, ["callee:0048ce84:8"]]
+ 005b9ab8 ["INT_ADD", "register:40f0:8", ["const:5b9ab8:8", "const:4:8"]]
+ 005b9ab8 ["CALL", null, ["callee:0048ce84:8"]]
- 005b9a78 bytes f34cfb97
+ 005b9ab8 bytes f34cfb97
~~~


<a id="compare-0ac885687f3dd0d3efd103dc07d8b6a5"></a>

### [`005b9aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9aa0.md) → [`005b9ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9ae0.md) FUN_005b9ae0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 3件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`005b9b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9b14.md)
- 新版 呼出元 1件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 3件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`005b9b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9b54.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

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
      "site": "005b9b00",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b9ac0",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "005b9b00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "005b9b00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b9ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9aa0.md#insn-005b9ac0) · [`005b9ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9aa0.md#insn-005b9ac4) · [`005b9aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9aa0.md#insn-005b9aec)
- 新版 `005b9b00`（命令位置の公開資料なし） · `005b9b04`（命令位置の公開資料なし） · `005b9b2c`（命令位置の公開資料なし）

~~~diff
- 005b9ac0 ["INT_ADD", "register:40f0:8", ["const:5b9ac0:8", "const:4:8"]]
- 005b9ac0 ["CALL", null, ["ram:48ccb8:8"]]
+ 005b9b00 ["INT_ADD", "register:40f0:8", ["const:5b9b00:8", "const:4:8"]]
+ 005b9b00 ["CALL", null, ["ram:48ccf8:8"]]
- 005b9ac0 bytes 7e4cfb97
+ 005b9b00 bytes 7e4cfb97
- 005b9ac4 ["INT_ADD", "register:40f0:8", ["const:5b9ac4:8", "const:4:8"]]
- 005b9ac4 ["CALL", null, ["callee:0048ce84:8"]]
+ 005b9b04 ["INT_ADD", "register:40f0:8", ["const:5b9b04:8", "const:4:8"]]
+ 005b9b04 ["CALL", null, ["callee:0048ce84:8"]]
- 005b9ac4 bytes e04cfb97
+ 005b9b04 bytes e04cfb97
- 005b9aec ["INT_ADD", "register:40f0:8", ["const:5b9aec:8", "const:4:8"]]
- 005b9aec ["CALL", null, ["callee:005b9b54:8"]]
+ 005b9b2c ["INT_ADD", "register:40f0:8", ["const:5b9b2c:8", "const:4:8"]]
+ 005b9b2c ["CALL", null, ["callee:005b9b54:8"]]
- 005b9aec bytes 0a000094
+ 005b9b2c bytes 0a000094
~~~


<a id="compare-95d87c2c09381b1a473a395efdd29a9d"></a>

### [`005b9b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9b14.md) → [`005b9b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9b54.md) FUN_005b9b54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005b9aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9aa0.md) · 呼出先 18件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`005b9ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9ae0.md) · 呼出先 18件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.65% / 新版 93.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b9ba4",
      "incomplete_value": false,
      "site": "005b9bac",
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
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b9b64",
      "incomplete_value": false,
      "site": "005b9b6c",
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
            "const:938:8"
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
      "definition_site": "005b9d94",
      "incomplete_value": true,
      "site": "005b9d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b9d54",
      "incomplete_value": true,
      "site": "005b9d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005b9d90",
      "incomplete_value": true,
      "site": "005b9d9c",
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
      "definition_site": "005b9d50",
      "incomplete_value": true,
      "site": "005b9d5c",
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
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b9bac",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "005b9bd4",
      "PARAM",
      [
        "storage",
        "00ca6470",
        null,
        null
      ]
    ],
    [
      "005b9d84",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b9bac",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "005b9bd4",
      "PARAM",
      [
        "storage",
        "00ca6870",
        null,
        null
      ]
    ],
    [
      "005b9d84",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b9ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9b14.md#insn-005b9ba0) · [`005b9be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9b14.md#insn-005b9be0) · [`005b9d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9b14.md#insn-005b9d9c)
- 新版 `005b9be0`（命令位置の公開資料なし） · `005b9c20`（命令位置の公開資料なし） · `005b9ddc`（命令位置の公開資料なし）

~~~diff
- 005b9ba0 ["INT_ADD", "register:40f0:8", ["const:5b9ba0:8", "const:4:8"]]
- 005b9ba0 ["CALL", null, ["callee:00492e08:8"]]
+ 005b9be0 ["INT_ADD", "register:40f0:8", ["const:5b9be0:8", "const:4:8"]]
+ 005b9be0 ["CALL", null, ["callee:00492e08:8"]]
- 005b9ba0 bytes 8a64fb97
+ 005b9be0 bytes 8a64fb97
- 005b9be0 ["INT_ADD", "register:40f0:8", ["const:5b9be0:8", "const:4:8"]]
- 005b9be0 ["CALL", null, ["callee:0048792c:8"]]
+ 005b9c20 ["INT_ADD", "register:40f0:8", ["const:5b9c20:8", "const:4:8"]]
+ 005b9c20 ["CALL", null, ["callee:0048792c:8"]]
- 005b9be0 bytes 4337fb97
+ 005b9c20 bytes 4337fb97
- 005b9d9c ["INT_ADD", "register:40f0:8", ["const:5b9d9c:8", "const:4:8"]]
- 005b9d9c ["CALL", null, ["callee:00c57fb0:8"]]
+ 005b9ddc ["INT_ADD", "register:40f0:8", ["const:5b9ddc:8", "const:4:8"]]
+ 005b9ddc ["CALL", null, ["callee:00c57fb0:8"]]
- 005b9d9c bytes 85771a94
+ 005b9ddc bytes 75781a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01170b8875ebe196f73cbadc7a96e928"></a>

### [`005b9ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ef4.md) → [`005b9f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9f34.md) _INIT_62

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 81.63% / 新版 81.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 2件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b9f70",
      "incomplete_value": true,
      "site": "005b9f8c",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b9f30",
      "incomplete_value": true,
      "site": "005b9f4c",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:ee6:8"
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
      "definition_site": "005b9f94",
      "incomplete_value": true,
      "site": "005b9fb0",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b9f54",
      "incomplete_value": true,
      "site": "005b9f70",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:ef9:8"
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
      "definition_site": "005b9fb4",
      "incomplete_value": true,
      "site": "005b9fd0",
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
                "const:dc2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b9f74",
      "incomplete_value": true,
      "site": "005b9f90",
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
                "const:d82:8"
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
      "005b9f70",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005b9f94",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005b9fb4",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005b9f70",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005b9f94",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005b9fb4",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b9f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ef4.md#insn-005b9f6c) · [`005b9f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ef4.md#insn-005b9f8c) · [`005ba114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9ef4.md#insn-005ba114)
- 新版 `005b9fac`（命令位置の公開資料なし） · `005b9fcc`（命令位置の公開資料なし） · `005ba154`（命令位置の公開資料なし）

~~~diff
- 005b9f6c ["COPY", "tmp:0:8", ["const:d82:8"]]
- 005b9f6c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b9f6c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b9f6c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b9fac ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 005b9fac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b9fac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b9fac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b9f6c bytes 4a093691
+ 005b9fac bytes 4a093791
- 005b9f8c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005b9f8c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b9f8c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b9f8c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b9fcc ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005b9fcc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b9fcc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b9fcc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b9f8c bytes 4a553a91
+ 005b9fcc bytes 4a893d91
- 005ba114 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 005ba114 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005ba114 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005ba114 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005ba154 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 005ba154 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005ba154 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005ba154 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005ba114 bytes 73422e91
+ 005ba154 bytes 73423e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00fc3c983e25c23dfdda17b545d3fb79"></a>

### [`005ba2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba2d0.md) → [`005ba310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba310.md) FUN_005ba310

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) · 呼出先 12件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00597e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e88.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) · 呼出先 12件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00597ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.40% / 新版 84.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_destination` 7件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ba34c",
      "incomplete_value": false,
      "site": "005ba350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ba30c",
      "incomplete_value": false,
      "site": "005ba310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005ba3d0",
      "incomplete_value": true,
      "site": "005ba3d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ba390",
      "incomplete_value": true,
      "site": "005ba390",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fec:8"
              ]
            ]
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
      "definition_site": "005ba3cc",
      "incomplete_value": true,
      "site": "005ba3d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005ba38c",
      "incomplete_value": true,
      "site": "005ba394",
      "value": [
        "LOAD",
        "8",
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
      "005ba350",
      "DATA",
      [
        "storage",
        "00c705f0",
        null,
        "undefined *"
      ]
    ],
    [
      "005ba370",
      "PARAM",
      [
        "storage",
        "002d72f4",
        null,
        "string"
      ]
    ],
    [
      "005ba384",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "005ba350",
      "DATA",
      [
        "storage",
        "00c709f0",
        null,
        "undefined *"
      ]
    ],
    [
      "005ba370",
      "PARAM",
      [
        "storage",
        "002d7334",
        null,
        "string"
      ]
    ],
    [
      "005ba384",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ba3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba2d0.md#insn-005ba3b4) · [`005ba3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba2d0.md#insn-005ba3d4) · [`005ba4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba2d0.md#insn-005ba4c0)
- 新版 `005ba3f4`（命令位置の公開資料なし） · `005ba414`（命令位置の公開資料なし） · `005ba500`（命令位置の公開資料なし）

~~~diff
- 005ba3b4 ["INT_ADD", "register:40f0:8", ["const:5ba3b4:8", "const:4:8"]]
- 005ba3b4 ["CALL", null, ["callee:0047e60c:8"]]
+ 005ba3f4 ["INT_ADD", "register:40f0:8", ["const:5ba3f4:8", "const:4:8"]]
+ 005ba3f4 ["CALL", null, ["callee:0047e60c:8"]]
- 005ba3b4 bytes 8610fb97
+ 005ba3f4 bytes 8610fb97
- 005ba3d4 ["INT_ADD", "register:40f0:8", ["const:5ba3d4:8", "const:4:8"]]
- 005ba3d4 ["CALL", null, ["callee:00c53d00:8"]]
+ 005ba414 ["INT_ADD", "register:40f0:8", ["const:5ba414:8", "const:4:8"]]
+ 005ba414 ["CALL", null, ["callee:00c53d00:8"]]
- 005ba3d4 bytes 43651a94
+ 005ba414 bytes 3b661a94
- 005ba4c0 ["INT_ADD", "register:40f0:8", ["const:5ba4c0:8", "const:4:8"]]
- 005ba4c0 ["CALL", null, ["callee:0047e8dc:8"]]
+ 005ba500 ["INT_ADD", "register:40f0:8", ["const:5ba500:8", "const:4:8"]]
+ 005ba500 ["CALL", null, ["callee:0047e8dc:8"]]
- 005ba4c0 bytes f710fb97
+ 005ba500 bytes f710fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7b4357024c14d5697ed85d18ecdbe51"></a>

### [`005ba758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md) → [`005ba798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba798.md) FUN_005ba798

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005badb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005badb4.md) · 呼出先 14件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047b780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b780.md) [`0047b788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b788.md) [`0047b80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b80c.md) [`0047cec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cec8.md)
- 新版 呼出元 1件 [`005badf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005badf4.md) · 呼出先 14件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047b7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b7c0.md) [`0047b7c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b7c8.md) [`0047b84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b84c.md) [`0047cf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf08.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.18% / 新版 90.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005ba7b0",
      "value": [
        "leaf",
        "ram:84e59c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005ba770",
      "value": [
        "leaf",
        "ram:84e55c:8"
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
      "site": "005ba7ec",
      "value": [
        "leaf",
        "ram:b1f428:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005ba7ac",
      "value": [
        "leaf",
        "ram:b1f000:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005ba884",
      "value": [
        "leaf",
        "ram:b28f54:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005ba844",
      "value": [
        "leaf",
        "ram:b28b2c:8"
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
      "005ba7b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0084e55c"
      ]
    ],
    [
      "005ba7ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b1f000"
      ]
    ],
    [
      "005ba878",
      "DATA",
      [
        "storage",
        "003c79f8",
        null,
        "byte[15]"
      ]
    ]
  ],
  "added": [
    [
      "005ba7b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0084e59c"
      ]
    ],
    [
      "005ba7ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b1f428"
      ]
    ],
    [
      "005ba878",
      "DATA",
      [
        "storage",
        "003c79f8",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ba76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md#insn-005ba76c) · [`005ba770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md#insn-005ba770) · [`005ba7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md#insn-005ba7ac)
- 新版 `005ba7ac`（命令位置の公開資料なし） · `005ba7b0`（命令位置の公開資料なし） · `005ba7ec`（命令位置の公開資料なし）

~~~diff
- 005ba76c ["INT_ADD", "register:40f0:8", ["const:5ba76c:8", "const:4:8"]]
- 005ba76c ["CALL", null, ["callee:008514f8:8"]]
+ 005ba7ac ["INT_ADD", "register:40f0:8", ["const:5ba7ac:8", "const:4:8"]]
+ 005ba7ac ["CALL", null, ["callee:008514f8:8"]]
- 005ba76c bytes 535b0a94
+ 005ba7ac bytes 535b0a94
- 005ba770 ["INT_ADD", "register:40f0:8", ["const:5ba770:8", "const:4:8"]]
- 005ba770 ["CALL", null, ["ram:84e55c:8"]]
+ 005ba7b0 ["INT_ADD", "register:40f0:8", ["const:5ba7b0:8", "const:4:8"]]
+ 005ba7b0 ["CALL", null, ["ram:84e59c:8"]]
- 005ba770 bytes 7b4f0a94
+ 005ba7b0 bytes 7b4f0a94
- 005ba7ac ["INT_ADD", "register:40f0:8", ["const:5ba7ac:8", "const:4:8"]]
- 005ba7ac ["CALL", null, ["ram:b1f000:8"]]
+ 005ba7ec ["INT_ADD", "register:40f0:8", ["const:5ba7ec:8", "const:4:8"]]
+ 005ba7ec ["CALL", null, ["ram:b1f428:8"]]
- 005ba7ac bytes 15921594
+ 005ba7ec bytes 0f931594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9346f977351c7fbf5cd0e392f45611d2"></a>

### [`005ba918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba918.md) → [`005ba958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba958.md) FUN_005ba958

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`005bad8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bad8c.md) [`005bae5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bae5c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`005badcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005badcc.md) [`005bae9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005bae9c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ba9e8",
      "incomplete_value": true,
      "site": "005ba9f4",
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ba9a8",
      "incomplete_value": true,
      "site": "005ba9b4",
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
                "const:d10:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005baaa8",
      "incomplete_value": false,
      "site": "005baaac",
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
            "const:f27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005baa68",
      "incomplete_value": false,
      "site": "005baa6c",
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
            "const:e5a:8"
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
      "005ba9a0",
      "DATA",
      [
        "storage",
        "00c70650",
        null,
        "pointer"
      ]
    ],
    [
      "005ba9e8",
      "READ",
      [
        "storage",
        "002c2d10",
        null,
        null
      ]
    ],
    [
      "005ba9fc",
      "PARAM",
      [
        "storage",
        "005bae5c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005ba9a0",
      "DATA",
      [
        "storage",
        "00c70a50",
        null,
        "pointer"
      ]
    ],
    [
      "005ba9e8",
      "READ",
      [
        "storage",
        "002c2d50",
        null,
        null
      ]
    ],
    [
      "005ba9fc",
      "PARAM",
      [
        "storage",
        "005bae9c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ba9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba918.md#insn-005ba9f4) · [`005baa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba918.md#insn-005baa6c) · [`005ba944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba918.md#insn-005ba944)
- 新版 `005baa34`（命令位置の公開資料なし） · `005baaac`（命令位置の公開資料なし） · `005ba984`（命令位置の公開資料なし）

~~~diff
- 005ba9f4 ["INT_ADD", "register:40f0:8", ["const:5ba9f4:8", "const:4:8"]]
- 005ba9f4 ["CALL", null, ["callee:00c53d00:8"]]
+ 005baa34 ["INT_ADD", "register:40f0:8", ["const:5baa34:8", "const:4:8"]]
+ 005baa34 ["CALL", null, ["callee:00c53d00:8"]]
- 005ba9f4 bytes bb631a94
+ 005baa34 bytes b3641a94
- 005baa6c ["INT_ADD", "register:40f0:8", ["const:5baa6c:8", "const:4:8"]]
- 005baa6c ["CALL", null, ["callee:00c58120:8"]]
+ 005baaac ["INT_ADD", "register:40f0:8", ["const:5baaac:8", "const:4:8"]]
+ 005baaac ["CALL", null, ["callee:00c58120:8"]]
- 005baa6c bytes ad741a94
+ 005baaac bytes 9d751a94
- 005ba944 ["INT_ADD", "register:40f0:8", ["const:5ba944:8", "const:4:8"]]
- 005ba944 ["CALL", null, ["callee:00c57e90:8"]]
+ 005ba984 ["INT_ADD", "register:40f0:8", ["const:5ba984:8", "const:4:8"]]
+ 005ba984 ["CALL", null, ["callee:00c57e90:8"]]
- 005ba944 bytes 53741a94
+ 005ba984 bytes 43751a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5601daee8e88a328c52cf76095034ca3"></a>

### [`005bab24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bab24.md) → [`005bab64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005bab64.md) FUN_005bab64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c580e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c584e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005bab7c",
      "incomplete_value": false,
      "site": "005bab80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bab3c",
      "incomplete_value": false,
      "site": "005bab40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "005bab80",
      "DATA",
      [
        "storage",
        "00c705f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005bab80",
      "DATA",
      [
        "storage",
        "00c709f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bab80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bab24.md#insn-005bab80) · [`005bab3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bab24.md#insn-005bab3c) · [`005bab4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bab24.md#insn-005bab4c)
- 新版 `005babc0`（命令位置の公開資料なし） · `005bab7c`（命令位置の公開資料なし） · `005bab8c`（命令位置の公開資料なし）

~~~diff
- 005bab80 ["INT_ADD", "register:40f0:8", ["const:5bab80:8", "const:4:8"]]
- 005bab80 ["CALL", null, ["callee:00c53d00:8"]]
+ 005babc0 ["INT_ADD", "register:40f0:8", ["const:5babc0:8", "const:4:8"]]
+ 005babc0 ["CALL", null, ["callee:00c53d00:8"]]
- 005bab80 bytes 58631a94
+ 005babc0 bytes 50641a94
- 005bab3c ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 005bab3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005bab3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005bab3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005bab7c ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 005bab7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005bab7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005bab7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005bab3c bytes 29c11791
+ 005bab7c bytes 29c12791
- 005bab4c ["INT_ADD", "register:40f0:8", ["const:5bab4c:8", "const:4:8"]]
- 005bab4c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005bab8c ["INT_ADD", "register:40f0:8", ["const:5bab8c:8", "const:4:8"]]
+ 005bab8c ["CALL", null, ["callee:00c57eb0:8"]]
- 005bab4c bytes d9731a94
+ 005bab8c bytes c9741a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7dcf26f8894a3290a164fc5302ec34"></a>

### [`005bad38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bad38.md) → [`005bad78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005bad78.md) FUN_005bad78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

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
      "definition_site": "005bad9c",
      "incomplete_value": true,
      "site": "005bad9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005bad5c",
      "incomplete_value": true,
      "site": "005bad5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005bad90",
      "READ",
      [
        "storage",
        "00c9a850",
        null,
        "pointer"
      ]
    ],
    [
      "005bad9c",
      "DATA",
      [
        "storage",
        "00c928d8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005bad90",
      "READ",
      [
        "storage",
        "00c9ac50",
        null,
        "pointer"
      ]
    ],
    [
      "005bad9c",
      "DATA",
      [
        "storage",
        "00c92cd8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bad50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bad38.md#insn-005bad50) · [`005bad60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bad38.md#insn-005bad60) · [`005bad68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bad38.md#insn-005bad68)
- 新版 `005bad90`（命令位置の公開資料なし） · `005bada0`（命令位置の公開資料なし） · `005bada8`（命令位置の公開資料なし）

~~~diff
- 005bad50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:850:8"]]
- 005bad50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005bad90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
+ 005bad90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005bad50 bytes 082944f9
+ 005bad90 bytes 082946f9
- 005bad60 ["INT_ADD", "register:40f0:8", ["const:5bad60:8", "const:4:8"]]
- 005bad60 ["CALL", null, ["callee:00c580d0:8"]]
+ 005bada0 ["INT_ADD", "register:40f0:8", ["const:5bada0:8", "const:4:8"]]
+ 005bada0 ["CALL", null, ["callee:00c580d0:8"]]
- 005bad60 bytes dc731a94
+ 005bada0 bytes cc741a94
- 005bad68 ["INT_ADD", "register:40f0:8", ["const:5bad68:8", "const:4:8"]]
- 005bad68 ["CALL", null, ["callee:00c57e60:8"]]
+ 005bada8 ["INT_ADD", "register:40f0:8", ["const:5bada8:8", "const:4:8"]]
+ 005bada8 ["CALL", null, ["callee:00c57e60:8"]]
- 005bad68 bytes 3e731a94
+ 005bada8 bytes 2e741a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afa4f0e65c8ac4b621b3373682b69bba"></a>

### [`005baf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005baf78.md) → [`005bafb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005bafb8.md) _INIT_63

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005bb038",
      "incomplete_value": true,
      "site": "005bb054",
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
                "const:dc2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005baff8",
      "incomplete_value": true,
      "site": "005bb014",
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
                "const:d82:8"
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
      "definition_site": "005bb058",
      "incomplete_value": true,
      "site": "005bb070",
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
                "const:f62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bb018",
      "incomplete_value": true,
      "site": "005bb030",
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
                "const:e95:8"
              ]
            ]
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
      "definition_site": "005bb074",
      "incomplete_value": true,
      "site": "005bb090",
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
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bb034",
      "incomplete_value": true,
      "site": "005bb050",
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
                "const:592:8"
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
      "005baff4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005bb018",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005bb038",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005baff4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005bb018",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005bb038",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005baff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005baf78.md#insn-005baff0) · [`005bb010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005baf78.md#insn-005bb010) · [`005bb1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005baf78.md#insn-005bb1ac)
- 新版 `005bb030`（命令位置の公開資料なし） · `005bb050`（命令位置の公開資料なし） · `005bb1ec`（命令位置の公開資料なし）

~~~diff
- 005baff0 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 005baff0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005baff0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005baff0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005bb030 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 005bb030 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005bb030 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005bb030 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005baff0 bytes 4a093691
+ 005bb030 bytes 4a093791
- 005bb010 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005bb010 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005bb010 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005bb010 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005bb050 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005bb050 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005bb050 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005bb050 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005bb010 bytes 4a553a91
+ 005bb050 bytes 4a893d91
- 005bb1ac ["INT_ADD", "register:40f0:8", ["const:5bb1ac:8", "const:4:8"]]
- 005bb1ac ["CALL", null, ["callee:00c57e30:8"]]
+ 005bb1ec ["INT_ADD", "register:40f0:8", ["const:5bb1ec:8", "const:4:8"]]
+ 005bb1ec ["CALL", null, ["callee:00c57e30:8"]]
- 005bb1ac bytes 21721a94
+ 005bb1ec bytes 11731a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7e445226dd7b6ba066be86b3834aa6e"></a>

### [`005bb344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb344.md) → [`005bb384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bb384.md) FUN_005bb384

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005bb308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb308.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487b40.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`005bb348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bb348.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.55% / 新版 90.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005bb3c4",
      "incomplete_value": false,
      "site": "005bb3d0",
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
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bb384",
      "incomplete_value": false,
      "site": "005bb390",
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
            "const:938:8"
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
      "definition_site": "005bb3f8",
      "incomplete_value": true,
      "site": "005bb408",
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
                "const:31c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bb3b8",
      "incomplete_value": true,
      "site": "005bb3c8",
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
                "const:24f:8"
              ]
            ]
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
      "definition_site": "005bb3fc",
      "incomplete_value": true,
      "site": "005bb40c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005bb3bc",
      "incomplete_value": true,
      "site": "005bb3cc",
      "value": [
        "LOAD",
        "8",
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
      "005bb3d0",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "005bb3f8",
      "READ",
      [
        "storage",
        "002a124f",
        null,
        "string"
      ]
    ],
    [
      "005bb3fc",
      "READ",
      [
        "storage",
        "002a125f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005bb3d0",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "005bb3f8",
      "READ",
      [
        "storage",
        "002a131c",
        null,
        "string"
      ]
    ],
    [
      "005bb3fc",
      "READ",
      [
        "storage",
        "002a132c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bb40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb344.md#insn-005bb40c) · [`005bb608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb344.md#insn-005bb608) · [`005bb378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb344.md#insn-005bb378)
- 新版 `005bb44c`（命令位置の公開資料なし） · `005bb648`（命令位置の公開資料なし） · `005bb3b8`（命令位置の公開資料なし）

~~~diff
- 005bb40c ["INT_ADD", "register:40f0:8", ["const:5bb40c:8", "const:4:8"]]
- 005bb40c ["CALL", null, ["callee:0043bba4:8"]]
+ 005bb44c ["INT_ADD", "register:40f0:8", ["const:5bb44c:8", "const:4:8"]]
+ 005bb44c ["CALL", null, ["callee:0043bba4:8"]]
- 005bb40c bytes d601fa97
+ 005bb44c bytes d601fa97
- 005bb608 ["INT_ADD", "register:40f0:8", ["const:5bb608:8", "const:4:8"]]
- 005bb608 ["CALL", null, ["callee:00c57fb0:8"]]
+ 005bb648 ["INT_ADD", "register:40f0:8", ["const:5bb648:8", "const:4:8"]]
+ 005bb648 ["CALL", null, ["callee:00c57fb0:8"]]
- 005bb608 bytes 6a711a94
+ 005bb648 bytes 5a721a94
- 005bb378 ["INT_ADD", "register:40f0:8", ["const:5bb378:8", "const:4:8"]]
- 005bb378 ["CALL", null, ["callee:00487e20:8"]]
+ 005bb3b8 ["INT_ADD", "register:40f0:8", ["const:5bb3b8:8", "const:4:8"]]
+ 005bb3b8 ["CALL", null, ["callee:00487e20:8"]]
- 005bb378 bytes 9a32fb97
+ 005bb3b8 bytes 9a32fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4897d0b220e2c115662617ca5d080b7"></a>

### [`005bb6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb6b8.md) → [`005bb6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bb6f8.md) FUN_005bb6f8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005bb308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb308.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)
- 新版 呼出元 1件 [`005bb348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bb348.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.17% / 新版 96.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005bb738",
      "incomplete_value": false,
      "site": "005bb73c",
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
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bb6f8",
      "incomplete_value": false,
      "site": "005bb6fc",
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
            "const:938:8"
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
      "definition_site": "005bb754",
      "incomplete_value": true,
      "site": "005bb764",
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
                "const:93e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bb714",
      "incomplete_value": true,
      "site": "005bb724",
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
                "const:8fe:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005bb758",
      "incomplete_value": true,
      "site": "005bb768",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005bb718",
      "incomplete_value": true,
      "site": "005bb728",
      "value": [
        "LOAD",
        "8",
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
      "005bb73c",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "005bb754",
      "READ",
      [
        "storage",
        "002ad8fe",
        null,
        "string"
      ]
    ],
    [
      "005bb758",
      "READ",
      [
        "storage",
        "002ad90e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005bb73c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "005bb754",
      "READ",
      [
        "storage",
        "002ad93e",
        null,
        "string"
      ]
    ],
    [
      "005bb758",
      "READ",
      [
        "storage",
        "002ad94e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bbda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb6b8.md#insn-005bbda0) · [`005bbe14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb6b8.md#insn-005bbe14) · [`005bb6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb6b8.md#insn-005bb6f0)
- 新版 `005bbde0`（命令位置の公開資料なし） · `005bbe54`（命令位置の公開資料なし） · `005bb730`（命令位置の公開資料なし）

~~~diff
- 005bbda0 ["INT_ADD", "register:40f0:8", ["const:5bbda0:8", "const:4:8"]]
- 005bbda0 ["CALL", null, ["callee:00488658:8"]]
+ 005bbde0 ["INT_ADD", "register:40f0:8", ["const:5bbde0:8", "const:4:8"]]
+ 005bbde0 ["CALL", null, ["callee:00488658:8"]]
- 005bbda0 bytes 1e32fb97
+ 005bbde0 bytes 1e32fb97
- 005bbe14 ["INT_ADD", "register:40f0:8", ["const:5bbe14:8", "const:4:8"]]
- 005bbe14 ["CALL", null, ["callee:00c57fb0:8"]]
+ 005bbe54 ["INT_ADD", "register:40f0:8", ["const:5bbe54:8", "const:4:8"]]
+ 005bbe54 ["CALL", null, ["callee:00c57fb0:8"]]
- 005bbe14 bytes 676f1a94
+ 005bbe54 bytes 57701a94
- 005bb6f0 ["INT_ADD", "register:40f0:8", ["const:5bb6f0:8", "const:4:8"]]
- 005bb6f0 ["CALL", null, ["callee:00487e20:8"]]
+ 005bb730 ["INT_ADD", "register:40f0:8", ["const:5bb730:8", "const:4:8"]]
+ 005bb730 ["CALL", null, ["callee:00487e20:8"]]
- 005bb6f0 bytes bc31fb97
+ 005bb730 bytes bc31fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bbdfeaab4a4ce86e657340dcf8cead5"></a>

### [`005bbed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bbed4.md) → [`005bbf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bbf14.md) FUN_005bbf14

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005bb308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb308.md) · 呼出先 15件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487b40.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`005bb348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bb348.md) · 呼出先 15件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.41% / 新版 93.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005bbf54",
      "incomplete_value": false,
      "site": "005bbf5c",
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
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bbf14",
      "incomplete_value": false,
      "site": "005bbf1c",
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
            "const:938:8"
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
      "definition_site": "005bbf78",
      "incomplete_value": true,
      "site": "005bbf88",
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
                "const:197:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bbf38",
      "incomplete_value": true,
      "site": "005bbf48",
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
                "const:ca:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005bbf7c",
      "incomplete_value": true,
      "site": "005bbf8c",
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
      "definition_site": "005bbf3c",
      "incomplete_value": true,
      "site": "005bbf4c",
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
      "005bbf5c",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "005bbf78",
      "READ",
      [
        "storage",
        "002a20ca",
        null,
        "string"
      ]
    ],
    [
      "005bbf7c",
      "READ",
      [
        "storage",
        "002a20d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005bbf5c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "005bbf78",
      "READ",
      [
        "storage",
        "002a2197",
        null,
        "string"
      ]
    ],
    [
      "005bbf7c",
      "READ",
      [
        "storage",
        "002a21a0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bbf08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bbed4.md#insn-005bbf08) · [`005bbf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bbed4.md#insn-005bbf90) · [`005bbf14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bbed4.md#insn-005bbf14)
- 新版 `005bbf48`（命令位置の公開資料なし） · `005bbfd0`（命令位置の公開資料なし） · `005bbf54`（命令位置の公開資料なし）

~~~diff
- 005bbf08 ["INT_ADD", "register:40f0:8", ["const:5bbf08:8", "const:4:8"]]
- 005bbf08 ["CALL", null, ["callee:00487e20:8"]]
+ 005bbf48 ["INT_ADD", "register:40f0:8", ["const:5bbf48:8", "const:4:8"]]
+ 005bbf48 ["CALL", null, ["callee:00487e20:8"]]
- 005bbf08 bytes b62ffb97
+ 005bbf48 bytes b62ffb97
- 005bbf90 ["INT_ADD", "register:40f0:8", ["const:5bbf90:8", "const:4:8"]]
- 005bbf90 ["CALL", null, ["callee:0048791c:8"]]
+ 005bbfd0 ["INT_ADD", "register:40f0:8", ["const:5bbfd0:8", "const:4:8"]]
+ 005bbfd0 ["CALL", null, ["callee:0048791c:8"]]
- 005bbf90 bytes 532efb97
+ 005bbfd0 bytes 532efb97
- 005bbf14 ["COPY", "tmp:0:8", ["const:938:8"]]
- 005bbf14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005bbf14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005bbf14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005bbf54 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 005bbf54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005bbf54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005bbf54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005bbf14 bytes 29e12491
+ 005bbf54 bytes 29e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5e74b3ad6a6b413d6fb3f582df91523"></a>

### [`005bc1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc1f8.md) → [`005bc238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc238.md) FUN_005bc238

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005bb308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb308.md) · 呼出先 15件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487b40.md)
- 新版 呼出元 1件 [`005bb348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bb348.md) · 呼出先 15件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.41% / 新版 88.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005bc27c",
      "incomplete_value": false,
      "site": "005bc284",
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
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bc23c",
      "incomplete_value": false,
      "site": "005bc244",
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
            "const:938:8"
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
      "definition_site": "005bc2a0",
      "incomplete_value": true,
      "site": "005bc2b0",
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
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:7a4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bc260",
      "incomplete_value": true,
      "site": "005bc270",
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
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:764:8"
              ]
            ]
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
      "definition_site": "005bc2a4",
      "incomplete_value": true,
      "site": "005bc2b4",
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
      "definition_site": "005bc264",
      "incomplete_value": true,
      "site": "005bc274",
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
      "005bc284",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "005bc2a0",
      "READ",
      [
        "storage",
        "002bc764",
        null,
        "string"
      ]
    ],
    [
      "005bc2a4",
      "READ",
      [
        "storage",
        "002bc76d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005bc284",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "005bc2a0",
      "READ",
      [
        "storage",
        "002bc7a4",
        null,
        "string"
      ]
    ],
    [
      "005bc2a4",
      "READ",
      [
        "storage",
        "002bc7ad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bc230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc1f8.md#insn-005bc230) · [`005bc3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc1f8.md#insn-005bc3f0) · [`005bc23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc1f8.md#insn-005bc23c)
- 新版 `005bc270`（命令位置の公開資料なし） · `005bc430`（命令位置の公開資料なし） · `005bc27c`（命令位置の公開資料なし）

~~~diff
- 005bc230 ["INT_ADD", "register:40f0:8", ["const:5bc230:8", "const:4:8"]]
- 005bc230 ["CALL", null, ["callee:00487e20:8"]]
+ 005bc270 ["INT_ADD", "register:40f0:8", ["const:5bc270:8", "const:4:8"]]
+ 005bc270 ["CALL", null, ["callee:00487e20:8"]]
- 005bc230 bytes ec2efb97
+ 005bc270 bytes ec2efb97
- 005bc3f0 ["INT_ADD", "register:40f0:8", ["const:5bc3f0:8", "const:4:8"]]
- 005bc3f0 ["CALL", null, ["callee:00c57fb0:8"]]
+ 005bc430 ["INT_ADD", "register:40f0:8", ["const:5bc430:8", "const:4:8"]]
+ 005bc430 ["CALL", null, ["callee:00c57fb0:8"]]
- 005bc3f0 bytes f06d1a94
+ 005bc430 bytes e06e1a94
- 005bc23c ["COPY", "tmp:0:8", ["const:938:8"]]
- 005bc23c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005bc23c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005bc23c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005bc27c ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 005bc27c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005bc27c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005bc27c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005bc23c bytes 29e12491
+ 005bc27c bytes 29e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dca3afe96f9745905b473775b1b4c19c"></a>

### [`005bc4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc4d8.md) → [`005bc518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc518.md) FUN_005bc518

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005bb308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb308.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487b40.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`005bb348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bb348.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.74% / 新版 87.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005bc558",
      "incomplete_value": false,
      "site": "005bc568",
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
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bc518",
      "incomplete_value": false,
      "site": "005bc528",
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
            "const:938:8"
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
      "definition_site": "005bc58c",
      "incomplete_value": true,
      "site": "005bc59c",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bc54c",
      "incomplete_value": true,
      "site": "005bc55c",
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
                "const:fc9:8"
              ]
            ]
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
      "definition_site": "005bc590",
      "incomplete_value": true,
      "site": "005bc5a0",
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
      "definition_site": "005bc550",
      "incomplete_value": true,
      "site": "005bc560",
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
      "005bc568",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "005bc58c",
      "READ",
      [
        "storage",
        "002b4fc9",
        null,
        "string"
      ]
    ],
    [
      "005bc590",
      "READ",
      [
        "storage",
        "002b4fd7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005bc568",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "005bc58c",
      "READ",
      [
        "storage",
        "002b5009",
        null,
        "string"
      ]
    ],
    [
      "005bc590",
      "READ",
      [
        "storage",
        "002b5017",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bc5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc4d8.md#insn-005bc5a0) · [`005bc6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc4d8.md#insn-005bc6e4) · [`005bc50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc4d8.md#insn-005bc50c)
- 新版 `005bc5e0`（命令位置の公開資料なし） · `005bc724`（命令位置の公開資料なし） · `005bc54c`（命令位置の公開資料なし）

~~~diff
- 005bc5a0 ["INT_ADD", "register:40f0:8", ["const:5bc5a0:8", "const:4:8"]]
- 005bc5a0 ["CALL", null, ["callee:0043bba4:8"]]
+ 005bc5e0 ["INT_ADD", "register:40f0:8", ["const:5bc5e0:8", "const:4:8"]]
+ 005bc5e0 ["CALL", null, ["callee:0043bba4:8"]]
- 005bc5a0 bytes 71fdf997
+ 005bc5e0 bytes 71fdf997
- 005bc6e4 ["INT_ADD", "register:40f0:8", ["const:5bc6e4:8", "const:4:8"]]
- 005bc6e4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 005bc724 ["INT_ADD", "register:40f0:8", ["const:5bc724:8", "const:4:8"]]
+ 005bc724 ["CALL", null, ["callee:00c57fb0:8"]]
- 005bc6e4 bytes 336d1a94
+ 005bc724 bytes 236e1a94
- 005bc50c ["INT_ADD", "register:40f0:8", ["const:5bc50c:8", "const:4:8"]]
- 005bc50c ["CALL", null, ["callee:00487e20:8"]]
+ 005bc54c ["INT_ADD", "register:40f0:8", ["const:5bc54c:8", "const:4:8"]]
+ 005bc54c ["CALL", null, ["callee:00487e20:8"]]
- 005bc50c bytes 352efb97
+ 005bc54c bytes 352efb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a92e0e3297698d167984c68c7e2612b"></a>

### [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) → [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) FUN_005bc7cc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00aefce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefce0.md) [`00af0298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0298.md) · 呼出先 59件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`0046da94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da94.md)
- 新版 呼出元 2件 [`00af0108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0108.md) [`00af06c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af06c0.md) · 呼出先 59件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046dabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dabc.md) [`0046dad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dad4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.46% / 新版 99.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005bcbb8",
      "incomplete_value": true,
      "site": "005bcbc4",
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
                "const:a10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bcb78",
      "incomplete_value": true,
      "site": "005bcb84",
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
                "const:9d0:8"
              ]
            ]
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
      "definition_site": "005bde28",
      "incomplete_value": true,
      "site": "005bde30",
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
      "definition_site": "005bdde8",
      "incomplete_value": true,
      "site": "005bddf0",
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
    "ordinal": 213,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005bde34",
      "incomplete_value": true,
      "site": "005bde38",
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
                "const:a10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bddf4",
      "incomplete_value": true,
      "site": "005bddf8",
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
                "const:9d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 214,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005bcb10",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "005bcbb8",
      "READ",
      [
        "storage",
        "002c29d0",
        null,
        null
      ]
    ],
    [
      "005bcc80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007ef644"
      ]
    ]
  ],
  "added": [
    [
      "005bcb10",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "005bcbb8",
      "READ",
      [
        "storage",
        "002c2a10",
        null,
        null
      ]
    ],
    [
      "005bcc80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007ef684"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bcc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md#insn-005bcc40) · [`005bcd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md#insn-005bcd94) · [`005bc7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md#insn-005bc7cc)
- 新版 `005bcc80`（命令位置の公開資料なし） · `005bcdd4`（命令位置の公開資料なし） · `005bc80c`（命令位置の公開資料なし）

~~~diff
- 005bcc40 ["INT_ADD", "register:40f0:8", ["const:5bcc40:8", "const:4:8"]]
- 005bcc40 ["CALL", null, ["ram:7ef644:8"]]
+ 005bcc80 ["INT_ADD", "register:40f0:8", ["const:5bcc80:8", "const:4:8"]]
+ 005bcc80 ["CALL", null, ["ram:7ef684:8"]]
- 005bcc40 bytes 81ca0894
+ 005bcc80 bytes 81ca0894
- 005bcd94 ["INT_ADD", "register:40f0:8", ["const:5bcd94:8", "const:4:8"]]
- 005bcd94 ["CALL", null, ["ram:afdfe4:8"]]
+ 005bcdd4 ["INT_ADD", "register:40f0:8", ["const:5bcdd4:8", "const:4:8"]]
+ 005bcdd4 ["CALL", null, ["ram:afe40c:8"]]
- 005bcd94 bytes 94041594
+ 005bcdd4 bytes 8e051594
- 005bc7cc ["INT_ADD", "register:40f0:8", ["const:5bc7cc:8", "const:4:8"]]
- 005bc7cc ["CALL", null, ["callee:008514f8:8"]]
+ 005bc80c ["INT_ADD", "register:40f0:8", ["const:5bc80c:8", "const:4:8"]]
+ 005bc80c ["CALL", null, ["callee:008514f8:8"]]
- 005bc7cc bytes 3b530a94
+ 005bc80c bytes 3b530a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-041b00166122c1a54237623c322e35cb"></a>

### [`005c17f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17f0.md) → [`005c1830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1830.md) FUN_005c1830

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005bbed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bbed4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`005bbf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bbf14.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005c183c",
      "incomplete_value": false,
      "site": "005c1840",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c17fc",
      "incomplete_value": false,
      "site": "005c1800",
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
      "005c183c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005c183c",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c1800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17f0.md#insn-005c1800) · [`005c17fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17f0.md#insn-005c17fc)
- 新版 `005c1840`（命令位置の公開資料なし） · `005c183c`（命令位置の公開資料なし）

~~~diff
- 005c1800 ["INT_ADD", "register:40f0:8", ["const:5c1800:8", "const:4:8"]]
- 005c1800 ["CALL", null, ["callee:0043b778:8"]]
+ 005c1840 ["INT_ADD", "register:40f0:8", ["const:5c1840:8", "const:4:8"]]
+ 005c1840 ["CALL", null, ["callee:0043b778:8"]]
- 005c1800 bytes cee7f997
+ 005c1840 bytes cee7f997
- 005c17fc ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005c17fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005c17fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005c17fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005c183c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005c183c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005c183c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005c183c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005c17fc bytes 00303c91
+ 005c183c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f5eceaac9ae54aa95b5f5dd7aa3ec63"></a>

### [`005c1804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1804.md) → [`005c1844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1844.md) FUN_005c1844

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 9件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`006847bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/006847bc.md) [`007435b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/007435b0.md) [`00744438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744438.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 2件 [`005c19bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c19bc.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 9件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`006847fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/006847fc.md) [`007435f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/007435f0.md) [`00744478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744478.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 2件 [`005c19fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c19fc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c197c",
      "incomplete_value": true,
      "site": "005c1988",
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
                "const:b60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c193c",
      "incomplete_value": true,
      "site": "005c1948",
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
                "const:b20:8"
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
      "005c1960",
      "READ",
      [
        "storage",
        "002c2b70",
        null,
        null
      ]
    ],
    [
      "005c196c",
      "READ",
      [
        "storage",
        "002c26b0",
        null,
        null
      ]
    ],
    [
      "005c197c",
      "READ",
      [
        "storage",
        "002c2b20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005c1960",
      "READ",
      [
        "storage",
        "002c2bb0",
        null,
        null
      ]
    ],
    [
      "005c196c",
      "READ",
      [
        "storage",
        "002c26f0",
        null,
        null
      ]
    ],
    [
      "005c197c",
      "READ",
      [
        "storage",
        "002c2b60",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c1920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1804.md#insn-005c1920) · [`005c192c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1804.md#insn-005c192c) · [`005c193c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1804.md#insn-005c193c)
- 新版 `005c1960`（命令位置の公開資料なし） · `005c196c`（命令位置の公開資料なし） · `005c197c`（命令位置の公開資料なし）

~~~diff
- 005c1920 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b70:8"]]
- 005c1920 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 005c1920 ["COPY", "register:5010:8", ["const:0:8"]]
- 005c1920 ["COPY", "register:5018:8", ["const:0:8"]]
+ 005c1960 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bb0:8"]]
+ 005c1960 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 005c1960 ["COPY", "register:5010:8", ["const:0:8"]]
+ 005c1960 ["COPY", "register:5018:8", ["const:0:8"]]
- 005c1920 bytes 00ddc23d
+ 005c1960 bytes 00edc23d
- 005c192c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:6b0:8"]]
- 005c192c ["LOAD", "register:5040:16", ["const:1b1:8", "tmp:0:8"]]
- 005c192c ["COPY", "register:5050:8", ["const:0:8"]]
- 005c192c ["COPY", "register:5058:8", ["const:0:8"]]
+ 005c196c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:6f0:8"]]
+ 005c196c ["LOAD", "register:5040:16", ["const:1b1:8", "tmp:0:8"]]
+ 005c196c ["COPY", "register:5050:8", ["const:0:8"]]
+ 005c196c ["COPY", "register:5058:8", ["const:0:8"]]
- 005c192c bytes 42adc13d
+ 005c196c bytes 42bdc13d
- 005c193c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b20:8"]]
- 005c193c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 005c193c ["COPY", "register:5010:8", ["const:0:8"]]
- 005c193c ["COPY", "register:5018:8", ["const:0:8"]]
+ 005c197c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b60:8"]]
+ 005c197c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 005c197c ["COPY", "register:5010:8", ["const:0:8"]]
+ 005c197c ["COPY", "register:5018:8", ["const:0:8"]]
- 005c193c bytes 00c9c23d
+ 005c197c bytes 00d9c23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9268db1a6872df56864175049847bf53"></a>

### [`005c1c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c88.md) → [`005c1cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1cc8.md) FUN_005c1cc8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005c1cd4",
      "incomplete_value": false,
      "site": "005c1cd8",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c1c94",
      "incomplete_value": false,
      "site": "005c1c98",
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
      "005c1cd4",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005c1cd4",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c1c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c88.md#insn-005c1c98) · [`005c1c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c88.md#insn-005c1c94)
- 新版 `005c1cd8`（命令位置の公開資料なし） · `005c1cd4`（命令位置の公開資料なし）

~~~diff
- 005c1c98 ["INT_ADD", "register:40f0:8", ["const:5c1c98:8", "const:4:8"]]
- 005c1c98 ["CALL", null, ["callee:0043b778:8"]]
+ 005c1cd8 ["INT_ADD", "register:40f0:8", ["const:5c1cd8:8", "const:4:8"]]
+ 005c1cd8 ["CALL", null, ["callee:0043b778:8"]]
- 005c1c98 bytes a8e6f997
+ 005c1cd8 bytes a8e6f997
- 005c1c94 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005c1c94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005c1c94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005c1c94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005c1cd4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005c1cd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005c1cd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005c1cd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005c1c94 bytes 00303c91
+ 005c1cd4 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ffb56a2bc10ab8de7a18000323cf5c1"></a>

### [`005c1c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c9c.md) → [`005c1cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1cdc.md) FUN_005c1cdc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`0069f0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069f/0069f0bc.md) [`006a2a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2a50.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 8件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`0069a504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) [`0069f0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069f/0069f0fc.md) [`006a2a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2a90.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005c1ce8",
      "incomplete_value": false,
      "site": "005c1cec",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c1ca8",
      "incomplete_value": false,
      "site": "005c1cac",
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
      "005c1ce8",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005c1ce8",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c1cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c9c.md#insn-005c1cac) · [`005c1ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c9c.md#insn-005c1ca8)
- 新版 `005c1cec`（命令位置の公開資料なし） · `005c1ce8`（命令位置の公開資料なし）

~~~diff
- 005c1cac ["INT_ADD", "register:40f0:8", ["const:5c1cac:8", "const:4:8"]]
- 005c1cac ["CALL", null, ["callee:0043b778:8"]]
+ 005c1cec ["INT_ADD", "register:40f0:8", ["const:5c1cec:8", "const:4:8"]]
+ 005c1cec ["CALL", null, ["callee:0043b778:8"]]
- 005c1cac bytes a3e6f997
+ 005c1cec bytes a3e6f997
- 005c1ca8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005c1ca8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005c1ca8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005c1ca8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005c1ce8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005c1ce8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005c1ce8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005c1ce8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005c1ca8 bytes 00303c91
+ 005c1ce8 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84f2eeaa6821940a24f64ab0c6f0a26a"></a>

### [`005c3e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e8c.md) → [`005c3ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3ecc.md) _INIT_64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c3f2c",
      "incomplete_value": true,
      "site": "005c3f48",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c3eec",
      "incomplete_value": true,
      "site": "005c3f08",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:ef9:8"
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
      "definition_site": "005c3f88",
      "incomplete_value": true,
      "site": "005c3fa4",
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
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c3f48",
      "incomplete_value": true,
      "site": "005c3f64",
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
                "const:592:8"
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
      "definition_site": "005c3fa8",
      "incomplete_value": true,
      "site": "005c3fc4",
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
                "const:f5d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c3f68",
      "incomplete_value": true,
      "site": "005c3f84",
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
                "const:e90:8"
              ]
            ]
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
      "005c3f08",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005c3f2c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005c3f4c",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005c3f08",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005c3f2c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005c3f4c",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c3f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e8c.md#insn-005c3f24) · [`005c40c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e8c.md#insn-005c40c0) · [`005c3eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e8c.md#insn-005c3eb8)
- 新版 `005c3f64`（命令位置の公開資料なし） · `005c4100`（命令位置の公開資料なし） · `005c3ef8`（命令位置の公開資料なし）

~~~diff
- 005c3f24 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005c3f24 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005c3f24 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005c3f24 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005c3f64 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005c3f64 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005c3f64 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005c3f64 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005c3f24 bytes 4a553a91
+ 005c3f64 bytes 4a893d91
- 005c40c0 ["INT_ADD", "register:40f0:8", ["const:5c40c0:8", "const:4:8"]]
- 005c40c0 ["CALL", null, ["callee:00c57e30:8"]]
+ 005c4100 ["INT_ADD", "register:40f0:8", ["const:5c4100:8", "const:4:8"]]
+ 005c4100 ["CALL", null, ["callee:00c57e30:8"]]
- 005c40c0 bytes 5c4e1a94
+ 005c4100 bytes 4c4f1a94
- 005c3eb8 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 005c3eb8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005c3eb8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005c3eb8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005c3ef8 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 005c3ef8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005c3ef8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005c3ef8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005c3eb8 bytes 73821291
+ 005c3ef8 bytes 73822291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1801401a3fa85784ea88f78bfa7cb02a"></a>

### [`005c421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c421c.md) → [`005c425c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c425c.md) FUN_005c425c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) · 呼出先 16件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`005c4560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4560.md) [`006875e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00687/006875e8.md)
- 新版 呼出元 1件 [`005c8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c8efc.md) · 呼出先 16件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`005c45a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c45a0.md) [`00687628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/00687628.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.02% / 新版 89.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c4374",
      "incomplete_value": true,
      "site": "005c4384",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:e2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c4334",
      "incomplete_value": true,
      "site": "005c4344",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:a2:8"
              ]
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
    "kind": "store_value",
    "new": {
      "definition_site": "005c4388",
      "incomplete_value": true,
      "site": "005c4388",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005c4348",
      "incomplete_value": true,
      "site": "005c4348",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005c4494",
      "incomplete_value": false,
      "site": "005c4498",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c4454",
      "incomplete_value": false,
      "site": "005c4458",
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
            "const:b38:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005c4304",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "005c4320",
      "READ",
      [
        "storage",
        "002b0d5c",
        null,
        "string"
      ]
    ],
    [
      "005c4324",
      "READ",
      [
        "storage",
        "002b0d6b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005c4304",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "005c4320",
      "READ",
      [
        "storage",
        "002b0d9c",
        null,
        "string"
      ]
    ],
    [
      "005c4324",
      "READ",
      [
        "storage",
        "002b0dab",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c4384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c421c.md#insn-005c4384) · [`005c4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c421c.md#insn-005c4418) · [`005c4454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c421c.md#insn-005c4454)
- 新版 `005c43c4`（命令位置の公開資料なし） · `005c4458`（命令位置の公開資料なし） · `005c4494`（命令位置の公開資料なし）

~~~diff
- 005c4384 ["INT_ADD", "register:40f0:8", ["const:5c4384:8", "const:4:8"]]
- 005c4384 ["CALL", null, ["callee:00c53d00:8"]]
+ 005c43c4 ["INT_ADD", "register:40f0:8", ["const:5c43c4:8", "const:4:8"]]
+ 005c43c4 ["CALL", null, ["callee:00c53d00:8"]]
- 005c4384 bytes 573d1a94
+ 005c43c4 bytes 4f3e1a94
- 005c4418 ["COPY", "register:0:8", ["register:4040:8"]]
- 005c4418 ["INT_ADD", "register:40f0:8", ["const:5c4418:8", "const:4:8"]]
- 005c4418 ["CALLIND", null, ["register:0:8"]]
+ 005c4458 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005c4458 ["INT_ADD", "register:40f0:8", ["const:5c4458:8", "const:4:8"]]
+ 005c4458 ["CALLIND", null, ["register:0:8"]]
- 005c4418 bytes 00013fd6
+ 005c4458 bytes 00013fd6
- 005c4454 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 005c4454 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005c4454 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005c4454 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005c4494 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 005c4494 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005c4494 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005c4494 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005c4454 bytes 00e02c91
+ 005c4494 bytes 00e03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0548839001f71cf39507c0a600ff1910"></a>

### [`005c4560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4560.md) → [`005c45a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c45a0.md) FUN_005c45a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005c421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c421c.md) [`005c6938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md) · 呼出先 12件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00684f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/00684f70.md) [`00685334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685334.md) [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006875e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00687/006875e8.md)
- 新版 呼出元 2件 [`005c425c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c425c.md) [`005c6978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6978.md) · 呼出先 12件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00684fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684fb0.md) [`00685374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685374.md) [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`00687628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00687/00687628.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.14% / 新版 95.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c4728",
      "incomplete_value": true,
      "site": "005c4728",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:b3b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c46e8",
      "incomplete_value": true,
      "site": "005c46e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
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
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c471c",
      "incomplete_value": true,
      "site": "005c472c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005c46dc",
      "incomplete_value": true,
      "site": "005c46ec",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005c4618",
      "incomplete_value": false,
      "site": "005c4620",
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
            "const:7be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c45d8",
      "incomplete_value": false,
      "site": "005c45e0",
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
            "const:77e:8"
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
      "005c4618",
      "PARAM",
      [
        "storage",
        "002bc77e",
        null,
        null
      ]
    ],
    [
      "005c4718",
      "READ",
      [
        "storage",
        "002bdafb",
        null,
        "string"
      ]
    ],
    [
      "005c471c",
      "READ",
      [
        "storage",
        "002bdb02",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005c4618",
      "PARAM",
      [
        "storage",
        "002bc7be",
        null,
        null
      ]
    ],
    [
      "005c4718",
      "READ",
      [
        "storage",
        "002bdb3b",
        null,
        "string"
      ]
    ],
    [
      "005c471c",
      "READ",
      [
        "storage",
        "002bdb42",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c45e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4560.md#insn-005c45e0) · [`005c46a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4560.md#insn-005c46a8) · [`005c4594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4560.md#insn-005c4594)
- 新版 `005c4620`（命令位置の公開資料なし） · `005c46e8`（命令位置の公開資料なし） · `005c45d4`（命令位置の公開資料なし）

~~~diff
- 005c45e0 ["INT_ADD", "register:40f0:8", ["const:5c45e0:8", "const:4:8"]]
- 005c45e0 ["CALL", null, ["callee:00c57f70:8"]]
+ 005c4620 ["INT_ADD", "register:40f0:8", ["const:5c4620:8", "const:4:8"]]
+ 005c4620 ["CALL", null, ["callee:00c57f70:8"]]
- 005c45e0 bytes 644d1a94
+ 005c4620 bytes 544e1a94
- 005c46a8 ["INT_ADD", "register:40f0:8", ["const:5c46a8:8", "const:4:8"]]
- 005c46a8 ["CALL", null, ["callee:008514f8:8"]]
+ 005c46e8 ["INT_ADD", "register:40f0:8", ["const:5c46e8:8", "const:4:8"]]
+ 005c46e8 ["CALL", null, ["callee:008514f8:8"]]
- 005c46a8 bytes 84330a94
+ 005c46e8 bytes 84330a94
- 005c4594 ["INT_ADD", "register:40f0:8", ["const:5c4594:8", "const:4:8"]]
- 005c4594 ["CALL", null, ["callee:008514f8:8"]]
+ 005c45d4 ["INT_ADD", "register:40f0:8", ["const:5c45d4:8", "const:4:8"]]
+ 005c45d4 ["CALL", null, ["callee:008514f8:8"]]
- 005c4594 bytes c9330a94
+ 005c45d4 bytes c9330a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ae0bc9e4e908bd25d2212d26f9c1869"></a>

### [`005c4918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md) → [`005c4958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c4958.md) FUN_005c4958

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005c7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md) · 呼出先 30件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00469c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469c8c.md) [`0046a210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a210.md)
- 新版 呼出元 1件 [`005c7d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7d00.md) · 呼出先 30件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00469ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469ccc.md) [`0046a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.41% / 新版 98.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005c4c38",
      "incomplete_value": true,
      "site": "005c4c50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:978:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c4bf8",
      "incomplete_value": true,
      "site": "005c4c10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:578:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005c4c40",
      "incomplete_value": false,
      "site": "005c4c50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c4c00",
      "incomplete_value": false,
      "site": "005c4c10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "definition_site": "005c4c48",
      "incomplete_value": false,
      "site": "005c4c50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c4c08",
      "incomplete_value": false,
      "site": "005c4c10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005c4c38",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "005c4c40",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005c4c48",
      "PARAM",
      [
        "storage",
        "00c70dc0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005c4c38",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "005c4c40",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005c4c48",
      "PARAM",
      [
        "storage",
        "00c711c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c4c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md#insn-005c4c10) · [`005c4c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md#insn-005c4c50) · [`005c4cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md#insn-005c4cf0)
- 新版 `005c4c50`（命令位置の公開資料なし） · `005c4c90`（命令位置の公開資料なし） · `005c4d30`（命令位置の公開資料なし）

~~~diff
- 005c4c10 ["INT_ADD", "register:40f0:8", ["const:5c4c10:8", "const:4:8"]]
- 005c4c10 ["CALL", null, ["callee:00c58610:8"]]
+ 005c4c50 ["INT_ADD", "register:40f0:8", ["const:5c4c50:8", "const:4:8"]]
+ 005c4c50 ["CALL", null, ["callee:00c58610:8"]]
- 005c4c10 bytes 804d1a94
+ 005c4c50 bytes 704e1a94
- 005c4c50 ["INT_ADD", "register:40f0:8", ["const:5c4c50:8", "const:4:8"]]
- 005c4c50 ["CALL", null, ["callee:00a468fc:8"]]
+ 005c4c90 ["INT_ADD", "register:40f0:8", ["const:5c4c90:8", "const:4:8"]]
+ 005c4c90 ["CALL", null, ["callee:00a468fc:8"]]
- 005c4c50 bytes ad061294
+ 005c4c90 bytes 1b071294
- 005c4cf0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005c4cf0 ["INT_ADD", "register:40f0:8", ["const:5c4cf0:8", "const:4:8"]]
- 005c4cf0 ["CALLIND", null, ["register:0:8"]]
+ 005c4d30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005c4d30 ["INT_ADD", "register:40f0:8", ["const:5c4d30:8", "const:4:8"]]
+ 005c4d30 ["CALLIND", null, ["register:0:8"]]
- 005c4cf0 bytes 00013fd6
+ 005c4d30 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b821aceb9f11a7d6457972d1c0c8cd56"></a>

### [`005c6114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6114.md) → [`005c6154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6154.md) FUN_005c6154

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00a46458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46458.md) · 呼出先 2件 [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 8件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00a46650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46650.md) · 呼出先 2件 [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c617c",
      "incomplete_value": true,
      "site": "005c617c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005c613c",
      "incomplete_value": true,
      "site": "005c613c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005c6174",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ],
    [
      "005c617c",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005c6174",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ],
    [
      "005c617c",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c612c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6114.md#insn-005c612c) · [`005c6134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6114.md#insn-005c6134) · [`005c6140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6114.md#insn-005c6140)
- 新版 `005c616c`（命令位置の公開資料なし） · `005c6174`（命令位置の公開資料なし） · `005c6180`（命令位置の公開資料なし）

~~~diff
- 005c612c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005c616c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005c612c bytes a8360090
+ 005c616c bytes a83600b0
- 005c6134 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f68:8"]]
- 005c6134 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005c6174 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 005c6174 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005c6134 bytes 08b547f9
+ 005c6174 bytes 08b541f9
- 005c6140 ["INT_ADD", "register:40f0:8", ["const:5c6140:8", "const:4:8"]]
- 005c6140 ["CALL", null, ["callee:005d8bc8:8"]]
+ 005c6180 ["INT_ADD", "register:40f0:8", ["const:5c6180:8", "const:4:8"]]
+ 005c6180 ["CALL", null, ["callee:005d8bc8:8"]]
- 005c6140 bytes 924a0094
+ 005c6180 bytes 924a0094
~~~


<a id="compare-1a07b03786f7390d6c50e2e291bbe337"></a>

### [`005c6160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6160.md) → [`005c61a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c61a0.md) FUN_005c61a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 4件 [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 4件 [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.86% / 新版 82.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005c61c4",
      "incomplete_value": false,
      "site": "005c61c8",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:7a0:8"
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
      "definition_site": "005c6184",
      "incomplete_value": false,
      "site": "005c6188",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:3a0:8"
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c6208",
      "incomplete_value": true,
      "site": "005c6208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005c61c8",
      "incomplete_value": true,
      "site": "005c61c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005c61c8",
      "DATA",
      [
        "storage",
        "00c8b3b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005c6200",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ],
    [
      "005c6208",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005c61c8",
      "DATA",
      [
        "storage",
        "00c8b7b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005c6200",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ],
    [
      "005c6208",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c617c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6160.md#insn-005c617c) · [`005c6198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6160.md#insn-005c6198) · [`005c61ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6160.md#insn-005c61ac)
- 新版 `005c61bc`（命令位置の公開資料なし） · `005c61d8`（命令位置の公開資料なし） · `005c61ec`（命令位置の公開資料なし）

~~~diff
- 005c617c ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 005c617c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005c617c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005c617c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005c61bc ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 005c61bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005c61bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005c61bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005c617c bytes 08810e91
+ 005c61bc bytes 08811e91
- 005c6198 ["INT_ADD", "register:40f0:8", ["const:5c6198:8", "const:4:8"]]
- 005c6198 ["CALL", null, ["callee:00c53d00:8"]]
+ 005c61d8 ["INT_ADD", "register:40f0:8", ["const:5c61d8:8", "const:4:8"]]
+ 005c61d8 ["CALL", null, ["callee:00c53d00:8"]]
- 005c6198 bytes d2351a94
+ 005c61d8 bytes ca361a94
- 005c61ac ["COPY", "register:0:8", ["register:4040:8"]]
- 005c61ac ["INT_ADD", "register:40f0:8", ["const:5c61ac:8", "const:4:8"]]
- 005c61ac ["CALLIND", null, ["register:0:8"]]
+ 005c61ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 005c61ec ["INT_ADD", "register:40f0:8", ["const:5c61ec:8", "const:4:8"]]
+ 005c61ec ["CALLIND", null, ["register:0:8"]]
- 005c61ac bytes 00013fd6
+ 005c61ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf89e213ac861662a6b9adfb9eaab9cd"></a>

### [`005c62c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c62c0.md) → [`005c6300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6300.md) FUN_005c6300

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0098527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/0098527c.md) · 呼出先 23件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)
- 新版 呼出元 1件 [`00985418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00985/00985418.md) · 呼出先 23件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005c6490",
      "incomplete_value": false,
      "site": "005c6498",
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
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c6450",
      "incomplete_value": false,
      "site": "005c6458",
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
            "const:938:8"
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
      "definition_site": "005c64c0",
      "incomplete_value": true,
      "site": "005c64c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:bdc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c6480",
      "incomplete_value": true,
      "site": "005c6480",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:b9c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c6834",
      "incomplete_value": true,
      "site": "005c6838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005c67f4",
      "incomplete_value": true,
      "site": "005c67f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 68,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005c6498",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "005c64ac",
      "READ",
      [
        "storage",
        "002afb9c",
        null,
        "string"
      ]
    ],
    [
      "005c64b4",
      "READ",
      [
        "storage",
        "002afba2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005c6498",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "005c64ac",
      "READ",
      [
        "storage",
        "002afbdc",
        null,
        "string"
      ]
    ],
    [
      "005c64b4",
      "READ",
      [
        "storage",
        "002afbe2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c6440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c62c0.md#insn-005c6440) · [`005c67dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c62c0.md#insn-005c67dc) · [`005c683c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c62c0.md#insn-005c683c)
- 新版 `005c6480`（命令位置の公開資料なし） · `005c681c`（命令位置の公開資料なし） · `005c687c`（命令位置の公開資料なし）

~~~diff
- 005c6440 ["INT_ADD", "register:40f0:8", ["const:5c6440:8", "const:4:8"]]
- 005c6440 ["CALL", null, ["callee:00487e20:8"]]
+ 005c6480 ["INT_ADD", "register:40f0:8", ["const:5c6480:8", "const:4:8"]]
+ 005c6480 ["CALL", null, ["callee:00487e20:8"]]
- 005c6440 bytes 6806fb97
+ 005c6480 bytes 6806fb97
- 005c67dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7b0:8"]]
- 005c67dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005c681c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bb0:8"]]
+ 005c681c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005c67dc bytes 08d943f9
+ 005c681c bytes 08d945f9
- 005c683c ["INT_ADD", "register:40f0:8", ["const:5c683c:8", "const:4:8"]]
- 005c683c ["CALL", null, ["callee:00c57fb0:8"]]
+ 005c687c ["INT_ADD", "register:40f0:8", ["const:5c687c:8", "const:4:8"]]
+ 005c687c ["CALL", null, ["callee:00c57fb0:8"]]
- 005c683c bytes dd441a94
+ 005c687c bytes cd451a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd3ab372c3a9e13da6b485296b62868b"></a>

### [`005c6938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md) → [`005c6978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6978.md) FUN_005c6978

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 37件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044d8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d8e0.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046da14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da14.md) [`0046da94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da94.md)
- 新版 呼出元 1件 [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 37件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044d920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d920.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046da54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da54.md) [`0046dad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dad4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.88% / 新版 98.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005c6a60",
      "incomplete_value": true,
      "site": "005c6a60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:263:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c6a20",
      "incomplete_value": true,
      "site": "005c6a20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:223:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005c6a34",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005c69f4",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005c6cd8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005c6c98",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 44,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005c69e0",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "005c69f8",
      "DATA",
      [
        "storage",
        "0039b1bc",
        "fde_0039b1bc",
        "dword"
      ]
    ],
    [
      "005c6a10",
      "DATA",
      [
        "storage",
        "0039b1bc",
        "fde_0039b1bc",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "005c69e0",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "005c69f8",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "uleb128"
      ]
    ],
    [
      "005c6a10",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "uleb128"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c69f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md#insn-005c69f4) · [`005c6c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md#insn-005c6c98) · [`005c6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md#insn-005c6d50)
- 新版 `005c6a34`（命令位置の公開資料なし） · `005c6cd8`（命令位置の公開資料なし） · `005c6d90`（命令位置の公開資料なし）

~~~diff
- 005c69f4 ["INT_ADD", "register:40f0:8", ["const:5c69f4:8", "const:4:8"]]
- 005c69f4 ["CALL", null, ["ram:48ccb8:8"]]
+ 005c6a34 ["INT_ADD", "register:40f0:8", ["const:5c6a34:8", "const:4:8"]]
+ 005c6a34 ["CALL", null, ["ram:48ccf8:8"]]
- 005c69f4 bytes b118fb97
+ 005c6a34 bytes b118fb97
- 005c6c98 ["INT_ADD", "register:40f0:8", ["const:5c6c98:8", "const:4:8"]]
- 005c6c98 ["CALL", null, ["ram:47acb4:8"]]
+ 005c6cd8 ["INT_ADD", "register:40f0:8", ["const:5c6cd8:8", "const:4:8"]]
+ 005c6cd8 ["CALL", null, ["ram:47acf4:8"]]
- 005c6c98 bytes 07d0fa97
+ 005c6cd8 bytes 07d0fa97
- 005c6d50 ["INT_ADD", "register:40f0:8", ["const:5c6d50:8", "const:4:8"]]
- 005c6d50 ["CALL", null, ["ram:46c984:8"]]
+ 005c6d90 ["INT_ADD", "register:40f0:8", ["const:5c6d90:8", "const:4:8"]]
+ 005c6d90 ["CALL", null, ["ram:46c9c4:8"]]
- 005c6d50 bytes 0d97fa97
+ 005c6d90 bytes 0d97fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-185b100200640e2e9b16f462bd808683"></a>

### [`005c71e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c71e0.md) → [`005c7220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7220.md) FUN_005c7220

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005c6938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md) · 呼出先 12件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00859b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b0c.md) [`0085b264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b264.md)
- 新版 呼出元 1件 [`005c6978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6978.md) · 呼出先 12件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00859b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b4c.md) [`0085b2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2a4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.78% / 新版 98.78%

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
      "site": "005c72e4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005c72a4",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005c7520",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005c74e0",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 26,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005c7238",
      "READ",
      [
        "storage",
        "002c4118",
        null,
        "undefined8"
      ]
    ],
    [
      "005c72e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "005c7520",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "005c7238",
      "READ",
      [
        "storage",
        "002c4158",
        null,
        "undefined8"
      ]
    ],
    [
      "005c72e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "005c7520",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c72a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c71e0.md#insn-005c72a4) · [`005c72e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c71e0.md#insn-005c72e4) · [`005c74a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c71e0.md#insn-005c74a0)
- 新版 `005c72e4`（命令位置の公開資料なし） · `005c7324`（命令位置の公開資料なし） · `005c74e0`（命令位置の公開資料なし）

~~~diff
- 005c72a4 ["INT_ADD", "register:40f0:8", ["const:5c72a4:8", "const:4:8"]]
- 005c72a4 ["CALL", null, ["ram:47acb4:8"]]
+ 005c72e4 ["INT_ADD", "register:40f0:8", ["const:5c72e4:8", "const:4:8"]]
+ 005c72e4 ["CALL", null, ["ram:47acf4:8"]]
- 005c72a4 bytes 84cefa97
+ 005c72e4 bytes 84cefa97
- 005c72e4 ["INT_ADD", "register:40f0:8", ["const:5c72e4:8", "const:4:8"]]
- 005c72e4 ["CALL", null, ["callee:008b6eac:8"]]
+ 005c7324 ["INT_ADD", "register:40f0:8", ["const:5c7324:8", "const:4:8"]]
+ 005c7324 ["CALL", null, ["callee:008b6eac:8"]]
- 005c72e4 bytes e1be0b94
+ 005c7324 bytes e2be0b94
- 005c74a0 ["INT_ADD", "register:40f0:8", ["const:5c74a0:8", "const:4:8"]]
- 005c74a0 ["CALL", null, ["callee:008514f8:8"]]
+ 005c74e0 ["INT_ADD", "register:40f0:8", ["const:5c74e0:8", "const:4:8"]]
+ 005c74e0 ["CALL", null, ["callee:008514f8:8"]]
- 005c74a0 bytes 06280a94
+ 005c74e0 bytes 06280a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbe955620707c34253fd602b5e31c59c"></a>

### [`005c7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md) → [`005c7d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7d00.md) FUN_005c7d00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) · 呼出先 29件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d74.md) [`00467edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467edc.md)
- 新版 呼出元 1件 [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) · 呼出先 29件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md) [`00467f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f1c.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 5件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005c8344",
      "incomplete_value": true,
      "site": "005c8344",
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
      "definition_site": "005c8304",
      "incomplete_value": true,
      "site": "005c8304",
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
    "ordinal": 21,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005c7d58",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005c7d18",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005c7d98",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005c7d58",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "005c7d58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "005c7d98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "005c7f7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "005c7d58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "005c7d98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "005c7f7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c7d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md#insn-005c7d18) · [`005c7d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md#insn-005c7d58) · [`005c7f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md#insn-005c7f3c)
- 新版 `005c7d58`（命令位置の公開資料なし） · `005c7d98`（命令位置の公開資料なし） · `005c7f7c`（命令位置の公開資料なし）

~~~diff
- 005c7d18 ["INT_ADD", "register:40f0:8", ["const:5c7d18:8", "const:4:8"]]
- 005c7d18 ["CALL", null, ["ram:46c984:8"]]
+ 005c7d58 ["INT_ADD", "register:40f0:8", ["const:5c7d58:8", "const:4:8"]]
+ 005c7d58 ["CALL", null, ["ram:46c9c4:8"]]
- 005c7d18 bytes 1b93fa97
+ 005c7d58 bytes 1b93fa97
- 005c7d58 ["INT_ADD", "register:40f0:8", ["const:5c7d58:8", "const:4:8"]]
- 005c7d58 ["CALL", null, ["ram:46c984:8"]]
+ 005c7d98 ["INT_ADD", "register:40f0:8", ["const:5c7d98:8", "const:4:8"]]
+ 005c7d98 ["CALL", null, ["ram:46c9c4:8"]]
- 005c7d58 bytes 0b93fa97
+ 005c7d98 bytes 0b93fa97
- 005c7f3c ["INT_ADD", "register:40f0:8", ["const:5c7f3c:8", "const:4:8"]]
- 005c7f3c ["CALL", null, ["ram:46c984:8"]]
+ 005c7f7c ["INT_ADD", "register:40f0:8", ["const:5c7f7c:8", "const:4:8"]]
+ 005c7f7c ["CALL", null, ["ram:46c9c4:8"]]
- 005c7f3c bytes 9292fa97
+ 005c7f7c bytes 9292fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d40cf32fd2748cbc9f66d0f7178bea1"></a>

### [`005c8780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8780.md) → [`005c87c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c87c0.md) FUN_005c87c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005d9f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9f0c.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`005c767c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c767c.md) [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)
- 新版 呼出元 1件 [`005d9f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9f4c.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005c76bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c76bc.md) [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.78% / 新版 99.78%

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
      "site": "005c89c8",
      "value": [
        "leaf",
        "ram:71c460:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005c8988",
      "value": [
        "leaf",
        "ram:71c420:8"
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
      "005c89c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ]
  ],
  "added": [
    [
      "005c89c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c460"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c8948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8780.md#insn-005c8948) · [`005c8988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8780.md#insn-005c8988) · [`005c87b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8780.md#insn-005c87b8)
- 新版 `005c8988`（命令位置の公開資料なし） · `005c89c8`（命令位置の公開資料なし） · `005c87f8`（命令位置の公開資料なし）

~~~diff
- 005c8948 ["INT_ADD", "register:40f0:8", ["const:5c8948:8", "const:4:8"]]
- 005c8948 ["CALL", null, ["callee:008b6ea4:8"]]
+ 005c8988 ["INT_ADD", "register:40f0:8", ["const:5c8988:8", "const:4:8"]]
+ 005c8988 ["CALL", null, ["callee:008b6ea4:8"]]
- 005c8948 bytes 46b90b94
+ 005c8988 bytes 47b90b94
- 005c8988 ["INT_ADD", "register:40f0:8", ["const:5c8988:8", "const:4:8"]]
- 005c8988 ["CALL", null, ["ram:71c420:8"]]
+ 005c89c8 ["INT_ADD", "register:40f0:8", ["const:5c89c8:8", "const:4:8"]]
+ 005c89c8 ["CALL", null, ["ram:71c460:8"]]
- 005c8988 bytes a64e0594
+ 005c89c8 bytes a64e0594
- 005c87b8 ["INT_ADD", "register:40f0:8", ["const:5c87b8:8", "const:4:8"]]
- 005c87b8 ["CALL", null, ["callee:00b071ec:8"]]
+ 005c87f8 ["INT_ADD", "register:40f0:8", ["const:5c87f8:8", "const:4:8"]]
+ 005c87f8 ["CALL", null, ["callee:00b071ec:8"]]
- 005c87b8 bytes 83f91494
+ 005c87f8 bytes 7dfa1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0b39d78e0b304df4ddc6428f9fe6ffa"></a>

### [`005cc174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc174.md) → [`005cc1b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005cc1b4.md) FUN_005cc1b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 1件 [`005c8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c8efc.md) · 呼出先 12件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.97% / 新版 84.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005cc2a8",
      "incomplete_value": true,
      "site": "005cc2bc",
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
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:7c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cc268",
      "incomplete_value": true,
      "site": "005cc27c",
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
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:783:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005cc2e0",
      "incomplete_value": true,
      "site": "005cc2f0",
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
                "const:1b1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cc2a0",
      "incomplete_value": true,
      "site": "005cc2b0",
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
                "const:e4:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005cc2f4",
      "incomplete_value": true,
      "site": "005cc2f4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005cc2b4",
      "incomplete_value": true,
      "site": "005cc2b4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 36,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005cc294",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "005cc2a8",
      "READ",
      [
        "storage",
        "002bc783",
        null,
        "string"
      ]
    ],
    [
      "005cc2e0",
      "READ",
      [
        "storage",
        "002a20e4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005cc294",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "005cc2a8",
      "READ",
      [
        "storage",
        "002bc7c3",
        null,
        "string"
      ]
    ],
    [
      "005cc2e0",
      "READ",
      [
        "storage",
        "002a21b1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cc290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc174.md#insn-005cc290) · [`005cc2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc174.md#insn-005cc2bc) · [`005cc2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc174.md#insn-005cc2d0)
- 新版 `005cc2d0`（命令位置の公開資料なし） · `005cc2fc`（命令位置の公開資料なし） · `005cc310`（命令位置の公開資料なし）

~~~diff
- 005cc290 ["INT_ADD", "register:40f0:8", ["const:5cc290:8", "const:4:8"]]
- 005cc290 ["CALL", null, ["callee:00447ef4:8"]]
+ 005cc2d0 ["INT_ADD", "register:40f0:8", ["const:5cc2d0:8", "const:4:8"]]
+ 005cc2d0 ["CALL", null, ["callee:00447ef4:8"]]
- 005cc290 bytes 09eff997
+ 005cc2d0 bytes 09eff997
- 005cc2bc ["COPY", "tmp:0:8", ["const:b00:8"]]
- 005cc2bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005cc2bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005cc2bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005cc2fc ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 005cc2fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005cc2fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005cc2fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005cc2bc bytes 00002c91
+ 005cc2fc bytes 00003c91
- 005cc2d0 ["INT_ADD", "register:40f0:8", ["const:5cc2d0:8", "const:4:8"]]
- 005cc2d0 ["CALL", null, ["callee:0047e60c:8"]]
+ 005cc310 ["INT_ADD", "register:40f0:8", ["const:5cc310:8", "const:4:8"]]
+ 005cc310 ["CALL", null, ["callee:0047e60c:8"]]
- 005cc2d0 bytes bfc8fa97
+ 005cc310 bytes bfc8fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b67ce5d9c698a00cbedb02d6b8d20b9"></a>

### [`005cc4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc4d4.md) → [`005cc514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005cc514.md) FUN_005cc514

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 4件 [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 4件 [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.86% / 新版 82.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005cc538",
      "incomplete_value": false,
      "site": "005cc53c",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:7a0:8"
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
      "definition_site": "005cc4f8",
      "incomplete_value": false,
      "site": "005cc4fc",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:3a0:8"
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005cc57c",
      "incomplete_value": true,
      "site": "005cc57c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cc53c",
      "incomplete_value": true,
      "site": "005cc53c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005cc53c",
      "DATA",
      [
        "storage",
        "00c8b3b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005cc574",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ],
    [
      "005cc57c",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005cc53c",
      "DATA",
      [
        "storage",
        "00c8b7b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005cc574",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ],
    [
      "005cc57c",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cc4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc4d4.md#insn-005cc4f0) · [`005cc50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc4d4.md#insn-005cc50c) · [`005cc520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc4d4.md#insn-005cc520)
- 新版 `005cc530`（命令位置の公開資料なし） · `005cc54c`（命令位置の公開資料なし） · `005cc560`（命令位置の公開資料なし）

~~~diff
- 005cc4f0 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 005cc4f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005cc4f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005cc4f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005cc530 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 005cc530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005cc530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005cc530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005cc4f0 bytes 08810e91
+ 005cc530 bytes 08811e91
- 005cc50c ["INT_ADD", "register:40f0:8", ["const:5cc50c:8", "const:4:8"]]
- 005cc50c ["CALL", null, ["callee:00c53d00:8"]]
+ 005cc54c ["INT_ADD", "register:40f0:8", ["const:5cc54c:8", "const:4:8"]]
+ 005cc54c ["CALL", null, ["callee:00c53d00:8"]]
- 005cc50c bytes f51c1a94
+ 005cc54c bytes ed1d1a94
- 005cc520 ["COPY", "register:0:8", ["register:4040:8"]]
- 005cc520 ["INT_ADD", "register:40f0:8", ["const:5cc520:8", "const:4:8"]]
- 005cc520 ["CALLIND", null, ["register:0:8"]]
+ 005cc560 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005cc560 ["INT_ADD", "register:40f0:8", ["const:5cc560:8", "const:4:8"]]
+ 005cc560 ["CALLIND", null, ["register:0:8"]]
- 005cc520 bytes 00013fd6
+ 005cc560 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15f2e57fb0777e81973bea3853673e07"></a>

### [`005cccc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cccc4.md) → [`005ccd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005ccd04.md) FUN_005ccd04

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`006788a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00678/006788a0.md) [`006ac8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ac/006ac8d8.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) [`0092472c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00924/0092472c.md) · 呼出先 16件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 7件 [`006788e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00678/006788e0.md) [`006ac918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ac/006ac918.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`00914e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00914/00914e30.md) [`009248c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00924/009248c8.md) · 呼出先 16件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.17% / 新版 90.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ccd7c",
      "incomplete_value": true,
      "site": "005ccd90",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:47f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ccd3c",
      "incomplete_value": true,
      "site": "005ccd50",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:43f:8"
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
      "definition_site": "005ccd80",
      "incomplete_value": true,
      "site": "005ccd94",
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
      "definition_site": "005ccd40",
      "incomplete_value": true,
      "site": "005ccd54",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ccd84",
      "incomplete_value": true,
      "site": "005ccd98",
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
                "const:a90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ccd44",
      "incomplete_value": true,
      "site": "005ccd58",
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
                "const:a50:8"
              ]
            ]
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
      "005ccd58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "005ccd7c",
      "READ",
      [
        "storage",
        "002ba43f",
        null,
        "string"
      ]
    ],
    [
      "005ccd80",
      "READ",
      [
        "storage",
        "002ba449",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005ccd58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "005ccd7c",
      "READ",
      [
        "storage",
        "002ba47f",
        null,
        "string"
      ]
    ],
    [
      "005ccd80",
      "READ",
      [
        "storage",
        "002ba489",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ccd18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cccc4.md#insn-005ccd18) · [`005ccd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cccc4.md#insn-005ccd88) · [`005ccda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cccc4.md#insn-005ccda0)
- 新版 `005ccd58`（命令位置の公開資料なし） · `005ccdc8`（命令位置の公開資料なし） · `005ccde0`（命令位置の公開資料なし）

~~~diff
- 005ccd18 ["INT_ADD", "register:40f0:8", ["const:5ccd18:8", "const:4:8"]]
- 005ccd18 ["CALL", null, ["ram:47acb4:8"]]
+ 005ccd58 ["INT_ADD", "register:40f0:8", ["const:5ccd58:8", "const:4:8"]]
+ 005ccd58 ["CALL", null, ["ram:47acf4:8"]]
- 005ccd18 bytes e7b7fa97
+ 005ccd58 bytes e7b7fa97
- 005ccd88 ["INT_ADD", "register:40f0:8", ["const:5ccd88:8", "const:4:8"]]
- 005ccd88 ["CALL", null, ["ram:664860:8"]]
+ 005ccdc8 ["INT_ADD", "register:40f0:8", ["const:5ccdc8:8", "const:4:8"]]
+ 005ccdc8 ["CALL", null, ["ram:6648a0:8"]]
- 005ccd88 bytes b65e0294
+ 005ccdc8 bytes b65e0294
- 005ccda0 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 005ccda0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ccda0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ccda0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ccde0 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 005ccde0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ccde0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ccde0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ccda0 bytes 08a13f91
+ 005ccde0 bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c164ab4a5b638a0448952e2625273932"></a>

### [`005cd0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd0b0.md) → [`005cd0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd0f0.md) FUN_005cd0f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 54件 [`005cccc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cccc4.md) [`005db448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db448.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0060a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060a/0060a860.md) [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) · 呼出先 14件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00493d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493d88.md) [`005cd620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd620.md) [`005d5c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md)
- 新版 呼出元 53件 [`005ccd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005ccd04.md) [`005db488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005db/005db488.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0060a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060a/0060a8a0.md) [`0060e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060e0c4.md) · 呼出先 14件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00493dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493dc8.md) [`005cd660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd660.md) [`005d5c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5c60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.57% / 新版 99.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cd128",
      "incomplete_value": false,
      "site": "005cd13c",
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
            "const:a73:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cd0e8",
      "incomplete_value": false,
      "site": "005cd0fc",
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
            "const:997:8"
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
      "005cd128",
      "PARAM",
      [
        "storage",
        "002a7997",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005cd128",
      "PARAM",
      [
        "storage",
        "002a7a73",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cd0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd0b0.md#insn-005cd0fc) · [`005cd0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd0b0.md#insn-005cd0e8) · [`005cd148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd0b0.md#insn-005cd148)
- 新版 `005cd13c`（命令位置の公開資料なし） · `005cd128`（命令位置の公開資料なし） · `005cd188`（命令位置の公開資料なし）

~~~diff
- 005cd0fc ["INT_ADD", "register:40f0:8", ["const:5cd0fc:8", "const:4:8"]]
- 005cd0fc ["CALL", null, ["callee:005cd660:8"]]
+ 005cd13c ["INT_ADD", "register:40f0:8", ["const:5cd13c:8", "const:4:8"]]
+ 005cd13c ["CALL", null, ["callee:005cd660:8"]]
- 005cd0fc bytes 49010094
+ 005cd13c bytes 49010094
- 005cd0e8 ["COPY", "tmp:0:8", ["const:997:8"]]
- 005cd0e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005cd0e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005cd0e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005cd128 ["COPY", "tmp:0:8", ["const:a73:8"]]
+ 005cd128 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005cd128 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005cd128 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005cd0e8 bytes 215c2691
+ 005cd128 bytes 21cc2991
- 005cd148 ["INT_ADD", "register:40f0:8", ["const:5cd148:8", "const:4:8"]]
- 005cd148 ["CALL", null, ["callee:0043bb20:8"]]
+ 005cd188 ["INT_ADD", "register:40f0:8", ["const:5cd188:8", "const:4:8"]]
+ 005cd188 ["CALL", null, ["callee:0043bb20:8"]]
- 005cd148 bytes 66baf997
+ 005cd188 bytes 66baf997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeeba3af6583f887c00ac6b06c038da1"></a>

### [`005cd620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd620.md) → [`005cd660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd660.md) FUN_005cd660

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005cd0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd0b0.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 8件 [`005cd728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd728.md) [`005cd778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd778.md) [`005cdabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdabc.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 2件 [`005cd0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd0f0.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 8件 [`005cd768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd768.md) [`005cd7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd7b8.md) [`005cdafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cdafc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

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
      "definition_site": "005cd688",
      "incomplete_value": true,
      "site": "005cd68c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cd648",
      "incomplete_value": true,
      "site": "005cd64c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
      "definition_site": "005cd69c",
      "incomplete_value": true,
      "site": "005cd6a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:378:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cd65c",
      "incomplete_value": true,
      "site": "005cd660",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f78:8"
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
      "005cd688",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "005cd688",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005cd69c",
      "READ",
      [
        "storage",
        "00c9af78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cd688",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "005cd688",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005cd69c",
      "READ",
      [
        "storage",
        "00c9b378",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cd64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd620.md#insn-005cd64c) · [`005cd660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd620.md#insn-005cd660) · [`005cd63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd620.md#insn-005cd63c)
- 新版 `005cd68c`（命令位置の公開資料なし） · `005cd6a0`（命令位置の公開資料なし） · `005cd67c`（命令位置の公開資料なし）

~~~diff
- 005cd64c ["INT_ADD", "register:40f0:8", ["const:5cd64c:8", "const:4:8"]]
- 005cd64c ["CALL", null, ["callee:00c58280:8"]]
+ 005cd68c ["INT_ADD", "register:40f0:8", ["const:5cd68c:8", "const:4:8"]]
+ 005cd68c ["CALL", null, ["callee:00c58280:8"]]
- 005cd64c bytes 0d2a1a94
+ 005cd68c bytes fd2a1a94
- 005cd660 ["INT_ADD", "register:40f0:8", ["const:5cd660:8", "const:4:8"]]
- 005cd660 ["CALL", null, ["callee:00c58280:8"]]
+ 005cd6a0 ["INT_ADD", "register:40f0:8", ["const:5cd6a0:8", "const:4:8"]]
+ 005cd6a0 ["CALL", null, ["callee:00c58280:8"]]
- 005cd660 bytes 082a1a94
+ 005cd6a0 bytes f82a1a94
- 005cd63c ["INT_ADD", "register:40f0:8", ["const:5cd63c:8", "const:4:8"]]
- 005cd63c ["CALL", null, ["callee:00c5a7a0:8"]]
+ 005cd67c ["INT_ADD", "register:40f0:8", ["const:5cd67c:8", "const:4:8"]]
+ 005cd67c ["CALL", null, ["callee:00c5a7a0:8"]]
- 005cd63c bytes 59331a94
+ 005cd67c bytes 49341a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d33d88d32509cb8d605f52955ffce6d4"></a>

### [`005cd778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd778.md) → [`005cd7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd7b8.md) FUN_005cd7b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005cd620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd620.md) [`005ce5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md) · 呼出先 11件 [`005cdcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdcc0.md) [`005cde4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cde4c.md) [`005cdfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdfc0.md) [`005ce174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce174.md) [`005ce328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce328.md)
- 新版 呼出元 2件 [`005cd660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd660.md) [`005ce600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce600.md) · 呼出先 11件 [`005cdd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cdd00.md) [`005cde8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cde8c.md) [`005ce000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce000.md) [`005ce1b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce1b4.md) [`005ce368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce368.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005cd7f4",
      "incomplete_value": true,
      "site": "005cd7f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cd7b4",
      "incomplete_value": true,
      "site": "005cd7b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cd814",
      "incomplete_value": true,
      "site": "005cd814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cd7d4",
      "incomplete_value": true,
      "site": "005cd7d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005cd838",
      "incomplete_value": true,
      "site": "005cd838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cd7f8",
      "incomplete_value": true,
      "site": "005cd7f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005cd7f0",
      "READ",
      [
        "storage",
        "00c9af80",
        null,
        "pointer"
      ]
    ],
    [
      "005cd7f8",
      "DATA",
      [
        "storage",
        "00c70698",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cd80c",
      "READ",
      [
        "storage",
        "00c9af88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cd7f0",
      "READ",
      [
        "storage",
        "00c9b380",
        null,
        "pointer"
      ]
    ],
    [
      "005cd7f8",
      "DATA",
      [
        "storage",
        "00c70a98",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cd80c",
      "READ",
      [
        "storage",
        "00c9b388",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cd7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd778.md#insn-005cd7a4) · [`005cd7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd778.md#insn-005cd7a8) · [`005cd7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd778.md#insn-005cd7b0)
- 新版 `005cd7e4`（命令位置の公開資料なし） · `005cd7e8`（命令位置の公開資料なし） · `005cd7f0`（命令位置の公開資料なし）

~~~diff
- 005cd7a4 ["INT_ADD", "register:40f0:8", ["const:5cd7a4:8", "const:4:8"]]
- 005cd7a4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005cd7e4 ["INT_ADD", "register:40f0:8", ["const:5cd7e4:8", "const:4:8"]]
+ 005cd7e4 ["CALL", null, ["callee:00c57e90:8"]]
- 005cd7a4 bytes bb281a94
+ 005cd7e4 bytes ab291a94
- 005cd7a8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005cd7e8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005cd7a8 bytes 683600b0
+ 005cd7e8 bytes 683600d0
- 005cd7b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f80:8"]]
- 005cd7b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cd7f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:380:8"]]
+ 005cd7f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005cd7b0 bytes 08c147f9
+ 005cd7f0 bytes 08c141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4234c4562d07c7c0e35facd15f9ce3eb"></a>

### [`005cdabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdabc.md) → [`005cdafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cdafc.md) FUN_005cdafc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005cd620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd620.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 1件 [`005cd660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd660.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cdb28",
      "incomplete_value": true,
      "site": "005cdb30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cdae8",
      "incomplete_value": true,
      "site": "005cdaf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005cdb2c",
      "incomplete_value": true,
      "site": "005cdb30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cdaec",
      "incomplete_value": true,
      "site": "005cdaf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005cdb28",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005cdb28",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005cdb2c",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cdb28",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005cdb28",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005cdb2c",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cdaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdabc.md#insn-005cdaf0) · [`005cdacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdabc.md#insn-005cdacc) · [`005cdad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdabc.md#insn-005cdad8)
- 新版 `005cdb30`（命令位置の公開資料なし） · `005cdb0c`（命令位置の公開資料なし） · `005cdb18`（命令位置の公開資料なし）

~~~diff
- 005cdaf0 ["INT_ADD", "register:40f0:8", ["const:5cdaf0:8", "const:4:8"]]
- 005cdaf0 ["CALL", null, ["callee:00c57f10:8"]]
+ 005cdb30 ["INT_ADD", "register:40f0:8", ["const:5cdb30:8", "const:4:8"]]
+ 005cdb30 ["CALL", null, ["callee:00c57f10:8"]]
- 005cdaf0 bytes 08281a94
+ 005cdb30 bytes f8281a94
- 005cdacc ["INT_ADD", "register:40f0:8", ["const:5cdacc:8", "const:4:8"]]
- 005cdacc ["CALL", null, ["callee:00c57ef0:8"]]
+ 005cdb0c ["INT_ADD", "register:40f0:8", ["const:5cdb0c:8", "const:4:8"]]
+ 005cdb0c ["CALL", null, ["callee:00c57ef0:8"]]
- 005cdacc bytes 09281a94
+ 005cdb0c bytes f9281a94
- 005cdad8 ["INT_ADD", "register:40f0:8", ["const:5cdad8:8", "const:4:8"]]
- 005cdad8 ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005cdb18 ["INT_ADD", "register:40f0:8", ["const:5cdb18:8", "const:4:8"]]
+ 005cdb18 ["CALL", null, ["callee:00c5a7b0:8"]]
- 005cdad8 bytes 36321a94
+ 005cdb18 bytes 26331a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31b26ee7662069fbfb6af062c01df862"></a>

### [`005cdcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdcc0.md) → [`005cdd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cdd00.md) FUN_005cdd00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005cd778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd778.md) [`005cdfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdfc0.md) · 呼出先 4件 [`005d5170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5170.md) [`005d51bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md) [`005d53c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`005cd7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd7b8.md) [`005ce000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce000.md) · 呼出先 4件 [`005d51b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d51b0.md) [`005d51fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d51fc.md) [`005d5408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5408.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

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
      "definition_site": "005cdd5c",
      "incomplete_value": true,
      "site": "005cdd74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cdd1c",
      "incomplete_value": true,
      "site": "005cdd34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cde34",
      "incomplete_value": true,
      "site": "005cde4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cddf4",
      "incomplete_value": true,
      "site": "005cde0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005cdd48",
      "READ",
      [
        "storage",
        "00c9afc0",
        null,
        "pointer"
      ]
    ],
    [
      "005cdd74",
      "DATA",
      [
        "storage",
        "00c707e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cde28",
      "READ",
      [
        "storage",
        "00c9afc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cdd48",
      "READ",
      [
        "storage",
        "00c9b3c0",
        null,
        "pointer"
      ]
    ],
    [
      "005cdd74",
      "DATA",
      [
        "storage",
        "00c70be8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cde28",
      "READ",
      [
        "storage",
        "00c9b3c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cdcf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdcc0.md#insn-005cdcf8) · [`005cdd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdcc0.md#insn-005cdd00) · [`005cdd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdcc0.md#insn-005cdd08)
- 新版 `005cdd38`（命令位置の公開資料なし） · `005cdd40`（命令位置の公開資料なし） · `005cdd48`（命令位置の公開資料なし）

~~~diff
- 005cdcf8 ["INT_ADD", "register:40f0:8", ["const:5cdcf8:8", "const:4:8"]]
- 005cdcf8 ["CALL", null, ["callee:00c57e90:8"]]
+ 005cdd38 ["INT_ADD", "register:40f0:8", ["const:5cdd38:8", "const:4:8"]]
+ 005cdd38 ["CALL", null, ["callee:00c57e90:8"]]
- 005cdcf8 bytes 66271a94
+ 005cdd38 bytes 56281a94
- 005cdd00 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 005cdd40 ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 005cdd00 bytes 6a3600b0
+ 005cdd40 bytes 6a3600d0
- 005cdd08 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:fc0:8"]]
- 005cdd08 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cdd48 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:3c0:8"]]
+ 005cdd48 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 005cdd08 bytes 4ae147f9
+ 005cdd48 bytes 4ae141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f1ff76abaf793aadf28d799047ccad8"></a>

### [`005ce328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce328.md) → [`005ce368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce368.md) FUN_005ce368

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005cd778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd778.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 1件 [`005cd7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd7b8.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005ce394",
      "incomplete_value": true,
      "site": "005ce39c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ce354",
      "incomplete_value": true,
      "site": "005ce35c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005ce398",
      "incomplete_value": true,
      "site": "005ce39c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ce358",
      "incomplete_value": true,
      "site": "005ce35c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005ce394",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005ce394",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ce398",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ce394",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005ce394",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ce398",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ce35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce328.md#insn-005ce35c) · [`005ce338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce328.md#insn-005ce338) · [`005ce344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce328.md#insn-005ce344)
- 新版 `005ce39c`（命令位置の公開資料なし） · `005ce378`（命令位置の公開資料なし） · `005ce384`（命令位置の公開資料なし）

~~~diff
- 005ce35c ["INT_ADD", "register:40f0:8", ["const:5ce35c:8", "const:4:8"]]
- 005ce35c ["CALL", null, ["callee:00c57f10:8"]]
+ 005ce39c ["INT_ADD", "register:40f0:8", ["const:5ce39c:8", "const:4:8"]]
+ 005ce39c ["CALL", null, ["callee:00c57f10:8"]]
- 005ce35c bytes ed251a94
+ 005ce39c bytes dd261a94
- 005ce338 ["INT_ADD", "register:40f0:8", ["const:5ce338:8", "const:4:8"]]
- 005ce338 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005ce378 ["INT_ADD", "register:40f0:8", ["const:5ce378:8", "const:4:8"]]
+ 005ce378 ["CALL", null, ["callee:00c57ef0:8"]]
- 005ce338 bytes ee251a94
+ 005ce378 bytes de261a94
- 005ce344 ["INT_ADD", "register:40f0:8", ["const:5ce344:8", "const:4:8"]]
- 005ce344 ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005ce384 ["INT_ADD", "register:40f0:8", ["const:5ce384:8", "const:4:8"]]
+ 005ce384 ["CALL", null, ["callee:00c5a7b0:8"]]
- 005ce344 bytes 1b301a94
+ 005ce384 bytes 0b311a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00865158b4b8029cffbbe313dd185411"></a>

### [`005ce5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md) → [`005ce600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce600.md) FUN_005ce600

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005ce48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce48c.md) [`005ce52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce52c.md) · 呼出先 8件 [`005cd6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd6d8.md) [`005cd778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd778.md) [`005cef3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cef3c.md) [`005cefa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cefa8.md) [`005cf05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf05c.md)
- 新版 呼出元 2件 [`005ce4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce4cc.md) [`005ce56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce56c.md) · 呼出先 8件 [`005cd718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd718.md) [`005cd7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd7b8.md) [`005cef7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005cef7c.md) [`005cefe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005cefe8.md) [`005cf09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf09c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.61% / 新版 95.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ce810",
      "incomplete_value": true,
      "site": "005ce810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ce7d0",
      "incomplete_value": true,
      "site": "005ce7d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ce860",
      "incomplete_value": true,
      "site": "005ce860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ce820",
      "incomplete_value": true,
      "site": "005ce820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005ce730",
      "READ",
      [
        "storage",
        "00c9afc0",
        null,
        "pointer"
      ]
    ],
    [
      "005ce75c",
      "READ",
      [
        "storage",
        "00c9afc8",
        null,
        "pointer"
      ]
    ],
    [
      "005ce780",
      "DATA",
      [
        "storage",
        "00c70830",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005ce730",
      "READ",
      [
        "storage",
        "00c9b3c0",
        null,
        "pointer"
      ]
    ],
    [
      "005ce75c",
      "READ",
      [
        "storage",
        "00c9b3c8",
        null,
        "pointer"
      ]
    ],
    [
      "005ce780",
      "DATA",
      [
        "storage",
        "00c70c30",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ce810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md#insn-005ce810) · [`005ce650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md#insn-005ce650) · [`005ce670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md#insn-005ce670)
- 新版 `005ce850`（命令位置の公開資料なし） · `005ce690`（命令位置の公開資料なし） · `005ce6b0`（命令位置の公開資料なし）

~~~diff
- 005ce810 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fd8:8"]]
- 005ce810 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ce850 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3d8:8"]]
+ 005ce850 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005ce810 bytes 29ed47f9
+ 005ce850 bytes 29ed41f9
- 005ce650 ["INT_ADD", "register:40f0:8", ["const:5ce650:8", "const:4:8"]]
- 005ce650 ["CALL", null, ["callee:005cef7c:8"]]
+ 005ce690 ["INT_ADD", "register:40f0:8", ["const:5ce690:8", "const:4:8"]]
+ 005ce690 ["CALL", null, ["callee:005cef7c:8"]]
- 005ce650 bytes 3b020094
+ 005ce690 bytes 3b020094
- 005ce670 ["INT_ADD", "register:40f0:8", ["const:5ce670:8", "const:4:8"]]
- 005ce670 ["CALL", null, ["callee:005cd7b8:8"]]
+ 005ce6b0 ["INT_ADD", "register:40f0:8", ["const:5ce6b0:8", "const:4:8"]]
+ 005ce6b0 ["CALL", null, ["callee:005cd7b8:8"]]
- 005ce670 bytes 42fcff97
+ 005ce6b0 bytes 42fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70afb975c89cee447561fca26ea551e9"></a>

### [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) → [`005ce964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce964.md) FUN_005ce964

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005ce48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce48c.md) [`005ce52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce52c.md) · 呼出先 10件 [`005cdb08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdb08.md) [`005cf05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf05c.md) [`005d0610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md) [`005d0764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0764.md) [`005d07b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d07b0.md)
- 新版 呼出元 2件 [`005ce4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce4cc.md) [`005ce56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce56c.md) · 呼出先 10件 [`005cdb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cdb48.md) [`005cf09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf09c.md) [`005d0650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0650.md) [`005d07a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d07a4.md) [`005d07f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d07f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ce9bc",
      "incomplete_value": true,
      "site": "005ce9cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ce97c",
      "incomplete_value": true,
      "site": "005ce98c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ceb10",
      "incomplete_value": true,
      "site": "005ceb28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cead0",
      "incomplete_value": true,
      "site": "005ceae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cebbc",
      "incomplete_value": true,
      "site": "005cebcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ceb7c",
      "incomplete_value": true,
      "site": "005ceb8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005ce9b4",
      "READ",
      [
        "storage",
        "00c9afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005ce9cc",
      "DATA",
      [
        "storage",
        "00c70908",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ceafc",
      "READ",
      [
        "storage",
        "00c9afe8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ce9b4",
      "READ",
      [
        "storage",
        "00c9b3e0",
        null,
        "pointer"
      ]
    ],
    [
      "005ce9cc",
      "DATA",
      [
        "storage",
        "00c70d08",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ceafc",
      "READ",
      [
        "storage",
        "00c9b3e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ce968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md#insn-005ce968) · [`005ce970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md#insn-005ce970) · [`005ce974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md#insn-005ce974)
- 新版 `005ce9a8`（命令位置の公開資料なし） · `005ce9b0`（命令位置の公開資料なし） · `005ce9b4`（命令位置の公開資料なし）

~~~diff
- 005ce968 ["INT_ADD", "register:40f0:8", ["const:5ce968:8", "const:4:8"]]
- 005ce968 ["CALL", null, ["callee:00c57e90:8"]]
+ 005ce9a8 ["INT_ADD", "register:40f0:8", ["const:5ce9a8:8", "const:4:8"]]
+ 005ce9a8 ["CALL", null, ["callee:00c57e90:8"]]
- 005ce968 bytes 4a241a94
+ 005ce9a8 bytes 3a251a94
- 005ce970 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 005ce9b0 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 005ce970 bytes 69360090
+ 005ce9b0 bytes 693600b0
- 005ce974 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fe0:8"]]
- 005ce974 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ce9b4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3e0:8"]]
+ 005ce9b4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005ce974 bytes 29f147f9
+ 005ce9b4 bytes 29f141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61f47f3b39e44931a48fc227d23198ae"></a>

### [`005cef3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cef3c.md) → [`005cef7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005cef7c.md) FUN_005cef7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005ce5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c5a3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3a0.md)
- 新版 呼出元 1件 [`005ce600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce600.md) · 呼出先 2件 [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c5a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cef98",
      "incomplete_value": true,
      "site": "005cef9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cef58",
      "incomplete_value": true,
      "site": "005cef5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
      "definition_site": "005cefac",
      "incomplete_value": true,
      "site": "005cefb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:378:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cef6c",
      "incomplete_value": true,
      "site": "005cef70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f78:8"
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
      "005cef98",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "005cef98",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005cefac",
      "READ",
      [
        "storage",
        "00c9af78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cef98",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "005cef98",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005cefac",
      "READ",
      [
        "storage",
        "00c9b378",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cef5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cef3c.md#insn-005cef5c) · [`005cef70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cef3c.md#insn-005cef70) · [`005cef4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cef3c.md#insn-005cef4c)
- 新版 `005cef9c`（命令位置の公開資料なし） · `005cefb0`（命令位置の公開資料なし） · `005cef8c`（命令位置の公開資料なし）

~~~diff
- 005cef5c ["INT_ADD", "register:40f0:8", ["const:5cef5c:8", "const:4:8"]]
- 005cef5c ["CALL", null, ["callee:00c58280:8"]]
+ 005cef9c ["INT_ADD", "register:40f0:8", ["const:5cef9c:8", "const:4:8"]]
+ 005cef9c ["CALL", null, ["callee:00c58280:8"]]
- 005cef5c bytes c9231a94
+ 005cef9c bytes b9241a94
- 005cef70 ["INT_ADD", "register:40f0:8", ["const:5cef70:8", "const:4:8"]]
- 005cef70 ["CALL", null, ["callee:00c58280:8"]]
+ 005cefb0 ["INT_ADD", "register:40f0:8", ["const:5cefb0:8", "const:4:8"]]
+ 005cefb0 ["CALL", null, ["callee:00c58280:8"]]
- 005cef70 bytes c4231a94
+ 005cefb0 bytes b4241a94
- 005cef4c ["INT_ADD", "register:40f0:8", ["const:5cef4c:8", "const:4:8"]]
- 005cef4c ["CALL", null, ["callee:00c5a7a0:8"]]
+ 005cef8c ["INT_ADD", "register:40f0:8", ["const:5cef8c:8", "const:4:8"]]
+ 005cef8c ["CALL", null, ["callee:00c5a7a0:8"]]
- 005cef4c bytes 152d1a94
+ 005cef8c bytes 052e1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6437b14168db5d9695676d55274fce8a"></a>

### [`005cefa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cefa8.md) → [`005cefe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005cefe8.md) FUN_005cefe8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005ce5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md) · 呼出先 3件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)
- 新版 呼出元 1件 [`005ce600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce600.md) · 呼出先 3件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005cf030",
      "incomplete_value": true,
      "site": "005cf030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ceff0",
      "incomplete_value": true,
      "site": "005ceff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005cf020",
      "READ",
      [
        "storage",
        "00c9aff8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf030",
      "DATA",
      [
        "storage",
        "00c708c0",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005cf020",
      "READ",
      [
        "storage",
        "00c9b3f8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf030",
      "DATA",
      [
        "storage",
        "00c70cc0",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cefd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cefa8.md#insn-005cefd0) · [`005cefd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cefa8.md#insn-005cefd8) · [`005cefe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cefa8.md#insn-005cefe0)
- 新版 `005cf010`（命令位置の公開資料なし） · `005cf018`（命令位置の公開資料なし） · `005cf020`（命令位置の公開資料なし）

~~~diff
- 005cefd0 ["INT_ADD", "register:40f0:8", ["const:5cefd0:8", "const:4:8"]]
- 005cefd0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005cf010 ["INT_ADD", "register:40f0:8", ["const:5cf010:8", "const:4:8"]]
+ 005cf010 ["CALL", null, ["callee:00c57e90:8"]]
- 005cefd0 bytes b0221a94
+ 005cf010 bytes a0231a94
- 005cefd8 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 005cf018 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 005cefd8 bytes 69360090
+ 005cf018 bytes 69360090
- 005cefe0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ff8:8"]]
- 005cefe0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cf020 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3f8:8"]]
+ 005cf020 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005cefe0 bytes 29fd47f9
+ 005cf020 bytes 29fd41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c35631db202cc0e5f0f610a655eade1b"></a>

### [`005cf05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf05c.md) → [`005cf09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf09c.md) FUN_005cf09c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005ce5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md) [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) [`005d51bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md) [`005d582c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d582c.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 4件 [`005ce600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce600.md) [`005ce964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce964.md) [`005d51fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d51fc.md) [`005d586c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d586c.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cf0c8",
      "incomplete_value": true,
      "site": "005cf0d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cf088",
      "incomplete_value": true,
      "site": "005cf090",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005cf0cc",
      "incomplete_value": true,
      "site": "005cf0d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cf08c",
      "incomplete_value": true,
      "site": "005cf090",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005cf0c8",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005cf0c8",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005cf0cc",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cf0c8",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005cf0c8",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005cf0cc",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cf090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf05c.md#insn-005cf090) · [`005cf06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf05c.md#insn-005cf06c) · [`005cf078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf05c.md#insn-005cf078)
- 新版 `005cf0d0`（命令位置の公開資料なし） · `005cf0ac`（命令位置の公開資料なし） · `005cf0b8`（命令位置の公開資料なし）

~~~diff
- 005cf090 ["INT_ADD", "register:40f0:8", ["const:5cf090:8", "const:4:8"]]
- 005cf090 ["CALL", null, ["callee:00c57f10:8"]]
+ 005cf0d0 ["INT_ADD", "register:40f0:8", ["const:5cf0d0:8", "const:4:8"]]
+ 005cf0d0 ["CALL", null, ["callee:00c57f10:8"]]
- 005cf090 bytes a0221a94
+ 005cf0d0 bytes 90231a94
- 005cf06c ["INT_ADD", "register:40f0:8", ["const:5cf06c:8", "const:4:8"]]
- 005cf06c ["CALL", null, ["callee:00c57ef0:8"]]
+ 005cf0ac ["INT_ADD", "register:40f0:8", ["const:5cf0ac:8", "const:4:8"]]
+ 005cf0ac ["CALL", null, ["callee:00c57ef0:8"]]
- 005cf06c bytes a1221a94
+ 005cf0ac bytes 91231a94
- 005cf078 ["INT_ADD", "register:40f0:8", ["const:5cf078:8", "const:4:8"]]
- 005cf078 ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005cf0b8 ["INT_ADD", "register:40f0:8", ["const:5cf0b8:8", "const:4:8"]]
+ 005cf0b8 ["CALL", null, ["callee:00c5a7b0:8"]]
- 005cf078 bytes ce2c1a94
+ 005cf0b8 bytes be2d1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ff904e5d415b3fbbbbe7d11de727eed"></a>

### [`005cf1e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf1e8.md) → [`005cf228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf228.md) FUN_005cf228

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005cf244",
      "incomplete_value": true,
      "site": "005cf244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cf204",
      "incomplete_value": true,
      "site": "005cf204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005cf258",
      "incomplete_value": true,
      "site": "005cf25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cf218",
      "incomplete_value": true,
      "site": "005cf21c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005cf23c",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf244",
      "DATA",
      [
        "storage",
        "00c70878",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf250",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cf23c",
      "READ",
      [
        "storage",
        "00c9b3d8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf244",
      "DATA",
      [
        "storage",
        "00c70c78",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf250",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cf1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf1e8.md#insn-005cf1f4) · [`005cf1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf1e8.md#insn-005cf1fc) · [`005cf208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf1e8.md#insn-005cf208)
- 新版 `005cf234`（命令位置の公開資料なし） · `005cf23c`（命令位置の公開資料なし） · `005cf248`（命令位置の公開資料なし）

~~~diff
- 005cf1f4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005cf234 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005cf1f4 bytes 483600f0
+ 005cf234 bytes 68360090
- 005cf1fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd8:8"]]
- 005cf1fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cf23c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3d8:8"]]
+ 005cf23c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005cf1fc bytes 08ed47f9
+ 005cf23c bytes 08ed41f9
- 005cf208 ["INT_ADD", "register:40f0:8", ["const:5cf208:8", "const:4:8"]]
- 005cf208 ["CALL", null, ["callee:00c58290:8"]]
+ 005cf248 ["INT_ADD", "register:40f0:8", ["const:5cf248:8", "const:4:8"]]
+ 005cf248 ["CALL", null, ["callee:00c58290:8"]]
- 005cf208 bytes 22231a94
+ 005cf248 bytes 12241a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68de6ecc819ab793de07f10e69753bb2"></a>

### [`005cf244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf244.md) → [`005cf284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf284.md) FUN_005cf284

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005cf2a0",
      "incomplete_value": true,
      "site": "005cf2a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cf260",
      "incomplete_value": true,
      "site": "005cf260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005cf2b4",
      "incomplete_value": true,
      "site": "005cf2b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cf274",
      "incomplete_value": true,
      "site": "005cf278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005cf298",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf2a0",
      "DATA",
      [
        "storage",
        "00c70878",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf2ac",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cf298",
      "READ",
      [
        "storage",
        "00c9b3d8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf2a0",
      "DATA",
      [
        "storage",
        "00c70c78",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf2ac",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cf250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf244.md#insn-005cf250) · [`005cf258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf244.md#insn-005cf258) · [`005cf264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf244.md#insn-005cf264)
- 新版 `005cf290`（命令位置の公開資料なし） · `005cf298`（命令位置の公開資料なし） · `005cf2a4`（命令位置の公開資料なし）

~~~diff
- 005cf250 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005cf290 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005cf250 bytes 483600f0
+ 005cf290 bytes 68360090
- 005cf258 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd8:8"]]
- 005cf258 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cf298 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3d8:8"]]
+ 005cf298 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005cf258 bytes 08ed47f9
+ 005cf298 bytes 08ed41f9
- 005cf264 ["INT_ADD", "register:40f0:8", ["const:5cf264:8", "const:4:8"]]
- 005cf264 ["CALL", null, ["callee:00c58290:8"]]
+ 005cf2a4 ["INT_ADD", "register:40f0:8", ["const:5cf2a4:8", "const:4:8"]]
+ 005cf2a4 ["CALL", null, ["callee:00c58290:8"]]
- 005cf264 bytes 0b231a94
+ 005cf2a4 bytes fb231a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bdd13d882694b9df914fe7febb304b1"></a>

### [`005cf3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf3ac.md) → [`005cf3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf3ec.md) FUN_005cf3ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

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
      "definition_site": "005cf408",
      "incomplete_value": true,
      "site": "005cf40c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cf3c8",
      "incomplete_value": true,
      "site": "005cf3cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cf450",
      "incomplete_value": true,
      "site": "005cf454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cf410",
      "incomplete_value": true,
      "site": "005cf414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005cf400",
      "READ",
      [
        "storage",
        "00c9aff8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf40c",
      "DATA",
      [
        "storage",
        "00c708c0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf448",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cf400",
      "READ",
      [
        "storage",
        "00c9b3f8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf40c",
      "DATA",
      [
        "storage",
        "00c70cc0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf448",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cf3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf3ac.md#insn-005cf3b8) · [`005cf3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf3ac.md#insn-005cf3c0) · [`005cf3dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf3ac.md#insn-005cf3dc)
- 新版 `005cf3f8`（命令位置の公開資料なし） · `005cf400`（命令位置の公開資料なし） · `005cf41c`（命令位置の公開資料なし）

~~~diff
- 005cf3b8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005cf3f8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005cf3b8 bytes 483600f0
+ 005cf3f8 bytes 68360090
- 005cf3c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff8:8"]]
- 005cf3c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cf400 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3f8:8"]]
+ 005cf400 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005cf3c0 bytes 08fd47f9
+ 005cf400 bytes 08fd41f9
- 005cf3dc ["INT_ADD", "register:40f0:8", ["const:5cf3dc:8", "const:4:8"]]
- 005cf3dc ["CALL", null, ["callee:00c53d00:8"]]
+ 005cf41c ["INT_ADD", "register:40f0:8", ["const:5cf41c:8", "const:4:8"]]
+ 005cf41c ["CALL", null, ["callee:00c53d00:8"]]
- 005cf3dc bytes 41111a94
+ 005cf41c bytes 39121a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a3f4e4408cb0953286398c6dc87d73f"></a>

### [`005cf43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf43c.md) → [`005cf47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf47c.md) FUN_005cf47c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

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
      "definition_site": "005cf498",
      "incomplete_value": true,
      "site": "005cf49c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cf458",
      "incomplete_value": true,
      "site": "005cf45c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cf4e0",
      "incomplete_value": true,
      "site": "005cf4e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005cf4a0",
      "incomplete_value": true,
      "site": "005cf4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005cf490",
      "READ",
      [
        "storage",
        "00c9aff8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf49c",
      "DATA",
      [
        "storage",
        "00c708c0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf4d8",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cf490",
      "READ",
      [
        "storage",
        "00c9b3f8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf49c",
      "DATA",
      [
        "storage",
        "00c70cc0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf4d8",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cf448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf43c.md#insn-005cf448) · [`005cf450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf43c.md#insn-005cf450) · [`005cf46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf43c.md#insn-005cf46c)
- 新版 `005cf488`（命令位置の公開資料なし） · `005cf490`（命令位置の公開資料なし） · `005cf4ac`（命令位置の公開資料なし）

~~~diff
- 005cf448 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005cf488 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005cf448 bytes 483600f0
+ 005cf488 bytes 68360090
- 005cf450 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff8:8"]]
- 005cf450 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cf490 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3f8:8"]]
+ 005cf490 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005cf450 bytes 08fd47f9
+ 005cf490 bytes 08fd41f9
- 005cf46c ["INT_ADD", "register:40f0:8", ["const:5cf46c:8", "const:4:8"]]
- 005cf46c ["CALL", null, ["callee:00c53d00:8"]]
+ 005cf4ac ["INT_ADD", "register:40f0:8", ["const:5cf4ac:8", "const:4:8"]]
+ 005cf4ac ["CALL", null, ["callee:00c53d00:8"]]
- 005cf46c bytes 1d111a94
+ 005cf4ac bytes 15121a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32d5ba2f69340c09d2d6752ba824e462"></a>

### [`005cfcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md) → [`005cfcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfcfc.md) FUN_005cfcfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005cfaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfaf4.md) [`005cfd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md) [`005d0344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0344.md) [`005d804c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d804c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 4件 [`005cfb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfb34.md) [`005cfda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfda0.md) [`005d0384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0384.md) [`005d808c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d808c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005cfd08",
      "incomplete_value": false,
      "site": "005cfd0c",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cfcc8",
      "incomplete_value": false,
      "site": "005cfccc",
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
      "005cfd08",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005cfd08",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cfccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md#insn-005cfccc) · [`005cfcc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md#insn-005cfcc8)
- 新版 `005cfd0c`（命令位置の公開資料なし） · `005cfd08`（命令位置の公開資料なし）

~~~diff
- 005cfccc ["INT_ADD", "register:40f0:8", ["const:5cfccc:8", "const:4:8"]]
- 005cfccc ["CALL", null, ["callee:0043b778:8"]]
+ 005cfd0c ["INT_ADD", "register:40f0:8", ["const:5cfd0c:8", "const:4:8"]]
+ 005cfd0c ["CALL", null, ["callee:0043b778:8"]]
- 005cfccc bytes 9baef997
+ 005cfd0c bytes 9baef997
- 005cfcc8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005cfcc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005cfcc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005cfcc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005cfd08 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005cfd08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005cfd08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005cfd08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005cfcc8 bytes 00303c91
+ 005cfd08 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55f10827df4236368c0cbcb1cf76a0a3"></a>

### [`005cfd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd14.md) → [`005cfd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfd54.md) FUN_005cfd54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 3件 [`005cf6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf6c0.md) [`005d6110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d6110.md) [`005d69f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d69f0.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cfd80",
      "incomplete_value": true,
      "site": "005cfd88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cfd40",
      "incomplete_value": true,
      "site": "005cfd48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005cfd84",
      "incomplete_value": true,
      "site": "005cfd88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cfd44",
      "incomplete_value": true,
      "site": "005cfd48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005cfd80",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005cfd80",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005cfd84",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cfd80",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005cfd80",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005cfd84",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cfd48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd14.md#insn-005cfd48) · [`005cfd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd14.md#insn-005cfd24) · [`005cfd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd14.md#insn-005cfd30)
- 新版 `005cfd88`（命令位置の公開資料なし） · `005cfd64`（命令位置の公開資料なし） · `005cfd70`（命令位置の公開資料なし）

~~~diff
- 005cfd48 ["INT_ADD", "register:40f0:8", ["const:5cfd48:8", "const:4:8"]]
- 005cfd48 ["CALL", null, ["callee:00c57f10:8"]]
+ 005cfd88 ["INT_ADD", "register:40f0:8", ["const:5cfd88:8", "const:4:8"]]
+ 005cfd88 ["CALL", null, ["callee:00c57f10:8"]]
- 005cfd48 bytes 721f1a94
+ 005cfd88 bytes 62201a94
- 005cfd24 ["INT_ADD", "register:40f0:8", ["const:5cfd24:8", "const:4:8"]]
- 005cfd24 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005cfd64 ["INT_ADD", "register:40f0:8", ["const:5cfd64:8", "const:4:8"]]
+ 005cfd64 ["CALL", null, ["callee:00c57ef0:8"]]
- 005cfd24 bytes 731f1a94
+ 005cfd64 bytes 63201a94
- 005cfd30 ["INT_ADD", "register:40f0:8", ["const:5cfd30:8", "const:4:8"]]
- 005cfd30 ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005cfd70 ["INT_ADD", "register:40f0:8", ["const:5cfd70:8", "const:4:8"]]
+ 005cfd70 ["CALL", null, ["callee:00c5a7b0:8"]]
- 005cfd30 bytes a0291a94
+ 005cfd70 bytes 902a1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbfc5f5f3ac0fa9bc2d6d6c404222993"></a>

### [`005cfed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfed8.md) → [`005cff18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cff18.md) FUN_005cff18

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 3件 [`005cf6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf6c0.md) [`005d6110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d6110.md) [`005d69f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d69f0.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cff44",
      "incomplete_value": true,
      "site": "005cff4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cff04",
      "incomplete_value": true,
      "site": "005cff0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005cff48",
      "incomplete_value": true,
      "site": "005cff4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cff08",
      "incomplete_value": true,
      "site": "005cff0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005cff44",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005cff44",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005cff48",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cff44",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005cff44",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005cff48",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cff0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfed8.md#insn-005cff0c) · [`005cfee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfed8.md#insn-005cfee8) · [`005cfef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfed8.md#insn-005cfef4)
- 新版 `005cff4c`（命令位置の公開資料なし） · `005cff28`（命令位置の公開資料なし） · `005cff34`（命令位置の公開資料なし）

~~~diff
- 005cff0c ["INT_ADD", "register:40f0:8", ["const:5cff0c:8", "const:4:8"]]
- 005cff0c ["CALL", null, ["callee:00c57f10:8"]]
+ 005cff4c ["INT_ADD", "register:40f0:8", ["const:5cff4c:8", "const:4:8"]]
+ 005cff4c ["CALL", null, ["callee:00c57f10:8"]]
- 005cff0c bytes 011f1a94
+ 005cff4c bytes f11f1a94
- 005cfee8 ["INT_ADD", "register:40f0:8", ["const:5cfee8:8", "const:4:8"]]
- 005cfee8 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005cff28 ["INT_ADD", "register:40f0:8", ["const:5cff28:8", "const:4:8"]]
+ 005cff28 ["CALL", null, ["callee:00c57ef0:8"]]
- 005cfee8 bytes 021f1a94
+ 005cff28 bytes f21f1a94
- 005cfef4 ["INT_ADD", "register:40f0:8", ["const:5cfef4:8", "const:4:8"]]
- 005cfef4 ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005cff34 ["INT_ADD", "register:40f0:8", ["const:5cff34:8", "const:4:8"]]
+ 005cff34 ["CALL", null, ["callee:00c5a7b0:8"]]
- 005cfef4 bytes 2f291a94
+ 005cff34 bytes 1f2a1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fa493b291986962ef2880e5932215d1"></a>

### [`005d0330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0330.md) → [`005d0370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0370.md) FUN_005d0370

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005cffac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cffac.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`005cffec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cffec.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005d037c",
      "incomplete_value": false,
      "site": "005d0380",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d033c",
      "incomplete_value": false,
      "site": "005d0340",
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
      "005d037c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005d037c",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d0340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0330.md#insn-005d0340) · [`005d033c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0330.md#insn-005d033c)
- 新版 `005d0380`（命令位置の公開資料なし） · `005d037c`（命令位置の公開資料なし）

~~~diff
- 005d0340 ["INT_ADD", "register:40f0:8", ["const:5d0340:8", "const:4:8"]]
- 005d0340 ["CALL", null, ["callee:0043b778:8"]]
+ 005d0380 ["INT_ADD", "register:40f0:8", ["const:5d0380:8", "const:4:8"]]
+ 005d0380 ["CALL", null, ["callee:0043b778:8"]]
- 005d0340 bytes feacf997
+ 005d0380 bytes feacf997
- 005d033c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005d033c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d033c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d033c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d037c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005d037c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d037c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d037c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d033c bytes 00303c91
+ 005d037c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94249e6eaaf2c3cc152b97f856c10c96"></a>

### [`005d05fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d05fc.md) → [`005d063c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d063c.md) FUN_005d063c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005cfd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md) [`005d04d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d04d0.md) [`005d8238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8238.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 3件 [`005cfda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfda0.md) [`005d0510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0510.md) [`005d8278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8278.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005d0648",
      "incomplete_value": false,
      "site": "005d064c",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d0608",
      "incomplete_value": false,
      "site": "005d060c",
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
      "005d0648",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005d0648",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d060c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d05fc.md#insn-005d060c) · [`005d0608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d05fc.md#insn-005d0608)
- 新版 `005d064c`（命令位置の公開資料なし） · `005d0648`（命令位置の公開資料なし）

~~~diff
- 005d060c ["INT_ADD", "register:40f0:8", ["const:5d060c:8", "const:4:8"]]
- 005d060c ["CALL", null, ["callee:0043b778:8"]]
+ 005d064c ["INT_ADD", "register:40f0:8", ["const:5d064c:8", "const:4:8"]]
+ 005d064c ["CALL", null, ["callee:0043b778:8"]]
- 005d060c bytes 4bacf997
+ 005d064c bytes 4bacf997
- 005d0608 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005d0608 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d0608 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d0608 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d0648 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005d0648 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d0648 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d0648 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d0608 bytes 00303c91
+ 005d0648 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-274768e982757d449fb9fe119bc4f878"></a>

### [`005d0764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0764.md) → [`005d07a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d07a4.md) FUN_005d07a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 1件 [`005ce964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce964.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d07d0",
      "incomplete_value": true,
      "site": "005d07d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d0790",
      "incomplete_value": true,
      "site": "005d0798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005d07d4",
      "incomplete_value": true,
      "site": "005d07d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d0794",
      "incomplete_value": true,
      "site": "005d0798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005d07d0",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005d07d0",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d07d4",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d07d0",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005d07d0",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d07d4",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d0798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0764.md#insn-005d0798) · [`005d0774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0764.md#insn-005d0774) · [`005d0780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0764.md#insn-005d0780)
- 新版 `005d07d8`（命令位置の公開資料なし） · `005d07b4`（命令位置の公開資料なし） · `005d07c0`（命令位置の公開資料なし）

~~~diff
- 005d0798 ["INT_ADD", "register:40f0:8", ["const:5d0798:8", "const:4:8"]]
- 005d0798 ["CALL", null, ["callee:00c57f10:8"]]
+ 005d07d8 ["INT_ADD", "register:40f0:8", ["const:5d07d8:8", "const:4:8"]]
+ 005d07d8 ["CALL", null, ["callee:00c57f10:8"]]
- 005d0798 bytes de1c1a94
+ 005d07d8 bytes ce1d1a94
- 005d0774 ["INT_ADD", "register:40f0:8", ["const:5d0774:8", "const:4:8"]]
- 005d0774 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005d07b4 ["INT_ADD", "register:40f0:8", ["const:5d07b4:8", "const:4:8"]]
+ 005d07b4 ["CALL", null, ["callee:00c57ef0:8"]]
- 005d0774 bytes df1c1a94
+ 005d07b4 bytes cf1d1a94
- 005d0780 ["INT_ADD", "register:40f0:8", ["const:5d0780:8", "const:4:8"]]
- 005d0780 ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005d07c0 ["INT_ADD", "register:40f0:8", ["const:5d07c0:8", "const:4:8"]]
+ 005d07c0 ["CALL", null, ["callee:00c5a7b0:8"]]
- 005d0780 bytes 0c271a94
+ 005d07c0 bytes fc271a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2a0ce32053d8f26bf0b3f752f77ba98"></a>

### [`005d0860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0860.md) → [`005d08a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d08a0.md) FUN_005d08a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) [`005d0b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0b78.md) [`005d343c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md) [`005d3560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3560.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 4件 [`005ce964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005ce964.md) [`005d0bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0bb8.md) [`005d347c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d347c.md) [`005d35a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d35a0.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d08cc",
      "incomplete_value": true,
      "site": "005d08d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d088c",
      "incomplete_value": true,
      "site": "005d0894",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005d08d0",
      "incomplete_value": true,
      "site": "005d08d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d0890",
      "incomplete_value": true,
      "site": "005d0894",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005d08cc",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005d08cc",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d08d0",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d08cc",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005d08cc",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d08d0",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d0894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0860.md#insn-005d0894) · [`005d0870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0860.md#insn-005d0870) · [`005d087c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0860.md#insn-005d087c)
- 新版 `005d08d4`（命令位置の公開資料なし） · `005d08b0`（命令位置の公開資料なし） · `005d08bc`（命令位置の公開資料なし）

~~~diff
- 005d0894 ["INT_ADD", "register:40f0:8", ["const:5d0894:8", "const:4:8"]]
- 005d0894 ["CALL", null, ["callee:00c57f10:8"]]
+ 005d08d4 ["INT_ADD", "register:40f0:8", ["const:5d08d4:8", "const:4:8"]]
+ 005d08d4 ["CALL", null, ["callee:00c57f10:8"]]
- 005d0894 bytes 9f1c1a94
+ 005d08d4 bytes 8f1d1a94
- 005d0870 ["INT_ADD", "register:40f0:8", ["const:5d0870:8", "const:4:8"]]
- 005d0870 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005d08b0 ["INT_ADD", "register:40f0:8", ["const:5d08b0:8", "const:4:8"]]
+ 005d08b0 ["CALL", null, ["callee:00c57ef0:8"]]
- 005d0870 bytes a01c1a94
+ 005d08b0 bytes 901d1a94
- 005d087c ["INT_ADD", "register:40f0:8", ["const:5d087c:8", "const:4:8"]]
- 005d087c ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005d08bc ["INT_ADD", "register:40f0:8", ["const:5d08bc:8", "const:4:8"]]
+ 005d08bc ["CALL", null, ["callee:00c5a7b0:8"]]
- 005d087c bytes cd261a94
+ 005d08bc bytes bd271a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b71e0dcce7148e5a4625d8d786d816dd"></a>

### [`005d0e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md) → [`005d0eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0eb8.md) FUN_005d0eb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`005d07b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d07b0.md) [`005d08ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d08ac.md) [`005d0b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0b78.md) [`005d3560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3560.md) [`005d5608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5608.md) · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)
- 新版 呼出元 7件 [`005d07f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d07f0.md) [`005d08ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d08ec.md) [`005d0bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0bb8.md) [`005d35a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d35a0.md) [`005d5648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5648.md) · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.06% / 新版 89.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d0efc",
      "incomplete_value": true,
      "site": "005d0efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d0ebc",
      "incomplete_value": true,
      "site": "005d0ebc",
      "value": [
        "INT_ADD",
        "8",
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
                "leaf",
                "const:c9b000:8"
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d0f80",
      "incomplete_value": true,
      "site": "005d0f80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d0f40",
      "incomplete_value": true,
      "site": "005d0f40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d0eec",
      "READ",
      [
        "storage",
        "00c9b000",
        null,
        "pointer"
      ]
    ],
    [
      "005d0efc",
      "DATA",
      [
        "storage",
        "00c709e0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d0f1c",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d0eec",
      "READ",
      [
        "storage",
        "00c9b400",
        null,
        "pointer"
      ]
    ],
    [
      "005d0efc",
      "DATA",
      [
        "storage",
        "00c70de0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d0f1c",
      "READ",
      [
        "storage",
        "00c9b408",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d0ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md#insn-005d0ea0) · [`005d0eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md#insn-005d0eac) · [`005d0ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md#insn-005d0ecc)
- 新版 `005d0ee0`（命令位置の公開資料なし） · `005d0eec`（命令位置の公開資料なし） · `005d0f0c`（命令位置の公開資料なし）

~~~diff
- 005d0ea0 ["INT_ADD", "register:40f0:8", ["const:5d0ea0:8", "const:4:8"]]
- 005d0ea0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d0ee0 ["INT_ADD", "register:40f0:8", ["const:5d0ee0:8", "const:4:8"]]
+ 005d0ee0 ["CALL", null, ["callee:00c57e90:8"]]
- 005d0ea0 bytes fc1a1a94
+ 005d0ee0 bytes ec1b1a94
- 005d0eac ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005d0eac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d0eec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:400:8"]]
+ 005d0eec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005d0eac bytes 290140f9
+ 005d0eec bytes 290142f9
- 005d0ecc ["INT_ADD", "register:40f0:8", ["const:5d0ecc:8", "const:4:8"]]
- 005d0ecc ["CALL", null, ["callee:00c57e90:8"]]
+ 005d0f0c ["INT_ADD", "register:40f0:8", ["const:5d0f0c:8", "const:4:8"]]
+ 005d0f0c ["CALL", null, ["callee:00c57e90:8"]]
- 005d0ecc bytes f11a1a94
+ 005d0f0c bytes e11b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4d6627cd0cdc453b5279feec83082d9"></a>

### [`005d0fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0fb8.md) → [`005d0ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0ff8.md) FUN_005d0ff8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005d08ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d08ac.md) [`005d16a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d16a4.md) [`005d51bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md) [`005d57cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d57cc.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 4件 [`005d08ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d08ec.md) [`005d16e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d16e4.md) [`005d51fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d51fc.md) [`005d580c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d580c.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d1024",
      "incomplete_value": true,
      "site": "005d102c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d0fe4",
      "incomplete_value": true,
      "site": "005d0fec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005d1028",
      "incomplete_value": true,
      "site": "005d102c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d0fe8",
      "incomplete_value": true,
      "site": "005d0fec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005d1024",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005d1024",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d1028",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d1024",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005d1024",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d1028",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d0fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0fb8.md#insn-005d0fec) · [`005d0fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0fb8.md#insn-005d0fc8) · [`005d0fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0fb8.md#insn-005d0fd4)
- 新版 `005d102c`（命令位置の公開資料なし） · `005d1008`（命令位置の公開資料なし） · `005d1014`（命令位置の公開資料なし）

~~~diff
- 005d0fec ["INT_ADD", "register:40f0:8", ["const:5d0fec:8", "const:4:8"]]
- 005d0fec ["CALL", null, ["callee:00c57f10:8"]]
+ 005d102c ["INT_ADD", "register:40f0:8", ["const:5d102c:8", "const:4:8"]]
+ 005d102c ["CALL", null, ["callee:00c57f10:8"]]
- 005d0fec bytes c91a1a94
+ 005d102c bytes b91b1a94
- 005d0fc8 ["INT_ADD", "register:40f0:8", ["const:5d0fc8:8", "const:4:8"]]
- 005d0fc8 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005d1008 ["INT_ADD", "register:40f0:8", ["const:5d1008:8", "const:4:8"]]
+ 005d1008 ["CALL", null, ["callee:00c57ef0:8"]]
- 005d0fc8 bytes ca1a1a94
+ 005d1008 bytes ba1b1a94
- 005d0fd4 ["INT_ADD", "register:40f0:8", ["const:5d0fd4:8", "const:4:8"]]
- 005d0fd4 ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005d1014 ["INT_ADD", "register:40f0:8", ["const:5d1014:8", "const:4:8"]]
+ 005d1014 ["CALL", null, ["callee:00c5a7b0:8"]]
- 005d0fd4 bytes f7241a94
+ 005d1014 bytes e7251a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc795e1d757b7fa6a6a97c91b0852bcf"></a>

### [`005d10cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d10cc.md) → [`005d110c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d110c.md) FUN_005d110c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005d1128",
      "incomplete_value": true,
      "site": "005d1128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d10e8",
      "incomplete_value": true,
      "site": "005d10e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005d113c",
      "incomplete_value": true,
      "site": "005d1140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d10fc",
      "incomplete_value": true,
      "site": "005d1100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d1120",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ],
    [
      "005d1128",
      "DATA",
      [
        "storage",
        "00c70950",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1134",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d1120",
      "READ",
      [
        "storage",
        "00c9b408",
        null,
        "pointer"
      ]
    ],
    [
      "005d1128",
      "DATA",
      [
        "storage",
        "00c70d50",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1134",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d10e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d10cc.md#insn-005d10e0) · [`005d10ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d10cc.md#insn-005d10ec) · [`005d10f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d10cc.md#insn-005d10f0)
- 新版 `005d1120`（命令位置の公開資料なし） · `005d112c`（命令位置の公開資料なし） · `005d1130`（命令位置の公開資料なし）

~~~diff
- 005d10e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
- 005d10e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d1120 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:408:8"]]
+ 005d1120 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d10e0 bytes 080540f9
+ 005d1120 bytes 080542f9
- 005d10ec ["INT_ADD", "register:40f0:8", ["const:5d10ec:8", "const:4:8"]]
- 005d10ec ["CALL", null, ["callee:00c58290:8"]]
+ 005d112c ["INT_ADD", "register:40f0:8", ["const:5d112c:8", "const:4:8"]]
+ 005d112c ["CALL", null, ["callee:00c58290:8"]]
- 005d10ec bytes 691b1a94
+ 005d112c bytes 591c1a94
- 005d10f0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005d1130 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005d10f0 bytes 483600b0
+ 005d1130 bytes 483600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbd4dde4141e14e18ab6b5c605b1dc3d"></a>

### [`005d1128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1128.md) → [`005d1168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1168.md) FUN_005d1168

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005d1184",
      "incomplete_value": true,
      "site": "005d1184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d1144",
      "incomplete_value": true,
      "site": "005d1144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005d1198",
      "incomplete_value": true,
      "site": "005d119c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d1158",
      "incomplete_value": true,
      "site": "005d115c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d117c",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ],
    [
      "005d1184",
      "DATA",
      [
        "storage",
        "00c70950",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1190",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d117c",
      "READ",
      [
        "storage",
        "00c9b408",
        null,
        "pointer"
      ]
    ],
    [
      "005d1184",
      "DATA",
      [
        "storage",
        "00c70d50",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1190",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d113c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1128.md#insn-005d113c) · [`005d1148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1128.md#insn-005d1148) · [`005d114c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1128.md#insn-005d114c)
- 新版 `005d117c`（命令位置の公開資料なし） · `005d1188`（命令位置の公開資料なし） · `005d118c`（命令位置の公開資料なし）

~~~diff
- 005d113c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
- 005d113c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d117c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:408:8"]]
+ 005d117c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d113c bytes 080540f9
+ 005d117c bytes 080542f9
- 005d1148 ["INT_ADD", "register:40f0:8", ["const:5d1148:8", "const:4:8"]]
- 005d1148 ["CALL", null, ["callee:00c58290:8"]]
+ 005d1188 ["INT_ADD", "register:40f0:8", ["const:5d1188:8", "const:4:8"]]
+ 005d1188 ["CALL", null, ["callee:00c58290:8"]]
- 005d1148 bytes 521b1a94
+ 005d1188 bytes 421c1a94
- 005d114c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005d118c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005d114c bytes 483600b0
+ 005d118c bytes 483600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d1edcd8777729f05e24a2a7d9a060d3"></a>

### [`005d11f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d11f8.md) → [`005d1238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1238.md) FUN_005d1238

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

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
      "definition_site": "005d1254",
      "incomplete_value": true,
      "site": "005d1254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d1214",
      "incomplete_value": true,
      "site": "005d1214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d124c",
      "READ",
      [
        "storage",
        "00c9b010",
        null,
        "pointer"
      ]
    ],
    [
      "005d1254",
      "DATA",
      [
        "storage",
        "00c70998",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1260",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d124c",
      "READ",
      [
        "storage",
        "00c9b410",
        null,
        "pointer"
      ]
    ],
    [
      "005d1254",
      "DATA",
      [
        "storage",
        "00c70d98",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1260",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d120c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d11f8.md#insn-005d120c) · [`005d1218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d11f8.md#insn-005d1218) · [`005d121c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d11f8.md#insn-005d121c)
- 新版 `005d124c`（命令位置の公開資料なし） · `005d1258`（命令位置の公開資料なし） · `005d125c`（命令位置の公開資料なし）

~~~diff
- 005d120c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
- 005d120c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d124c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:410:8"]]
+ 005d124c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d120c bytes 080940f9
+ 005d124c bytes 080942f9
- 005d1218 ["INT_ADD", "register:40f0:8", ["const:5d1218:8", "const:4:8"]]
- 005d1218 ["CALL", null, ["callee:00c58290:8"]]
+ 005d1258 ["INT_ADD", "register:40f0:8", ["const:5d1258:8", "const:4:8"]]
+ 005d1258 ["CALL", null, ["callee:00c58290:8"]]
- 005d1218 bytes 1e1b1a94
+ 005d1258 bytes 0e1c1a94
- 005d121c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005d125c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005d121c bytes 483600b0
+ 005d125c bytes 483600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b41163fae03024c7ee6736a112ec62c9"></a>

### [`005d1254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1254.md) → [`005d1294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1294.md) FUN_005d1294

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005d12b0",
      "incomplete_value": true,
      "site": "005d12b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d1270",
      "incomplete_value": true,
      "site": "005d1270",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005d12c4",
      "incomplete_value": true,
      "site": "005d12c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d1284",
      "incomplete_value": true,
      "site": "005d1288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d12a8",
      "READ",
      [
        "storage",
        "00c9b010",
        null,
        "pointer"
      ]
    ],
    [
      "005d12b0",
      "DATA",
      [
        "storage",
        "00c70998",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d12bc",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d12a8",
      "READ",
      [
        "storage",
        "00c9b410",
        null,
        "pointer"
      ]
    ],
    [
      "005d12b0",
      "DATA",
      [
        "storage",
        "00c70d98",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d12bc",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d1268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1254.md#insn-005d1268) · [`005d1274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1254.md#insn-005d1274) · [`005d1278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1254.md#insn-005d1278)
- 新版 `005d12a8`（命令位置の公開資料なし） · `005d12b4`（命令位置の公開資料なし） · `005d12b8`（命令位置の公開資料なし）

~~~diff
- 005d1268 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
- 005d1268 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d12a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:410:8"]]
+ 005d12a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d1268 bytes 080940f9
+ 005d12a8 bytes 080942f9
- 005d1274 ["INT_ADD", "register:40f0:8", ["const:5d1274:8", "const:4:8"]]
- 005d1274 ["CALL", null, ["callee:00c58290:8"]]
+ 005d12b4 ["INT_ADD", "register:40f0:8", ["const:5d12b4:8", "const:4:8"]]
+ 005d12b4 ["CALL", null, ["callee:00c58290:8"]]
- 005d1274 bytes 071b1a94
+ 005d12b4 bytes f71b1a94
- 005d1278 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005d12b8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005d1278 bytes 483600b0
+ 005d12b8 bytes 483600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e737efad8113878536486b6520405e56"></a>

### [`005d1384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1384.md) → [`005d13c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d13c4.md) FUN_005d13c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005d13e0",
      "incomplete_value": true,
      "site": "005d13e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d13a0",
      "incomplete_value": true,
      "site": "005d13a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005d13f4",
      "incomplete_value": true,
      "site": "005d13f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d13b4",
      "incomplete_value": true,
      "site": "005d13b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d13d8",
      "READ",
      [
        "storage",
        "00c9b020",
        null,
        "pointer"
      ]
    ],
    [
      "005d13e0",
      "DATA",
      [
        "storage",
        "00c70a28",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d13ec",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d13d8",
      "READ",
      [
        "storage",
        "00c9b420",
        null,
        "pointer"
      ]
    ],
    [
      "005d13e0",
      "DATA",
      [
        "storage",
        "00c70e28",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d13ec",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d1398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1384.md#insn-005d1398) · [`005d13a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1384.md#insn-005d13a4) · [`005d13a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1384.md#insn-005d13a8)
- 新版 `005d13d8`（命令位置の公開資料なし） · `005d13e4`（命令位置の公開資料なし） · `005d13e8`（命令位置の公開資料なし）

~~~diff
- 005d1398 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:20:8"]]
- 005d1398 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d13d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:420:8"]]
+ 005d13d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d1398 bytes 081140f9
+ 005d13d8 bytes 081142f9
- 005d13a4 ["INT_ADD", "register:40f0:8", ["const:5d13a4:8", "const:4:8"]]
- 005d13a4 ["CALL", null, ["callee:00c58290:8"]]
+ 005d13e4 ["INT_ADD", "register:40f0:8", ["const:5d13e4:8", "const:4:8"]]
+ 005d13e4 ["CALL", null, ["callee:00c58290:8"]]
- 005d13a4 bytes bb1a1a94
+ 005d13e4 bytes ab1b1a94
- 005d13a8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005d13e8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005d13a8 bytes 483600b0
+ 005d13e8 bytes 483600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec328e9ea21f168df39f9495e3c9d046"></a>

### [`005d13e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d13e0.md) → [`005d1420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1420.md) FUN_005d1420

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005d143c",
      "incomplete_value": true,
      "site": "005d143c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d13fc",
      "incomplete_value": true,
      "site": "005d13fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005d1450",
      "incomplete_value": true,
      "site": "005d1454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d1410",
      "incomplete_value": true,
      "site": "005d1414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d1434",
      "READ",
      [
        "storage",
        "00c9b020",
        null,
        "pointer"
      ]
    ],
    [
      "005d143c",
      "DATA",
      [
        "storage",
        "00c70a28",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1448",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d1434",
      "READ",
      [
        "storage",
        "00c9b420",
        null,
        "pointer"
      ]
    ],
    [
      "005d143c",
      "DATA",
      [
        "storage",
        "00c70e28",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1448",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d13f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d13e0.md#insn-005d13f4) · [`005d1400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d13e0.md#insn-005d1400) · [`005d1404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d13e0.md#insn-005d1404)
- 新版 `005d1434`（命令位置の公開資料なし） · `005d1440`（命令位置の公開資料なし） · `005d1444`（命令位置の公開資料なし）

~~~diff
- 005d13f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:20:8"]]
- 005d13f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d1434 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:420:8"]]
+ 005d1434 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d13f4 bytes 081140f9
+ 005d1434 bytes 081142f9
- 005d1400 ["INT_ADD", "register:40f0:8", ["const:5d1400:8", "const:4:8"]]
- 005d1400 ["CALL", null, ["callee:00c58290:8"]]
+ 005d1440 ["INT_ADD", "register:40f0:8", ["const:5d1440:8", "const:4:8"]]
+ 005d1440 ["CALL", null, ["callee:00c58290:8"]]
- 005d1400 bytes a41a1a94
+ 005d1440 bytes 941b1a94
- 005d1404 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005d1444 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005d1404 bytes 483600b0
+ 005d1444 bytes 483600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86d20cdd99aa6ae6b70be7de6313a267"></a>

### [`005d1520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1520.md) → [`005d1560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1560.md) FUN_005d1560

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005d157c",
      "incomplete_value": true,
      "site": "005d157c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d153c",
      "incomplete_value": true,
      "site": "005d153c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005d1590",
      "incomplete_value": true,
      "site": "005d1594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d1550",
      "incomplete_value": true,
      "site": "005d1554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d1574",
      "READ",
      [
        "storage",
        "00c9b028",
        null,
        "pointer"
      ]
    ],
    [
      "005d157c",
      "DATA",
      [
        "storage",
        "00c70a70",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1588",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d1574",
      "READ",
      [
        "storage",
        "00c9b428",
        null,
        "pointer"
      ]
    ],
    [
      "005d157c",
      "DATA",
      [
        "storage",
        "00c70e70",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1588",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d1534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1520.md#insn-005d1534) · [`005d1540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1520.md#insn-005d1540) · [`005d1544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1520.md#insn-005d1544)
- 新版 `005d1574`（命令位置の公開資料なし） · `005d1580`（命令位置の公開資料なし） · `005d1584`（命令位置の公開資料なし）

~~~diff
- 005d1534 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:28:8"]]
- 005d1534 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d1574 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:428:8"]]
+ 005d1574 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d1534 bytes 081540f9
+ 005d1574 bytes 081542f9
- 005d1540 ["INT_ADD", "register:40f0:8", ["const:5d1540:8", "const:4:8"]]
- 005d1540 ["CALL", null, ["callee:00c58290:8"]]
+ 005d1580 ["INT_ADD", "register:40f0:8", ["const:5d1580:8", "const:4:8"]]
+ 005d1580 ["CALL", null, ["callee:00c58290:8"]]
- 005d1540 bytes 541a1a94
+ 005d1580 bytes 441b1a94
- 005d1544 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005d1584 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005d1544 bytes 483600b0
+ 005d1584 bytes 483600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c07136c31921b7139f913c9d090621f9"></a>

### [`005d157c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d157c.md) → [`005d15bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d15bc.md) FUN_005d15bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005d15d8",
      "incomplete_value": true,
      "site": "005d15d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d1598",
      "incomplete_value": true,
      "site": "005d1598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005d15ec",
      "incomplete_value": true,
      "site": "005d15f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d15ac",
      "incomplete_value": true,
      "site": "005d15b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d15d0",
      "READ",
      [
        "storage",
        "00c9b028",
        null,
        "pointer"
      ]
    ],
    [
      "005d15d8",
      "DATA",
      [
        "storage",
        "00c70a70",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d15e4",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d15d0",
      "READ",
      [
        "storage",
        "00c9b428",
        null,
        "pointer"
      ]
    ],
    [
      "005d15d8",
      "DATA",
      [
        "storage",
        "00c70e70",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d15e4",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d1590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d157c.md#insn-005d1590) · [`005d159c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d157c.md#insn-005d159c) · [`005d15a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d157c.md#insn-005d15a0)
- 新版 `005d15d0`（命令位置の公開資料なし） · `005d15dc`（命令位置の公開資料なし） · `005d15e0`（命令位置の公開資料なし）

~~~diff
- 005d1590 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:28:8"]]
- 005d1590 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d15d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:428:8"]]
+ 005d15d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d1590 bytes 081540f9
+ 005d15d0 bytes 081542f9
- 005d159c ["INT_ADD", "register:40f0:8", ["const:5d159c:8", "const:4:8"]]
- 005d159c ["CALL", null, ["callee:00c58290:8"]]
+ 005d15dc ["INT_ADD", "register:40f0:8", ["const:5d15dc:8", "const:4:8"]]
+ 005d15dc ["CALL", null, ["callee:00c58290:8"]]
- 005d159c bytes 3d1a1a94
+ 005d15dc bytes 2d1b1a94
- 005d15a0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005d15e0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005d15a0 bytes 483600b0
+ 005d15e0 bytes 483600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61551c7bb879c10916d06014926a57bd"></a>

### [`005d18c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d18c0.md) → [`005d1900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1900.md) FUN_005d1900

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005d0610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md) [`005d0974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0974.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5a3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3f0.md)
- 新版 呼出元 2件 [`005d0650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0650.md) [`005d09b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d09b4.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5a7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d1948",
      "incomplete_value": true,
      "site": "005d1948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d1908",
      "incomplete_value": true,
      "site": "005d1908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d192c",
      "READ",
      [
        "storage",
        "00c9b030",
        null,
        "pointer"
      ]
    ],
    [
      "005d1948",
      "DATA",
      [
        "storage",
        "00c70b00",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005d192c",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ],
    [
      "005d1948",
      "DATA",
      [
        "storage",
        "00c70f00",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d18ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d18c0.md#insn-005d18ec) · [`005d190c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d18c0.md#insn-005d190c) · [`005d1950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d18c0.md#insn-005d1950)
- 新版 `005d192c`（命令位置の公開資料なし） · `005d194c`（命令位置の公開資料なし） · `005d1990`（命令位置の公開資料なし）

~~~diff
- 005d18ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
- 005d18ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d192c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:430:8"]]
+ 005d192c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005d18ec bytes 291940f9
+ 005d192c bytes 291942f9
- 005d190c ["INT_ADD", "register:40f0:8", ["const:5d190c:8", "const:4:8"]]
- 005d190c ["CALL", null, ["callee:00c5a7d0:8"]]
+ 005d194c ["INT_ADD", "register:40f0:8", ["const:5d194c:8", "const:4:8"]]
+ 005d194c ["CALL", null, ["callee:00c5a7d0:8"]]
- 005d190c bytes b1221a94
+ 005d194c bytes a1231a94
- 005d1950 ["INT_ADD", "register:40f0:8", ["const:5d1950:8", "const:4:8"]]
- 005d1950 ["CALL", null, ["callee:00c5a7d0:8"]]
+ 005d1990 ["INT_ADD", "register:40f0:8", ["const:5d1990:8", "const:4:8"]]
+ 005d1990 ["CALL", null, ["callee:00c5a7d0:8"]]
- 005d1950 bytes a0221a94
+ 005d1990 bytes 90231a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58b1897cebefbb6f61bfd6dc87f7fb5a"></a>

### [`005d1b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1b08.md) → [`005d1b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1b48.md) FUN_005d1b48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005d1c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c4c.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`005d1c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1c8c.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

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
      "definition_site": "005d1b68",
      "incomplete_value": true,
      "site": "005d1b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d1b28",
      "incomplete_value": true,
      "site": "005d1b2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d1c58",
      "incomplete_value": true,
      "site": "005d1c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d1c18",
      "incomplete_value": true,
      "site": "005d1c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d1b60",
      "READ",
      [
        "storage",
        "00c9b030",
        null,
        "pointer"
      ]
    ],
    [
      "005d1b6c",
      "DATA",
      [
        "storage",
        "00c70b00",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1c50",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d1b60",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ],
    [
      "005d1b6c",
      "DATA",
      [
        "storage",
        "00c70f00",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1c50",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d1b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1b08.md#insn-005d1b20) · [`005d1b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1b08.md#insn-005d1b64) · [`005d1b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1b08.md#insn-005d1b74)
- 新版 `005d1b60`（命令位置の公開資料なし） · `005d1ba4`（命令位置の公開資料なし） · `005d1bb4`（命令位置の公開資料なし）

~~~diff
- 005d1b20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 005d1b20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d1b60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:430:8"]]
+ 005d1b60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d1b20 bytes 081940f9
+ 005d1b60 bytes 081942f9
- 005d1b64 ["INT_ADD", "register:40f0:8", ["const:5d1b64:8", "const:4:8"]]
- 005d1b64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d1ba4 ["INT_ADD", "register:40f0:8", ["const:5d1ba4:8", "const:4:8"]]
+ 005d1ba4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d1b64 bytes d3171a94
+ 005d1ba4 bytes c3181a94
- 005d1b74 ["INT_ADD", "register:40f0:8", ["const:5d1b74:8", "const:4:8"]]
- 005d1b74 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005d1bb4 ["INT_ADD", "register:40f0:8", ["const:5d1bb4:8", "const:4:8"]]
+ 005d1bb4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005d1b74 bytes cf171a94
+ 005d1bb4 bytes bf181a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-471004e3ec034b919a5b0cac1a1a624d"></a>

### [`005d2b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2b78.md) → [`005d2bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2bb8.md) FUN_005d2bb8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005d0610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md) [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) [`005d3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md) [`005d3320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3320.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 4件 [`005d0650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0650.md) [`005d2c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2c04.md) [`005d30d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d30d4.md) [`005d3360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3360.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d2be4",
      "incomplete_value": true,
      "site": "005d2bec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d2ba4",
      "incomplete_value": true,
      "site": "005d2bac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005d2be8",
      "incomplete_value": true,
      "site": "005d2bec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d2ba8",
      "incomplete_value": true,
      "site": "005d2bac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005d2be4",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005d2be4",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d2be8",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d2be4",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005d2be4",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d2be8",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d2bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2b78.md#insn-005d2bac) · [`005d2b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2b78.md#insn-005d2b88) · [`005d2b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2b78.md#insn-005d2b94)
- 新版 `005d2bec`（命令位置の公開資料なし） · `005d2bc8`（命令位置の公開資料なし） · `005d2bd4`（命令位置の公開資料なし）

~~~diff
- 005d2bac ["INT_ADD", "register:40f0:8", ["const:5d2bac:8", "const:4:8"]]
- 005d2bac ["CALL", null, ["callee:00c57f10:8"]]
+ 005d2bec ["INT_ADD", "register:40f0:8", ["const:5d2bec:8", "const:4:8"]]
+ 005d2bec ["CALL", null, ["callee:00c57f10:8"]]
- 005d2bac bytes d9131a94
+ 005d2bec bytes c9141a94
- 005d2b88 ["INT_ADD", "register:40f0:8", ["const:5d2b88:8", "const:4:8"]]
- 005d2b88 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005d2bc8 ["INT_ADD", "register:40f0:8", ["const:5d2bc8:8", "const:4:8"]]
+ 005d2bc8 ["CALL", null, ["callee:00c57ef0:8"]]
- 005d2b88 bytes da131a94
+ 005d2bc8 bytes ca141a94
- 005d2b94 ["INT_ADD", "register:40f0:8", ["const:5d2b94:8", "const:4:8"]]
- 005d2b94 ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005d2bd4 ["INT_ADD", "register:40f0:8", ["const:5d2bd4:8", "const:4:8"]]
+ 005d2bd4 ["CALL", null, ["callee:00c5a7b0:8"]]
- 005d2b94 bytes 071e1a94
+ 005d2bd4 bytes f71e1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64c4a3b574d712788af6b11753e3072c"></a>

### [`005d3e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e24.md) → [`005d3e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3e64.md) FUN_005d3e64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005d3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md) [`005d3320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3320.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 2件 [`005d30d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d30d4.md) [`005d3360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3360.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d3e90",
      "incomplete_value": true,
      "site": "005d3e98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d3e50",
      "incomplete_value": true,
      "site": "005d3e58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005d3e94",
      "incomplete_value": true,
      "site": "005d3e98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d3e54",
      "incomplete_value": true,
      "site": "005d3e58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005d3e90",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005d3e90",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d3e94",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d3e90",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005d3e90",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d3e94",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d3e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e24.md#insn-005d3e58) · [`005d3e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e24.md#insn-005d3e34) · [`005d3e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e24.md#insn-005d3e40)
- 新版 `005d3e98`（命令位置の公開資料なし） · `005d3e74`（命令位置の公開資料なし） · `005d3e80`（命令位置の公開資料なし）

~~~diff
- 005d3e58 ["INT_ADD", "register:40f0:8", ["const:5d3e58:8", "const:4:8"]]
- 005d3e58 ["CALL", null, ["callee:00c57f10:8"]]
+ 005d3e98 ["INT_ADD", "register:40f0:8", ["const:5d3e98:8", "const:4:8"]]
+ 005d3e98 ["CALL", null, ["callee:00c57f10:8"]]
- 005d3e58 bytes 2e0f1a94
+ 005d3e98 bytes 1e101a94
- 005d3e34 ["INT_ADD", "register:40f0:8", ["const:5d3e34:8", "const:4:8"]]
- 005d3e34 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005d3e74 ["INT_ADD", "register:40f0:8", ["const:5d3e74:8", "const:4:8"]]
+ 005d3e74 ["CALL", null, ["callee:00c57ef0:8"]]
- 005d3e34 bytes 2f0f1a94
+ 005d3e74 bytes 1f101a94
- 005d3e40 ["INT_ADD", "register:40f0:8", ["const:5d3e40:8", "const:4:8"]]
- 005d3e40 ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005d3e80 ["INT_ADD", "register:40f0:8", ["const:5d3e80:8", "const:4:8"]]
+ 005d3e80 ["CALL", null, ["callee:00c5a7b0:8"]]
- 005d3e40 bytes 5c191a94
+ 005d3e80 bytes 4c1a1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3daf0395204c9dfbd2293ba0b08d81b4"></a>

### [`005d42fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d42fc.md) → [`005d433c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d433c.md) FUN_005d433c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 1件 [`005d2c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d2/005d2c04.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d4368",
      "incomplete_value": true,
      "site": "005d4370",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d4328",
      "incomplete_value": true,
      "site": "005d4330",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005d436c",
      "incomplete_value": true,
      "site": "005d4370",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d432c",
      "incomplete_value": true,
      "site": "005d4330",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005d4368",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005d4368",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d436c",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d4368",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005d4368",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d436c",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d4330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d42fc.md#insn-005d4330) · [`005d430c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d42fc.md#insn-005d430c) · [`005d4318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d42fc.md#insn-005d4318)
- 新版 `005d4370`（命令位置の公開資料なし） · `005d434c`（命令位置の公開資料なし） · `005d4358`（命令位置の公開資料なし）

~~~diff
- 005d4330 ["INT_ADD", "register:40f0:8", ["const:5d4330:8", "const:4:8"]]
- 005d4330 ["CALL", null, ["callee:00c57f10:8"]]
+ 005d4370 ["INT_ADD", "register:40f0:8", ["const:5d4370:8", "const:4:8"]]
+ 005d4370 ["CALL", null, ["callee:00c57f10:8"]]
- 005d4330 bytes f80d1a94
+ 005d4370 bytes e80e1a94
- 005d430c ["INT_ADD", "register:40f0:8", ["const:5d430c:8", "const:4:8"]]
- 005d430c ["CALL", null, ["callee:00c57ef0:8"]]
+ 005d434c ["INT_ADD", "register:40f0:8", ["const:5d434c:8", "const:4:8"]]
+ 005d434c ["CALL", null, ["callee:00c57ef0:8"]]
- 005d430c bytes f90d1a94
+ 005d434c bytes e90e1a94
- 005d4318 ["INT_ADD", "register:40f0:8", ["const:5d4318:8", "const:4:8"]]
- 005d4318 ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005d4358 ["INT_ADD", "register:40f0:8", ["const:5d4358:8", "const:4:8"]]
+ 005d4358 ["CALL", null, ["callee:00c5a7b0:8"]]
- 005d4318 bytes 26181a94
+ 005d4358 bytes 16191a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-175264f91eb6b8c960ebb8867d705c4f"></a>

### [`005d47fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d47fc.md) → [`005d483c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d483c.md) FUN_005d483c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005d3748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3748.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 1件 [`005d3788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3788.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d4868",
      "incomplete_value": true,
      "site": "005d4870",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d4828",
      "incomplete_value": true,
      "site": "005d4830",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005d486c",
      "incomplete_value": true,
      "site": "005d4870",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d482c",
      "incomplete_value": true,
      "site": "005d4830",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005d4868",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005d4868",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d486c",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d4868",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005d4868",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d486c",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d4830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d47fc.md#insn-005d4830) · [`005d480c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d47fc.md#insn-005d480c) · [`005d4818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d47fc.md#insn-005d4818)
- 新版 `005d4870`（命令位置の公開資料なし） · `005d484c`（命令位置の公開資料なし） · `005d4858`（命令位置の公開資料なし）

~~~diff
- 005d4830 ["INT_ADD", "register:40f0:8", ["const:5d4830:8", "const:4:8"]]
- 005d4830 ["CALL", null, ["callee:00c57f10:8"]]
+ 005d4870 ["INT_ADD", "register:40f0:8", ["const:5d4870:8", "const:4:8"]]
+ 005d4870 ["CALL", null, ["callee:00c57f10:8"]]
- 005d4830 bytes b80c1a94
+ 005d4870 bytes a80d1a94
- 005d480c ["INT_ADD", "register:40f0:8", ["const:5d480c:8", "const:4:8"]]
- 005d480c ["CALL", null, ["callee:00c57ef0:8"]]
+ 005d484c ["INT_ADD", "register:40f0:8", ["const:5d484c:8", "const:4:8"]]
+ 005d484c ["CALL", null, ["callee:00c57ef0:8"]]
- 005d480c bytes b90c1a94
+ 005d484c bytes a90d1a94
- 005d4818 ["INT_ADD", "register:40f0:8", ["const:5d4818:8", "const:4:8"]]
- 005d4818 ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005d4858 ["INT_ADD", "register:40f0:8", ["const:5d4858:8", "const:4:8"]]
+ 005d4858 ["CALL", null, ["callee:00c5a7b0:8"]]
- 005d4818 bytes e6161a94
+ 005d4858 bytes d6171a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c3ec6e4e37547192dddbba382158cc7"></a>

### [`005d49e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49e8.md) → [`005d4a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4a28.md) FUN_005d4a28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005d4848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4848.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`005d4888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4888.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005d4a34",
      "incomplete_value": false,
      "site": "005d4a38",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d49f4",
      "incomplete_value": false,
      "site": "005d49f8",
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
      "005d4a34",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005d4a34",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d49f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49e8.md#insn-005d49f8) · [`005d49f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49e8.md#insn-005d49f4)
- 新版 `005d4a38`（命令位置の公開資料なし） · `005d4a34`（命令位置の公開資料なし）

~~~diff
- 005d49f8 ["INT_ADD", "register:40f0:8", ["const:5d49f8:8", "const:4:8"]]
- 005d49f8 ["CALL", null, ["callee:0043b778:8"]]
+ 005d4a38 ["INT_ADD", "register:40f0:8", ["const:5d4a38:8", "const:4:8"]]
+ 005d4a38 ["CALL", null, ["callee:0043b778:8"]]
- 005d49f8 bytes 509bf997
+ 005d4a38 bytes 509bf997
- 005d49f4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005d49f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d49f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d49f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d4a34 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005d4a34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d4a34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d4a34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d49f4 bytes 00303c91
+ 005d4a34 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f903ddf86c31d4719d33399f38bc6b7"></a>

### [`005d49fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49fc.md) → [`005d4a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4a3c.md) FUN_005d4a3c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005d3c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3c18.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`005d3c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d3/005d3c58.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005d4a48",
      "incomplete_value": false,
      "site": "005d4a4c",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d4a08",
      "incomplete_value": false,
      "site": "005d4a0c",
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
      "005d4a48",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005d4a48",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d4a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49fc.md#insn-005d4a0c) · [`005d4a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49fc.md#insn-005d4a08)
- 新版 `005d4a4c`（命令位置の公開資料なし） · `005d4a48`（命令位置の公開資料なし）

~~~diff
- 005d4a0c ["INT_ADD", "register:40f0:8", ["const:5d4a0c:8", "const:4:8"]]
- 005d4a0c ["CALL", null, ["callee:0043b778:8"]]
+ 005d4a4c ["INT_ADD", "register:40f0:8", ["const:5d4a4c:8", "const:4:8"]]
+ 005d4a4c ["CALL", null, ["callee:0043b778:8"]]
- 005d4a0c bytes 4b9bf997
+ 005d4a4c bytes 4b9bf997
- 005d4a08 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005d4a08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d4a08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d4a08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d4a48 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005d4a48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d4a48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d4a48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d4a08 bytes 00303c91
+ 005d4a48 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f6b82a435d1baaf99626b6da310b265"></a>

### [`005d4b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4b08.md) → [`005d4b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4b48.md) FUN_005d4b48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005cebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cebdc.md) [`005d53c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`005cec1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005cec1c.md) [`005d5408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5408.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.16% / 新版 90.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d4ba0",
      "incomplete_value": true,
      "site": "005d4ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d4b60",
      "incomplete_value": true,
      "site": "005d4b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d4bd4",
      "incomplete_value": true,
      "site": "005d4bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d4b94",
      "incomplete_value": true,
      "site": "005d4b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d4c04",
      "incomplete_value": true,
      "site": "005d4c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d4bc4",
      "incomplete_value": true,
      "site": "005d4bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d4b94",
      "READ",
      [
        "storage",
        "00c9af88",
        null,
        "pointer"
      ]
    ],
    [
      "005d4ba0",
      "DATA",
      [
        "storage",
        "00c70740",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d4bbc",
      "READ",
      [
        "storage",
        "00c9b038",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d4b94",
      "READ",
      [
        "storage",
        "00c9b388",
        null,
        "pointer"
      ]
    ],
    [
      "005d4ba0",
      "DATA",
      [
        "storage",
        "00c70b40",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d4bbc",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d4b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4b08.md#insn-005d4b54) · [`005d4b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4b08.md#insn-005d4b44) · [`005d4b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4b08.md#insn-005d4b4c)
- 新版 `005d4b94`（命令位置の公開資料なし） · `005d4b84`（命令位置の公開資料なし） · `005d4b8c`（命令位置の公開資料なし）

~~~diff
- 005d4b54 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f88:8"]]
- 005d4b54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d4b94 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:388:8"]]
+ 005d4b94 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005d4b54 bytes 29c547f9
+ 005d4b94 bytes 29c541f9
- 005d4b44 ["INT_ADD", "register:40f0:8", ["const:5d4b44:8", "const:4:8"]]
- 005d4b44 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d4b84 ["INT_ADD", "register:40f0:8", ["const:5d4b84:8", "const:4:8"]]
+ 005d4b84 ["CALL", null, ["callee:00c57e90:8"]]
- 005d4b44 bytes d30b1a94
+ 005d4b84 bytes c30c1a94
- 005d4b4c ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 005d4b8c ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 005d4b4c bytes 293600d0
+ 005d4b8c bytes 293600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-952d35e6ea4404f95125f63b4e98b8fc"></a>

### [`005d4c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c48.md) → [`005d4c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4c88.md) FUN_005d4c88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005cebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cebdc.md) [`005d53c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 2件 [`005cec1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005cec1c.md) [`005d5408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5408.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d4cb4",
      "incomplete_value": true,
      "site": "005d4cbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d4c74",
      "incomplete_value": true,
      "site": "005d4c7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005d4cb8",
      "incomplete_value": true,
      "site": "005d4cbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d4c78",
      "incomplete_value": true,
      "site": "005d4c7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005d4cb4",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005d4cb4",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d4cb8",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d4cb4",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005d4cb4",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d4cb8",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d4c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c48.md#insn-005d4c7c) · [`005d4c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c48.md#insn-005d4c58) · [`005d4c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c48.md#insn-005d4c64)
- 新版 `005d4cbc`（命令位置の公開資料なし） · `005d4c98`（命令位置の公開資料なし） · `005d4ca4`（命令位置の公開資料なし）

~~~diff
- 005d4c7c ["INT_ADD", "register:40f0:8", ["const:5d4c7c:8", "const:4:8"]]
- 005d4c7c ["CALL", null, ["callee:00c57f10:8"]]
+ 005d4cbc ["INT_ADD", "register:40f0:8", ["const:5d4cbc:8", "const:4:8"]]
+ 005d4cbc ["CALL", null, ["callee:00c57f10:8"]]
- 005d4c7c bytes a50b1a94
+ 005d4cbc bytes 950c1a94
- 005d4c58 ["INT_ADD", "register:40f0:8", ["const:5d4c58:8", "const:4:8"]]
- 005d4c58 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005d4c98 ["INT_ADD", "register:40f0:8", ["const:5d4c98:8", "const:4:8"]]
+ 005d4c98 ["CALL", null, ["callee:00c57ef0:8"]]
- 005d4c58 bytes a60b1a94
+ 005d4c98 bytes 960c1a94
- 005d4c64 ["INT_ADD", "register:40f0:8", ["const:5d4c64:8", "const:4:8"]]
- 005d4c64 ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005d4ca4 ["INT_ADD", "register:40f0:8", ["const:5d4ca4:8", "const:4:8"]]
+ 005d4ca4 ["CALL", null, ["callee:00c5a7b0:8"]]
- 005d4c64 bytes d3151a94
+ 005d4ca4 bytes c3161a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e4146a05df5cbc33df9fde92f952c00"></a>

### [`005d4c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c94.md) → [`005d4cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4cd4.md) FUN_005d4cd4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005cebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cebdc.md) [`005d53c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 2件 [`005cec1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005cec1c.md) [`005d5408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5408.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d4d00",
      "incomplete_value": true,
      "site": "005d4d08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d4cc0",
      "incomplete_value": true,
      "site": "005d4cc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005d4d04",
      "incomplete_value": true,
      "site": "005d4d08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d4cc4",
      "incomplete_value": true,
      "site": "005d4cc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005d4d00",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005d4d00",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d4d04",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d4d00",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005d4d00",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d4d04",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d4cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c94.md#insn-005d4cc8) · [`005d4ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c94.md#insn-005d4ca4) · [`005d4cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c94.md#insn-005d4cb0)
- 新版 `005d4d08`（命令位置の公開資料なし） · `005d4ce4`（命令位置の公開資料なし） · `005d4cf0`（命令位置の公開資料なし）

~~~diff
- 005d4cc8 ["INT_ADD", "register:40f0:8", ["const:5d4cc8:8", "const:4:8"]]
- 005d4cc8 ["CALL", null, ["callee:00c57f10:8"]]
+ 005d4d08 ["INT_ADD", "register:40f0:8", ["const:5d4d08:8", "const:4:8"]]
+ 005d4d08 ["CALL", null, ["callee:00c57f10:8"]]
- 005d4cc8 bytes 920b1a94
+ 005d4d08 bytes 820c1a94
- 005d4ca4 ["INT_ADD", "register:40f0:8", ["const:5d4ca4:8", "const:4:8"]]
- 005d4ca4 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005d4ce4 ["INT_ADD", "register:40f0:8", ["const:5d4ce4:8", "const:4:8"]]
+ 005d4ce4 ["CALL", null, ["callee:00c57ef0:8"]]
- 005d4ca4 bytes 930b1a94
+ 005d4ce4 bytes 830c1a94
- 005d4cb0 ["INT_ADD", "register:40f0:8", ["const:5d4cb0:8", "const:4:8"]]
- 005d4cb0 ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005d4cf0 ["INT_ADD", "register:40f0:8", ["const:5d4cf0:8", "const:4:8"]]
+ 005d4cf0 ["CALL", null, ["callee:00c5a7b0:8"]]
- 005d4cb0 bytes c0151a94
+ 005d4cf0 bytes b0161a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1c6d06058ee323ea65250053cf4439f"></a>

### [`005d4ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4ce0.md) → [`005d4d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d4/005d4d20.md) FUN_005d4d20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

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
      "definition_site": "005d4d3c",
      "incomplete_value": true,
      "site": "005d4d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d4cfc",
      "incomplete_value": true,
      "site": "005d4d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005d4d60",
      "incomplete_value": true,
      "site": "005d4d64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d4d20",
      "incomplete_value": true,
      "site": "005d4d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d4d34",
      "READ",
      [
        "storage",
        "00c9b048",
        null,
        "pointer"
      ]
    ],
    [
      "005d4d40",
      "DATA",
      [
        "storage",
        "00c70c38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d4d58",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d4d34",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "005d4d40",
      "DATA",
      [
        "storage",
        "00c71038",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d4d58",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d4cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4ce0.md#insn-005d4cf4) · [`005d4d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4ce0.md#insn-005d4d10) · [`005d4d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4ce0.md#insn-005d4d14)
- 新版 `005d4d34`（命令位置の公開資料なし） · `005d4d50`（命令位置の公開資料なし） · `005d4d54`（命令位置の公開資料なし）

~~~diff
- 005d4cf4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 005d4cf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d4d34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:448:8"]]
+ 005d4d34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d4cf4 bytes 082540f9
+ 005d4d34 bytes 082542f9
- 005d4d10 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d4d10 ["INT_ADD", "register:40f0:8", ["const:5d4d10:8", "const:4:8"]]
- 005d4d10 ["CALLIND", null, ["register:0:8"]]
+ 005d4d50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d4d50 ["INT_ADD", "register:40f0:8", ["const:5d4d50:8", "const:4:8"]]
+ 005d4d50 ["CALLIND", null, ["register:0:8"]]
- 005d4d10 bytes 00013fd6
+ 005d4d50 bytes 00013fd6
- 005d4d14 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005d4d54 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005d4d14 bytes 283600d0
+ 005d4d54 bytes 283600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8398a90354c5d403da6c7a6b924363fc"></a>

### [`005d4fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4fd0.md) → [`005d5010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5010.md) FUN_005d5010

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

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
      "definition_site": "005d502c",
      "incomplete_value": true,
      "site": "005d5030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d4fec",
      "incomplete_value": true,
      "site": "005d4ff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005d5050",
      "incomplete_value": true,
      "site": "005d5054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d5010",
      "incomplete_value": true,
      "site": "005d5014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d5024",
      "READ",
      [
        "storage",
        "00c9b048",
        null,
        "pointer"
      ]
    ],
    [
      "005d5030",
      "DATA",
      [
        "storage",
        "00c70c38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5048",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d5024",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "005d5030",
      "DATA",
      [
        "storage",
        "00c71038",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5048",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d4fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4fd0.md#insn-005d4fe4) · [`005d5000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4fd0.md#insn-005d5000) · [`005d5004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4fd0.md#insn-005d5004)
- 新版 `005d5024`（命令位置の公開資料なし） · `005d5040`（命令位置の公開資料なし） · `005d5044`（命令位置の公開資料なし）

~~~diff
- 005d4fe4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 005d4fe4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d5024 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:448:8"]]
+ 005d5024 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d4fe4 bytes 082540f9
+ 005d5024 bytes 082542f9
- 005d5000 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d5000 ["INT_ADD", "register:40f0:8", ["const:5d5000:8", "const:4:8"]]
- 005d5000 ["CALLIND", null, ["register:0:8"]]
+ 005d5040 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d5040 ["INT_ADD", "register:40f0:8", ["const:5d5040:8", "const:4:8"]]
+ 005d5040 ["CALLIND", null, ["register:0:8"]]
- 005d5000 bytes 00013fd6
+ 005d5040 bytes 00013fd6
- 005d5004 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005d5044 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005d5004 bytes 283600b0
+ 005d5044 bytes 283600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06912a61508e0c5746fd651cc8d60f98"></a>

### [`005d5050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5050.md) → [`005d5090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5090.md) FUN_005d5090

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "definition_site": "005d50ac",
      "incomplete_value": true,
      "site": "005d50b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d506c",
      "incomplete_value": true,
      "site": "005d5070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005d50d0",
      "incomplete_value": true,
      "site": "005d50d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d5090",
      "incomplete_value": true,
      "site": "005d5094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d50a4",
      "READ",
      [
        "storage",
        "00c9b048",
        null,
        "pointer"
      ]
    ],
    [
      "005d50b0",
      "DATA",
      [
        "storage",
        "00c70c38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d50c8",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d50a4",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "005d50b0",
      "DATA",
      [
        "storage",
        "00c71038",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d50c8",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d5064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5050.md#insn-005d5064) · [`005d5080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5050.md#insn-005d5080) · [`005d5084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5050.md#insn-005d5084)
- 新版 `005d50a4`（命令位置の公開資料なし） · `005d50c0`（命令位置の公開資料なし） · `005d50c4`（命令位置の公開資料なし）

~~~diff
- 005d5064 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 005d5064 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d50a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:448:8"]]
+ 005d50a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d5064 bytes 082540f9
+ 005d50a4 bytes 082542f9
- 005d5080 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d5080 ["INT_ADD", "register:40f0:8", ["const:5d5080:8", "const:4:8"]]
- 005d5080 ["CALLIND", null, ["register:0:8"]]
+ 005d50c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d50c0 ["INT_ADD", "register:40f0:8", ["const:5d50c0:8", "const:4:8"]]
+ 005d50c0 ["CALLIND", null, ["register:0:8"]]
- 005d5080 bytes 00013fd6
+ 005d50c0 bytes 00013fd6
- 005d5084 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005d50c4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005d5084 bytes 283600b0
+ 005d50c4 bytes 283600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9660b158efda60fbe3e32f5f53932256"></a>

### [`005d50bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d50bc.md) → [`005d50fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d50fc.md) FUN_005d50fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

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
      "definition_site": "005d5118",
      "incomplete_value": true,
      "site": "005d511c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d50d8",
      "incomplete_value": true,
      "site": "005d50dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005d513c",
      "incomplete_value": true,
      "site": "005d5140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d50fc",
      "incomplete_value": true,
      "site": "005d5100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d5110",
      "READ",
      [
        "storage",
        "00c9b048",
        null,
        "pointer"
      ]
    ],
    [
      "005d511c",
      "DATA",
      [
        "storage",
        "00c70c38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5134",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d5110",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "005d511c",
      "DATA",
      [
        "storage",
        "00c71038",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5134",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d50d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d50bc.md#insn-005d50d0) · [`005d50ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d50bc.md#insn-005d50ec) · [`005d50f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d50bc.md#insn-005d50f0)
- 新版 `005d5110`（命令位置の公開資料なし） · `005d512c`（命令位置の公開資料なし） · `005d5130`（命令位置の公開資料なし）

~~~diff
- 005d50d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
- 005d50d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d5110 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:448:8"]]
+ 005d5110 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d50d0 bytes 082540f9
+ 005d5110 bytes 082542f9
- 005d50ec ["COPY", "register:0:8", ["register:4040:8"]]
- 005d50ec ["INT_ADD", "register:40f0:8", ["const:5d50ec:8", "const:4:8"]]
- 005d50ec ["CALLIND", null, ["register:0:8"]]
+ 005d512c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d512c ["INT_ADD", "register:40f0:8", ["const:5d512c:8", "const:4:8"]]
+ 005d512c ["CALLIND", null, ["register:0:8"]]
- 005d50ec bytes 00013fd6
+ 005d512c bytes 00013fd6
- 005d50f0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005d5130 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005d50f0 bytes 283600b0
+ 005d5130 bytes 283600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff806b87da5e444dc1e0070131c16790"></a>

### [`005d5170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5170.md) → [`005d51b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d51b0.md) FUN_005d51b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005cdcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdcc0.md) [`005cde4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cde4c.md) · 呼出先 4件 [`00c36e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e60.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md)
- 新版 呼出元 2件 [`005cdd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cdd00.md) [`005cde8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cde8c.md) · 呼出先 4件 [`00c37288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37288.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5a7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d51dc",
      "incomplete_value": true,
      "site": "005d51e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d519c",
      "incomplete_value": true,
      "site": "005d51a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "005d51e0",
      "incomplete_value": true,
      "site": "005d51e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d51a0",
      "incomplete_value": true,
      "site": "005d51a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "005d51dc",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "005d51dc",
      "PARAM",
      [
        "storage",
        "00c961b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d51e0",
      "READ",
      [
        "storage",
        "00c9afb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d51dc",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "005d51dc",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d51e0",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d51a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5170.md#insn-005d51a4) · [`005d5180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5170.md#insn-005d5180) · [`005d518c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5170.md#insn-005d518c)
- 新版 `005d51e4`（命令位置の公開資料なし） · `005d51c0`（命令位置の公開資料なし） · `005d51cc`（命令位置の公開資料なし）

~~~diff
- 005d51a4 ["INT_ADD", "register:40f0:8", ["const:5d51a4:8", "const:4:8"]]
- 005d51a4 ["CALL", null, ["callee:00c57f10:8"]]
+ 005d51e4 ["INT_ADD", "register:40f0:8", ["const:5d51e4:8", "const:4:8"]]
+ 005d51e4 ["CALL", null, ["callee:00c57f10:8"]]
- 005d51a4 bytes 5b0a1a94
+ 005d51e4 bytes 4b0b1a94
- 005d5180 ["INT_ADD", "register:40f0:8", ["const:5d5180:8", "const:4:8"]]
- 005d5180 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005d51c0 ["INT_ADD", "register:40f0:8", ["const:5d51c0:8", "const:4:8"]]
+ 005d51c0 ["CALL", null, ["callee:00c57ef0:8"]]
- 005d5180 bytes 5c0a1a94
+ 005d51c0 bytes 4c0b1a94
- 005d518c ["INT_ADD", "register:40f0:8", ["const:5d518c:8", "const:4:8"]]
- 005d518c ["CALL", null, ["callee:00c5a7b0:8"]]
+ 005d51cc ["INT_ADD", "register:40f0:8", ["const:5d51cc:8", "const:4:8"]]
+ 005d51cc ["CALL", null, ["callee:00c5a7b0:8"]]
- 005d518c bytes 89141a94
+ 005d51cc bytes 79151a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1798485d9170cacde6a29b6128042bce"></a>

### [`005d51bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md) → [`005d51fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d51fc.md) FUN_005d51fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005cdcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdcc0.md) [`005d51bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md) · 呼出先 7件 [`005cf05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf05c.md) [`005d0fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0fb8.md) [`005d1004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1004.md) [`005d51bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md) [`005d53c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md)
- 新版 呼出元 2件 [`005cdd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cdd00.md) [`005d51fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d51fc.md) · 呼出先 7件 [`005cf09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cf09c.md) [`005d0ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0ff8.md) [`005d1044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d1/005d1044.md) [`005d51fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d51fc.md) [`005d5408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5408.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.42% / 新版 95.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d528c",
      "incomplete_value": true,
      "site": "005d52a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d524c",
      "incomplete_value": true,
      "site": "005d5264",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005d53e0",
      "incomplete_value": true,
      "site": "005d53f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d53a0",
      "incomplete_value": true,
      "site": "005d53b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d527c",
      "READ",
      [
        "storage",
        "00c9afe8",
        null,
        "pointer"
      ]
    ],
    [
      "005d52a4",
      "DATA",
      [
        "storage",
        "00c70b48",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d53d0",
      "READ",
      [
        "storage",
        "00c9aff0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d527c",
      "READ",
      [
        "storage",
        "00c9b3e8",
        null,
        "pointer"
      ]
    ],
    [
      "005d52a4",
      "DATA",
      [
        "storage",
        "00c70f48",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d53d0",
      "READ",
      [
        "storage",
        "00c9b3f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d51dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md#insn-005d51dc) · [`005d522c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md#insn-005d522c) · [`005d5234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md#insn-005d5234)
- 新版 `005d521c`（命令位置の公開資料なし） · `005d526c`（命令位置の公開資料なし） · `005d5274`（命令位置の公開資料なし）

~~~diff
- 005d51dc ["INT_ADD", "register:40f0:8", ["const:5d51dc:8", "const:4:8"]]
- 005d51dc ["CALL", null, ["callee:005d5648:8"]]
+ 005d521c ["INT_ADD", "register:40f0:8", ["const:5d521c:8", "const:4:8"]]
+ 005d521c ["CALL", null, ["callee:005d5648:8"]]
- 005d51dc bytes 0b010094
+ 005d521c bytes 0b010094
- 005d522c ["INT_ADD", "register:40f0:8", ["const:5d522c:8", "const:4:8"]]
- 005d522c ["CALL", null, ["callee:00c57e90:8"]]
+ 005d526c ["INT_ADD", "register:40f0:8", ["const:5d526c:8", "const:4:8"]]
+ 005d526c ["CALL", null, ["callee:00c57e90:8"]]
- 005d522c bytes 190a1a94
+ 005d526c bytes 090b1a94
- 005d5234 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 005d5274 ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 005d5234 bytes 2a3600b0
+ 005d5274 bytes 2a3600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72e6e984d883c234359b146b1b271747"></a>

### [`005d5718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5718.md) → [`005d5758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5758.md) FUN_005d5758

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005d5768",
      "incomplete_value": true,
      "site": "005d576c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005d5728",
      "incomplete_value": true,
      "site": "005d572c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005d5760",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ],
    [
      "005d576c",
      "DATA",
      [
        "storage",
        "00c707b8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005d5760",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ],
    [
      "005d576c",
      "DATA",
      [
        "storage",
        "00c70bb8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d5718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5718.md#insn-005d5718) · [`005d5720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5718.md#insn-005d5720)
- 新版 `005d5758`（命令位置の公開資料なし） · `005d5760`（命令位置の公開資料なし）

~~~diff
- 005d5718 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 005d5758 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 005d5718 bytes 293600b0
+ 005d5758 bytes 293600d0
- 005d5720 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fa8:8"]]
- 005d5720 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d5760 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3a8:8"]]
+ 005d5760 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005d5720 bytes 29d547f9
+ 005d5760 bytes 29d541f9
~~~


<a id="compare-a8a9eb860f7e549db5ebaaf5be008493"></a>

### [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) → [`005d6110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d6/005d6110.md) FUN_005d6110

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005d5c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md) · 呼出先 10件 [`005cfd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd14.md) [`005cfd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md) [`005cfed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfed8.md) [`005d04d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d04d0.md) [`005d7100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7100.md)
- 新版 呼出元 1件 [`005d5c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d5/005d5c60.md) · 呼出先 10件 [`005cfd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfd54.md) [`005cfda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cfda0.md) [`005cff18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cff18.md) [`005d0510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d0/005d0510.md) [`005d7140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d7/005d7140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.64% / 新版 99.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d6300",
      "incomplete_value": true,
      "site": "005d6310",
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
                "const:3f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d62c0",
      "incomplete_value": true,
      "site": "005d62d0",
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 51,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d6300",
      "READ",
      [
        "storage",
        "002c23b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005d6300",
      "READ",
      [
        "storage",
        "002c23f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d6148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md#insn-005d6148) · [`005d6248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md#insn-005d6248) · [`005d62c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md#insn-005d62c0)
- 新版 `005d6188`（命令位置の公開資料なし） · `005d6288`（命令位置の公開資料なし） · `005d6300`（命令位置の公開資料なし）

~~~diff
- 005d6148 ["INT_ADD", "register:40f0:8", ["const:5d6148:8", "const:4:8"]]
- 005d6148 ["CALL", null, ["callee:005d71bc:8"]]
+ 005d6188 ["INT_ADD", "register:40f0:8", ["const:5d6188:8", "const:4:8"]]
+ 005d6188 ["CALL", null, ["callee:005d71bc:8"]]
- 005d6148 bytes 0d040094
+ 005d6188 bytes 0d040094
- 005d6248 ["INT_ADD", "register:40f0:8", ["const:5d6248:8", "const:4:8"]]
- 005d6248 ["CALL", null, ["callee:005d0510:8"]]
+ 005d6288 ["INT_ADD", "register:40f0:8", ["const:5d6288:8", "const:4:8"]]
+ 005d6288 ["CALL", null, ["callee:005d0510:8"]]
- 005d6248 bytes a2e8ff97
+ 005d6288 bytes a2e8ff97
- 005d62c0 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:3b0:8"]]
- 005d62c0 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 005d62c0 ["COPY", "register:5010:8", ["const:0:8"]]
- 005d62c0 ["COPY", "register:5018:8", ["const:0:8"]]
+ 005d6300 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:3f0:8"]]
+ 005d6300 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 005d6300 ["COPY", "register:5010:8", ["const:0:8"]]
+ 005d6300 ["COPY", "register:5018:8", ["const:0:8"]]
- 005d62c0 bytes 80edc03d
+ 005d6300 bytes 80fdc03d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-760dd5b96010eff22b24c16c9cc94a2a"></a>

### [`005d8698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8698.md) → [`005d86d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d86d8.md) FUN_005d86d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005d851c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d851c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`005d855c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d855c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005d86e4",
      "incomplete_value": false,
      "site": "005d86e8",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d86a4",
      "incomplete_value": false,
      "site": "005d86a8",
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
      "005d86e4",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005d86e4",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d86a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8698.md#insn-005d86a8) · [`005d86a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8698.md#insn-005d86a4)
- 新版 `005d86e8`（命令位置の公開資料なし） · `005d86e4`（命令位置の公開資料なし）

~~~diff
- 005d86a8 ["INT_ADD", "register:40f0:8", ["const:5d86a8:8", "const:4:8"]]
- 005d86a8 ["CALL", null, ["callee:0043b778:8"]]
+ 005d86e8 ["INT_ADD", "register:40f0:8", ["const:5d86e8:8", "const:4:8"]]
+ 005d86e8 ["CALL", null, ["callee:0043b778:8"]]
- 005d86a8 bytes 248cf997
+ 005d86e8 bytes 248cf997
- 005d86a4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005d86a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d86a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d86a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d86e4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005d86e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d86e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d86e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d86a4 bytes 00303c91
+ 005d86e4 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-360ee04579fe041b74fd98f8d2faf1bd"></a>

### [`005d8ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8ef4.md) → [`005d8f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8f34.md) FUN_005d8f34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005d8f58",
      "incomplete_value": false,
      "site": "005d8f58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d8f18",
      "incomplete_value": false,
      "site": "005d8f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "005d8f58",
      "DATA",
      [
        "storage",
        "00c70de8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005d8f58",
      "DATA",
      [
        "storage",
        "00c711e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d8f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8ef4.md#insn-005d8f08) · [`005d8f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8ef4.md#insn-005d8f10) · [`005d8f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8ef4.md#insn-005d8f14)
- 新版 `005d8f48`（命令位置の公開資料なし） · `005d8f50`（命令位置の公開資料なし） · `005d8f54`（命令位置の公開資料なし）

~~~diff
- 005d8f08 ["INT_ADD", "register:40f0:8", ["const:5d8f08:8", "const:4:8"]]
- 005d8f08 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d8f48 ["INT_ADD", "register:40f0:8", ["const:5d8f48:8", "const:4:8"]]
+ 005d8f48 ["CALL", null, ["callee:00c57e90:8"]]
- 005d8f08 bytes e2fa1994
+ 005d8f48 bytes d2fb1994
- 005d8f10 ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005d8f50 ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005d8f10 bytes c8340090
+ 005d8f50 bytes c83400b0
- 005d8f14 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 005d8f14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005d8f14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005d8f14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005d8f54 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 005d8f54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005d8f54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005d8f54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005d8f14 bytes 08a13791
+ 005d8f54 bytes 08a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e10bfd8c0890e543d0718d0e1579c85b"></a>

### [`005d8f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8f44.md) → [`005d8f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8f84.md) FUN_005d8f84

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 32件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0043e7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e7e8.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md)
- 新版 呼出元 0件  · 呼出先 32件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d93bc",
      "incomplete_value": true,
      "site": "005d93c0",
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d937c",
      "incomplete_value": true,
      "site": "005d9380",
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
                "const:540:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 46,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005d95c0",
      "incomplete_value": false,
      "site": "005d95c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d9580",
      "incomplete_value": false,
      "site": "005d9580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d8fc8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d8f88",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "005d8fc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "005d8fe4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "005d9140",
      "PARAM",
      [
        "storage",
        "002ac93c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005d8fc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "005d8fe4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "005d9140",
      "PARAM",
      [
        "storage",
        "002ac97c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d8f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8f44.md#insn-005d8f88) · [`005d8fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8f44.md#insn-005d8fa4) · [`005d9108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8f44.md#insn-005d9108)
- 新版 `005d8fc8`（命令位置の公開資料なし） · `005d8fe4`（命令位置の公開資料なし） · `005d9148`（命令位置の公開資料なし）

~~~diff
- 005d8f88 ["INT_ADD", "register:40f0:8", ["const:5d8f88:8", "const:4:8"]]
- 005d8f88 ["CALL", null, ["ram:47acb4:8"]]
+ 005d8fc8 ["INT_ADD", "register:40f0:8", ["const:5d8fc8:8", "const:4:8"]]
+ 005d8fc8 ["CALL", null, ["ram:47acf4:8"]]
- 005d8f88 bytes 4b87fa97
+ 005d8fc8 bytes 4b87fa97
- 005d8fa4 ["INT_ADD", "register:40f0:8", ["const:5d8fa4:8", "const:4:8"]]
- 005d8fa4 ["CALL", null, ["ram:47acb4:8"]]
+ 005d8fe4 ["INT_ADD", "register:40f0:8", ["const:5d8fe4:8", "const:4:8"]]
+ 005d8fe4 ["CALL", null, ["ram:47acf4:8"]]
- 005d8fa4 bytes 4487fa97
+ 005d8fe4 bytes 4487fa97
- 005d9108 ["INT_ADD", "register:40f0:8", ["const:5d9108:8", "const:4:8"]]
- 005d9108 ["CALL", null, ["callee:0043ddd8:8"]]
+ 005d9148 ["INT_ADD", "register:40f0:8", ["const:5d9148:8", "const:4:8"]]
+ 005d9148 ["CALL", null, ["callee:0043ddd8:8"]]
- 005d9108 bytes 2493f997
+ 005d9148 bytes 2493f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a875b8adae941ed6f27d2b8d3d4a28f"></a>

### [`005d9c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c18.md) → [`005d9c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9c58.md) FUN_005d9c58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005d9c6c",
      "incomplete_value": false,
      "site": "005d9c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d9c2c",
      "incomplete_value": false,
      "site": "005d9c30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "005d9c70",
      "DATA",
      [
        "storage",
        "00c70e68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005d9c70",
      "DATA",
      [
        "storage",
        "00c71268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d9c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c18.md#insn-005d9c24) · [`005d9c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c18.md#insn-005d9c28) · [`005d9c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c18.md#insn-005d9c2c)
- 新版 `005d9c64`（命令位置の公開資料なし） · `005d9c68`（命令位置の公開資料なし） · `005d9c6c`（命令位置の公開資料なし）

~~~diff
- 005d9c24 ["INT_ADD", "register:40f0:8", ["const:5d9c24:8", "const:4:8"]]
- 005d9c24 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d9c64 ["INT_ADD", "register:40f0:8", ["const:5d9c64:8", "const:4:8"]]
+ 005d9c64 ["CALL", null, ["callee:00c57e90:8"]]
- 005d9c24 bytes 9bf71994
+ 005d9c64 bytes 8bf81994
- 005d9c28 ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005d9c68 ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005d9c28 bytes a83400f0
+ 005d9c68 bytes c8340090
- 005d9c2c ["COPY", "tmp:0:8", ["const:e68:8"]]
- 005d9c2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005d9c2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005d9c2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005d9c6c ["COPY", "tmp:0:8", ["const:268:8"]]
+ 005d9c6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005d9c6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005d9c6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005d9c2c bytes 08a13991
+ 005d9c6c bytes 08a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02fc0c71363eb32330cc3dd4953c01cf"></a>

### [`005d9c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c3c.md) → [`005d9c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9c7c.md) FUN_005d9c7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005d9c80",
      "incomplete_value": false,
      "site": "005d9c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d9c40",
      "incomplete_value": false,
      "site": "005d9c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "005d9c84",
      "DATA",
      [
        "storage",
        "00c70e68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005d9c84",
      "DATA",
      [
        "storage",
        "00c71268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d9c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c3c.md#insn-005d9c3c) · [`005d9c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c3c.md#insn-005d9c40)
- 新版 `005d9c7c`（命令位置の公開資料なし） · `005d9c80`（命令位置の公開資料なし）

~~~diff
- 005d9c3c ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005d9c7c ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005d9c3c bytes a83400f0
+ 005d9c7c bytes c8340090
- 005d9c40 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 005d9c40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005d9c40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005d9c40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005d9c80 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 005d9c80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005d9c80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005d9c80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005d9c40 bytes 08a13991
+ 005d9c80 bytes 08a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-377759baad190981807aa2a098a4c96b"></a>

### [`005d9c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c54.md) → [`005d9c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9c94.md) FUN_005d9c94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "site": "005d9cb8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d9c78",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "005d9cb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "005d9cb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d9c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c54.md#insn-005d9c78) · [`005d9c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c54.md#insn-005d9c84)
- 新版 `005d9cb8`（命令位置の公開資料なし） · `005d9cc4`（命令位置の公開資料なし）

~~~diff
- 005d9c78 ["INT_ADD", "register:40f0:8", ["const:5d9c78:8", "const:4:8"]]
- 005d9c78 ["CALL", null, ["ram:47acb4:8"]]
+ 005d9cb8 ["INT_ADD", "register:40f0:8", ["const:5d9cb8:8", "const:4:8"]]
+ 005d9cb8 ["CALL", null, ["ram:47acf4:8"]]
- 005d9c78 bytes 0f84fa97
+ 005d9cb8 bytes 0f84fa97
- 005d9c84 ["INT_ADD", "register:40f0:8", ["const:5d9c84:8", "const:4:8"]]
- 005d9c84 ["CALL", null, ["callee:0047cdd4:8"]]
+ 005d9cc4 ["INT_ADD", "register:40f0:8", ["const:5d9cc4:8", "const:4:8"]]
+ 005d9cc4 ["CALL", null, ["callee:0047cdd4:8"]]
- 005d9c84 bytes 448cfa97
+ 005d9cc4 bytes 448cfa97
~~~


<a id="compare-d82b4152806c57bd200797ef4a89cefa"></a>

### [`005d9eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9eb4.md) → [`005d9ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9ef4.md) FUN_005d9ef4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005d9f14",
      "incomplete_value": false,
      "site": "005d9f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d9ed4",
      "incomplete_value": false,
      "site": "005d9ed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
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
      "005d9f18",
      "DATA",
      [
        "storage",
        "00c70ef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005d9f18",
      "DATA",
      [
        "storage",
        "00c712f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d9ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9eb4.md#insn-005d9ec8) · [`005d9ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9eb4.md#insn-005d9ed0) · [`005d9ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9eb4.md#insn-005d9ed4)
- 新版 `005d9f08`（命令位置の公開資料なし） · `005d9f10`（命令位置の公開資料なし） · `005d9f14`（命令位置の公開資料なし）

~~~diff
- 005d9ec8 ["INT_ADD", "register:40f0:8", ["const:5d9ec8:8", "const:4:8"]]
- 005d9ec8 ["CALL", null, ["callee:00c57e90:8"]]
+ 005d9f08 ["INT_ADD", "register:40f0:8", ["const:5d9f08:8", "const:4:8"]]
+ 005d9f08 ["CALL", null, ["callee:00c57e90:8"]]
- 005d9ec8 bytes f2f61994
+ 005d9f08 bytes e2f71994
- 005d9ed0 ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005d9f10 ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005d9ed0 bytes a83400f0
+ 005d9f10 bytes c8340090
- 005d9ed4 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 005d9ed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005d9ed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005d9ed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005d9f14 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 005d9f14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005d9f14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005d9f14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005d9ed4 bytes 08e13b91
+ 005d9f14 bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c572808f33ee8f826fd81361243ce850"></a>

### [`005d9eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9eec.md) → [`005d9f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9f2c.md) FUN_005d9f2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005d9f30",
      "incomplete_value": false,
      "site": "005d9f34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d9ef0",
      "incomplete_value": false,
      "site": "005d9ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "005d9f34",
      "DATA",
      [
        "storage",
        "00c70ef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005d9f34",
      "DATA",
      [
        "storage",
        "00c712f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d9eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9eec.md#insn-005d9eec) · [`005d9ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9eec.md#insn-005d9ef0)
- 新版 `005d9f2c`（命令位置の公開資料なし） · `005d9f30`（命令位置の公開資料なし）

~~~diff
- 005d9eec ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 005d9f2c ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005d9eec bytes a83400f0
+ 005d9f2c bytes c8340090
- 005d9ef0 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 005d9ef0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005d9ef0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005d9ef0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005d9f30 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 005d9f30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005d9f30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005d9f30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005d9ef0 bytes 08e13b91
+ 005d9f30 bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17e113d69573625df74afd7d5ae895c0"></a>

### [`005d9f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9f0c.md) → [`005d9f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9f4c.md) FUN_005d9f4c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 18件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_count, call_target, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.35% / 新版 90.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 7件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005da020",
      "incomplete_value": true,
      "site": "005da030",
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
                "const:82a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d9fe0",
      "incomplete_value": true,
      "site": "005d9ff0",
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
                "const:74e:8"
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
      "definition_site": "005da024",
      "incomplete_value": true,
      "site": "005da034",
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
      "definition_site": "005d9fe4",
      "incomplete_value": true,
      "site": "005d9ff4",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005da028",
      "incomplete_value": true,
      "site": "005da038",
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
                "const:290:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d9fe8",
      "incomplete_value": true,
      "site": "005d9ff8",
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
                "const:250:8"
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
      "005d9fa8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0075b8e4"
      ]
    ],
    [
      "unmatched:005d9f6c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "005d9fb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "005d9fa8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0075b924"
      ]
    ],
    [
      "005d9fac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "005d9fb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d9f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9f0c.md#insn-005d9f68) · [`005d9f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9f0c.md#insn-005d9f6c) · [`005d9f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9f0c.md#insn-005d9f74)
- 新版 `005d9fa8`（命令位置の公開資料なし） · `005d9fb4`（命令位置の公開資料なし）

~~~diff
- 005d9f68 ["INT_ADD", "register:40f0:8", ["const:5d9f68:8", "const:4:8"]]
- 005d9f68 ["CALL", null, ["ram:75b8e4:8"]]
+ 005d9fa8 ["INT_ADD", "register:40f0:8", ["const:5d9fa8:8", "const:4:8"]]
+ 005d9fa8 ["CALL", null, ["ram:75b924:8"]]
- 005d9f68 bytes 5f060694
+ 005d9fa8 bytes 5f060694
- 005d9f6c ["INT_ADD", "register:40f0:8", ["const:5d9f6c:8", "const:4:8"]]
- 005d9f6c ["CALL", null, ["callee:008514f8:8"]]
- 005d9f6c bytes 53dd0994
- 005d9f74 ["INT_ADD", "register:40f0:8", ["const:5d9f74:8", "const:4:8"]]
- 005d9f74 ["CALL", null, ["ram:47acb4:8"]]
+ 005d9fb4 ["INT_ADD", "register:40f0:8", ["const:5d9fb4:8", "const:4:8"]]
+ 005d9fb4 ["CALL", null, ["ram:47acf4:8"]]
- 005d9f74 bytes 5083fa97
+ 005d9fb4 bytes 5083fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ceb4ed60543e7af1e5b4ade01299711"></a>

### [`005da66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da66c.md) → [`005da6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005da/005da6ac.md) FUN_005da6ac

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005da544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da544.md) [`005da66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da66c.md) [`00628d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00628/00628d04.md) [`006675e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/006675e0.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 4件 [`005da584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005da/005da584.md) [`005da6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005da/005da6ac.md) [`00628d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00628/00628d44.md) [`00667620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00667/00667620.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005da8d0",
      "incomplete_value": false,
      "site": "005da8d8",
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
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005da890",
      "incomplete_value": false,
      "site": "005da898",
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
            "const:da7:8"
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
      "definition_site": "005da8ec",
      "incomplete_value": false,
      "site": "005da8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005da8ac",
      "incomplete_value": false,
      "site": "005da8b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ea9:8"
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
      "definition_site": "005da9a0",
      "incomplete_value": false,
      "site": "005da9ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005da960",
      "incomplete_value": false,
      "site": "005da96c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ea9:8"
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
      "005da818",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "005da8d0",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "005da8ec",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005da818",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "005da8d0",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "005da8ec",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005da898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da66c.md#insn-005da898) · [`005da8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da66c.md#insn-005da8b8) · [`005da96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da66c.md#insn-005da96c)
- 新版 `005da8d8`（命令位置の公開資料なし） · `005da8f8`（命令位置の公開資料なし） · `005da9ac`（命令位置の公開資料なし）

~~~diff
- 005da898 ["INT_ADD", "register:40f0:8", ["const:5da898:8", "const:4:8"]]
- 005da898 ["CALL", null, ["callee:00441e94:8"]]
+ 005da8d8 ["INT_ADD", "register:40f0:8", ["const:5da8d8:8", "const:4:8"]]
+ 005da8d8 ["CALL", null, ["callee:00441e94:8"]]
- 005da898 bytes 6f9df997
+ 005da8d8 bytes 6f9df997
- 005da8b8 ["INT_ADD", "register:40f0:8", ["const:5da8b8:8", "const:4:8"]]
- 005da8b8 ["CALL", null, ["callee:004427f4:8"]]
+ 005da8f8 ["INT_ADD", "register:40f0:8", ["const:5da8f8:8", "const:4:8"]]
+ 005da8f8 ["CALL", null, ["callee:004427f4:8"]]
- 005da8b8 bytes bf9ff997
+ 005da8f8 bytes bf9ff997
- 005da96c ["INT_ADD", "register:40f0:8", ["const:5da96c:8", "const:4:8"]]
- 005da96c ["CALL", null, ["callee:004427f4:8"]]
+ 005da9ac ["INT_ADD", "register:40f0:8", ["const:5da9ac:8", "const:4:8"]]
+ 005da9ac ["CALL", null, ["callee:004427f4:8"]]
- 005da96c bytes 929ff997
+ 005da9ac bytes 929ff997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

