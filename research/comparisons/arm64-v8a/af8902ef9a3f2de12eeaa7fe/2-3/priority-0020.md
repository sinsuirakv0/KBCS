# v16.0.0 → v16.0.1 · 最優先の変更候補 (20)

[一覧の目次](README.md)

<a id="compare-77b0d80773297b27dbd06030df65adb2"></a>

### [`005997c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md) → [`00599804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md) FUN_00599804

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00599674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599674.md) · 呼出先 12件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`0059b300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b300.md) [`0059b350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b350.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md)
- 新版 呼出元 1件 [`005996b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md) · 呼出先 12件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`0059b340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b340.md) [`0059b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b390.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 95.05% / 新版 95.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005998a4",
      "incomplete_value": false,
      "site": "005998a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599864",
      "incomplete_value": false,
      "site": "00599864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00599830",
      "value": [
        "leaf",
        "ram:764384:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005997f0",
      "value": [
        "leaf",
        "ram:764344:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005997f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00599830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ],
    [
      "unmatched:005997f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "0059983c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768564"
      ]
    ]
  ],
  "added": [
    [
      "00599830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "00599834",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "0059983c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007685a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005997f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md#insn-005997f0) · [`005997f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md#insn-005997f4) · [`005997fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md#insn-005997fc)
- 新版 `00599830`（命令位置の公開資料なし） · `0059983c`（命令位置の公開資料なし）

~~~diff
- 005997f0 ["INT_ADD", "register:40f0:8", ["const:5997f0:8", "const:4:8"]]
- 005997f0 ["CALL", null, ["ram:764344:8"]]
+ 00599830 ["INT_ADD", "register:40f0:8", ["const:599830:8", "const:4:8"]]
+ 00599830 ["CALL", null, ["ram:764384:8"]]
- 005997f0 bytes d52a0794
+ 00599830 bytes d52a0794
- 005997f4 ["INT_ADD", "register:40f0:8", ["const:5997f4:8", "const:4:8"]]
- 005997f4 ["CALL", null, ["callee:008514f8:8"]]
- 005997f4 bytes 31df0a94
- 005997fc ["INT_ADD", "register:40f0:8", ["const:5997fc:8", "const:4:8"]]
- 005997fc ["CALL", null, ["ram:768564:8"]]
+ 0059983c ["INT_ADD", "register:40f0:8", ["const:59983c:8", "const:4:8"]]
+ 0059983c ["CALL", null, ["ram:7685a4:8"]]
- 005997fc bytes 5a3b0794
+ 0059983c bytes 5a3b0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8b2620be4f1892d0a4bf36728408e71"></a>

### [`00599a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599a34.md) → [`00599a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599a74.md) FUN_00599a74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0059a6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a6c8.md) [`0059add8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059add8.md) · 呼出先 4件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`0059a708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a708.md) [`0059ae18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ae18.md) · 呼出先 4件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00599aa8",
      "incomplete_value": false,
      "site": "00599ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599a68",
      "incomplete_value": false,
      "site": "00599a78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:188:8"
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
      "definition_site": "00599b1c",
      "incomplete_value": false,
      "site": "00599b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599adc",
      "incomplete_value": false,
      "site": "00599ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "00599aa8",
      "PARAM",
      [
        "storage",
        "00ca6188",
        null,
        "undefined1"
      ]
    ],
    [
      "00599b1c",
      "PARAM",
      [
        "storage",
        "00ca6170",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00599aa8",
      "PARAM",
      [
        "storage",
        "00ca6588",
        null,
        "undefined1"
      ]
    ],
    [
      "00599b1c",
      "PARAM",
      [
        "storage",
        "00ca6570",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599a34.md#insn-00599a78) · [`00599ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599a34.md#insn-00599ae4) · [`00599a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599a34.md#insn-00599a68)
- 新版 `00599ab8`（命令位置の公開資料なし） · `00599b24`（命令位置の公開資料なし） · `00599aa8`（命令位置の公開資料なし）

~~~diff
- 00599a78 ["INT_ADD", "register:40f0:8", ["const:599a78:8", "const:4:8"]]
- 00599a78 ["CALL", null, ["callee:0044108c:8"]]
+ 00599ab8 ["INT_ADD", "register:40f0:8", ["const:599ab8:8", "const:4:8"]]
+ 00599ab8 ["CALL", null, ["callee:0044108c:8"]]
- 00599a78 bytes 759dfa97
+ 00599ab8 bytes 759dfa97
- 00599ae4 ["INT_ADD", "register:40f0:8", ["const:599ae4:8", "const:4:8"]]
- 00599ae4 ["CALL", null, ["callee:0044108c:8"]]
+ 00599b24 ["INT_ADD", "register:40f0:8", ["const:599b24:8", "const:4:8"]]
+ 00599b24 ["CALL", null, ["callee:0044108c:8"]]
- 00599ae4 bytes 5a9dfa97
+ 00599b24 bytes 5a9dfa97
- 00599a68 ["COPY", "tmp:0:8", ["const:188:8"]]
- 00599a68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00599a68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00599a68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00599aa8 ["COPY", "tmp:0:8", ["const:588:8"]]
+ 00599aa8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00599aa8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00599aa8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00599a68 bytes 21200691
+ 00599aa8 bytes 21201691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c99401ed8d502a5e084a5021f7cbc44"></a>

### [`00599e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599e14.md) → [`00599e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e54.md) FUN_00599e54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00599ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599ef8.md) [`005ad444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad444.md) [`005ad4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad4d0.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 3件 [`00599f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599f38.md) [`005ad484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad484.md) [`005ad510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad510.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00599e6c",
      "incomplete_value": false,
      "site": "00599e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599e2c",
      "incomplete_value": false,
      "site": "00599e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "00599e70",
      "DATA",
      [
        "storage",
        "00c6d328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00599e70",
      "DATA",
      [
        "storage",
        "00c6d728",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599e14.md#insn-00599e2c) · [`00599e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599e14.md#insn-00599e40) · [`00599e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599e14.md#insn-00599e54)
- 新版 `00599e6c`（命令位置の公開資料なし） · `00599e80`（命令位置の公開資料なし） · `00599e94`（命令位置の公開資料なし）

~~~diff
- 00599e2c ["COPY", "tmp:0:8", ["const:328:8"]]
- 00599e2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00599e2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00599e2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00599e6c ["COPY", "tmp:0:8", ["const:728:8"]]
+ 00599e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00599e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00599e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00599e2c bytes 08a10c91
+ 00599e6c bytes 08a11c91
- 00599e40 ["INT_ADD", "register:40f0:8", ["const:599e40:8", "const:4:8"]]
- 00599e40 ["CALL", null, ["callee:00c53d00:8"]]
+ 00599e80 ["INT_ADD", "register:40f0:8", ["const:599e80:8", "const:4:8"]]
+ 00599e80 ["CALL", null, ["callee:00c53d00:8"]]
- 00599e40 bytes a8e61a94
+ 00599e80 bytes a0e71a94
- 00599e54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599e54 ["INT_ADD", "register:40f0:8", ["const:599e54:8", "const:4:8"]]
- 00599e54 ["CALLIND", null, ["register:0:8"]]
+ 00599e94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599e94 ["INT_ADD", "register:40f0:8", ["const:599e94:8", "const:4:8"]]
+ 00599e94 ["CALLIND", null, ["register:0:8"]]
- 00599e54 bytes 00013fd6
+ 00599e94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1909d430914d2a2403dd72777197c9b7"></a>

### [`00599f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599f1c.md) → [`00599f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599f5c.md) FUN_00599f5c

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
      "definition_site": "00599f68",
      "incomplete_value": false,
      "site": "00599f74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599f28",
      "incomplete_value": false,
      "site": "00599f34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:390:8"
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
      "00599f74",
      "DATA",
      [
        "storage",
        "00c6d390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00599f74",
      "DATA",
      [
        "storage",
        "00c6d790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599f1c.md#insn-00599f28)
- 新版 `00599f68`（命令位置の公開資料なし）

~~~diff
- 00599f28 ["COPY", "tmp:0:8", ["const:390:8"]]
- 00599f28 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00599f28 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00599f28 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00599f68 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 00599f68 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00599f68 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00599f68 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00599f28 bytes 4a410e91
+ 00599f68 bytes 4a411e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-062c3b8648ddc91716884e09cc4b27af"></a>

### [`00599f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599f60.md) → [`00599fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599fa0.md) FUN_00599fa0

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
      "definition_site": "00599fb8",
      "incomplete_value": false,
      "site": "00599fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599f78",
      "incomplete_value": false,
      "site": "00599f84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:390:8"
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
      "00599fc4",
      "DATA",
      [
        "storage",
        "00c6d390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00599fc4",
      "DATA",
      [
        "storage",
        "00c6d790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599f60.md#insn-00599f78) · [`00599fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599f60.md#insn-00599fa8)
- 新版 `00599fb8`（命令位置の公開資料なし） · `00599fe8`（命令位置の公開資料なし）

~~~diff
- 00599f78 ["COPY", "tmp:0:8", ["const:390:8"]]
- 00599f78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00599f78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00599f78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00599fb8 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 00599fb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00599fb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00599fb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00599f78 bytes 08410e91
+ 00599fb8 bytes 08411e91
- 00599fa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599fa8 ["INT_ADD", "register:40f0:8", ["const:599fa8:8", "const:4:8"]]
- 00599fa8 ["CALLIND", null, ["register:0:8"]]
+ 00599fe8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599fe8 ["INT_ADD", "register:40f0:8", ["const:599fe8:8", "const:4:8"]]
+ 00599fe8 ["CALLIND", null, ["register:0:8"]]
- 00599fa8 bytes 00013fd6
+ 00599fe8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc6924d6a4d8c77eaa8e6422120dbced"></a>

### [`00599fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599fbc.md) → [`00599ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599ffc.md) FUN_00599ffc

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
      "definition_site": "0059a028",
      "incomplete_value": false,
      "site": "0059a028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599fe8",
      "incomplete_value": false,
      "site": "00599fe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:390:8"
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
      "0059a028",
      "DATA",
      [
        "storage",
        "00c6d390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a028",
      "DATA",
      [
        "storage",
        "00c6d790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599fbc.md#insn-00599fd0) · [`00599fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599fbc.md#insn-00599fe0) · [`0059a004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599fbc.md#insn-0059a004)
- 新版 `0059a010`（命令位置の公開資料なし） · `0059a020`（命令位置の公開資料なし） · `0059a044`（命令位置の公開資料なし）

~~~diff
- 00599fd0 ["INT_ADD", "register:40f0:8", ["const:599fd0:8", "const:4:8"]]
- 00599fd0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0059a010 ["INT_ADD", "register:40f0:8", ["const:59a010:8", "const:4:8"]]
+ 0059a010 ["CALL", null, ["callee:00c57e90:8"]]
- 00599fd0 bytes b0f61a94
+ 0059a010 bytes a0f71a94
- 00599fe0 ["COPY", "tmp:0:8", ["const:390:8"]]
- 00599fe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00599fe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00599fe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059a020 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 0059a020 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059a020 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059a020 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00599fe0 bytes 08410e91
+ 0059a020 bytes 08411e91
- 0059a004 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a004 ["INT_ADD", "register:40f0:8", ["const:59a004:8", "const:4:8"]]
- 0059a004 ["CALLIND", null, ["register:0:8"]]
+ 0059a044 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a044 ["INT_ADD", "register:40f0:8", ["const:59a044:8", "const:4:8"]]
+ 0059a044 ["CALLIND", null, ["register:0:8"]]
- 0059a004 bytes 00013fd6
+ 0059a044 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b7e671bcc54edfbca12d2559a20fba4"></a>

### [`0059a044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a044.md) → [`0059a084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a084.md) FUN_0059a084

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
      "definition_site": "0059a0a0",
      "incomplete_value": false,
      "site": "0059a0a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a060",
      "incomplete_value": false,
      "site": "0059a060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:390:8"
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
      "0059a0a0",
      "DATA",
      [
        "storage",
        "00c6d390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a0a0",
      "DATA",
      [
        "storage",
        "00c6d790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a044.md#insn-0059a05c) · [`0059a080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a044.md#insn-0059a080)
- 新版 `0059a09c`（命令位置の公開資料なし） · `0059a0c0`（命令位置の公開資料なし）

~~~diff
- 0059a05c ["COPY", "tmp:0:8", ["const:390:8"]]
- 0059a05c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059a05c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059a05c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a09c ["COPY", "tmp:0:8", ["const:790:8"]]
+ 0059a09c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a09c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a09c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059a05c bytes 29410e91
+ 0059a09c bytes 29411e91
- 0059a080 ["COPY", "register:0:8", ["register:4048:8"]]
- 0059a080 ["INT_ADD", "register:40f0:8", ["const:59a080:8", "const:4:8"]]
- 0059a080 ["CALLIND", null, ["register:0:8"]]
+ 0059a0c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0059a0c0 ["INT_ADD", "register:40f0:8", ["const:59a0c0:8", "const:4:8"]]
+ 0059a0c0 ["CALLIND", null, ["register:0:8"]]
- 0059a080 bytes 20013fd6
+ 0059a0c0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8669f5c19821da2dff1e4143e85b378c"></a>

### [`0059a458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a458.md) → [`0059a498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a498.md) FUN_0059a498

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00598d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598d80.md) [`005aca04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005aca04.md) · 呼出先 3件 [`00beffac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beffac.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 2件 [`00598dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md) [`005aca44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md) · 呼出先 3件 [`00bf03d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf03d4.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059a4b8",
      "incomplete_value": true,
      "site": "0059a4bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a478",
      "incomplete_value": true,
      "site": "0059a47c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059a4c0",
      "incomplete_value": true,
      "site": "0059a4c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:310:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a480",
      "incomplete_value": true,
      "site": "0059a488",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
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
      "definition_site": "0059a4c4",
      "incomplete_value": true,
      "site": "0059a4c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:318:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a484",
      "incomplete_value": true,
      "site": "0059a488",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0059a4b4",
      "READ",
      [
        "storage",
        "00c9af08",
        null,
        "pointer"
      ]
    ],
    [
      "0059a4bc",
      "DATA",
      [
        "storage",
        "00c92608",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "0059a4c0",
      "READ",
      [
        "storage",
        "00c9af10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059a4b4",
      "READ",
      [
        "storage",
        "00c9b308",
        null,
        "pointer"
      ]
    ],
    [
      "0059a4bc",
      "DATA",
      [
        "storage",
        "00c92a08",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "0059a4c0",
      "READ",
      [
        "storage",
        "00c9b310",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a458.md#insn-0059a488) · [`0059a464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a458.md#insn-0059a464) · [`0059a468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a458.md#insn-0059a468)
- 新版 `0059a4c8`（命令位置の公開資料なし） · `0059a4a4`（命令位置の公開資料なし） · `0059a4a8`（命令位置の公開資料なし）

~~~diff
- 0059a488 ["INT_ADD", "register:40f0:8", ["const:59a488:8", "const:4:8"]]
- 0059a488 ["CALL", null, ["callee:00c57f10:8"]]
+ 0059a4c8 ["INT_ADD", "register:40f0:8", ["const:59a4c8:8", "const:4:8"]]
+ 0059a4c8 ["CALL", null, ["callee:00c57f10:8"]]
- 0059a488 bytes a2f51a94
+ 0059a4c8 bytes 92f61a94
- 0059a464 ["INT_ADD", "register:40f0:8", ["const:59a464:8", "const:4:8"]]
- 0059a464 ["CALL", null, ["callee:00c57ef0:8"]]
+ 0059a4a4 ["INT_ADD", "register:40f0:8", ["const:59a4a4:8", "const:4:8"]]
+ 0059a4a4 ["CALL", null, ["callee:00c57ef0:8"]]
- 0059a464 bytes a3f51a94
+ 0059a4a4 bytes 93f61a94
- 0059a468 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0059a4a8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0059a468 bytes 08380090
+ 0059a4a8 bytes 083800b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92fb07991d69465c70fb34bd85724bd2"></a>

### [`0059a48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a48c.md) → [`0059a4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a4cc.md) FUN_0059a4cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059a4e4",
      "incomplete_value": false,
      "site": "0059a4e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a4a4",
      "incomplete_value": false,
      "site": "0059a4a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "0059a4e8",
      "DATA",
      [
        "storage",
        "00c6d480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a4e8",
      "DATA",
      [
        "storage",
        "00c6d880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a48c.md#insn-0059a4a4) · [`0059a4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a48c.md#insn-0059a4b4)
- 新版 `0059a4e4`（命令位置の公開資料なし） · `0059a4f4`（命令位置の公開資料なし）

~~~diff
- 0059a4a4 ["COPY", "tmp:0:8", ["const:480:8"]]
- 0059a4a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059a4a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059a4a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a4e4 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 0059a4e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a4e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a4e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059a4a4 bytes 29011291
+ 0059a4e4 bytes 29012291
- 0059a4b4 ["INT_ADD", "register:40f0:8", ["const:59a4b4:8", "const:4:8"]]
- 0059a4b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059a4f4 ["INT_ADD", "register:40f0:8", ["const:59a4f4:8", "const:4:8"]]
+ 0059a4f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059a4b4 bytes 7ff51a94
+ 0059a4f4 bytes 6ff61a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc9fc3065ea25fa00522139dbc6c6797"></a>

### [`0059a4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a4d8.md) → [`0059a518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a518.md) FUN_0059a518

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059a530",
      "incomplete_value": false,
      "site": "0059a534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a4f0",
      "incomplete_value": false,
      "site": "0059a4f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "0059a534",
      "DATA",
      [
        "storage",
        "00c6d480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a534",
      "DATA",
      [
        "storage",
        "00c6d880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a4d8.md#insn-0059a4f0) · [`0059a500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a4d8.md#insn-0059a500) · [`0059a50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a4d8.md#insn-0059a50c)
- 新版 `0059a530`（命令位置の公開資料なし） · `0059a540`（命令位置の公開資料なし） · `0059a54c`（命令位置の公開資料なし）

~~~diff
- 0059a4f0 ["COPY", "tmp:0:8", ["const:480:8"]]
- 0059a4f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059a4f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059a4f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a530 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 0059a530 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a530 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a530 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059a4f0 bytes 29011291
+ 0059a530 bytes 29012291
- 0059a500 ["INT_ADD", "register:40f0:8", ["const:59a500:8", "const:4:8"]]
- 0059a500 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059a540 ["INT_ADD", "register:40f0:8", ["const:59a540:8", "const:4:8"]]
+ 0059a540 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059a500 bytes 6cf51a94
+ 0059a540 bytes 5cf61a94
- 0059a50c ["INT_ADD", "register:40f0:8", ["const:59a50c:8", "const:4:8"]]
- 0059a50c ["CALL", null, ["callee:00c57e80:8"]]
+ 0059a54c ["INT_ADD", "register:40f0:8", ["const:59a54c:8", "const:4:8"]]
+ 0059a54c ["CALL", null, ["callee:00c57e80:8"]]
- 0059a50c bytes 5df51a94
+ 0059a54c bytes 4df61a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4ec41569a67ae6bbdd9626c35e20bc2"></a>

### [`0059a520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a520.md) → [`0059a560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a560.md) FUN_0059a560

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0059a588",
      "incomplete_value": false,
      "site": "0059a588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a548",
      "incomplete_value": false,
      "site": "0059a548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "0059a588",
      "DATA",
      [
        "storage",
        "00c6d480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a588",
      "DATA",
      [
        "storage",
        "00c6d880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a520.md#insn-0059a588) · [`0059a534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a520.md#insn-0059a534) · [`0059a544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a520.md#insn-0059a544)
- 新版 `0059a5c8`（命令位置の公開資料なし） · `0059a574`（命令位置の公開資料なし） · `0059a584`（命令位置の公開資料なし）

~~~diff
- 0059a588 ["INT_ADD", "register:40f0:8", ["const:59a588:8", "const:4:8"]]
- 0059a588 ["CALL", null, ["callee:0043bb20:8"]]
+ 0059a5c8 ["INT_ADD", "register:40f0:8", ["const:59a5c8:8", "const:4:8"]]
+ 0059a5c8 ["CALL", null, ["callee:0043bb20:8"]]
- 0059a588 bytes 5685fa97
+ 0059a5c8 bytes 5685fa97
- 0059a534 ["INT_ADD", "register:40f0:8", ["const:59a534:8", "const:4:8"]]
- 0059a534 ["CALL", null, ["callee:00c57e90:8"]]
+ 0059a574 ["INT_ADD", "register:40f0:8", ["const:59a574:8", "const:4:8"]]
+ 0059a574 ["CALL", null, ["callee:00c57e90:8"]]
- 0059a534 bytes 57f51a94
+ 0059a574 bytes 47f61a94
- 0059a544 ["COPY", "tmp:0:8", ["const:480:8"]]
- 0059a544 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059a544 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059a544 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a584 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 0059a584 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a584 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a584 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059a544 bytes 29011291
+ 0059a584 bytes 29012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-571ffda535f7c8a74516de4ab0c9aef8"></a>

### [`0059a5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a5c0.md) → [`0059a600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a600.md) FUN_0059a600

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "0059a620",
      "incomplete_value": false,
      "site": "0059a620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a5e0",
      "incomplete_value": false,
      "site": "0059a5e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "0059a620",
      "DATA",
      [
        "storage",
        "00c6d480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a620",
      "DATA",
      [
        "storage",
        "00c6d880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a5c0.md#insn-0059a620) · [`0059a5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a5c0.md#insn-0059a5dc) · [`0059a5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a5c0.md#insn-0059a5f4)
- 新版 `0059a660`（命令位置の公開資料なし） · `0059a61c`（命令位置の公開資料なし） · `0059a634`（命令位置の公開資料なし）

~~~diff
- 0059a620 ["INT_ADD", "register:40f0:8", ["const:59a620:8", "const:4:8"]]
- 0059a620 ["CALL", null, ["callee:0043bb20:8"]]
+ 0059a660 ["INT_ADD", "register:40f0:8", ["const:59a660:8", "const:4:8"]]
+ 0059a660 ["CALL", null, ["callee:0043bb20:8"]]
- 0059a620 bytes 3085fa97
+ 0059a660 bytes 3085fa97
- 0059a5dc ["COPY", "tmp:0:8", ["const:480:8"]]
- 0059a5dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059a5dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059a5dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a61c ["COPY", "tmp:0:8", ["const:880:8"]]
+ 0059a61c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a61c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a61c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059a5dc bytes 29011291
+ 0059a61c bytes 29012291
- 0059a5f4 ["INT_ADD", "register:40f0:8", ["const:59a5f4:8", "const:4:8"]]
- 0059a5f4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0059a634 ["INT_ADD", "register:40f0:8", ["const:59a634:8", "const:4:8"]]
+ 0059a634 ["CALL", null, ["callee:00c53cd0:8"]]
- 0059a5f4 bytes afe41a94
+ 0059a634 bytes a7e51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35a774cf2e6a0b3ca7c9f838ef665715"></a>

### [`0059aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059aaf8.md) → [`0059ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ab38.md) FUN_0059ab38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059ab50",
      "incomplete_value": false,
      "site": "0059ab54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ab10",
      "incomplete_value": false,
      "site": "0059ab14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "0059ab54",
      "DATA",
      [
        "storage",
        "00c6d500",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059ab54",
      "DATA",
      [
        "storage",
        "00c6d900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ab54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059aaf8.md#insn-0059ab54) · [`0059ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059aaf8.md#insn-0059ab10) · [`0059ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059aaf8.md#insn-0059ab20)
- 新版 `0059ab94`（命令位置の公開資料なし） · `0059ab50`（命令位置の公開資料なし） · `0059ab60`（命令位置の公開資料なし）

~~~diff
- 0059ab54 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059ab54 ["INT_ADD", "register:40f0:8", ["const:59ab54:8", "const:4:8"]]
- 0059ab54 ["CALLIND", null, ["register:0:8"]]
+ 0059ab94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059ab94 ["INT_ADD", "register:40f0:8", ["const:59ab94:8", "const:4:8"]]
+ 0059ab94 ["CALLIND", null, ["register:0:8"]]
- 0059ab54 bytes 00013fd6
+ 0059ab94 bytes 00013fd6
- 0059ab10 ["COPY", "tmp:0:8", ["const:500:8"]]
- 0059ab10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059ab10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059ab10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059ab50 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 0059ab50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059ab50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059ab50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059ab10 bytes 29011491
+ 0059ab50 bytes 29012491
- 0059ab20 ["INT_ADD", "register:40f0:8", ["const:59ab20:8", "const:4:8"]]
- 0059ab20 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059ab60 ["INT_ADD", "register:40f0:8", ["const:59ab60:8", "const:4:8"]]
+ 0059ab60 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059ab20 bytes e4f31a94
+ 0059ab60 bytes d4f41a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27d3d8710e494767f7c0281f2792f5ee"></a>

### [`0059ab68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ab68.md) → [`0059aba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059aba8.md) FUN_0059aba8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059abc0",
      "incomplete_value": false,
      "site": "0059abc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ab80",
      "incomplete_value": false,
      "site": "0059ab84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "0059abc4",
      "DATA",
      [
        "storage",
        "00c6d500",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059abc4",
      "DATA",
      [
        "storage",
        "00c6d900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ab80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ab68.md#insn-0059ab80) · [`0059ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ab68.md#insn-0059ab90) · [`0059aba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ab68.md#insn-0059aba4)
- 新版 `0059abc0`（命令位置の公開資料なし） · `0059abd0`（命令位置の公開資料なし） · `0059abe4`（命令位置の公開資料なし）

~~~diff
- 0059ab80 ["COPY", "tmp:0:8", ["const:500:8"]]
- 0059ab80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059ab80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059ab80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059abc0 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 0059abc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059abc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059abc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059ab80 bytes 29011491
+ 0059abc0 bytes 29012491
- 0059ab90 ["INT_ADD", "register:40f0:8", ["const:59ab90:8", "const:4:8"]]
- 0059ab90 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059abd0 ["INT_ADD", "register:40f0:8", ["const:59abd0:8", "const:4:8"]]
+ 0059abd0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059ab90 bytes c8f31a94
+ 0059abd0 bytes b8f41a94
- 0059aba4 ["INT_ADD", "register:40f0:8", ["const:59aba4:8", "const:4:8"]]
- 0059aba4 ["CALL", null, ["callee:00c53d00:8"]]
+ 0059abe4 ["INT_ADD", "register:40f0:8", ["const:59abe4:8", "const:4:8"]]
+ 0059abe4 ["CALL", null, ["callee:00c53d00:8"]]
- 0059aba4 bytes 4fe31a94
+ 0059abe4 bytes 47e41a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f301aad9ec3efe1b955616f1a9b8dcf6"></a>

### [`0059abd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059abd4.md) → [`0059ac14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ac14.md) FUN_0059ac14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059ac34",
      "incomplete_value": false,
      "site": "0059ac3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059abf4",
      "incomplete_value": false,
      "site": "0059abfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "0059ac3c",
      "DATA",
      [
        "storage",
        "00c6d500",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059ac3c",
      "DATA",
      [
        "storage",
        "00c6d900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059abec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059abd4.md#insn-0059abec) · [`0059abf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059abd4.md#insn-0059abf4) · [`0059abf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059abd4.md#insn-0059abf8)
- 新版 `0059ac2c`（命令位置の公開資料なし） · `0059ac34`（命令位置の公開資料なし）

~~~diff
- 0059abec ["INT_ADD", "register:40f0:8", ["const:59abec:8", "const:4:8"]]
- 0059abec ["CALL", null, ["callee:00c57e90:8"]]
+ 0059ac2c ["INT_ADD", "register:40f0:8", ["const:59ac2c:8", "const:4:8"]]
+ 0059ac2c ["CALL", null, ["callee:00c57e90:8"]]
- 0059abec bytes a9f31a94
+ 0059ac2c bytes 99f41a94
- 0059abf4 ["COPY", "tmp:0:8", ["const:500:8"]]
- 0059abf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059abf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059abf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059ac34 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 0059ac34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ac34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ac34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059abf4 bytes 08011491
+ 0059ac34 bytes 08012491
- 0059abf8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 0059abf8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e34e7eb667c0939513bf61f18be5457"></a>

### [`0059ac7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ac7c.md) → [`0059acbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059acbc.md) FUN_0059acbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059acd0",
      "incomplete_value": false,
      "site": "0059acd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ac90",
      "incomplete_value": false,
      "site": "0059ac98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "0059acd8",
      "DATA",
      [
        "storage",
        "00c6d500",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059acd8",
      "DATA",
      [
        "storage",
        "00c6d900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ac90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ac7c.md#insn-0059ac90) · [`0059acc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ac7c.md#insn-0059acc0) · [`0059acec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ac7c.md#insn-0059acec)
- 新版 `0059acd0`（命令位置の公開資料なし） · `0059ad00`（命令位置の公開資料なし） · `0059ad2c`（命令位置の公開資料なし）

~~~diff
- 0059ac90 ["COPY", "tmp:0:8", ["const:500:8"]]
- 0059ac90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059ac90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059ac90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059acd0 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 0059acd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059acd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059acd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059ac90 bytes 08011491
+ 0059acd0 bytes 08012491
- 0059acc0 ["INT_ADD", "register:40f0:8", ["const:59acc0:8", "const:4:8"]]
- 0059acc0 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0059ad00 ["INT_ADD", "register:40f0:8", ["const:59ad00:8", "const:4:8"]]
+ 0059ad00 ["CALL", null, ["callee:00c53cd0:8"]]
- 0059acc0 bytes fce21a94
+ 0059ad00 bytes f4e31a94
- 0059acec ["INT_ADD", "register:40f0:8", ["const:59acec:8", "const:4:8"]]
- 0059acec ["CALL", null, ["callee:0043bb20:8"]]
+ 0059ad2c ["INT_ADD", "register:40f0:8", ["const:59ad2c:8", "const:4:8"]]
+ 0059ad2c ["CALL", null, ["callee:0043bb20:8"]]
- 0059acec bytes 7d83fa97
+ 0059ad2c bytes 7d83fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-427c7570a6a53872ce543606e282a1bd"></a>

### [`0059b1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b1c4.md) → [`0059b204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b204.md) FUN_0059b204

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "0059b218",
      "incomplete_value": false,
      "site": "0059b21c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059b1d8",
      "incomplete_value": false,
      "site": "0059b1dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:580:8"
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
      "0059b21c",
      "DATA",
      [
        "storage",
        "00c6d580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059b21c",
      "DATA",
      [
        "storage",
        "00c6d980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059b1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b1c4.md#insn-0059b1d8) · [`0059b1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b1c4.md#insn-0059b1ec) · [`0059b20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b1c4.md#insn-0059b20c)
- 新版 `0059b218`（命令位置の公開資料なし） · `0059b22c`（命令位置の公開資料なし） · `0059b24c`（命令位置の公開資料なし）

~~~diff
- 0059b1d8 ["COPY", "tmp:0:8", ["const:580:8"]]
- 0059b1d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059b1d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059b1d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059b218 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 0059b218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059b218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059b218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059b1d8 bytes 08011691
+ 0059b218 bytes 08012691
- 0059b1ec ["INT_ADD", "register:40f0:8", ["const:59b1ec:8", "const:4:8"]]
- 0059b1ec ["CALL", null, ["callee:00c53d00:8"]]
+ 0059b22c ["INT_ADD", "register:40f0:8", ["const:59b22c:8", "const:4:8"]]
+ 0059b22c ["CALL", null, ["callee:00c53d00:8"]]
- 0059b1ec bytes bde11a94
+ 0059b22c bytes b5e21a94
- 0059b20c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059b20c ["INT_ADD", "register:40f0:8", ["const:59b20c:8", "const:4:8"]]
- 0059b20c ["CALLIND", null, ["register:0:8"]]
+ 0059b24c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059b24c ["INT_ADD", "register:40f0:8", ["const:59b24c:8", "const:4:8"]]
+ 0059b24c ["CALLIND", null, ["register:0:8"]]
- 0059b20c bytes 00013fd6
+ 0059b24c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a2e57b28d8a5e90d992956e82fd0758"></a>

### [`0059b220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b220.md) → [`0059b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b260.md) FUN_0059b260

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059b278",
      "incomplete_value": false,
      "site": "0059b27c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059b238",
      "incomplete_value": false,
      "site": "0059b23c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:580:8"
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
      "0059b27c",
      "DATA",
      [
        "storage",
        "00c6d580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059b27c",
      "DATA",
      [
        "storage",
        "00c6d980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059b238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b220.md#insn-0059b238) · [`0059b24c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b220.md#insn-0059b24c) · [`0059b260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b220.md#insn-0059b260)
- 新版 `0059b278`（命令位置の公開資料なし） · `0059b28c`（命令位置の公開資料なし） · `0059b2a0`（命令位置の公開資料なし）

~~~diff
- 0059b238 ["COPY", "tmp:0:8", ["const:580:8"]]
- 0059b238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059b238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059b238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059b278 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 0059b278 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059b278 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059b278 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059b238 bytes 08011691
+ 0059b278 bytes 08012691
- 0059b24c ["INT_ADD", "register:40f0:8", ["const:59b24c:8", "const:4:8"]]
- 0059b24c ["CALL", null, ["callee:00c53d00:8"]]
+ 0059b28c ["INT_ADD", "register:40f0:8", ["const:59b28c:8", "const:4:8"]]
+ 0059b28c ["CALL", null, ["callee:00c53d00:8"]]
- 0059b24c bytes a5e11a94
+ 0059b28c bytes 9de21a94
- 0059b260 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059b260 ["INT_ADD", "register:40f0:8", ["const:59b260:8", "const:4:8"]]
- 0059b260 ["CALLIND", null, ["register:0:8"]]
+ 0059b2a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059b2a0 ["INT_ADD", "register:40f0:8", ["const:59b2a0:8", "const:4:8"]]
+ 0059b2a0 ["CALLIND", null, ["register:0:8"]]
- 0059b260 bytes 00013fd6
+ 0059b2a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e262f4b252bfcfe3b436f2dc28b55005"></a>

### [`0059b27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b27c.md) → [`0059b2bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b2bc.md) FUN_0059b2bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0059b2e0",
      "incomplete_value": false,
      "site": "0059b2e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059b2a0",
      "incomplete_value": false,
      "site": "0059b2a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:580:8"
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
      "0059b2e0",
      "DATA",
      [
        "storage",
        "00c6d580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059b2e0",
      "DATA",
      [
        "storage",
        "00c6d980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059b290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b27c.md#insn-0059b290) · [`0059b29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b27c.md#insn-0059b29c) · [`0059b2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b27c.md#insn-0059b2b8)
- 新版 `0059b2d0`（命令位置の公開資料なし） · `0059b2dc`（命令位置の公開資料なし） · `0059b2f8`（命令位置の公開資料なし）

~~~diff
- 0059b290 ["INT_ADD", "register:40f0:8", ["const:59b290:8", "const:4:8"]]
- 0059b290 ["CALL", null, ["callee:00c57e90:8"]]
+ 0059b2d0 ["INT_ADD", "register:40f0:8", ["const:59b2d0:8", "const:4:8"]]
+ 0059b2d0 ["CALL", null, ["callee:00c57e90:8"]]
- 0059b290 bytes 00f21a94
+ 0059b2d0 bytes f0f21a94
- 0059b29c ["COPY", "tmp:0:8", ["const:580:8"]]
- 0059b29c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059b29c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059b29c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059b2dc ["COPY", "tmp:0:8", ["const:980:8"]]
+ 0059b2dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059b2dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059b2dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059b29c bytes 29011691
+ 0059b2dc bytes 29012691
- 0059b2b8 ["INT_ADD", "register:40f0:8", ["const:59b2b8:8", "const:4:8"]]
- 0059b2b8 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0059b2f8 ["INT_ADD", "register:40f0:8", ["const:59b2f8:8", "const:4:8"]]
+ 0059b2f8 ["CALL", null, ["callee:00c53cd0:8"]]
- 0059b2b8 bytes 7ee11a94
+ 0059b2f8 bytes 76e21a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ea036ce16249860731a849e5c1cea5b"></a>

### [`0059b2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b2cc.md) → [`0059b30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b30c.md) FUN_0059b30c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "0059b318",
      "incomplete_value": false,
      "site": "0059b318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059b2d8",
      "incomplete_value": false,
      "site": "0059b2d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:580:8"
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
      "0059b318",
      "DATA",
      [
        "storage",
        "00c6d580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059b318",
      "DATA",
      [
        "storage",
        "00c6d980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059b2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b2cc.md#insn-0059b2d4) · [`0059b2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b2cc.md#insn-0059b2f4)
- 新版 `0059b314`（命令位置の公開資料なし） · `0059b334`（命令位置の公開資料なし）

~~~diff
- 0059b2d4 ["COPY", "tmp:0:8", ["const:580:8"]]
- 0059b2d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059b2d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059b2d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059b314 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 0059b314 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059b314 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059b314 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059b2d4 bytes 29011691
+ 0059b314 bytes 29012691
- 0059b2f4 ["INT_ADD", "register:40f0:8", ["const:59b2f4:8", "const:4:8"]]
- 0059b2f4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0059b334 ["INT_ADD", "register:40f0:8", ["const:59b334:8", "const:4:8"]]
+ 0059b334 ["CALL", null, ["callee:00c53cd0:8"]]
- 0059b2f4 bytes 6fe11a94
+ 0059b334 bytes 67e21a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-194d240117ed5a7f7de5ebe7c3d23f08"></a>

### [`0059b3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b3a0.md) → [`0059b3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b3e0.md) FUN_0059b3e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0059b94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b94c.md) [`00768e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768e50.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0059b98c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b98c.md) [`00768e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768e90.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

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
      "site": "0059b41c",
      "value": [
        "leaf",
        "ram:768e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0059b3dc",
      "value": [
        "leaf",
        "ram:768e50:8"
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
      "0059b41c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e50"
      ]
    ]
  ],
  "added": [
    [
      "0059b41c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059b3dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b3a0.md#insn-0059b3dc) · [`0059b3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b3a0.md#insn-0059b3d4) · [`0059b3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b3a0.md#insn-0059b3e8)
- 新版 `0059b41c`（命令位置の公開資料なし） · `0059b414`（命令位置の公開資料なし） · `0059b428`（命令位置の公開資料なし）

~~~diff
- 0059b3dc ["INT_ADD", "register:40f0:8", ["const:59b3dc:8", "const:4:8"]]
- 0059b3dc ["CALL", null, ["ram:768e50:8"]]
+ 0059b41c ["INT_ADD", "register:40f0:8", ["const:59b41c:8", "const:4:8"]]
+ 0059b41c ["CALL", null, ["ram:768e90:8"]]
- 0059b3dc bytes 9d360794
+ 0059b41c bytes 9d360794
- 0059b3d4 ["INT_ADD", "register:40f0:8", ["const:59b3d4:8", "const:4:8"]]
- 0059b3d4 ["CALL", null, ["callee:008514f8:8"]]
+ 0059b414 ["INT_ADD", "register:40f0:8", ["const:59b414:8", "const:4:8"]]
+ 0059b414 ["CALL", null, ["callee:008514f8:8"]]
- 0059b3d4 bytes 39d80a94
+ 0059b414 bytes 39d80a94
- 0059b3e8 ["INT_ADD", "register:40f0:8", ["const:59b3e8:8", "const:4:8"]]
- 0059b3e8 ["CALL", null, ["callee:0059b98c:8"]]
+ 0059b428 ["INT_ADD", "register:40f0:8", ["const:59b428:8", "const:4:8"]]
+ 0059b428 ["CALL", null, ["callee:0059b98c:8"]]
- 0059b3e8 bytes 59010094
+ 0059b428 bytes 59010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e096f35e6c820293b1d48d1f7755a98b"></a>

### [`0059b498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b498.md) → [`0059b4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b4d8.md) _INIT_36

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 77.18% / 新版 77.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 7件, `store_value` 6件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059b514",
      "incomplete_value": true,
      "site": "0059b530",
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
      "definition_site": "0059b4d4",
      "incomplete_value": true,
      "site": "0059b4f0",
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
      "definition_site": "0059b538",
      "incomplete_value": true,
      "site": "0059b554",
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
      "definition_site": "0059b4f8",
      "incomplete_value": true,
      "site": "0059b514",
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
      "definition_site": "0059b558",
      "incomplete_value": true,
      "site": "0059b574",
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
      "definition_site": "0059b518",
      "incomplete_value": true,
      "site": "0059b534",
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
      "0059b514",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0059b538",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0059b558",
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
      "0059b514",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0059b538",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0059b558",
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

- 旧版 [`0059b510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b498.md#insn-0059b510) · [`0059b530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b498.md#insn-0059b530) · [`0059b6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b498.md#insn-0059b6b8)
- 新版 `0059b550`（命令位置の公開資料なし） · `0059b570`（命令位置の公開資料なし） · `0059b6f8`（命令位置の公開資料なし）

~~~diff
- 0059b510 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0059b510 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059b510 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059b510 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059b550 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0059b550 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059b550 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059b550 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059b510 bytes 4a093691
+ 0059b550 bytes 4a093791
- 0059b530 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0059b530 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059b530 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059b530 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059b570 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0059b570 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059b570 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059b570 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059b530 bytes 4a553a91
+ 0059b570 bytes 4a893d91
- 0059b6b8 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 0059b6b8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0059b6b8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0059b6b8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0059b6f8 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 0059b6f8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0059b6f8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0059b6f8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0059b6b8 bytes 73422e91
+ 0059b6f8 bytes 73423e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ad66aaebf4f1a35ab90177ad0918ae8"></a>

### [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) → [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) FUN_0059b8dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 18件 [`0059c508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c508.md) [`0059d124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d124.md) [`0059e110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e110.md) [`0059e6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e6dc.md) [`0059f2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f2d0.md) · 呼出先 0件 
- 新版 呼出元 18件 [`0059c548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059c548.md) [`0059d164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d164.md) [`0059e150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059e150.md) [`0059e71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059e71c.md) [`0059f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f310.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059b8e0",
      "incomplete_value": false,
      "site": "0059b8e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059b8a0",
      "incomplete_value": false,
      "site": "0059b8a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059b8e8",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059b8e8",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059b8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md#insn-0059b8a0)
- 新版 `0059b8e0`（命令位置の公開資料なし）

~~~diff
- 0059b8a0 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059b8a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059b8a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059b8a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059b8e0 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059b8e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059b8e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059b8e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059b8a0 bytes 08011891
+ 0059b8e0 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e35000956dce981a6b68c0213b4ca58"></a>

### [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md) → [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md) FUN_0059b908

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 18件 [`0059c85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c85c.md) [`0059d314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d314.md) [`0059eb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059eb20.md) [`0059f4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f4c0.md) [`005a0628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0628.md) · 呼出先 1件 [`0059b94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b94c.md)
- 新版 呼出元 18件 [`0059c89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059c89c.md) [`0059d354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d354.md) [`0059eb60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059eb60.md) [`0059f500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f500.md) [`005a0668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0668.md) · 呼出先 1件 [`0059b98c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b98c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "0059b924",
      "incomplete_value": false,
      "site": "0059b92c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059b8e4",
      "incomplete_value": false,
      "site": "0059b8ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "0059b92c",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059b92c",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059b8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md#insn-0059b8e4) · [`0059b8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md#insn-0059b8e8) · [`0059b8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md#insn-0059b8fc)
- 新版 `0059b924`（命令位置の公開資料なし） · `0059b93c`（命令位置の公開資料なし）

~~~diff
- 0059b8e4 ["COPY", "tmp:0:8", ["const:620:8"]]
- 0059b8e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059b8e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059b8e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059b924 ["COPY", "tmp:0:8", ["const:a20:8"]]
+ 0059b924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059b924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059b924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059b8e4 bytes 08811891
+ 0059b924 bytes 08812891
- 0059b8e8 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 0059b8e8 bytes f50300aa
- 0059b8fc ["INT_ADD", "register:40f0:8", ["const:59b8fc:8", "const:4:8"]]
- 0059b8fc ["CALL", null, ["callee:0059b98c:8"]]
+ 0059b93c ["INT_ADD", "register:40f0:8", ["const:59b93c:8", "const:4:8"]]
+ 0059b93c ["CALL", null, ["callee:0059b98c:8"]]
- 0059b8fc bytes 14000094
+ 0059b93c bytes 14000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78f508508def157de5a913f40c04e08d"></a>

### [`0059b94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b94c.md) → [`0059b98c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b98c.md) FUN_0059b98c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0059b3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b3a0.md) [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md) · 呼出先 8件 [`00560414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560414.md) [`00560418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560418.md) [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 2件 [`0059b3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b3e0.md) [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md) · 呼出先 8件 [`00560454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560454.md) [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.31% / 新版 98.31%

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
      "site": "0059b9b8",
      "value": [
        "leaf",
        "ram:764ee0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0059b978",
      "value": [
        "leaf",
        "ram:764ea0:8"
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
      "0059b9b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ea0"
      ]
    ]
  ],
  "added": [
    [
      "0059b9b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059b978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b94c.md#insn-0059b978) · [`0059b9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b94c.md#insn-0059b9b8) · [`0059b970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b94c.md#insn-0059b970)
- 新版 `0059b9b8`（命令位置の公開資料なし） · `0059b9f8`（命令位置の公開資料なし） · `0059b9b0`（命令位置の公開資料なし）

~~~diff
- 0059b978 ["INT_ADD", "register:40f0:8", ["const:59b978:8", "const:4:8"]]
- 0059b978 ["CALL", null, ["ram:764ea0:8"]]
+ 0059b9b8 ["INT_ADD", "register:40f0:8", ["const:59b9b8:8", "const:4:8"]]
+ 0059b9b8 ["CALL", null, ["ram:764ee0:8"]]
- 0059b978 bytes 4a250794
+ 0059b9b8 bytes 4a250794
- 0059b9b8 ["INT_ADD", "register:40f0:8", ["const:59b9b8:8", "const:4:8"]]
- 0059b9b8 ["CALL", null, ["callee:00560458:8"]]
+ 0059b9f8 ["INT_ADD", "register:40f0:8", ["const:59b9f8:8", "const:4:8"]]
+ 0059b9f8 ["CALL", null, ["callee:00560458:8"]]
- 0059b9b8 bytes 9812ff97
+ 0059b9f8 bytes 9812ff97
- 0059b970 ["INT_ADD", "register:40f0:8", ["const:59b970:8", "const:4:8"]]
- 0059b970 ["CALL", null, ["callee:008514f8:8"]]
+ 0059b9b0 ["INT_ADD", "register:40f0:8", ["const:59b9b0:8", "const:4:8"]]
+ 0059b9b0 ["CALL", null, ["callee:008514f8:8"]]
- 0059b970 bytes d2d60a94
+ 0059b9b0 bytes d2d60a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66d0153f676f5b1abf572a44b26500a6"></a>

### [`0059baa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059baa4.md) → [`0059bae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bae4.md) FUN_0059bae4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004593b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md) [`00459a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459a90.md) [`0059bd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059bd60.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004593f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md) [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md) [`0059bda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bda0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.37% / 新版 88.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059bb1c",
      "incomplete_value": false,
      "site": "0059bb24",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059badc",
      "incomplete_value": false,
      "site": "0059bae4",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059bb3c",
      "incomplete_value": false,
      "site": "0059bb3c",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059bafc",
      "incomplete_value": false,
      "site": "0059bafc",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059bc0c",
      "incomplete_value": true,
      "site": "0059bc0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:f54:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059bbcc",
      "incomplete_value": true,
      "site": "0059bbcc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:e87:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0059bb24",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ],
    [
      "0059bb3c",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ],
    [
      "0059bb68",
      "READ",
      [
        "storage",
        "002b38ce",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0059bb24",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ],
    [
      "0059bb3c",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "0059bb68",
      "READ",
      [
        "storage",
        "002b390e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059bbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059baa4.md#insn-0059bbe4) · [`0059bad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059baa4.md#insn-0059bad4) · [`0059badc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059baa4.md#insn-0059badc)
- 新版 `0059bc24`（命令位置の公開資料なし） · `0059bb14`（命令位置の公開資料なし） · `0059bb1c`（命令位置の公開資料なし）

~~~diff
- 0059bbe4 ["INT_ADD", "register:40f0:8", ["const:59bbe4:8", "const:4:8"]]
- 0059bbe4 ["CALL", null, ["callee:00c580b0:8"]]
+ 0059bc24 ["INT_ADD", "register:40f0:8", ["const:59bc24:8", "const:4:8"]]
+ 0059bc24 ["CALL", null, ["callee:00c580b0:8"]]
- 0059bbe4 bytes 33f01a94
+ 0059bc24 bytes 23f11a94
- 0059bad4 ["INT_ADD", "register:40f0:8", ["const:59bad4:8", "const:4:8"]]
- 0059bad4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0059bb14 ["INT_ADD", "register:40f0:8", ["const:59bb14:8", "const:4:8"]]
+ 0059bb14 ["CALL", null, ["callee:00c57e90:8"]]
- 0059bad4 bytes efef1a94
+ 0059bb14 bytes dff01a94
- 0059badc ["COPY", "tmp:0:8", ["const:690:8"]]
- 0059badc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059badc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059badc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059bb1c ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 0059bb1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059bb1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059bb1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059badc bytes 08411a91
+ 0059bb1c bytes 08412a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91baae60f1f6e104d5562053102d0715"></a>

### [`0059bd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059bd60.md) → [`0059bda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bda0.md) FUN_0059bda0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0059baa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059baa4.md) · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0059bae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bae4.md) · 呼出先 7件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059be64",
      "incomplete_value": false,
      "site": "0059be68",
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
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059be24",
      "incomplete_value": false,
      "site": "0059be28",
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
            "const:360:8"
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
      "0059be68",
      "DATA",
      [
        "storage",
        "00c63360",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059be68",
      "DATA",
      [
        "storage",
        "00c63760",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059bd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059bd60.md#insn-0059bd94) · [`0059bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059bd60.md#insn-0059bda0) · [`0059bdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059bd60.md#insn-0059bdec)
- 新版 `0059bdd4`（命令位置の公開資料なし） · `0059bde0`（命令位置の公開資料なし） · `0059be2c`（命令位置の公開資料なし）

~~~diff
- 0059bd94 ["INT_ADD", "register:40f0:8", ["const:59bd94:8", "const:4:8"]]
- 0059bd94 ["CALL", null, ["callee:00c57e90:8"]]
+ 0059bdd4 ["INT_ADD", "register:40f0:8", ["const:59bdd4:8", "const:4:8"]]
+ 0059bdd4 ["CALL", null, ["callee:00c57e90:8"]]
- 0059bd94 bytes 3fef1a94
+ 0059bdd4 bytes 2ff01a94
- 0059bda0 ["INT_ADD", "register:40f0:8", ["const:59bda0:8", "const:4:8"]]
- 0059bda0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0059bde0 ["INT_ADD", "register:40f0:8", ["const:59bde0:8", "const:4:8"]]
+ 0059bde0 ["CALL", null, ["callee:00c57fe0:8"]]
- 0059bda0 bytes 90ef1a94
+ 0059bde0 bytes 80f01a94
- 0059bdec ["INT_ADD", "register:40f0:8", ["const:59bdec:8", "const:4:8"]]
- 0059bdec ["CALL", null, ["callee:00c57e90:8"]]
+ 0059be2c ["INT_ADD", "register:40f0:8", ["const:59be2c:8", "const:4:8"]]
+ 0059be2c ["CALL", null, ["callee:00c57e90:8"]]
- 0059bdec bytes 29ef1a94
+ 0059be2c bytes 19f01a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e298c12f1d9725104a3bd15873a0fae0"></a>

### [`0059c004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c004.md) → [`0059c044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059c044.md) FUN_0059c044

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059c05c",
      "incomplete_value": false,
      "site": "0059c060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059c01c",
      "incomplete_value": false,
      "site": "0059c020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "0059c060",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059c060",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059c01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c004.md#insn-0059c01c) · [`0059c02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c004.md#insn-0059c02c)
- 新版 `0059c05c`（命令位置の公開資料なし） · `0059c06c`（命令位置の公開資料なし）

~~~diff
- 0059c01c ["COPY", "tmp:0:8", ["const:620:8"]]
- 0059c01c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059c01c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059c01c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059c05c ["COPY", "tmp:0:8", ["const:a20:8"]]
+ 0059c05c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059c05c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059c05c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059c01c bytes 29811891
+ 0059c05c bytes 29812891
- 0059c02c ["INT_ADD", "register:40f0:8", ["const:59c02c:8", "const:4:8"]]
- 0059c02c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059c06c ["INT_ADD", "register:40f0:8", ["const:59c06c:8", "const:4:8"]]
+ 0059c06c ["CALL", null, ["callee:00c57eb0:8"]]
- 0059c02c bytes a1ee1a94
+ 0059c06c bytes 91ef1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0301188ab49640e328b3e278b5b7561"></a>

### [`0059c058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c058.md) → [`0059c098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059c098.md) FUN_0059c098

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059c0a0",
      "incomplete_value": false,
      "site": "0059c0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059c060",
      "incomplete_value": false,
      "site": "0059c064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059c0a4",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059c0a4",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059c060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c058.md#insn-0059c060)
- 新版 `0059c0a0`（命令位置の公開資料なし）

~~~diff
- 0059c060 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059c060 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059c060 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059c060 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059c0a0 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059c0a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059c0a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059c0a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059c060 bytes 29011891
+ 0059c0a0 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c8c2a5c95018717fdc830b91df38371"></a>

### [`0059c078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c078.md) → [`0059c0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059c0b8.md) FUN_0059c0b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059c0c0",
      "incomplete_value": false,
      "site": "0059c0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059c080",
      "incomplete_value": false,
      "site": "0059c084",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059c0c4",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059c0c4",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059c080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c078.md#insn-0059c080) · [`0059c0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c078.md#insn-0059c0a4)
- 新版 `0059c0c0`（命令位置の公開資料なし） · `0059c0e4`（命令位置の公開資料なし）

~~~diff
- 0059c080 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059c080 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059c080 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059c080 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059c0c0 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059c0c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059c0c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059c0c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059c080 bytes 29011891
+ 0059c0c0 bytes 29012891
- 0059c0a4 ["INT_ADD", "register:40f0:8", ["const:59c0a4:8", "const:4:8"]]
- 0059c0a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059c0e4 ["INT_ADD", "register:40f0:8", ["const:59c0e4:8", "const:4:8"]]
+ 0059c0e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059c0a4 bytes 83ee1a94
+ 0059c0e4 bytes 73ef1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83c00a3a7743a06fa9d8d801aafcbc28"></a>

### [`0059c0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c0b8.md) → [`0059c0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059c0f8.md) _INIT_37

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 80.44% / 新版 80.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 9件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059c138",
      "incomplete_value": true,
      "site": "0059c154",
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
      "definition_site": "0059c0f8",
      "incomplete_value": true,
      "site": "0059c114",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059c15c",
      "incomplete_value": true,
      "site": "0059c178",
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
      "definition_site": "0059c11c",
      "incomplete_value": true,
      "site": "0059c138",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059c17c",
      "incomplete_value": true,
      "site": "0059c198",
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
      "definition_site": "0059c13c",
      "incomplete_value": true,
      "site": "0059c158",
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
      "0059c138",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0059c15c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0059c17c",
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
      "0059c138",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0059c15c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0059c17c",
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

- 旧版 [`0059c134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c0b8.md#insn-0059c134) · [`0059c154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c0b8.md#insn-0059c154) · [`0059c21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c0b8.md#insn-0059c21c)
- 新版 `0059c174`（命令位置の公開資料なし） · `0059c194`（命令位置の公開資料なし） · `0059c25c`（命令位置の公開資料なし）

~~~diff
- 0059c134 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0059c134 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059c134 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059c134 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059c174 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0059c174 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059c174 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059c174 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059c134 bytes 4a093691
+ 0059c174 bytes 4a093791
- 0059c154 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0059c154 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059c154 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059c154 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059c194 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0059c194 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059c194 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059c194 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059c154 bytes 4a553a91
+ 0059c194 bytes 4a893d91
- 0059c21c ["INT_ADD", "register:40f0:8", ["const:59c21c:8", "const:4:8"]]
- 0059c21c ["CALL", null, ["callee:0043b7f8:8"]]
+ 0059c25c ["INT_ADD", "register:40f0:8", ["const:59c25c:8", "const:4:8"]]
+ 0059c25c ["CALL", null, ["callee:0043b7f8:8"]]
- 0059c21c bytes 677dfa97
+ 0059c25c bytes 677dfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-580e3a4b286245154db6d7a5d1a66f06"></a>

### [`0059c508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c508.md) → [`0059c548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059c548.md) FUN_0059c548

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.98% / 新版 95.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059c778",
      "incomplete_value": false,
      "site": "0059c784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059c738",
      "incomplete_value": false,
      "site": "0059c744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "definition_site": "0059c79c",
      "incomplete_value": false,
      "site": "0059c7a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059c75c",
      "incomplete_value": false,
      "site": "0059c764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0059c57c",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "0059c6a8",
      "READ",
      [
        "storage",
        "002a5626",
        null,
        "string"
      ]
    ],
    [
      "0059c784",
      "DATA",
      [
        "storage",
        "00c6d780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059c57c",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "0059c6a8",
      "READ",
      [
        "storage",
        "002a5702",
        null,
        "string"
      ]
    ],
    [
      "0059c784",
      "DATA",
      [
        "storage",
        "00c6db80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059c724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c508.md#insn-0059c724) · [`0059c530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c508.md#insn-0059c530) · [`0059c568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c508.md#insn-0059c568)
- 新版 `0059c764`（命令位置の公開資料なし） · `0059c570`（命令位置の公開資料なし） · `0059c5a8`（命令位置の公開資料なし）

~~~diff
- 0059c724 ["INT_ADD", "register:40f0:8", ["const:59c724:8", "const:4:8"]]
- 0059c724 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059c764 ["INT_ADD", "register:40f0:8", ["const:59c764:8", "const:4:8"]]
+ 0059c764 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059c724 bytes e3ec1a94
+ 0059c764 bytes d3ed1a94
- 0059c530 ["COPY", "tmp:0:8", ["const:165:8"]]
- 0059c530 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059c530 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059c530 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059c570 ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 0059c570 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059c570 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059c570 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059c530 bytes 4a950591
+ 0059c570 bytes 4a950691
- 0059c568 ["INT_ADD", "register:40f0:8", ["const:59c568:8", "const:4:8"]]
- 0059c568 ["CALL", null, ["callee:0044108c:8"]]
+ 0059c5a8 ["INT_ADD", "register:40f0:8", ["const:59c5a8:8", "const:4:8"]]
+ 0059c5a8 ["CALL", null, ["callee:0044108c:8"]]
- 0059c568 bytes b992fa97
+ 0059c5a8 bytes b992fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4892e1dd38b816333b2b4e9e1addc1fb"></a>

### [`0059c85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c85c.md) → [`0059c89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059c89c.md) FUN_0059c89c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b4e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4e14.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)
- 新版 呼出元 1件 [`005b4e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4e54.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)

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
      "definition_site": "0059c8c4",
      "incomplete_value": false,
      "site": "0059c8c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059c884",
      "incomplete_value": false,
      "site": "0059c888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
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
      "0059c8c8",
      "DATA",
      [
        "storage",
        "00c6d6b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059c8c8",
      "DATA",
      [
        "storage",
        "00c6dab8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059c87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c85c.md#insn-0059c87c) · [`0059c884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c85c.md#insn-0059c884)
- 新版 `0059c8bc`（命令位置の公開資料なし） · `0059c8c4`（命令位置の公開資料なし）

~~~diff
- 0059c87c ["INT_ADD", "register:40f0:8", ["const:59c87c:8", "const:4:8"]]
- 0059c87c ["CALL", null, ["callee:0059b908:8"]]
+ 0059c8bc ["INT_ADD", "register:40f0:8", ["const:59c8bc:8", "const:4:8"]]
+ 0059c8bc ["CALL", null, ["callee:0059b908:8"]]
- 0059c87c bytes 13fcff97
+ 0059c8bc bytes 13fcff97
- 0059c884 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 0059c884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059c884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059c884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059c8c4 ["COPY", "tmp:0:8", ["const:ab8:8"]]
+ 0059c8c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059c8c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059c8c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059c884 bytes 08e11a91
+ 0059c8c4 bytes 08e12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae4c42cfb13a15d93725dff38bba2950"></a>

### [`0059c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c8f8.md) → [`0059c938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059c938.md) FUN_0059c938

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`005970d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d0.md) [`0059bf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059bf04.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`00597110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597110.md) [`0059bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bf44.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0059c9f4",
      "incomplete_value": true,
      "site": "0059c9fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059c9b4",
      "incomplete_value": true,
      "site": "0059c9bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0059c9e8",
      "READ",
      [
        "storage",
        "00c9a820",
        null,
        "pointer"
      ]
    ],
    [
      "0059c9fc",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ],
    [
      "0059ca24",
      "READ",
      [
        "storage",
        "00c6d210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059c9e8",
      "READ",
      [
        "storage",
        "00c9ac20",
        null,
        "pointer"
      ]
    ],
    [
      "0059c9fc",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ],
    [
      "0059ca24",
      "READ",
      [
        "storage",
        "00c6d610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c8f8.md#insn-0059c928) · [`0059c95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c8f8.md#insn-0059c95c) · [`0059c96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c8f8.md#insn-0059c96c)
- 新版 `0059c968`（命令位置の公開資料なし） · `0059c99c`（命令位置の公開資料なし） · `0059c9ac`（命令位置の公開資料なし）

~~~diff
- 0059c928 ["INT_ADD", "register:40f0:8", ["const:59c928:8", "const:4:8"]]
- 0059c928 ["CALL", null, ["callee:0059bf44:8"]]
+ 0059c968 ["INT_ADD", "register:40f0:8", ["const:59c968:8", "const:4:8"]]
+ 0059c968 ["CALL", null, ["callee:0059bf44:8"]]
- 0059c928 bytes 77fdff97
+ 0059c968 bytes 77fdff97
- 0059c95c ["INT_ADD", "register:40f0:8", ["const:59c95c:8", "const:4:8"]]
- 0059c95c ["CALL", null, ["callee:0045179c:8"]]
+ 0059c99c ["INT_ADD", "register:40f0:8", ["const:59c99c:8", "const:4:8"]]
+ 0059c99c ["CALL", null, ["callee:0045179c:8"]]
- 0059c95c bytes 80d3fa97
+ 0059c99c bytes 80d3fa97
- 0059c96c ["INT_ADD", "register:40f0:8", ["const:59c96c:8", "const:4:8"]]
- 0059c96c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059c9ac ["INT_ADD", "register:40f0:8", ["const:59c9ac:8", "const:4:8"]]
+ 0059c9ac ["CALL", null, ["callee:00c57eb0:8"]]
- 0059c96c bytes 51ec1a94
+ 0059c9ac bytes 41ed1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0b87237564d24de868698379e9e9a17"></a>

### [`0059caf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059caf0.md) → [`0059cb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059cb30.md) FUN_0059cb30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059cb4c",
      "incomplete_value": false,
      "site": "0059cb54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059cb0c",
      "incomplete_value": false,
      "site": "0059cb14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059cb64",
      "incomplete_value": false,
      "site": "0059cb64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059cb24",
      "incomplete_value": false,
      "site": "0059cb24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      "0059cb54",
      "DATA",
      [
        "storage",
        "00c6d7d0",
        null,
        "undefined *"
      ]
    ],
    [
      "0059cb64",
      "DATA",
      [
        "storage",
        "00c6d710",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0059cb54",
      "DATA",
      [
        "storage",
        "00c6dbd0",
        null,
        "undefined *"
      ]
    ],
    [
      "0059cb64",
      "DATA",
      [
        "storage",
        "00c6db10",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059cb04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059caf0.md#insn-0059cb04) · [`0059cb0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059caf0.md#insn-0059cb0c) · [`0059cb18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059caf0.md#insn-0059cb18)
- 新版 `0059cb44`（命令位置の公開資料なし） · `0059cb4c`（命令位置の公開資料なし）

~~~diff
- 0059cb04 ["INT_ADD", "register:40f0:8", ["const:59cb04:8", "const:4:8"]]
- 0059cb04 ["CALL", null, ["callee:00c57e90:8"]]
+ 0059cb44 ["INT_ADD", "register:40f0:8", ["const:59cb44:8", "const:4:8"]]
+ 0059cb44 ["CALL", null, ["callee:00c57e90:8"]]
- 0059cb04 bytes e3eb1a94
+ 0059cb44 bytes d3ec1a94
- 0059cb0c ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 0059cb0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059cb0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059cb0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059cb4c ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 0059cb4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059cb4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059cb4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059cb0c bytes 08411f91
+ 0059cb4c bytes 08412f91
- 0059cb18 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0059cb18 bytes 883600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dff25d814aa7c50c0fd1b3adc2051f9f"></a>

### [`0059cb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cb38.md) → [`0059cb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059cb78.md) FUN_0059cb78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059cbb4",
      "incomplete_value": false,
      "site": "0059cbb8",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "0059cb74",
      "incomplete_value": false,
      "site": "0059cb78",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
      "0059cbb8",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059cbb8",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059cb54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cb38.md#insn-0059cb54) · [`0059cb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cb38.md#insn-0059cb64) · [`0059cb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cb38.md#insn-0059cb6c)
- 新版 `0059cb94`（命令位置の公開資料なし） · `0059cba4`（命令位置の公開資料なし） · `0059cbac`（命令位置の公開資料なし）

~~~diff
- 0059cb54 ["INT_ADD", "register:40f0:8", ["const:59cb54:8", "const:4:8"]]
- 0059cb54 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059cb94 ["INT_ADD", "register:40f0:8", ["const:59cb94:8", "const:4:8"]]
+ 0059cb94 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059cb54 bytes d7eb1a94
+ 0059cb94 bytes c7ec1a94
- 0059cb64 ["INT_ADD", "register:40f0:8", ["const:59cb64:8", "const:4:8"]]
- 0059cb64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059cba4 ["INT_ADD", "register:40f0:8", ["const:59cba4:8", "const:4:8"]]
+ 0059cba4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059cb64 bytes d3eb1a94
+ 0059cba4 bytes c3ec1a94
- 0059cb6c ["COPY", "tmp:0:8", ["const:610:8"]]
- 0059cb6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059cb6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059cb6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059cbac ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0059cbac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059cbac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059cbac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059cb6c bytes 08411891
+ 0059cbac bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaf8aca326749bb0553b764afeee9158"></a>

### [`0059cbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cbac.md) → [`0059cbec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059cbec.md) FUN_0059cbec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059cc28",
      "incomplete_value": false,
      "site": "0059cc2c",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "0059cbe8",
      "incomplete_value": false,
      "site": "0059cbec",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
      "0059cc2c",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059cc2c",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059cbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cbac.md#insn-0059cbc8) · [`0059cbd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cbac.md#insn-0059cbd8) · [`0059cbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cbac.md#insn-0059cbe0)
- 新版 `0059cc08`（命令位置の公開資料なし） · `0059cc18`（命令位置の公開資料なし） · `0059cc20`（命令位置の公開資料なし）

~~~diff
- 0059cbc8 ["INT_ADD", "register:40f0:8", ["const:59cbc8:8", "const:4:8"]]
- 0059cbc8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059cc08 ["INT_ADD", "register:40f0:8", ["const:59cc08:8", "const:4:8"]]
+ 0059cc08 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059cbc8 bytes baeb1a94
+ 0059cc08 bytes aaec1a94
- 0059cbd8 ["INT_ADD", "register:40f0:8", ["const:59cbd8:8", "const:4:8"]]
- 0059cbd8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059cc18 ["INT_ADD", "register:40f0:8", ["const:59cc18:8", "const:4:8"]]
+ 0059cc18 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059cbd8 bytes b6eb1a94
+ 0059cc18 bytes a6ec1a94
- 0059cbe0 ["COPY", "tmp:0:8", ["const:610:8"]]
- 0059cbe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059cbe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059cbe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059cc20 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0059cc20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059cc20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059cc20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059cbe0 bytes 08411891
+ 0059cc20 bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46d6ed2f6bd146488fba8c2561fb2b1e"></a>

### [`0059cc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cc1c.md) → [`0059cc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059cc5c.md) FUN_0059cc5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059cc84",
      "incomplete_value": false,
      "site": "0059cc88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059cc44",
      "incomplete_value": false,
      "site": "0059cc48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059cc88",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059cc88",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059cc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cc1c.md#insn-0059cc38) · [`0059cc44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cc1c.md#insn-0059cc44)
- 新版 `0059cc78`（命令位置の公開資料なし） · `0059cc84`（命令位置の公開資料なし）

~~~diff
- 0059cc38 ["INT_ADD", "register:40f0:8", ["const:59cc38:8", "const:4:8"]]
- 0059cc38 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059cc78 ["INT_ADD", "register:40f0:8", ["const:59cc78:8", "const:4:8"]]
+ 0059cc78 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059cc38 bytes 9eeb1a94
+ 0059cc78 bytes 8eec1a94
- 0059cc44 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059cc44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059cc44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059cc44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059cc84 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059cc84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059cc84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059cc84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059cc44 bytes 29011891
+ 0059cc84 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-201c98481e3f4929d1c27afc3e0665fe"></a>

### [`0059cc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cc6c.md) → [`0059ccac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059ccac.md) FUN_0059ccac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059ccd4",
      "incomplete_value": false,
      "site": "0059ccd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059cc94",
      "incomplete_value": false,
      "site": "0059cc98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059ccd8",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059ccd8",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059cc88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cc6c.md#insn-0059cc88) · [`0059cc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cc6c.md#insn-0059cc94) · [`0059cca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cc6c.md#insn-0059cca4)
- 新版 `0059ccc8`（命令位置の公開資料なし） · `0059ccd4`（命令位置の公開資料なし） · `0059cce4`（命令位置の公開資料なし）

~~~diff
- 0059cc88 ["INT_ADD", "register:40f0:8", ["const:59cc88:8", "const:4:8"]]
- 0059cc88 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059ccc8 ["INT_ADD", "register:40f0:8", ["const:59ccc8:8", "const:4:8"]]
+ 0059ccc8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059cc88 bytes 8aeb1a94
+ 0059ccc8 bytes 7aec1a94
- 0059cc94 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059cc94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059cc94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059cc94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059ccd4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059ccd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059ccd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059ccd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059cc94 bytes 29011891
+ 0059ccd4 bytes 29012891
- 0059cca4 ["INT_ADD", "register:40f0:8", ["const:59cca4:8", "const:4:8"]]
- 0059cca4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059cce4 ["INT_ADD", "register:40f0:8", ["const:59cce4:8", "const:4:8"]]
+ 0059cce4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059cca4 bytes 83eb1a94
+ 0059cce4 bytes 73ec1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4ecead92921dd90125ea284e339ee46"></a>

### [`0059ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059ccb8.md) → [`0059ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059ccf8.md) FUN_0059ccf8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0059ccfc",
      "incomplete_value": false,
      "site": "0059cd00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ccbc",
      "incomplete_value": false,
      "site": "0059ccc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "0059cd00",
      "DATA",
      [
        "storage",
        "00c6d780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059cd00",
      "DATA",
      [
        "storage",
        "00c6db80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ccbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059ccb8.md#insn-0059ccbc)
- 新版 `0059ccfc`（命令位置の公開資料なし）

~~~diff
- 0059ccbc ["COPY", "tmp:0:8", ["const:780:8"]]
- 0059ccbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059ccbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059ccbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059ccfc ["COPY", "tmp:0:8", ["const:b80:8"]]
+ 0059ccfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ccfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ccfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059ccbc bytes 08011e91
+ 0059ccfc bytes 08012e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d88e1c1f9121ec9056f99d0c98a03db"></a>

### [`0059ccc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059ccc8.md) → [`0059cd08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059cd08.md) FUN_0059cd08

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059cd18",
      "incomplete_value": false,
      "site": "0059cd20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ccd8",
      "incomplete_value": false,
      "site": "0059cce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "0059cd20",
      "DATA",
      [
        "storage",
        "00c6d780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059cd20",
      "DATA",
      [
        "storage",
        "00c6db80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ccd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059ccc8.md#insn-0059ccd8) · [`0059cce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059ccc8.md#insn-0059cce4)
- 新版 `0059cd18`（命令位置の公開資料なし） · `0059cd24`（命令位置の公開資料なし）

~~~diff
- 0059ccd8 ["COPY", "tmp:0:8", ["const:780:8"]]
- 0059ccd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059ccd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059ccd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059cd18 ["COPY", "tmp:0:8", ["const:b80:8"]]
+ 0059cd18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059cd18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059cd18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059ccd8 bytes 08011e91
+ 0059cd18 bytes 08012e91
- 0059cce4 ["INT_ADD", "register:40f0:8", ["const:59cce4:8", "const:4:8"]]
- 0059cce4 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0059cd24 ["INT_ADD", "register:40f0:8", ["const:59cd24:8", "const:4:8"]]
+ 0059cd24 ["CALL", null, ["callee:00c57ea0:8"]]
- 0059cce4 bytes 6feb1a94
+ 0059cd24 bytes 5fec1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8581b6ab86304939a67a99d3e2dd225"></a>

### [`0059ccf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059ccf8.md) → [`0059cd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059cd38.md) FUN_0059cd38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059cd60",
      "incomplete_value": false,
      "site": "0059cd64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059cd20",
      "incomplete_value": false,
      "site": "0059cd24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059cd64",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059cd64",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059cd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059ccf8.md#insn-0059cd14) · [`0059cd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059ccf8.md#insn-0059cd20)
- 新版 `0059cd54`（命令位置の公開資料なし） · `0059cd60`（命令位置の公開資料なし）

~~~diff
- 0059cd14 ["INT_ADD", "register:40f0:8", ["const:59cd14:8", "const:4:8"]]
- 0059cd14 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059cd54 ["INT_ADD", "register:40f0:8", ["const:59cd54:8", "const:4:8"]]
+ 0059cd54 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059cd14 bytes 67eb1a94
+ 0059cd54 bytes 57ec1a94
- 0059cd20 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059cd20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059cd20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059cd20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059cd60 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059cd60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059cd60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059cd60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059cd20 bytes 29011891
+ 0059cd60 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-313d2ec0612bf148b8d79c970c935fe8"></a>

### [`0059cd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cd4c.md) → [`0059cd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059cd8c.md) FUN_0059cd8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0059cd90",
      "incomplete_value": false,
      "site": "0059cd94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059cd50",
      "incomplete_value": false,
      "site": "0059cd54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
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
      "0059cd94",
      "DATA",
      [
        "storage",
        "00c6d7d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059cd94",
      "DATA",
      [
        "storage",
        "00c6dbd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059cd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cd4c.md#insn-0059cd50)
- 新版 `0059cd90`（命令位置の公開資料なし）

~~~diff
- 0059cd50 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 0059cd50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059cd50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059cd50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059cd90 ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 0059cd90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059cd90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059cd90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059cd50 bytes 08411f91
+ 0059cd90 bytes 08412f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29a1e3fb7cde9e17528bc0b7f279c6ab"></a>

### [`0059cd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cd5c.md) → [`0059cd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059cd9c.md) FUN_0059cd9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059cdac",
      "incomplete_value": false,
      "site": "0059cdb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059cd6c",
      "incomplete_value": false,
      "site": "0059cd74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
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
      "0059cdb4",
      "DATA",
      [
        "storage",
        "00c6d7d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059cdb4",
      "DATA",
      [
        "storage",
        "00c6dbd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059cd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cd5c.md#insn-0059cd6c) · [`0059cd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cd5c.md#insn-0059cd78)
- 新版 `0059cdac`（命令位置の公開資料なし） · `0059cdb8`（命令位置の公開資料なし）

~~~diff
- 0059cd6c ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 0059cd6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059cd6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059cd6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059cdac ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 0059cdac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059cdac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059cdac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059cd6c bytes 08411f91
+ 0059cdac bytes 08412f91
- 0059cd78 ["INT_ADD", "register:40f0:8", ["const:59cd78:8", "const:4:8"]]
- 0059cd78 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0059cdb8 ["INT_ADD", "register:40f0:8", ["const:59cdb8:8", "const:4:8"]]
+ 0059cdb8 ["CALL", null, ["callee:00c57ea0:8"]]
- 0059cd78 bytes 4aeb1a94
+ 0059cdb8 bytes 3aec1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-292b3ba497cd9fb9ffbaa9bcaf4c3d22"></a>

### [`0059cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cd94.md) → [`0059cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059c/0059cdd4.md) _INIT_38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059ce10",
      "incomplete_value": true,
      "site": "0059ce2c",
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
      "definition_site": "0059cdd0",
      "incomplete_value": true,
      "site": "0059cdec",
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
      "definition_site": "0059ce34",
      "incomplete_value": true,
      "site": "0059ce50",
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
      "definition_site": "0059cdf4",
      "incomplete_value": true,
      "site": "0059ce10",
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
      "definition_site": "0059ce54",
      "incomplete_value": true,
      "site": "0059ce70",
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
      "definition_site": "0059ce14",
      "incomplete_value": true,
      "site": "0059ce30",
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
      "0059ce10",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0059ce34",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0059ce54",
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
      "0059ce10",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0059ce34",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0059ce54",
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

- 旧版 [`0059ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cd94.md#insn-0059ce0c) · [`0059ce2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cd94.md#insn-0059ce2c) · [`0059cef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059cd94.md#insn-0059cef4)
- 新版 `0059ce4c`（命令位置の公開資料なし） · `0059ce6c`（命令位置の公開資料なし） · `0059cf34`（命令位置の公開資料なし）

~~~diff
- 0059ce0c ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0059ce0c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059ce0c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059ce0c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059ce4c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0059ce4c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059ce4c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059ce4c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059ce0c bytes 4a093691
+ 0059ce4c bytes 4a093791
- 0059ce2c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0059ce2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059ce2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059ce2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059ce6c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0059ce6c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059ce6c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059ce6c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059ce2c bytes 4a553a91
+ 0059ce6c bytes 4a893d91
- 0059cef4 ["INT_ADD", "register:40f0:8", ["const:59cef4:8", "const:4:8"]]
- 0059cef4 ["CALL", null, ["callee:0043b7f8:8"]]
+ 0059cf34 ["INT_ADD", "register:40f0:8", ["const:59cf34:8", "const:4:8"]]
+ 0059cf34 ["CALL", null, ["callee:0043b7f8:8"]]
- 0059cef4 bytes 317afa97
+ 0059cf34 bytes 317afa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cec2afa9f7cf834660c3a3f92c0ef37"></a>

### [`0059d124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d124.md) → [`0059d164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d164.md) FUN_0059d164

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059d1b0",
      "incomplete_value": true,
      "site": "0059d1b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059d170",
      "incomplete_value": true,
      "site": "0059d170",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059d260",
      "incomplete_value": false,
      "site": "0059d26c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059d220",
      "incomplete_value": false,
      "site": "0059d22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "definition_site": "0059d284",
      "incomplete_value": false,
      "site": "0059d28c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059d244",
      "incomplete_value": false,
      "site": "0059d24c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:820:8"
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
      "0059d194",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "0059d26c",
      "DATA",
      [
        "storage",
        "00c6d8f8",
        null,
        "undefined *"
      ]
    ],
    [
      "0059d28c",
      "DATA",
      [
        "storage",
        "00c6d820",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059d194",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "0059d26c",
      "DATA",
      [
        "storage",
        "00c6dcf8",
        null,
        "undefined *"
      ]
    ],
    [
      "0059d28c",
      "DATA",
      [
        "storage",
        "00c6dc20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059d1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d124.md#insn-0059d1b0) · [`0059d20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d124.md#insn-0059d20c) · [`0059d148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d124.md#insn-0059d148)
- 新版 `0059d1f0`（命令位置の公開資料なし） · `0059d24c`（命令位置の公開資料なし） · `0059d188`（命令位置の公開資料なし）

~~~diff
- 0059d1b0 ["INT_ADD", "register:40f0:8", ["const:59d1b0:8", "const:4:8"]]
- 0059d1b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059d1f0 ["INT_ADD", "register:40f0:8", ["const:59d1f0:8", "const:4:8"]]
+ 0059d1f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059d1b0 bytes 40ea1a94
+ 0059d1f0 bytes 30eb1a94
- 0059d20c ["INT_ADD", "register:40f0:8", ["const:59d20c:8", "const:4:8"]]
- 0059d20c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059d24c ["INT_ADD", "register:40f0:8", ["const:59d24c:8", "const:4:8"]]
+ 0059d24c ["CALL", null, ["callee:00c57eb0:8"]]
- 0059d20c bytes 29ea1a94
+ 0059d24c bytes 19eb1a94
- 0059d148 ["COPY", "tmp:0:8", ["const:165:8"]]
- 0059d148 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059d148 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059d148 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059d188 ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 0059d188 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059d188 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059d188 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059d148 bytes 4a950591
+ 0059d188 bytes 4a950691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f3232675e11a5cb911ee8e5af4143b3"></a>

### [`0059d314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d314.md) → [`0059d354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d354.md) FUN_0059d354

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b35b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b35b8.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)
- 新版 呼出元 1件 [`005b35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059d370",
      "incomplete_value": false,
      "site": "0059d374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059d330",
      "incomplete_value": false,
      "site": "0059d334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "0059d374",
      "DATA",
      [
        "storage",
        "00c6d840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059d374",
      "DATA",
      [
        "storage",
        "00c6dc40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059d328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d314.md#insn-0059d328) · [`0059d330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d314.md#insn-0059d330)
- 新版 `0059d368`（命令位置の公開資料なし） · `0059d370`（命令位置の公開資料なし）

~~~diff
- 0059d328 ["INT_ADD", "register:40f0:8", ["const:59d328:8", "const:4:8"]]
- 0059d328 ["CALL", null, ["callee:0059b908:8"]]
+ 0059d368 ["INT_ADD", "register:40f0:8", ["const:59d368:8", "const:4:8"]]
+ 0059d368 ["CALL", null, ["callee:0059b908:8"]]
- 0059d328 bytes 68f9ff97
+ 0059d368 bytes 68f9ff97
- 0059d330 ["COPY", "tmp:0:8", ["const:840:8"]]
- 0059d330 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059d330 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059d330 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059d370 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 0059d370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059d330 bytes 08012191
+ 0059d370 bytes 08013191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a3a2b43aedac1fe15000d0a82fa4e24"></a>

### [`0059d480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d480.md) → [`0059d4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d4c0.md) FUN_0059d4c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059d4dc",
      "incomplete_value": false,
      "site": "0059d4e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059d49c",
      "incomplete_value": false,
      "site": "0059d4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059d4f4",
      "incomplete_value": false,
      "site": "0059d4f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059d4b4",
      "incomplete_value": false,
      "site": "0059d4b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "0059d4e4",
      "DATA",
      [
        "storage",
        "00c6d948",
        null,
        "undefined *"
      ]
    ],
    [
      "0059d4f4",
      "DATA",
      [
        "storage",
        "00c6d898",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0059d4e4",
      "DATA",
      [
        "storage",
        "00c6dd48",
        null,
        "undefined *"
      ]
    ],
    [
      "0059d4f4",
      "DATA",
      [
        "storage",
        "00c6dc98",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059d494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d480.md#insn-0059d494) · [`0059d49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d480.md#insn-0059d49c) · [`0059d4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d480.md#insn-0059d4a8)
- 新版 `0059d4d4`（命令位置の公開資料なし） · `0059d4dc`（命令位置の公開資料なし）

~~~diff
- 0059d494 ["INT_ADD", "register:40f0:8", ["const:59d494:8", "const:4:8"]]
- 0059d494 ["CALL", null, ["callee:00c57e90:8"]]
+ 0059d4d4 ["INT_ADD", "register:40f0:8", ["const:59d4d4:8", "const:4:8"]]
+ 0059d4d4 ["CALL", null, ["callee:00c57e90:8"]]
- 0059d494 bytes 7fe91a94
+ 0059d4d4 bytes 6fea1a94
- 0059d49c ["COPY", "tmp:0:8", ["const:948:8"]]
- 0059d49c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059d49c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059d49c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059d4dc ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 0059d4dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d4dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d4dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059d49c bytes 08212591
+ 0059d4dc bytes 08213591
- 0059d4a8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0059d4a8 bytes 88360090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bf3186fea86ce2a3b889ac668ae1072"></a>

### [`0059d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d4c8.md) → [`0059d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d508.md) FUN_0059d508

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "0059d534",
      "incomplete_value": false,
      "site": "0059d538",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "0059d4f4",
      "incomplete_value": false,
      "site": "0059d4f8",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
      "0059d538",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059d538",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059d4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d4c8.md#insn-0059d4e4) · [`0059d4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d4c8.md#insn-0059d4ec) · [`0059d504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d4c8.md#insn-0059d504)
- 新版 `0059d524`（命令位置の公開資料なし） · `0059d52c`（命令位置の公開資料なし） · `0059d544`（命令位置の公開資料なし）

~~~diff
- 0059d4e4 ["INT_ADD", "register:40f0:8", ["const:59d4e4:8", "const:4:8"]]
- 0059d4e4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059d524 ["INT_ADD", "register:40f0:8", ["const:59d524:8", "const:4:8"]]
+ 0059d524 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059d4e4 bytes 73e91a94
+ 0059d524 bytes 63ea1a94
- 0059d4ec ["COPY", "tmp:0:8", ["const:610:8"]]
- 0059d4ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059d4ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059d4ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059d52c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0059d52c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d52c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d52c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059d4ec bytes 08411891
+ 0059d52c bytes 08412891
- 0059d504 ["INT_ADD", "register:40f0:8", ["const:59d504:8", "const:4:8"]]
- 0059d504 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059d544 ["INT_ADD", "register:40f0:8", ["const:59d544:8", "const:4:8"]]
+ 0059d544 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059d504 bytes 6be91a94
+ 0059d544 bytes 5bea1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d8255eb1ba903a0975f1ef011a9a177"></a>

### [`0059d52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d52c.md) → [`0059d56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d56c.md) FUN_0059d56c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059d598",
      "incomplete_value": false,
      "site": "0059d59c",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "0059d558",
      "incomplete_value": false,
      "site": "0059d55c",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
      "0059d59c",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059d59c",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059d548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d52c.md#insn-0059d548) · [`0059d550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d52c.md#insn-0059d550) · [`0059d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d52c.md#insn-0059d568)
- 新版 `0059d588`（命令位置の公開資料なし） · `0059d590`（命令位置の公開資料なし） · `0059d5a8`（命令位置の公開資料なし）

~~~diff
- 0059d548 ["INT_ADD", "register:40f0:8", ["const:59d548:8", "const:4:8"]]
- 0059d548 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059d588 ["INT_ADD", "register:40f0:8", ["const:59d588:8", "const:4:8"]]
+ 0059d588 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059d548 bytes 5ae91a94
+ 0059d588 bytes 4aea1a94
- 0059d550 ["COPY", "tmp:0:8", ["const:610:8"]]
- 0059d550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059d550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059d550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059d590 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0059d590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059d550 bytes 08411891
+ 0059d590 bytes 08412891
- 0059d568 ["INT_ADD", "register:40f0:8", ["const:59d568:8", "const:4:8"]]
- 0059d568 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059d5a8 ["INT_ADD", "register:40f0:8", ["const:59d5a8:8", "const:4:8"]]
+ 0059d5a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059d568 bytes 52e91a94
+ 0059d5a8 bytes 42ea1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9b3d2ad2d578065d1b8fe444410f715"></a>

### [`0059d58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d58c.md) → [`0059d5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d5cc.md) FUN_0059d5cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059d5d4",
      "incomplete_value": false,
      "site": "0059d5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059d594",
      "incomplete_value": false,
      "site": "0059d598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059d5d8",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059d5d8",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059d594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d58c.md#insn-0059d594) · [`0059d5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d58c.md#insn-0059d5b8)
- 新版 `0059d5d4`（命令位置の公開資料なし） · `0059d5f8`（命令位置の公開資料なし）

~~~diff
- 0059d594 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059d594 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059d594 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059d594 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059d5d4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059d5d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059d5d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059d5d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059d594 bytes 29011891
+ 0059d5d4 bytes 29012891
- 0059d5b8 ["INT_ADD", "register:40f0:8", ["const:59d5b8:8", "const:4:8"]]
- 0059d5b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059d5f8 ["INT_ADD", "register:40f0:8", ["const:59d5f8:8", "const:4:8"]]
+ 0059d5f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059d5b8 bytes 3ee91a94
+ 0059d5f8 bytes 2eea1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30dd7d7ac929b540a2211e8fe6102aeb"></a>

### [`0059d5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d5cc.md) → [`0059d60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d60c.md) FUN_0059d60c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0059d610",
      "incomplete_value": false,
      "site": "0059d614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059d5d0",
      "incomplete_value": false,
      "site": "0059d5d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "0059d614",
      "DATA",
      [
        "storage",
        "00c6d8f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059d614",
      "DATA",
      [
        "storage",
        "00c6dcf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059d5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d5cc.md#insn-0059d5d0)
- 新版 `0059d610`（命令位置の公開資料なし）

~~~diff
- 0059d5d0 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 0059d5d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059d5d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059d5d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059d610 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 0059d610 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d610 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d610 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059d5d0 bytes 08e12391
+ 0059d610 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-accf91704f1248b0c4e6dbd69b14cc3d"></a>

### [`0059d5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d5dc.md) → [`0059d61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d61c.md) FUN_0059d61c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059d62c",
      "incomplete_value": false,
      "site": "0059d634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059d5ec",
      "incomplete_value": false,
      "site": "0059d5f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "0059d634",
      "DATA",
      [
        "storage",
        "00c6d8f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059d634",
      "DATA",
      [
        "storage",
        "00c6dcf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059d5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d5dc.md#insn-0059d5ec) · [`0059d5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d5dc.md#insn-0059d5f8)
- 新版 `0059d62c`（命令位置の公開資料なし） · `0059d638`（命令位置の公開資料なし）

~~~diff
- 0059d5ec ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 0059d5ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059d5ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059d5ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059d62c ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 0059d62c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d62c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d62c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059d5ec bytes 08e12391
+ 0059d62c bytes 08e13391
- 0059d5f8 ["INT_ADD", "register:40f0:8", ["const:59d5f8:8", "const:4:8"]]
- 0059d5f8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0059d638 ["INT_ADD", "register:40f0:8", ["const:59d638:8", "const:4:8"]]
+ 0059d638 ["CALL", null, ["callee:00c57ea0:8"]]
- 0059d5f8 bytes 2ae91a94
+ 0059d638 bytes 1aea1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85d8a5075fafac17b598eb3435fb4fe6"></a>

### [`0059d60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d60c.md) → [`0059d64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d64c.md) FUN_0059d64c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059d654",
      "incomplete_value": false,
      "site": "0059d658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059d614",
      "incomplete_value": false,
      "site": "0059d618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059d658",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059d658",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059d614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d60c.md#insn-0059d614)
- 新版 `0059d654`（命令位置の公開資料なし）

~~~diff
- 0059d614 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059d614 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059d614 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059d614 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059d654 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059d654 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059d654 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059d654 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059d614 bytes 29011891
+ 0059d654 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff64e50fdd06edd5c33ffefd02889dcf"></a>

### [`0059d630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d630.md) → [`0059d670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d670.md) FUN_0059d670

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0059d674",
      "incomplete_value": false,
      "site": "0059d678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059d634",
      "incomplete_value": false,
      "site": "0059d638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "0059d678",
      "DATA",
      [
        "storage",
        "00c6d948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059d678",
      "DATA",
      [
        "storage",
        "00c6dd48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059d634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d630.md#insn-0059d634)
- 新版 `0059d674`（命令位置の公開資料なし）

~~~diff
- 0059d634 ["COPY", "tmp:0:8", ["const:948:8"]]
- 0059d634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059d634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059d634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059d674 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 0059d674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059d634 bytes 08212591
+ 0059d674 bytes 08213591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dddf8d0edb4a1ca9b059f701ead4ea8"></a>

### [`0059d640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d640.md) → [`0059d680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d680.md) FUN_0059d680

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059d690",
      "incomplete_value": false,
      "site": "0059d698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059d650",
      "incomplete_value": false,
      "site": "0059d658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "0059d698",
      "DATA",
      [
        "storage",
        "00c6d948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059d698",
      "DATA",
      [
        "storage",
        "00c6dd48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059d650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d640.md#insn-0059d650) · [`0059d65c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d640.md#insn-0059d65c)
- 新版 `0059d690`（命令位置の公開資料なし） · `0059d69c`（命令位置の公開資料なし）

~~~diff
- 0059d650 ["COPY", "tmp:0:8", ["const:948:8"]]
- 0059d650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059d650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059d650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059d690 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 0059d690 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d690 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059d690 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059d650 bytes 08212591
+ 0059d690 bytes 08213591
- 0059d65c ["INT_ADD", "register:40f0:8", ["const:59d65c:8", "const:4:8"]]
- 0059d65c ["CALL", null, ["callee:00c57ea0:8"]]
+ 0059d69c ["INT_ADD", "register:40f0:8", ["const:59d69c:8", "const:4:8"]]
+ 0059d69c ["CALL", null, ["callee:00c57ea0:8"]]
- 0059d65c bytes 11e91a94
+ 0059d69c bytes 01ea1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28ade6b37bc2f06db2551fb026256192"></a>

### [`0059d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d678.md) → [`0059d6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d6b8.md) _INIT_39

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059d6f4",
      "incomplete_value": true,
      "site": "0059d710",
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
      "definition_site": "0059d6b4",
      "incomplete_value": true,
      "site": "0059d6d0",
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
      "definition_site": "0059d718",
      "incomplete_value": true,
      "site": "0059d734",
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
      "definition_site": "0059d6d8",
      "incomplete_value": true,
      "site": "0059d6f4",
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
      "definition_site": "0059d738",
      "incomplete_value": true,
      "site": "0059d754",
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
      "definition_site": "0059d6f8",
      "incomplete_value": true,
      "site": "0059d714",
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
      "0059d6f4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0059d718",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0059d738",
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
      "0059d6f4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0059d718",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0059d738",
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

- 旧版 [`0059d6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d678.md#insn-0059d6f0) · [`0059d710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d678.md#insn-0059d710) · [`0059d7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d678.md#insn-0059d7d8)
- 新版 `0059d730`（命令位置の公開資料なし） · `0059d750`（命令位置の公開資料なし） · `0059d818`（命令位置の公開資料なし）

~~~diff
- 0059d6f0 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0059d6f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059d6f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059d6f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059d730 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0059d730 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059d730 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059d730 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059d6f0 bytes 4a093691
+ 0059d730 bytes 4a093791
- 0059d710 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0059d710 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059d710 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059d710 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059d750 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0059d750 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059d750 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059d750 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059d710 bytes 4a553a91
+ 0059d750 bytes 4a893d91
- 0059d7d8 ["INT_ADD", "register:40f0:8", ["const:59d7d8:8", "const:4:8"]]
- 0059d7d8 ["CALL", null, ["callee:0043b7f8:8"]]
+ 0059d818 ["INT_ADD", "register:40f0:8", ["const:59d818:8", "const:4:8"]]
+ 0059d818 ["CALL", null, ["callee:0043b7f8:8"]]
- 0059d7d8 bytes f877fa97
+ 0059d818 bytes f877fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e731861be142f5a24b5e1c850ac2491"></a>

### [`0059da30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059da30.md) → [`0059da70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059da70.md) FUN_0059da70

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0059e110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e110.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0059e150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059e150.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.88% / 新版 98.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059dac8",
      "incomplete_value": true,
      "site": "0059dac8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059da88",
      "incomplete_value": true,
      "site": "0059da88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0059daac",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0059daac",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059dac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059da30.md#insn-0059dac8) · [`0059da5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059da30.md#insn-0059da5c) · [`0059da98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059da30.md#insn-0059da98)
- 新版 `0059db08`（命令位置の公開資料なし） · `0059da9c`（命令位置の公開資料なし） · `0059dad8`（命令位置の公開資料なし）

~~~diff
- 0059dac8 ["INT_ADD", "register:40f0:8", ["const:59dac8:8", "const:4:8"]]
- 0059dac8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059db08 ["INT_ADD", "register:40f0:8", ["const:59db08:8", "const:4:8"]]
+ 0059db08 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059dac8 bytes fae71a94
+ 0059db08 bytes eae81a94
- 0059da5c ["COPY", "tmp:0:8", ["const:165:8"]]
- 0059da5c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059da5c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059da5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059da9c ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 0059da9c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059da9c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059da9c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059da5c bytes 4a950591
+ 0059da9c bytes 4a950691
- 0059da98 ["INT_ADD", "register:40f0:8", ["const:59da98:8", "const:4:8"]]
- 0059da98 ["CALL", null, ["callee:0044108c:8"]]
+ 0059dad8 ["INT_ADD", "register:40f0:8", ["const:59dad8:8", "const:4:8"]]
+ 0059dad8 ["CALL", null, ["callee:0044108c:8"]]
- 0059da98 bytes 6d8dfa97
+ 0059dad8 bytes 6d8dfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b78ca03c9e6ba649546a6553724b04b"></a>

### [`0059df50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059df50.md) → [`0059df90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059df90.md) FUN_0059df90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059dfac",
      "incomplete_value": false,
      "site": "0059dfb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059df6c",
      "incomplete_value": false,
      "site": "0059df74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059dfc4",
      "incomplete_value": false,
      "site": "0059dfc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059df84",
      "incomplete_value": false,
      "site": "0059df84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "0059dfb4",
      "DATA",
      [
        "storage",
        "00c6dac0",
        null,
        "undefined *"
      ]
    ],
    [
      "0059dfc4",
      "DATA",
      [
        "storage",
        "00c6d9b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0059dfb4",
      "DATA",
      [
        "storage",
        "00c6dec0",
        null,
        "undefined *"
      ]
    ],
    [
      "0059dfc4",
      "DATA",
      [
        "storage",
        "00c6ddb8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059df64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059df50.md#insn-0059df64) · [`0059df6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059df50.md#insn-0059df6c) · [`0059df78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059df50.md#insn-0059df78)
- 新版 `0059dfa4`（命令位置の公開資料なし） · `0059dfac`（命令位置の公開資料なし）

~~~diff
- 0059df64 ["INT_ADD", "register:40f0:8", ["const:59df64:8", "const:4:8"]]
- 0059df64 ["CALL", null, ["callee:00c57e90:8"]]
+ 0059dfa4 ["INT_ADD", "register:40f0:8", ["const:59dfa4:8", "const:4:8"]]
+ 0059dfa4 ["CALL", null, ["callee:00c57e90:8"]]
- 0059df64 bytes cbe61a94
+ 0059dfa4 bytes bbe71a94
- 0059df6c ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 0059df6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059df6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059df6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059dfac ["COPY", "tmp:0:8", ["const:ec0:8"]]
+ 0059dfac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059dfac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059dfac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059df6c bytes 08012b91
+ 0059dfac bytes 08013b91
- 0059df78 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0059df78 bytes 88360090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e58b0e38f86d9cf32c97048d1e80c7e"></a>

### [`0059df98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059df98.md) → [`0059dfd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059dfd8.md) FUN_0059dfd8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059dff4",
      "incomplete_value": true,
      "site": "0059dff8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059dfb4",
      "incomplete_value": true,
      "site": "0059dfb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0059dfec",
      "READ",
      [
        "storage",
        "00c9af20",
        null,
        "pointer"
      ]
    ],
    [
      "0059dff8",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059dfec",
      "READ",
      [
        "storage",
        "00c9b320",
        null,
        "pointer"
      ]
    ],
    [
      "0059dff8",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059dfa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059df98.md#insn-0059dfa4) · [`0059dfac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059df98.md#insn-0059dfac) · [`0059dfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059df98.md#insn-0059dfc4)
- 新版 `0059dfe4`（命令位置の公開資料なし） · `0059dfec`（命令位置の公開資料なし） · `0059e004`（命令位置の公開資料なし）

~~~diff
- 0059dfa4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0059dfe4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0059dfa4 bytes e83700b0
+ 0059dfe4 bytes e83700d0
- 0059dfac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
- 0059dfac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0059dfec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:320:8"]]
+ 0059dfec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0059dfac bytes 089147f9
+ 0059dfec bytes 089141f9
- 0059dfc4 ["INT_ADD", "register:40f0:8", ["const:59dfc4:8", "const:4:8"]]
- 0059dfc4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059e004 ["INT_ADD", "register:40f0:8", ["const:59e004:8", "const:4:8"]]
+ 0059e004 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059dfc4 bytes bbe61a94
+ 0059e004 bytes abe71a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-702ed19a967e5e6b728c723bc30e4c35"></a>

### [`0059dfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059dfe8.md) → [`0059e028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059e028.md) FUN_0059e028

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059e090",
      "incomplete_value": false,
      "site": "0059e094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059e050",
      "incomplete_value": false,
      "site": "0059e054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059e094",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059e094",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059e034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059dfe8.md#insn-0059e034) · [`0059e044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059dfe8.md#insn-0059e044) · [`0059e050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059dfe8.md#insn-0059e050)
- 新版 `0059e074`（命令位置の公開資料なし） · `0059e084`（命令位置の公開資料なし） · `0059e090`（命令位置の公開資料なし）

~~~diff
- 0059e034 ["INT_ADD", "register:40f0:8", ["const:59e034:8", "const:4:8"]]
- 0059e034 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059e074 ["INT_ADD", "register:40f0:8", ["const:59e074:8", "const:4:8"]]
+ 0059e074 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059e034 bytes 9fe61a94
+ 0059e074 bytes 8fe71a94
- 0059e044 ["INT_ADD", "register:40f0:8", ["const:59e044:8", "const:4:8"]]
- 0059e044 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059e084 ["INT_ADD", "register:40f0:8", ["const:59e084:8", "const:4:8"]]
+ 0059e084 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059e044 bytes 9be61a94
+ 0059e084 bytes 8be71a94
- 0059e050 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059e050 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059e050 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059e050 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059e090 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059e090 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059e090 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059e090 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059e050 bytes 29011891
+ 0059e090 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af9ef96d2a1bbc0f455dbcf889de289f"></a>

### [`0059e080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e080.md) → [`0059e0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059e0c0.md) FUN_0059e0c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059e128",
      "incomplete_value": false,
      "site": "0059e12c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059e0e8",
      "incomplete_value": false,
      "site": "0059e0ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059e12c",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059e12c",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059e0cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e080.md#insn-0059e0cc) · [`0059e0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e080.md#insn-0059e0dc) · [`0059e0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e080.md#insn-0059e0e8)
- 新版 `0059e10c`（命令位置の公開資料なし） · `0059e11c`（命令位置の公開資料なし） · `0059e128`（命令位置の公開資料なし）

~~~diff
- 0059e0cc ["INT_ADD", "register:40f0:8", ["const:59e0cc:8", "const:4:8"]]
- 0059e0cc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059e10c ["INT_ADD", "register:40f0:8", ["const:59e10c:8", "const:4:8"]]
+ 0059e10c ["CALL", null, ["callee:00c57eb0:8"]]
- 0059e0cc bytes 79e61a94
+ 0059e10c bytes 69e71a94
- 0059e0dc ["INT_ADD", "register:40f0:8", ["const:59e0dc:8", "const:4:8"]]
- 0059e0dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059e11c ["INT_ADD", "register:40f0:8", ["const:59e11c:8", "const:4:8"]]
+ 0059e11c ["CALL", null, ["callee:00c57eb0:8"]]
- 0059e0dc bytes 75e61a94
+ 0059e11c bytes 65e71a94
- 0059e0e8 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059e0e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059e0e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059e0e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059e128 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059e128 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059e128 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059e128 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059e0e8 bytes 29011891
+ 0059e128 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b788a526c859a4f9ac8ae8874bdaeef9"></a>

### [`0059e110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e110.md) → [`0059e150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059e150.md) FUN_0059e150

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0059da30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059da30.md) · 呼出先 4件 [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0059da70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059da70.md) · 呼出先 4件 [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059e1bc",
      "incomplete_value": false,
      "site": "0059e1c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059e17c",
      "incomplete_value": false,
      "site": "0059e180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059e1e4",
      "incomplete_value": false,
      "site": "0059e1ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059e1a4",
      "incomplete_value": false,
      "site": "0059e1ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "0059e1c0",
      "DATA",
      [
        "storage",
        "00c6da70",
        null,
        "undefined *"
      ]
    ],
    [
      "0059e1ec",
      "DATA",
      [
        "storage",
        "00c6d998",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059e1c0",
      "DATA",
      [
        "storage",
        "00c6de70",
        null,
        "undefined *"
      ]
    ],
    [
      "0059e1ec",
      "DATA",
      [
        "storage",
        "00c6dd98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059e148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e110.md#insn-0059e148) · [`0059e17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e110.md#insn-0059e17c) · [`0059e188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e110.md#insn-0059e188)
- 新版 `0059e188`（命令位置の公開資料なし） · `0059e1bc`（命令位置の公開資料なし） · `0059e1c8`（命令位置の公開資料なし）

~~~diff
- 0059e148 ["INT_ADD", "register:40f0:8", ["const:59e148:8", "const:4:8"]]
- 0059e148 ["CALL", null, ["callee:00c57e90:8"]]
+ 0059e188 ["INT_ADD", "register:40f0:8", ["const:59e188:8", "const:4:8"]]
+ 0059e188 ["CALL", null, ["callee:00c57e90:8"]]
- 0059e148 bytes 52e61a94
+ 0059e188 bytes 42e71a94
- 0059e17c ["COPY", "tmp:0:8", ["const:a70:8"]]
- 0059e17c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059e17c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059e17c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059e1bc ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 0059e1bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059e1bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059e1bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059e17c bytes 08c12991
+ 0059e1bc bytes 08c13991
- 0059e188 ["INT_ADD", "register:40f0:8", ["const:59e188:8", "const:4:8"]]
- 0059e188 ["CALL", null, ["callee:0054075c:8"]]
+ 0059e1c8 ["INT_ADD", "register:40f0:8", ["const:59e1c8:8", "const:4:8"]]
+ 0059e1c8 ["CALL", null, ["callee:0054075c:8"]]
- 0059e188 bytes 6589fe97
+ 0059e1c8 bytes 6589fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c41eb323414ab86ddad4b4b3dc1c3b40"></a>

### [`0059e228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e228.md) → [`0059e268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059e268.md) FUN_0059e268

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0059e26c",
      "incomplete_value": false,
      "site": "0059e270",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059e22c",
      "incomplete_value": false,
      "site": "0059e230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "0059e270",
      "DATA",
      [
        "storage",
        "00c6da70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059e270",
      "DATA",
      [
        "storage",
        "00c6de70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059e22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e228.md#insn-0059e22c)
- 新版 `0059e26c`（命令位置の公開資料なし）

~~~diff
- 0059e22c ["COPY", "tmp:0:8", ["const:a70:8"]]
- 0059e22c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059e22c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059e22c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059e26c ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 0059e26c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059e26c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059e26c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059e22c bytes 08c12991
+ 0059e26c bytes 08c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf83e61b7b1824a0373c90b5c3a62744"></a>

### [`0059e238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e238.md) → [`0059e278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059e278.md) FUN_0059e278

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059e288",
      "incomplete_value": false,
      "site": "0059e290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059e248",
      "incomplete_value": false,
      "site": "0059e250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "0059e290",
      "DATA",
      [
        "storage",
        "00c6da70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059e290",
      "DATA",
      [
        "storage",
        "00c6de70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059e248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e238.md#insn-0059e248) · [`0059e254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e238.md#insn-0059e254)
- 新版 `0059e288`（命令位置の公開資料なし） · `0059e294`（命令位置の公開資料なし）

~~~diff
- 0059e248 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 0059e248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059e248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059e248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059e288 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 0059e288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059e288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059e288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059e248 bytes 08c12991
+ 0059e288 bytes 08c13991
- 0059e254 ["INT_ADD", "register:40f0:8", ["const:59e254:8", "const:4:8"]]
- 0059e254 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0059e294 ["INT_ADD", "register:40f0:8", ["const:59e294:8", "const:4:8"]]
+ 0059e294 ["CALL", null, ["callee:00c57ea0:8"]]
- 0059e254 bytes 13e61a94
+ 0059e294 bytes 03e71a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cce704e8b798a9b3ef9cad72b1567431"></a>

### [`0059e268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e268.md) → [`0059e2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059e2a8.md) FUN_0059e2a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059e310",
      "incomplete_value": false,
      "site": "0059e314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059e2d0",
      "incomplete_value": false,
      "site": "0059e2d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059e314",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059e314",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059e2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e268.md#insn-0059e2b4) · [`0059e2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e268.md#insn-0059e2c4) · [`0059e2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e268.md#insn-0059e2d0)
- 新版 `0059e2f4`（命令位置の公開資料なし） · `0059e304`（命令位置の公開資料なし） · `0059e310`（命令位置の公開資料なし）

~~~diff
- 0059e2b4 ["INT_ADD", "register:40f0:8", ["const:59e2b4:8", "const:4:8"]]
- 0059e2b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059e2f4 ["INT_ADD", "register:40f0:8", ["const:59e2f4:8", "const:4:8"]]
+ 0059e2f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059e2b4 bytes ffe51a94
+ 0059e2f4 bytes efe61a94
- 0059e2c4 ["INT_ADD", "register:40f0:8", ["const:59e2c4:8", "const:4:8"]]
- 0059e2c4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059e304 ["INT_ADD", "register:40f0:8", ["const:59e304:8", "const:4:8"]]
+ 0059e304 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059e2c4 bytes fbe51a94
+ 0059e304 bytes ebe61a94
- 0059e2d0 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059e2d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059e2d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059e2d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059e310 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059e310 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059e310 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059e310 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059e2d0 bytes 29011891
+ 0059e310 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-155f7fdd34e277e15a8027b4089f137f"></a>

### [`0059e304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e304.md) → [`0059e344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059e344.md) FUN_0059e344

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0059e348",
      "incomplete_value": false,
      "site": "0059e34c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059e308",
      "incomplete_value": false,
      "site": "0059e30c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "0059e34c",
      "DATA",
      [
        "storage",
        "00c6dac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059e34c",
      "DATA",
      [
        "storage",
        "00c6dec0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059e308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e304.md#insn-0059e308)
- 新版 `0059e348`（命令位置の公開資料なし）

~~~diff
- 0059e308 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 0059e308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059e308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059e308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059e348 ["COPY", "tmp:0:8", ["const:ec0:8"]]
+ 0059e348 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059e348 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059e348 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059e308 bytes 08012b91
+ 0059e348 bytes 08013b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-015d4ead2afcbf6c214f9a6d63d4979d"></a>

### [`0059e314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e314.md) → [`0059e354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059e354.md) FUN_0059e354

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059e364",
      "incomplete_value": false,
      "site": "0059e36c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059e324",
      "incomplete_value": false,
      "site": "0059e32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "0059e36c",
      "DATA",
      [
        "storage",
        "00c6dac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059e36c",
      "DATA",
      [
        "storage",
        "00c6dec0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059e324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e314.md#insn-0059e324) · [`0059e330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e314.md#insn-0059e330)
- 新版 `0059e364`（命令位置の公開資料なし） · `0059e370`（命令位置の公開資料なし）

~~~diff
- 0059e324 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 0059e324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059e324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059e324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059e364 ["COPY", "tmp:0:8", ["const:ec0:8"]]
+ 0059e364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059e364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059e364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059e324 bytes 08012b91
+ 0059e364 bytes 08013b91
- 0059e330 ["INT_ADD", "register:40f0:8", ["const:59e330:8", "const:4:8"]]
- 0059e330 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0059e370 ["INT_ADD", "register:40f0:8", ["const:59e370:8", "const:4:8"]]
+ 0059e370 ["CALL", null, ["callee:00c57ea0:8"]]
- 0059e330 bytes dce51a94
+ 0059e370 bytes cce61a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a09a23b69e87af6ecd5c995cb8ede1ce"></a>

### [`0059e34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e34c.md) → [`0059e38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059e38c.md) _INIT_40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.31% / 新版 85.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059e3c8",
      "incomplete_value": true,
      "site": "0059e3e4",
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
      "definition_site": "0059e388",
      "incomplete_value": true,
      "site": "0059e3a4",
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
      "definition_site": "0059e3ec",
      "incomplete_value": true,
      "site": "0059e408",
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
      "definition_site": "0059e3ac",
      "incomplete_value": true,
      "site": "0059e3c8",
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
      "definition_site": "0059e40c",
      "incomplete_value": true,
      "site": "0059e428",
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
      "definition_site": "0059e3cc",
      "incomplete_value": true,
      "site": "0059e3e8",
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
      "0059e3c8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0059e3ec",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0059e40c",
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
      "0059e3c8",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0059e3ec",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0059e40c",
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

- 旧版 [`0059e3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e34c.md#insn-0059e3c4) · [`0059e3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e34c.md#insn-0059e3e4) · [`0059e580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e34c.md#insn-0059e580)
- 新版 `0059e404`（命令位置の公開資料なし） · `0059e424`（命令位置の公開資料なし） · `0059e5c0`（命令位置の公開資料なし）

~~~diff
- 0059e3c4 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0059e3c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059e3c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059e3c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059e404 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0059e404 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059e404 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059e404 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059e3c4 bytes 4a093691
+ 0059e404 bytes 4a093791
- 0059e3e4 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0059e3e4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059e3e4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059e3e4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059e424 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0059e424 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059e424 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059e424 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059e3e4 bytes 4a553a91
+ 0059e424 bytes 4a893d91
- 0059e580 ["INT_ADD", "register:40f0:8", ["const:59e580:8", "const:4:8"]]
- 0059e580 ["CALL", null, ["callee:00c57e30:8"]]
+ 0059e5c0 ["INT_ADD", "register:40f0:8", ["const:59e5c0:8", "const:4:8"]]
+ 0059e5c0 ["CALL", null, ["callee:00c57e30:8"]]
- 0059e580 bytes 2ce51a94
+ 0059e5c0 bytes 1ce61a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ee3689bd9dd83734567d3d1c8439d5d"></a>

### [`0059e6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e6dc.md) → [`0059e71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059e71c.md) FUN_0059e71c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.69% / 新版 94.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059e770",
      "incomplete_value": true,
      "site": "0059e770",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059e730",
      "incomplete_value": true,
      "site": "0059e730",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059e8a4",
      "incomplete_value": true,
      "site": "0059e8a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f2d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059e864",
      "incomplete_value": true,
      "site": "0059e864",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059e980",
      "incomplete_value": true,
      "site": "0059e980",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b7b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059e940",
      "incomplete_value": true,
      "site": "0059e940",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b3b:8"
              ]
            ]
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
      "0059e754",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "0059e890",
      "READ",
      [
        "storage",
        "0029fe60",
        null,
        "string"
      ]
    ],
    [
      "0059e96c",
      "READ",
      [
        "storage",
        "002afb3b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0059e754",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "0059e890",
      "READ",
      [
        "storage",
        "0029ff2d",
        null,
        "string"
      ]
    ],
    [
      "0059e96c",
      "READ",
      [
        "storage",
        "002afb7b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059e770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e6dc.md#insn-0059e770) · [`0059e708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e6dc.md#insn-0059e708) · [`0059e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e6dc.md#insn-0059e740)
- 新版 `0059e7b0`（命令位置の公開資料なし） · `0059e748`（命令位置の公開資料なし） · `0059e780`（命令位置の公開資料なし）

~~~diff
- 0059e770 ["INT_ADD", "register:40f0:8", ["const:59e770:8", "const:4:8"]]
- 0059e770 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059e7b0 ["INT_ADD", "register:40f0:8", ["const:59e7b0:8", "const:4:8"]]
+ 0059e7b0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059e770 bytes d0e41a94
+ 0059e7b0 bytes c0e51a94
- 0059e708 ["COPY", "tmp:0:8", ["const:165:8"]]
- 0059e708 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059e708 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059e708 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059e748 ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 0059e748 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059e748 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059e748 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059e708 bytes 4a950591
+ 0059e748 bytes 4a950691
- 0059e740 ["INT_ADD", "register:40f0:8", ["const:59e740:8", "const:4:8"]]
- 0059e740 ["CALL", null, ["callee:0044108c:8"]]
+ 0059e780 ["INT_ADD", "register:40f0:8", ["const:59e780:8", "const:4:8"]]
+ 0059e780 ["CALL", null, ["callee:0044108c:8"]]
- 0059e740 bytes 438afa97
+ 0059e780 bytes 438afa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10d969a90f55c7e993f03544d662b6b6"></a>

### [`0059eb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059eb20.md) → [`0059eb60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059eb60.md) FUN_0059eb60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b3fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3fe0.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)
- 新版 呼出元 1件 [`005b4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059eb7c",
      "incomplete_value": false,
      "site": "0059eb80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059eb3c",
      "incomplete_value": false,
      "site": "0059eb40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b30:8"
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
      "0059eb80",
      "DATA",
      [
        "storage",
        "00c6db30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059eb80",
      "DATA",
      [
        "storage",
        "00c6df30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059eb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059eb20.md#insn-0059eb34) · [`0059eb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059eb20.md#insn-0059eb3c)
- 新版 `0059eb74`（命令位置の公開資料なし） · `0059eb7c`（命令位置の公開資料なし）

~~~diff
- 0059eb34 ["INT_ADD", "register:40f0:8", ["const:59eb34:8", "const:4:8"]]
- 0059eb34 ["CALL", null, ["callee:0059b908:8"]]
+ 0059eb74 ["INT_ADD", "register:40f0:8", ["const:59eb74:8", "const:4:8"]]
+ 0059eb74 ["CALL", null, ["callee:0059b908:8"]]
- 0059eb34 bytes 65f3ff97
+ 0059eb74 bytes 65f3ff97
- 0059eb3c ["COPY", "tmp:0:8", ["const:b30:8"]]
- 0059eb3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059eb3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059eb3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059eb7c ["COPY", "tmp:0:8", ["const:f30:8"]]
+ 0059eb7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059eb7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059eb7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059eb3c bytes 08c12c91
+ 0059eb7c bytes 08c13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10e13608b20f887baeb2b106e1ba5597"></a>

### [`0059ec8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ec8c.md) → [`0059eccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059eccc.md) FUN_0059eccc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059ece8",
      "incomplete_value": false,
      "site": "0059ecf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059eca8",
      "incomplete_value": false,
      "site": "0059ecb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059ed00",
      "incomplete_value": false,
      "site": "0059ed00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ecc0",
      "incomplete_value": false,
      "site": "0059ecc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b88:8"
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
      "0059ecf0",
      "DATA",
      [
        "storage",
        "00c6dc38",
        null,
        "undefined *"
      ]
    ],
    [
      "0059ed00",
      "DATA",
      [
        "storage",
        "00c6db88",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0059ecf0",
      "DATA",
      [
        "storage",
        "00c6e038",
        null,
        "undefined *"
      ]
    ],
    [
      "0059ed00",
      "DATA",
      [
        "storage",
        "00c6df88",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059eca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ec8c.md#insn-0059eca0) · [`0059eca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ec8c.md#insn-0059eca4) · [`0059eca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ec8c.md#insn-0059eca8)
- 新版 `0059ece0`（命令位置の公開資料なし） · `0059ece4`（命令位置の公開資料なし） · `0059ece8`（命令位置の公開資料なし）

~~~diff
- 0059eca0 ["INT_ADD", "register:40f0:8", ["const:59eca0:8", "const:4:8"]]
- 0059eca0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0059ece0 ["INT_ADD", "register:40f0:8", ["const:59ece0:8", "const:4:8"]]
+ 0059ece0 ["CALL", null, ["callee:00c57e90:8"]]
- 0059eca0 bytes 7ce31a94
+ 0059ece0 bytes 6ce41a94
- 0059eca4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059ece4 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059eca4 bytes 683600f0
+ 0059ece4 bytes 88360090
- 0059eca8 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 0059eca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059eca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059eca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059ece8 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0059ece8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ece8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ece8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059eca8 bytes 08e13091
+ 0059ece8 bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72a388395cc1980da6b203c196db0a18"></a>

### [`0059ecd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ecd4.md) → [`0059ed14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059ed14.md) FUN_0059ed14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "0059ed40",
      "incomplete_value": false,
      "site": "0059ed44",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "0059ed00",
      "incomplete_value": false,
      "site": "0059ed04",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
      "0059ed44",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059ed44",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ecf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ecd4.md#insn-0059ecf0) · [`0059ecf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ecd4.md#insn-0059ecf8) · [`0059ed10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ecd4.md#insn-0059ed10)
- 新版 `0059ed30`（命令位置の公開資料なし） · `0059ed38`（命令位置の公開資料なし） · `0059ed50`（命令位置の公開資料なし）

~~~diff
- 0059ecf0 ["INT_ADD", "register:40f0:8", ["const:59ecf0:8", "const:4:8"]]
- 0059ecf0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059ed30 ["INT_ADD", "register:40f0:8", ["const:59ed30:8", "const:4:8"]]
+ 0059ed30 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059ecf0 bytes 70e31a94
+ 0059ed30 bytes 60e41a94
- 0059ecf8 ["COPY", "tmp:0:8", ["const:610:8"]]
- 0059ecf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059ecf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059ecf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059ed38 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0059ed38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ed38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ed38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059ecf8 bytes 08411891
+ 0059ed38 bytes 08412891
- 0059ed10 ["INT_ADD", "register:40f0:8", ["const:59ed10:8", "const:4:8"]]
- 0059ed10 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059ed50 ["INT_ADD", "register:40f0:8", ["const:59ed50:8", "const:4:8"]]
+ 0059ed50 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059ed10 bytes 68e31a94
+ 0059ed50 bytes 58e41a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38fb7ad1a895573cc5bd62b925608f46"></a>

### [`0059ed38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ed38.md) → [`0059ed78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059ed78.md) FUN_0059ed78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059eda4",
      "incomplete_value": false,
      "site": "0059eda8",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "0059ed64",
      "incomplete_value": false,
      "site": "0059ed68",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
      "0059eda8",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059eda8",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ed54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ed38.md#insn-0059ed54) · [`0059ed5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ed38.md#insn-0059ed5c) · [`0059ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ed38.md#insn-0059ed74)
- 新版 `0059ed94`（命令位置の公開資料なし） · `0059ed9c`（命令位置の公開資料なし） · `0059edb4`（命令位置の公開資料なし）

~~~diff
- 0059ed54 ["INT_ADD", "register:40f0:8", ["const:59ed54:8", "const:4:8"]]
- 0059ed54 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059ed94 ["INT_ADD", "register:40f0:8", ["const:59ed94:8", "const:4:8"]]
+ 0059ed94 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059ed54 bytes 57e31a94
+ 0059ed94 bytes 47e41a94
- 0059ed5c ["COPY", "tmp:0:8", ["const:610:8"]]
- 0059ed5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059ed5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059ed5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059ed9c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0059ed9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ed9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ed9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059ed5c bytes 08411891
+ 0059ed9c bytes 08412891
- 0059ed74 ["INT_ADD", "register:40f0:8", ["const:59ed74:8", "const:4:8"]]
- 0059ed74 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059edb4 ["INT_ADD", "register:40f0:8", ["const:59edb4:8", "const:4:8"]]
+ 0059edb4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059ed74 bytes 4fe31a94
+ 0059edb4 bytes 3fe41a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97669924a1b0015d3e6abd6866db08fc"></a>

### [`0059ed98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ed98.md) → [`0059edd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059edd8.md) FUN_0059edd8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059ee10",
      "incomplete_value": false,
      "site": "0059ee14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059edd0",
      "incomplete_value": false,
      "site": "0059edd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059ee14",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059ee14",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059edb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ed98.md#insn-0059edb4) · [`0059edc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ed98.md#insn-0059edc4) · [`0059edd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ed98.md#insn-0059edd0)
- 新版 `0059edf4`（命令位置の公開資料なし） · `0059ee04`（命令位置の公開資料なし） · `0059ee10`（命令位置の公開資料なし）

~~~diff
- 0059edb4 ["INT_ADD", "register:40f0:8", ["const:59edb4:8", "const:4:8"]]
- 0059edb4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059edf4 ["INT_ADD", "register:40f0:8", ["const:59edf4:8", "const:4:8"]]
+ 0059edf4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059edb4 bytes 3fe31a94
+ 0059edf4 bytes 2fe41a94
- 0059edc4 ["INT_ADD", "register:40f0:8", ["const:59edc4:8", "const:4:8"]]
- 0059edc4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059ee04 ["INT_ADD", "register:40f0:8", ["const:59ee04:8", "const:4:8"]]
+ 0059ee04 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059edc4 bytes 3be31a94
+ 0059ee04 bytes 2be41a94
- 0059edd0 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059edd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059edd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059edd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059ee10 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059ee10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059ee10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059ee10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059edd0 bytes 29011891
+ 0059ee10 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee322ae91088f3ca1522e279a40e9dc8"></a>

### [`0059ee54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ee54.md) → [`0059ee94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059ee94.md) FUN_0059ee94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0059ee98",
      "incomplete_value": false,
      "site": "0059ee9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ee58",
      "incomplete_value": false,
      "site": "0059ee5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "0059ee9c",
      "DATA",
      [
        "storage",
        "00c6dbe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059ee9c",
      "DATA",
      [
        "storage",
        "00c6dfe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ee58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ee54.md#insn-0059ee58)
- 新版 `0059ee98`（命令位置の公開資料なし）

~~~diff
- 0059ee58 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 0059ee58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059ee58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059ee58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059ee98 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 0059ee98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ee98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ee98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059ee58 bytes 08a12f91
+ 0059ee98 bytes 08a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfa7049cc5cbe6508077c93ce6223d36"></a>

### [`0059ee64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ee64.md) → [`0059eea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059eea4.md) FUN_0059eea4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059eeb4",
      "incomplete_value": false,
      "site": "0059eebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ee74",
      "incomplete_value": false,
      "site": "0059ee7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "0059eebc",
      "DATA",
      [
        "storage",
        "00c6dbe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059eebc",
      "DATA",
      [
        "storage",
        "00c6dfe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ee74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ee64.md#insn-0059ee74) · [`0059ee80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ee64.md#insn-0059ee80)
- 新版 `0059eeb4`（命令位置の公開資料なし） · `0059eec0`（命令位置の公開資料なし）

~~~diff
- 0059ee74 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 0059ee74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059ee74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059ee74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059eeb4 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 0059eeb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059eeb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059eeb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059ee74 bytes 08a12f91
+ 0059eeb4 bytes 08a13f91
- 0059ee80 ["INT_ADD", "register:40f0:8", ["const:59ee80:8", "const:4:8"]]
- 0059ee80 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0059eec0 ["INT_ADD", "register:40f0:8", ["const:59eec0:8", "const:4:8"]]
+ 0059eec0 ["CALL", null, ["callee:00c57ea0:8"]]
- 0059ee80 bytes 08e31a94
+ 0059eec0 bytes f8e31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-447367151f983e921e371abb7cda3259"></a>

### [`0059ee94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ee94.md) → [`0059eed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059eed4.md) FUN_0059eed4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059ef0c",
      "incomplete_value": false,
      "site": "0059ef10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059eecc",
      "incomplete_value": false,
      "site": "0059eed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059ef10",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059ef10",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059eeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ee94.md#insn-0059eeb0) · [`0059eec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ee94.md#insn-0059eec0) · [`0059eecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ee94.md#insn-0059eecc)
- 新版 `0059eef0`（命令位置の公開資料なし） · `0059ef00`（命令位置の公開資料なし） · `0059ef0c`（命令位置の公開資料なし）

~~~diff
- 0059eeb0 ["INT_ADD", "register:40f0:8", ["const:59eeb0:8", "const:4:8"]]
- 0059eeb0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059eef0 ["INT_ADD", "register:40f0:8", ["const:59eef0:8", "const:4:8"]]
+ 0059eef0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059eeb0 bytes 00e31a94
+ 0059eef0 bytes f0e31a94
- 0059eec0 ["INT_ADD", "register:40f0:8", ["const:59eec0:8", "const:4:8"]]
- 0059eec0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059ef00 ["INT_ADD", "register:40f0:8", ["const:59ef00:8", "const:4:8"]]
+ 0059ef00 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059eec0 bytes fce21a94
+ 0059ef00 bytes ece31a94
- 0059eecc ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059eecc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059eecc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059eecc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059ef0c ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059ef0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059ef0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059ef0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059eecc bytes 29011891
+ 0059ef0c bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf0745e7c3a4bd05b27a92d446eeba73"></a>

### [`0059eef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059eef8.md) → [`0059ef38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059ef38.md) FUN_0059ef38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0059ef3c",
      "incomplete_value": false,
      "site": "0059ef40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059eefc",
      "incomplete_value": false,
      "site": "0059ef00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "0059ef40",
      "DATA",
      [
        "storage",
        "00c6dc38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059ef40",
      "DATA",
      [
        "storage",
        "00c6e038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059eef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059eef8.md#insn-0059eef8) · [`0059eefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059eef8.md#insn-0059eefc)
- 新版 `0059ef38`（命令位置の公開資料なし） · `0059ef3c`（命令位置の公開資料なし）

~~~diff
- 0059eef8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059ef38 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059eef8 bytes 683600f0
+ 0059ef38 bytes 88360090
- 0059eefc ["COPY", "tmp:0:8", ["const:c38:8"]]
- 0059eefc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059eefc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059eefc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059ef3c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0059ef3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ef3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ef3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059eefc bytes 08e13091
+ 0059ef3c bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b76908eb7a37e5c0ba35bb2305f5f80"></a>

### [`0059ef08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ef08.md) → [`0059ef48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059ef48.md) FUN_0059ef48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059ef58",
      "incomplete_value": false,
      "site": "0059ef60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ef18",
      "incomplete_value": false,
      "site": "0059ef20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "0059ef60",
      "DATA",
      [
        "storage",
        "00c6dc38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059ef60",
      "DATA",
      [
        "storage",
        "00c6e038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ef14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ef08.md#insn-0059ef14) · [`0059ef18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ef08.md#insn-0059ef18) · [`0059ef24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ef08.md#insn-0059ef24)
- 新版 `0059ef54`（命令位置の公開資料なし） · `0059ef58`（命令位置の公開資料なし） · `0059ef64`（命令位置の公開資料なし）

~~~diff
- 0059ef14 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059ef54 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059ef14 bytes 683600f0
+ 0059ef54 bytes 88360090
- 0059ef18 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 0059ef18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059ef18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059ef18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059ef58 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0059ef58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ef58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ef58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059ef18 bytes 08e13091
+ 0059ef58 bytes 08e10091
- 0059ef24 ["INT_ADD", "register:40f0:8", ["const:59ef24:8", "const:4:8"]]
- 0059ef24 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0059ef64 ["INT_ADD", "register:40f0:8", ["const:59ef64:8", "const:4:8"]]
+ 0059ef64 ["CALL", null, ["callee:00c57ea0:8"]]
- 0059ef24 bytes dfe21a94
+ 0059ef64 bytes cfe31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06200c48f8b6371b417d0c61ffa2fb9a"></a>

### [`0059ef40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ef40.md) → [`0059ef80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059ef80.md) _INIT_41

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.31% / 新版 85.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059efbc",
      "incomplete_value": true,
      "site": "0059efd8",
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
      "definition_site": "0059ef7c",
      "incomplete_value": true,
      "site": "0059ef98",
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
      "definition_site": "0059efe0",
      "incomplete_value": true,
      "site": "0059effc",
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
      "definition_site": "0059efa0",
      "incomplete_value": true,
      "site": "0059efbc",
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
      "definition_site": "0059f020",
      "incomplete_value": true,
      "site": "0059f038",
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
      "definition_site": "0059efe0",
      "incomplete_value": true,
      "site": "0059eff8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0059efbc",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0059efe0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0059f000",
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
      "0059efbc",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0059efe0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0059f000",
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

- 旧版 [`0059efb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ef40.md#insn-0059efb8) · [`0059efd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ef40.md#insn-0059efd8) · [`0059f174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ef40.md#insn-0059f174)
- 新版 `0059eff8`（命令位置の公開資料なし） · `0059f018`（命令位置の公開資料なし） · `0059f1b4`（命令位置の公開資料なし）

~~~diff
- 0059efb8 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0059efb8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059efb8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059efb8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059eff8 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0059eff8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059eff8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059eff8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059efb8 bytes 4a093691
+ 0059eff8 bytes 4a093791
- 0059efd8 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0059efd8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059efd8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059efd8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059f018 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0059f018 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059f018 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059f018 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059efd8 bytes 4a553a91
+ 0059f018 bytes 4a893d91
- 0059f174 ["INT_ADD", "register:40f0:8", ["const:59f174:8", "const:4:8"]]
- 0059f174 ["CALL", null, ["callee:00c57e30:8"]]
+ 0059f1b4 ["INT_ADD", "register:40f0:8", ["const:59f1b4:8", "const:4:8"]]
+ 0059f1b4 ["CALL", null, ["callee:00c57e30:8"]]
- 0059f174 bytes 2fe21a94
+ 0059f1b4 bytes 1fe31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ff631dbaa94cd550fee88f7f7b93d05"></a>

### [`0059f2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f2d0.md) → [`0059f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f310.md) FUN_0059f310

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059f35c",
      "incomplete_value": true,
      "site": "0059f35c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059f31c",
      "incomplete_value": true,
      "site": "0059f31c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059f40c",
      "incomplete_value": false,
      "site": "0059f418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059f3cc",
      "incomplete_value": false,
      "site": "0059f3d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d60:8"
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
      "definition_site": "0059f430",
      "incomplete_value": false,
      "site": "0059f438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059f3f0",
      "incomplete_value": false,
      "site": "0059f3f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "0059f340",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "0059f418",
      "DATA",
      [
        "storage",
        "00c6dd60",
        null,
        "undefined *"
      ]
    ],
    [
      "0059f438",
      "DATA",
      [
        "storage",
        "00c6dc88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059f340",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "0059f418",
      "DATA",
      [
        "storage",
        "00c6e160",
        null,
        "undefined *"
      ]
    ],
    [
      "0059f438",
      "DATA",
      [
        "storage",
        "00c6e088",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059f35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f2d0.md#insn-0059f35c) · [`0059f3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f2d0.md#insn-0059f3b8) · [`0059f2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f2d0.md#insn-0059f2f4)
- 新版 `0059f39c`（命令位置の公開資料なし） · `0059f3f8`（命令位置の公開資料なし） · `0059f334`（命令位置の公開資料なし）

~~~diff
- 0059f35c ["INT_ADD", "register:40f0:8", ["const:59f35c:8", "const:4:8"]]
- 0059f35c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059f39c ["INT_ADD", "register:40f0:8", ["const:59f39c:8", "const:4:8"]]
+ 0059f39c ["CALL", null, ["callee:00c57eb0:8"]]
- 0059f35c bytes d5e11a94
+ 0059f39c bytes c5e21a94
- 0059f3b8 ["INT_ADD", "register:40f0:8", ["const:59f3b8:8", "const:4:8"]]
- 0059f3b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059f3f8 ["INT_ADD", "register:40f0:8", ["const:59f3f8:8", "const:4:8"]]
+ 0059f3f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059f3b8 bytes bee11a94
+ 0059f3f8 bytes aee21a94
- 0059f2f4 ["COPY", "tmp:0:8", ["const:165:8"]]
- 0059f2f4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059f2f4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059f2f4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059f334 ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 0059f334 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059f334 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059f334 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059f2f4 bytes 4a950591
+ 0059f334 bytes 4a950691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3296c75b110ce10817a7f492915e7f36"></a>

### [`0059f4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f4c0.md) → [`0059f500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f500.md) FUN_0059f500

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b271c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b271c.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)
- 新版 呼出元 1件 [`005b275c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059f51c",
      "incomplete_value": false,
      "site": "0059f520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059f4dc",
      "incomplete_value": false,
      "site": "0059f4e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
      "0059f520",
      "DATA",
      [
        "storage",
        "00c6dca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059f520",
      "DATA",
      [
        "storage",
        "00c6e0a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059f4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f4c0.md#insn-0059f4d4) · [`0059f4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f4c0.md#insn-0059f4d8) · [`0059f4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f4c0.md#insn-0059f4dc)
- 新版 `0059f514`（命令位置の公開資料なし） · `0059f518`（命令位置の公開資料なし） · `0059f51c`（命令位置の公開資料なし）

~~~diff
- 0059f4d4 ["INT_ADD", "register:40f0:8", ["const:59f4d4:8", "const:4:8"]]
- 0059f4d4 ["CALL", null, ["callee:0059b908:8"]]
+ 0059f514 ["INT_ADD", "register:40f0:8", ["const:59f514:8", "const:4:8"]]
+ 0059f514 ["CALL", null, ["callee:0059b908:8"]]
- 0059f4d4 bytes fdf0ff97
+ 0059f514 bytes fdf0ff97
- 0059f4d8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059f518 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059f4d8 bytes 683600d0
+ 0059f518 bytes 683600f0
- 0059f4dc ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 0059f4dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059f4dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059f4dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059f51c ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 0059f51c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f51c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f51c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059f4dc bytes 08a13291
+ 0059f51c bytes 08a10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3578d6512e6c7d9f700602e0bcc1b7d"></a>

### [`0059f630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f630.md) → [`0059f670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f670.md) FUN_0059f670

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059f68c",
      "incomplete_value": false,
      "site": "0059f694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059f64c",
      "incomplete_value": false,
      "site": "0059f654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059f6a4",
      "incomplete_value": false,
      "site": "0059f6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059f664",
      "incomplete_value": false,
      "site": "0059f664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d00:8"
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
      "0059f694",
      "DATA",
      [
        "storage",
        "00c6ddb0",
        null,
        "undefined *"
      ]
    ],
    [
      "0059f6a4",
      "DATA",
      [
        "storage",
        "00c6dd00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0059f694",
      "DATA",
      [
        "storage",
        "00c6e1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0059f6a4",
      "DATA",
      [
        "storage",
        "00c6e100",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059f644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f630.md#insn-0059f644) · [`0059f648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f630.md#insn-0059f648) · [`0059f64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f630.md#insn-0059f64c)
- 新版 `0059f684`（命令位置の公開資料なし） · `0059f688`（命令位置の公開資料なし） · `0059f68c`（命令位置の公開資料なし）

~~~diff
- 0059f644 ["INT_ADD", "register:40f0:8", ["const:59f644:8", "const:4:8"]]
- 0059f644 ["CALL", null, ["callee:00c57e90:8"]]
+ 0059f684 ["INT_ADD", "register:40f0:8", ["const:59f684:8", "const:4:8"]]
+ 0059f684 ["CALL", null, ["callee:00c57e90:8"]]
- 0059f644 bytes 13e11a94
+ 0059f684 bytes 03e21a94
- 0059f648 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059f688 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059f648 bytes 683600d0
+ 0059f688 bytes 683600f0
- 0059f64c ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0059f64c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059f64c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059f64c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059f68c ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 0059f68c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f68c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f68c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059f64c bytes 08c13691
+ 0059f68c bytes 08c10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7643a9f95b8d291dba2afbd9a48fa5de"></a>

### [`0059f678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f678.md) → [`0059f6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f6b8.md) FUN_0059f6b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "0059f6e4",
      "incomplete_value": false,
      "site": "0059f6e8",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "0059f6a4",
      "incomplete_value": false,
      "site": "0059f6a8",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
      "0059f6e8",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059f6e8",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059f694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f678.md#insn-0059f694) · [`0059f69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f678.md#insn-0059f69c) · [`0059f6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f678.md#insn-0059f6b4)
- 新版 `0059f6d4`（命令位置の公開資料なし） · `0059f6dc`（命令位置の公開資料なし） · `0059f6f4`（命令位置の公開資料なし）

~~~diff
- 0059f694 ["INT_ADD", "register:40f0:8", ["const:59f694:8", "const:4:8"]]
- 0059f694 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059f6d4 ["INT_ADD", "register:40f0:8", ["const:59f6d4:8", "const:4:8"]]
+ 0059f6d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059f694 bytes 07e11a94
+ 0059f6d4 bytes f7e11a94
- 0059f69c ["COPY", "tmp:0:8", ["const:610:8"]]
- 0059f69c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059f69c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059f69c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059f6dc ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0059f6dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f6dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f6dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059f69c bytes 08411891
+ 0059f6dc bytes 08412891
- 0059f6b4 ["INT_ADD", "register:40f0:8", ["const:59f6b4:8", "const:4:8"]]
- 0059f6b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059f6f4 ["INT_ADD", "register:40f0:8", ["const:59f6f4:8", "const:4:8"]]
+ 0059f6f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059f6b4 bytes ffe01a94
+ 0059f6f4 bytes efe11a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-325c3aeba200d1883cdc4fc72badf160"></a>

### [`0059f6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f6dc.md) → [`0059f71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f71c.md) FUN_0059f71c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059f748",
      "incomplete_value": false,
      "site": "0059f74c",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "0059f708",
      "incomplete_value": false,
      "site": "0059f70c",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
      "0059f74c",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059f74c",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059f6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f6dc.md#insn-0059f6f8) · [`0059f700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f6dc.md#insn-0059f700) · [`0059f718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f6dc.md#insn-0059f718)
- 新版 `0059f738`（命令位置の公開資料なし） · `0059f740`（命令位置の公開資料なし） · `0059f758`（命令位置の公開資料なし）

~~~diff
- 0059f6f8 ["INT_ADD", "register:40f0:8", ["const:59f6f8:8", "const:4:8"]]
- 0059f6f8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059f738 ["INT_ADD", "register:40f0:8", ["const:59f738:8", "const:4:8"]]
+ 0059f738 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059f6f8 bytes eee01a94
+ 0059f738 bytes dee11a94
- 0059f700 ["COPY", "tmp:0:8", ["const:610:8"]]
- 0059f700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059f700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059f700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059f740 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0059f740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059f700 bytes 08411891
+ 0059f740 bytes 08412891
- 0059f718 ["INT_ADD", "register:40f0:8", ["const:59f718:8", "const:4:8"]]
- 0059f718 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059f758 ["INT_ADD", "register:40f0:8", ["const:59f758:8", "const:4:8"]]
+ 0059f758 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059f718 bytes e6e01a94
+ 0059f758 bytes d6e11a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c37f9f51f580863a2dda52585443de5"></a>

### [`0059f73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f73c.md) → [`0059f77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f77c.md) FUN_0059f77c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059f784",
      "incomplete_value": false,
      "site": "0059f788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059f744",
      "incomplete_value": false,
      "site": "0059f748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059f788",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059f788",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059f744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f73c.md#insn-0059f744) · [`0059f768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f73c.md#insn-0059f768)
- 新版 `0059f784`（命令位置の公開資料なし） · `0059f7a8`（命令位置の公開資料なし）

~~~diff
- 0059f744 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059f744 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059f744 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059f744 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059f784 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059f784 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059f784 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059f784 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059f744 bytes 29011891
+ 0059f784 bytes 29012891
- 0059f768 ["INT_ADD", "register:40f0:8", ["const:59f768:8", "const:4:8"]]
- 0059f768 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059f7a8 ["INT_ADD", "register:40f0:8", ["const:59f7a8:8", "const:4:8"]]
+ 0059f7a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059f768 bytes d2e01a94
+ 0059f7a8 bytes c2e11a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c345262b2fa1aa681c170fc7d25cc78"></a>

### [`0059f77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f77c.md) → [`0059f7bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f7bc.md) FUN_0059f7bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0059f7c0",
      "incomplete_value": false,
      "site": "0059f7c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059f780",
      "incomplete_value": false,
      "site": "0059f784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d60:8"
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
      "0059f7c4",
      "DATA",
      [
        "storage",
        "00c6dd60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059f7c4",
      "DATA",
      [
        "storage",
        "00c6e160",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059f77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f77c.md#insn-0059f77c) · [`0059f780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f77c.md#insn-0059f780)
- 新版 `0059f7bc`（命令位置の公開資料なし） · `0059f7c0`（命令位置の公開資料なし）

~~~diff
- 0059f77c ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059f7bc ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059f77c bytes 683600d0
+ 0059f7bc bytes 683600f0
- 0059f780 ["COPY", "tmp:0:8", ["const:d60:8"]]
- 0059f780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059f780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059f780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059f7c0 ["COPY", "tmp:0:8", ["const:160:8"]]
+ 0059f7c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f7c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f7c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059f780 bytes 08813591
+ 0059f7c0 bytes 08810591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0ff14ef04f1945df84eda379280f904"></a>

### [`0059f78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f78c.md) → [`0059f7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f7cc.md) FUN_0059f7cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059f7dc",
      "incomplete_value": false,
      "site": "0059f7e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059f79c",
      "incomplete_value": false,
      "site": "0059f7a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d60:8"
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
      "0059f7e4",
      "DATA",
      [
        "storage",
        "00c6dd60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059f7e4",
      "DATA",
      [
        "storage",
        "00c6e160",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059f798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f78c.md#insn-0059f798) · [`0059f79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f78c.md#insn-0059f79c) · [`0059f7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f78c.md#insn-0059f7a8)
- 新版 `0059f7d8`（命令位置の公開資料なし） · `0059f7dc`（命令位置の公開資料なし） · `0059f7e8`（命令位置の公開資料なし）

~~~diff
- 0059f798 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059f7d8 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059f798 bytes 683600d0
+ 0059f7d8 bytes 683600f0
- 0059f79c ["COPY", "tmp:0:8", ["const:d60:8"]]
- 0059f79c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059f79c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059f79c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059f7dc ["COPY", "tmp:0:8", ["const:160:8"]]
+ 0059f7dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f7dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f7dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059f79c bytes 08813591
+ 0059f7dc bytes 08810591
- 0059f7a8 ["INT_ADD", "register:40f0:8", ["const:59f7a8:8", "const:4:8"]]
- 0059f7a8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0059f7e8 ["INT_ADD", "register:40f0:8", ["const:59f7e8:8", "const:4:8"]]
+ 0059f7e8 ["CALL", null, ["callee:00c57ea0:8"]]
- 0059f7a8 bytes bee01a94
+ 0059f7e8 bytes aee11a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09e81f6752ab05c28def3c830e236557"></a>

### [`0059f7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f7bc.md) → [`0059f7fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f7fc.md) FUN_0059f7fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059f804",
      "incomplete_value": false,
      "site": "0059f808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059f7c4",
      "incomplete_value": false,
      "site": "0059f7c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059f808",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059f808",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059f7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f7bc.md#insn-0059f7c4)
- 新版 `0059f804`（命令位置の公開資料なし）

~~~diff
- 0059f7c4 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059f7c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059f7c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059f7c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059f804 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059f804 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059f804 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059f804 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059f7c4 bytes 29011891
+ 0059f804 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bccf968120ea9153ab6bd920259909de"></a>

### [`0059f7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f7e0.md) → [`0059f820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f820.md) FUN_0059f820

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0059f824",
      "incomplete_value": false,
      "site": "0059f828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059f7e4",
      "incomplete_value": false,
      "site": "0059f7e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "0059f828",
      "DATA",
      [
        "storage",
        "00c6ddb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059f828",
      "DATA",
      [
        "storage",
        "00c6e1b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059f7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f7e0.md#insn-0059f7e0) · [`0059f7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f7e0.md#insn-0059f7e4)
- 新版 `0059f820`（命令位置の公開資料なし） · `0059f824`（命令位置の公開資料なし）

~~~diff
- 0059f7e0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059f820 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059f7e0 bytes 683600d0
+ 0059f820 bytes 683600f0
- 0059f7e4 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0059f7e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059f7e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059f7e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059f824 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 0059f824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059f7e4 bytes 08c13691
+ 0059f824 bytes 08c10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-573242056ebaad77da9920f0dfbb5932"></a>

### [`0059f7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f7f0.md) → [`0059f830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f830.md) FUN_0059f830

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059f840",
      "incomplete_value": false,
      "site": "0059f848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059f800",
      "incomplete_value": false,
      "site": "0059f808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "0059f848",
      "DATA",
      [
        "storage",
        "00c6ddb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059f848",
      "DATA",
      [
        "storage",
        "00c6e1b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059f7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f7f0.md#insn-0059f7fc) · [`0059f800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f7f0.md#insn-0059f800) · [`0059f80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f7f0.md#insn-0059f80c)
- 新版 `0059f83c`（命令位置の公開資料なし） · `0059f840`（命令位置の公開資料なし） · `0059f84c`（命令位置の公開資料なし）

~~~diff
- 0059f7fc ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059f83c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059f7fc bytes 683600d0
+ 0059f83c bytes 683600f0
- 0059f800 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0059f800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059f800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059f800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059f840 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 0059f840 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f840 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059f840 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059f800 bytes 08c13691
+ 0059f840 bytes 08c10691
- 0059f80c ["INT_ADD", "register:40f0:8", ["const:59f80c:8", "const:4:8"]]
- 0059f80c ["CALL", null, ["callee:00c57ea0:8"]]
+ 0059f84c ["INT_ADD", "register:40f0:8", ["const:59f84c:8", "const:4:8"]]
+ 0059f84c ["CALL", null, ["callee:00c57ea0:8"]]
- 0059f80c bytes a5e01a94
+ 0059f84c bytes 95e11a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c385fb18d7724f59108413b5f59377e6"></a>

### [`0059f828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f828.md) → [`0059f868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f868.md) _INIT_42

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059f8a4",
      "incomplete_value": true,
      "site": "0059f8c0",
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
      "definition_site": "0059f864",
      "incomplete_value": true,
      "site": "0059f880",
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
      "definition_site": "0059f8c8",
      "incomplete_value": true,
      "site": "0059f8e4",
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
      "definition_site": "0059f888",
      "incomplete_value": true,
      "site": "0059f8a4",
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
      "definition_site": "0059f8e8",
      "incomplete_value": true,
      "site": "0059f904",
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
      "definition_site": "0059f8a8",
      "incomplete_value": true,
      "site": "0059f8c4",
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
      "0059f8a4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0059f8c8",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0059f8e8",
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
      "0059f8a4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0059f8c8",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0059f8e8",
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

- 旧版 [`0059f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f828.md#insn-0059f8a0) · [`0059f8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f828.md#insn-0059f8c0) · [`0059f988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f828.md#insn-0059f988)
- 新版 `0059f8e0`（命令位置の公開資料なし） · `0059f900`（命令位置の公開資料なし） · `0059f9c8`（命令位置の公開資料なし）

~~~diff
- 0059f8a0 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0059f8a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059f8a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059f8a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059f8e0 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0059f8e0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059f8e0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059f8e0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059f8a0 bytes 4a093691
+ 0059f8e0 bytes 4a093791
- 0059f8c0 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0059f8c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059f8c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059f8c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059f900 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0059f900 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059f900 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059f900 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059f8c0 bytes 4a553a91
+ 0059f900 bytes 4a893d91
- 0059f988 ["INT_ADD", "register:40f0:8", ["const:59f988:8", "const:4:8"]]
- 0059f988 ["CALL", null, ["callee:0043b7f8:8"]]
+ 0059f9c8 ["INT_ADD", "register:40f0:8", ["const:59f9c8:8", "const:4:8"]]
+ 0059f9c8 ["CALL", null, ["callee:0043b7f8:8"]]
- 0059f988 bytes 8c6ffa97
+ 0059f9c8 bytes 8c6ffa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-907ba5d84bd5a961a33da08f4b183989"></a>

### [`0059fbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fbb8.md) → [`0059fbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059fbf8.md) FUN_0059fbf8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059fc00",
      "incomplete_value": false,
      "site": "0059fc04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059fbc0",
      "incomplete_value": false,
      "site": "0059fbc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059fc04",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059fc04",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059fbc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fbb8.md#insn-0059fbc0)
- 新版 `0059fc00`（命令位置の公開資料なし）

~~~diff
- 0059fbc0 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059fbc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059fbc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059fbc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059fc00 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059fc00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059fc00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059fc00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059fbc0 bytes 29011891
+ 0059fc00 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a09e053ae183e5d596874ac715a33302"></a>

### [`0059fbd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fbd8.md) → [`0059fc18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059fc18.md) FUN_0059fc18

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059fc20",
      "incomplete_value": false,
      "site": "0059fc24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059fbe0",
      "incomplete_value": false,
      "site": "0059fbe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059fc24",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059fc24",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059fbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fbd8.md#insn-0059fbe0) · [`0059fc04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fbd8.md#insn-0059fc04)
- 新版 `0059fc20`（命令位置の公開資料なし） · `0059fc44`（命令位置の公開資料なし）

~~~diff
- 0059fbe0 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059fbe0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059fbe0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059fbe0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059fc20 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059fc20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059fc20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059fc20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059fbe0 bytes 29011891
+ 0059fc20 bytes 29012891
- 0059fc04 ["INT_ADD", "register:40f0:8", ["const:59fc04:8", "const:4:8"]]
- 0059fc04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059fc44 ["INT_ADD", "register:40f0:8", ["const:59fc44:8", "const:4:8"]]
+ 0059fc44 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059fc04 bytes abdf1a94
+ 0059fc44 bytes 9be01a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0119bbadbbf606b294154bba994b21ed"></a>

### [`0059fc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fc18.md) → [`0059fc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059fc58.md) FUN_0059fc58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059fca4",
      "incomplete_value": true,
      "site": "0059fca4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059fc64",
      "incomplete_value": true,
      "site": "0059fc64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059fd54",
      "incomplete_value": false,
      "site": "0059fd60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059fd14",
      "incomplete_value": false,
      "site": "0059fd20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "definition_site": "0059fd78",
      "incomplete_value": false,
      "site": "0059fd80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059fd38",
      "incomplete_value": false,
      "site": "0059fd40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "0059fc88",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "0059fd60",
      "DATA",
      [
        "storage",
        "00c6ded8",
        null,
        "undefined *"
      ]
    ],
    [
      "0059fd80",
      "DATA",
      [
        "storage",
        "00c6de00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059fc88",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "0059fd60",
      "DATA",
      [
        "storage",
        "00c6e2d8",
        null,
        "undefined *"
      ]
    ],
    [
      "0059fd80",
      "DATA",
      [
        "storage",
        "00c6e200",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059fca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fc18.md#insn-0059fca4) · [`0059fd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fc18.md#insn-0059fd00) · [`0059fc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fc18.md#insn-0059fc3c)
- 新版 `0059fce4`（命令位置の公開資料なし） · `0059fd40`（命令位置の公開資料なし） · `0059fc7c`（命令位置の公開資料なし）

~~~diff
- 0059fca4 ["INT_ADD", "register:40f0:8", ["const:59fca4:8", "const:4:8"]]
- 0059fca4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059fce4 ["INT_ADD", "register:40f0:8", ["const:59fce4:8", "const:4:8"]]
+ 0059fce4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059fca4 bytes 83df1a94
+ 0059fce4 bytes 73e01a94
- 0059fd00 ["INT_ADD", "register:40f0:8", ["const:59fd00:8", "const:4:8"]]
- 0059fd00 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0059fd40 ["INT_ADD", "register:40f0:8", ["const:59fd40:8", "const:4:8"]]
+ 0059fd40 ["CALL", null, ["callee:00c57eb0:8"]]
- 0059fd00 bytes 6cdf1a94
+ 0059fd40 bytes 5ce01a94
- 0059fc3c ["COPY", "tmp:0:8", ["const:165:8"]]
- 0059fc3c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059fc3c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059fc3c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059fc7c ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 0059fc7c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059fc7c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059fc7c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059fc3c bytes 4a950591
+ 0059fc7c bytes 4a950691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d4b595edcd6561a553cd0a73b8801e0"></a>

### [`0059fe64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fe64.md) → [`0059fea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059fea4.md) FUN_0059fea4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059fec0",
      "incomplete_value": false,
      "site": "0059fec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059fe80",
      "incomplete_value": false,
      "site": "0059fe88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:f28:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059fed8",
      "incomplete_value": false,
      "site": "0059fed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059fe98",
      "incomplete_value": false,
      "site": "0059fe98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "0059fec8",
      "DATA",
      [
        "storage",
        "00c6df28",
        null,
        "undefined *"
      ]
    ],
    [
      "0059fed8",
      "DATA",
      [
        "storage",
        "00c6de38",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0059fec8",
      "DATA",
      [
        "storage",
        "00c6e328",
        null,
        "undefined *"
      ]
    ],
    [
      "0059fed8",
      "DATA",
      [
        "storage",
        "00c6e238",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059fe78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fe64.md#insn-0059fe78) · [`0059fe7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fe64.md#insn-0059fe7c) · [`0059fe80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fe64.md#insn-0059fe80)
- 新版 `0059feb8`（命令位置の公開資料なし） · `0059febc`（命令位置の公開資料なし） · `0059fec0`（命令位置の公開資料なし）

~~~diff
- 0059fe78 ["INT_ADD", "register:40f0:8", ["const:59fe78:8", "const:4:8"]]
- 0059fe78 ["CALL", null, ["callee:00c57e90:8"]]
+ 0059feb8 ["INT_ADD", "register:40f0:8", ["const:59feb8:8", "const:4:8"]]
+ 0059feb8 ["CALL", null, ["callee:00c57e90:8"]]
- 0059fe78 bytes 06df1a94
+ 0059feb8 bytes f6df1a94
- 0059fe7c ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059febc ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059fe7c bytes 683600d0
+ 0059febc bytes 683600f0
- 0059fe80 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 0059fe80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059fe80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059fe80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059fec0 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 0059fec0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059fec0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059fec0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059fe80 bytes 08a13c91
+ 0059fec0 bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c89f2ac8f641123e6b420f85106fd93"></a>

### [`0059fefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fefc.md) → [`0059ff3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059ff3c.md) FUN_0059ff3c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0059ff40",
      "incomplete_value": false,
      "site": "0059ff44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ff00",
      "incomplete_value": false,
      "site": "0059ff04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "0059ff44",
      "DATA",
      [
        "storage",
        "00c6ded8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059ff44",
      "DATA",
      [
        "storage",
        "00c6e2d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059fefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fefc.md#insn-0059fefc) · [`0059ff00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fefc.md#insn-0059ff00)
- 新版 `0059ff3c`（命令位置の公開資料なし） · `0059ff40`（命令位置の公開資料なし）

~~~diff
- 0059fefc ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059ff3c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059fefc bytes 683600d0
+ 0059ff3c bytes 683600f0
- 0059ff00 ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 0059ff00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059ff00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059ff00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059ff40 ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 0059ff40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ff40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ff40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059ff00 bytes 08613b91
+ 0059ff40 bytes 08610b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d327869511bcef10b8094383f80ed418"></a>

### [`0059ff0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff0c.md) → [`0059ff4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059ff4c.md) FUN_0059ff4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059ff5c",
      "incomplete_value": false,
      "site": "0059ff64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ff1c",
      "incomplete_value": false,
      "site": "0059ff24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "0059ff64",
      "DATA",
      [
        "storage",
        "00c6ded8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059ff64",
      "DATA",
      [
        "storage",
        "00c6e2d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ff18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff0c.md#insn-0059ff18) · [`0059ff1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff0c.md#insn-0059ff1c) · [`0059ff28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff0c.md#insn-0059ff28)
- 新版 `0059ff58`（命令位置の公開資料なし） · `0059ff5c`（命令位置の公開資料なし） · `0059ff68`（命令位置の公開資料なし）

~~~diff
- 0059ff18 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059ff58 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059ff18 bytes 683600d0
+ 0059ff58 bytes 683600f0
- 0059ff1c ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 0059ff1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059ff1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059ff1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059ff5c ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 0059ff5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ff5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059ff5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059ff1c bytes 08613b91
+ 0059ff5c bytes 08610b91
- 0059ff28 ["INT_ADD", "register:40f0:8", ["const:59ff28:8", "const:4:8"]]
- 0059ff28 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0059ff68 ["INT_ADD", "register:40f0:8", ["const:59ff68:8", "const:4:8"]]
+ 0059ff68 ["CALL", null, ["callee:00c57ea0:8"]]
- 0059ff28 bytes dede1a94
+ 0059ff68 bytes cedf1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-937e14cc4839a1ad328ed3cf98453bb8"></a>

### [`0059ff3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff3c.md) → [`0059ff7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059ff7c.md) FUN_0059ff7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059ff84",
      "incomplete_value": false,
      "site": "0059ff88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ff44",
      "incomplete_value": false,
      "site": "0059ff48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "0059ff88",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059ff88",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ff44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff3c.md#insn-0059ff44)
- 新版 `0059ff84`（命令位置の公開資料なし）

~~~diff
- 0059ff44 ["COPY", "tmp:0:8", ["const:600:8"]]
- 0059ff44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059ff44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059ff44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059ff84 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0059ff84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059ff84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059ff84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059ff44 bytes 29011891
+ 0059ff84 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

