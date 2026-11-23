# v15.7.4 → v16.0.0 · 命令位置の検査未完了 (21)

[一覧の目次](README.md)

<a id="compare-2c332e5368a4304631ba7a1b0dca75fa"></a>

### [`00bdc650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc650.md) → [`00c590a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590a0.md) _ZN5Botan8PEM_Code18decode_check_labelERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004c36b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c36b4.md) [`004ce004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce004.md) · 呼出先 1件 [`004c2d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2d3c.md)
- 新版 呼出元 2件 [`004e654c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e654c.md) [`004f0e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0e9c.md) · 呼出先 1件 [`004e5bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5bd4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc654",
      "READ",
      [
        "storage",
        "00c1cbe0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc65c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e5bd4"
      ]
    ]
  ],
  "added": [
    [
      "00c590a4",
      "READ",
      [
        "storage",
        "00c9c610",
        null,
        "pointer"
      ]
    ],
    [
      "00c590ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e5bd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc650.md#insn-00bdc650) · [`00bdc654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc650.md#insn-00bdc654) · [`00bdc658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc650.md#insn-00bdc658)

~~~diff
- 00bdc650 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc650 bytes 10020090
- 00bdc654 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:be0:8"]]
- 00bdc654 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc654 bytes 11f245f9
- 00bdc658 ["COPY", "tmp:0:8", ["const:be0:8"]]
- 00bdc658 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc658 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc658 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc658 bytes 10822f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-424a1faaf923754afcdabf9e6a580137"></a>

### [`00bdc660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc660.md) → [`00c590b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590b0.md) _ZN5Botan8PEM_Code6decodeERNS_10DataSourceERNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`004c2d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2d3c.md) [`004c37cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c37cc.md) [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`004ea660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea660.md) · 呼出先 1件 [`004c2f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2f88.md)
- 新版 呼出元 4件 [`004e5bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5bd4.md) [`004e6664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6664.md) [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`0050d4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d4f8.md) · 呼出先 1件 [`004e5e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5e20.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc664",
      "READ",
      [
        "storage",
        "00c1cbe8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc66c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e5e20"
      ]
    ]
  ],
  "added": [
    [
      "00c590b4",
      "READ",
      [
        "storage",
        "00c9c618",
        null,
        "pointer"
      ]
    ],
    [
      "00c590bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e5e20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc660.md#insn-00bdc660) · [`00bdc664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc660.md#insn-00bdc664) · [`00bdc668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc660.md#insn-00bdc668)

~~~diff
- 00bdc660 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc660 bytes 10020090
- 00bdc664 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:be8:8"]]
- 00bdc664 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc664 bytes 11f645f9
- 00bdc668 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 00bdc668 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc668 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc668 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc668 bytes 10a22f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8c89969c0e7f20a821b813ec947e4dc"></a>

### [`00bdc6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6b0.md) → [`00c59100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59100.md) _ZN5Botan17EMSA_PKCS1v15_RawC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004c3c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3c00.md) [`005104e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005104e0.md) · 呼出先 1件 [`0049e24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e24c.md)
- 新版 呼出元 2件 [`004e6a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6a98.md) [`00533378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533378.md) · 呼出先 1件 [`004c10e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c10e4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc6b4",
      "READ",
      [
        "storage",
        "00c1cc10",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc6bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c10e4"
      ]
    ]
  ],
  "added": [
    [
      "00c59104",
      "READ",
      [
        "storage",
        "00c9c640",
        null,
        "pointer"
      ]
    ],
    [
      "00c5910c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c10e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6b0.md#insn-00bdc6b0) · [`00bdc6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6b0.md#insn-00bdc6b4) · [`00bdc6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6b0.md#insn-00bdc6b8)

~~~diff
- 00bdc6b0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc6b0 bytes 10020090
- 00bdc6b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c10:8"]]
- 00bdc6b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc6b4 bytes 110a46f9
- 00bdc6b8 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 00bdc6b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc6b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc6b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc6b8 bytes 10423091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4ad58b59d8fc326ea7a8b44256d736d"></a>

### [`00bdc720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc720.md) → [`00c59170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59170.md) _ZN5Botan15load_public_keyERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS3_9allocatorIhEEEE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004ce004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce004.md) · 呼出先 1件 [`004c52e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c52e0.md)
- 新版 呼出元 1件 [`004f0e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0e9c.md) · 呼出先 1件 [`004e8178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8178.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc724",
      "READ",
      [
        "storage",
        "00c1cc48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc72c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e8178"
      ]
    ]
  ],
  "added": [
    [
      "00c59174",
      "READ",
      [
        "storage",
        "00c9c678",
        null,
        "pointer"
      ]
    ],
    [
      "00c5917c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e8178"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc720.md#insn-00bdc720) · [`00bdc724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc720.md#insn-00bdc724) · [`00bdc728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc720.md#insn-00bdc728)

~~~diff
- 00bdc720 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc720 bytes 10020090
- 00bdc724 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c48:8"]]
- 00bdc724 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc724 bytes 112646f9
- 00bdc728 ["COPY", "tmp:0:8", ["const:c48:8"]]
- 00bdc728 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc728 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc728 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc728 bytes 10223191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e6b4c46d62106ab3728a5891230462e"></a>

### [`00bdc730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc730.md) → [`00c59180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59180.md) _ZN5Botan13RSA_PublicKeyC1ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004c52e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c52e0.md) · 呼出先 1件 [`004c56b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c56b0.md)
- 新版 呼出元 1件 [`004e8178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8178.md) · 呼出先 1件 [`004e8548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8548.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc734",
      "READ",
      [
        "storage",
        "00c1cc50",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc73c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e8548"
      ]
    ]
  ],
  "added": [
    [
      "00c59184",
      "READ",
      [
        "storage",
        "00c9c680",
        null,
        "pointer"
      ]
    ],
    [
      "00c5918c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e8548"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc730.md#insn-00bdc730) · [`00bdc734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc730.md#insn-00bdc734) · [`00bdc738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc730.md#insn-00bdc738)

~~~diff
- 00bdc730 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc730 bytes 10020090
- 00bdc734 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c50:8"]]
- 00bdc734 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc734 bytes 112a46f9
- 00bdc738 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 00bdc738 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc738 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc738 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc738 bytes 10423191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cab5de5cbb1cd6823ea5403f3d86e0b1"></a>

### [`00bdc880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc880.md) → [`00c592d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592d0.md) _ZN5Botan4X5098load_keyERNS_10DataSourceE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`004ce670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce670.md) [`004ce6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce6fc.md) [`004ce7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce7d8.md) [`004ec0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec0b4.md) [`0055ddc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055ddc8.md) · 呼出先 1件 [`004ce004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce004.md)
- 新版 呼出元 5件 [`004f1508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1508.md) [`004f1594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1594.md) [`004f1670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1670.md) [`0050ef4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ef4c.md) [`00580c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580c60.md) · 呼出先 1件 [`004f0e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0e9c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc884",
      "READ",
      [
        "storage",
        "00c1ccf8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc88c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004f0e9c"
      ]
    ]
  ],
  "added": [
    [
      "00c592d4",
      "READ",
      [
        "storage",
        "00c9c728",
        null,
        "pointer"
      ]
    ],
    [
      "00c592dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004f0e9c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc880.md#insn-00bdc880) · [`00bdc884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc880.md#insn-00bdc884) · [`00bdc888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc880.md#insn-00bdc888)

~~~diff
- 00bdc880 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc880 bytes 10020090
- 00bdc884 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:cf8:8"]]
- 00bdc884 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc884 bytes 117e46f9
- 00bdc888 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 00bdc888 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc888 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc888 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc888 bytes 10e23391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d418ba3935efbea828f9749fac522028"></a>

### [`00bdc890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc890.md) → [`00c592e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592e0.md) _ZN5Botan11BER_DecoderC2ERNS_10DataSourceE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`004ce004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce004.md) [`004ea660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea660.md) [`00513c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513c60.md) · 呼出先 1件 [`0048d668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d668.md)
- 新版 呼出元 3件 [`004f0e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0e9c.md) [`0050d4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d4f8.md) [`00536af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536af8.md) · 呼出先 1件 [`004b0500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0500.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc894",
      "READ",
      [
        "storage",
        "00c1cd00",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc89c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004b0500"
      ]
    ]
  ],
  "added": [
    [
      "00c592e4",
      "READ",
      [
        "storage",
        "00c9c730",
        null,
        "pointer"
      ]
    ],
    [
      "00c592ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004b0500"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc890.md#insn-00bdc890) · [`00bdc894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc890.md#insn-00bdc894) · [`00bdc898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc890.md#insn-00bdc898)

~~~diff
- 00bdc890 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc890 bytes 10020090
- 00bdc894 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:d00:8"]]
- 00bdc894 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc894 bytes 118246f9
- 00bdc898 ["COPY", "tmp:0:8", ["const:d00:8"]]
- 00bdc898 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc898 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc898 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc898 bytes 10023491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d82304be648c77f95ac1d03078e41878"></a>

### [`00bdccd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccd0.md) → [`00c59720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59720.md) _ZN5Botan25key_constraints_to_stringENS_15Key_ConstraintsE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004e3024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3024.md) · 呼出先 1件 [`004e242c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e242c.md)
- 新版 呼出元 1件 [`00505ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505ebc.md) · 呼出先 1件 [`005052c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/005052c4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdccd4",
      "READ",
      [
        "storage",
        "00c1cf20",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdccdc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "005052c4"
      ]
    ]
  ],
  "added": [
    [
      "00c59724",
      "READ",
      [
        "storage",
        "00c9c950",
        null,
        "pointer"
      ]
    ],
    [
      "00c5972c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "005052c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdccd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccd0.md#insn-00bdccd0) · [`00bdccd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccd0.md#insn-00bdccd4) · [`00bdccd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccd0.md#insn-00bdccd8)

~~~diff
- 00bdccd0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdccd0 bytes 10020090
- 00bdccd4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f20:8"]]
- 00bdccd4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdccd4 bytes 119247f9
- 00bdccd8 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00bdccd8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdccd8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdccd8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdccd8 bytes 10823c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcaa4cadfa647085a7a12471b22de012"></a>

### [`00bdcda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcda0.md) → [`00c597f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c597f0.md) _ZN5Botan11BER_Decoder15decode_optionalINS_10ExtensionsEEERS0_RT_NS_8ASN1_TagES6_RKS4_

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004e6d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6d3c.md) [`004e9fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9fdc.md) · 呼出先 1件 [`004e82ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e82ac.md)
- 新版 呼出元 2件 [`00509bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md) [`0050ce74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050ce74.md) · 呼出先 1件 [`0050b144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b144.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcda4",
      "READ",
      [
        "storage",
        "00c1cf88",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcdac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0050b144"
      ]
    ]
  ],
  "added": [
    [
      "00c597f4",
      "READ",
      [
        "storage",
        "00c9c9b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c597fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0050b144"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcda0.md#insn-00bdcda0) · [`00bdcda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcda0.md#insn-00bdcda4) · [`00bdcda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcda0.md#insn-00bdcda8)

~~~diff
- 00bdcda0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcda0 bytes 10020090
- 00bdcda4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f88:8"]]
- 00bdcda4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcda4 bytes 11c647f9
- 00bdcda8 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 00bdcda8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcda8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcda8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcda8 bytes 10223e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0970bc984078accd7cdbc51041490086"></a>

### [`00bdcdc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcdc0.md) → [`00c59810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59810.md) _ZNK5Botan16X509_Certificate23load_subject_public_keyEv

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`004e85ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e85ec.md) [`00501b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501b08.md) [`00503af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503af8.md) [`005054cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00505/005054cc.md) · 呼出先 1件 [`00500f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/00500f10.md)
- 新版 呼出元 4件 [`0050b484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b484.md) [`005249a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005249a0.md) [`00526990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526990.md) [`00528364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528364.md) · 呼出先 1件 [`00523da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523da8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcdc4",
      "READ",
      [
        "storage",
        "00c1cf98",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcdcc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00523da8"
      ]
    ]
  ],
  "added": [
    [
      "00c59814",
      "READ",
      [
        "storage",
        "00c9c9c8",
        null,
        "pointer"
      ]
    ],
    [
      "00c5981c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00523da8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcdc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcdc0.md#insn-00bdcdc0) · [`00bdcdc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcdc0.md#insn-00bdcdc4) · [`00bdcdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcdc0.md#insn-00bdcdc8)

~~~diff
- 00bdcdc0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcdc0 bytes 10020090
- 00bdcdc4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f98:8"]]
- 00bdcdc4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcdc4 bytes 11ce47f9
- 00bdcdc8 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00bdcdc8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcdc8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcdc8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcdc8 bytes 10623e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9648441b50bc1abc6a2b73d1cab1c8ed"></a>

### [`00bdced0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdced0.md) → [`00c59920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59920.md) _ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004ec8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec8c8.md) [`004fdfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdfd8.md) · 呼出先 1件 [`004eca70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004eca70.md)
- 新版 呼出元 2件 [`0050f760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f760.md) [`00520e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) · 呼出先 1件 [`0050f908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f908.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdced4",
      "READ",
      [
        "storage",
        "00c1d020",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcedc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0050f908"
      ]
    ]
  ],
  "added": [
    [
      "00c59924",
      "READ",
      [
        "storage",
        "00c9ca50",
        null,
        "pointer"
      ]
    ],
    [
      "00c5992c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0050f908"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdced0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdced0.md#insn-00bdced0) · [`00bdced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdced0.md#insn-00bdced4) · [`00bdced8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdced0.md#insn-00bdced8)

~~~diff
- 00bdced0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdced0 bytes 100200b0
- 00bdced4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:20:8"]]
- 00bdced4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdced4 bytes 111240f9
- 00bdced8 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00bdced8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdced8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdced8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdced8 bytes 10820091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-499d6e27f72db82a3d5b71fd87c9690d"></a>

### [`00bdcee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcee0.md) → [`00c59930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59930.md) _ZN5Botan10Extensions7replaceEPNS_21Certificate_ExtensionEb

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004ede80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md) · 呼出先 1件 [`004ee4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee4f4.md)
- 新版 呼出元 1件 [`00510d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md) · 呼出先 1件 [`0051138c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcee4",
      "READ",
      [
        "storage",
        "00c1d028",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdceec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0051138c"
      ]
    ]
  ],
  "added": [
    [
      "00c59934",
      "READ",
      [
        "storage",
        "00c9ca58",
        null,
        "pointer"
      ]
    ],
    [
      "00c5993c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0051138c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcee0.md#insn-00bdcee0) · [`00bdcee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcee0.md#insn-00bdcee4) · [`00bdcee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcee0.md#insn-00bdcee8)

~~~diff
- 00bdcee0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdcee0 bytes 100200b0
- 00bdcee4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:28:8"]]
- 00bdcee4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcee4 bytes 111640f9
- 00bdcee8 ["COPY", "tmp:0:8", ["const:28:8"]]
- 00bdcee8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcee8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcee8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcee8 bytes 10a20091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fc00d401f3e4be2415363d19f06d798"></a>

### [`00bdcf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf50.md) → [`00c599a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599a0.md) _ZNK5Botan8X509_CRL10is_revokedERKNS_16X509_CertificateE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005054cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00505/005054cc.md) · 呼出先 1件 [`004f00b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f00b0.md)
- 新版 呼出元 1件 [`00528364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528364.md) · 呼出先 1件 [`00512f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512f48.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcf54",
      "READ",
      [
        "storage",
        "00c1d060",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcf5c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00512f48"
      ]
    ]
  ],
  "added": [
    [
      "00c599a4",
      "READ",
      [
        "storage",
        "00c9ca90",
        null,
        "pointer"
      ]
    ],
    [
      "00c599ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00512f48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf50.md#insn-00bdcf50) · [`00bdcf54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf50.md#insn-00bdcf54) · [`00bdcf58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf50.md#insn-00bdcf58)

~~~diff
- 00bdcf50 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdcf50 bytes 100200b0
- 00bdcf54 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:60:8"]]
- 00bdcf54 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcf54 bytes 113240f9
- 00bdcf58 ["COPY", "tmp:0:8", ["const:60:8"]]
- 00bdcf58 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf58 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf58 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcf58 bytes 10820191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d71f0f1608c9bcbcfa71caa927c15d25"></a>

### [`00bdcf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf60.md) → [`00c599b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599b0.md) _ZNK5Botan14Cert_Extension10CRL_Number14get_crl_numberEv

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004f03d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f03d8.md) · 呼出先 1件 [`004fa788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fa/004fa788.md)
- 新版 呼出元 1件 [`00513270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md) · 呼出先 1件 [`0051d620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d620.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcf64",
      "READ",
      [
        "storage",
        "00c1d068",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcf6c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0051d620"
      ]
    ]
  ],
  "added": [
    [
      "00c599b4",
      "READ",
      [
        "storage",
        "00c9ca98",
        null,
        "pointer"
      ]
    ],
    [
      "00c599bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0051d620"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf60.md#insn-00bdcf60) · [`00bdcf64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf60.md#insn-00bdcf64) · [`00bdcf68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf60.md#insn-00bdcf68)

~~~diff
- 00bdcf60 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdcf60 bytes 100200b0
- 00bdcf64 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:68:8"]]
- 00bdcf64 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcf64 bytes 113640f9
- 00bdcf68 ["COPY", "tmp:0:8", ["const:68:8"]]
- 00bdcf68 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf68 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf68 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcf68 bytes 10a20191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39dc34d02ffea0170aa6f508725a72f5"></a>

### [`00bdd000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd000.md) → [`00c59a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a50.md) _ZNK5Botan16X509_Certificate11is_criticalERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004f8244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8244.md) · 呼出先 1件 [`004f8990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8990.md)
- 新版 呼出元 1件 [`0051b0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b0dc.md) · 呼出先 1件 [`0051b828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b828.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd004",
      "READ",
      [
        "storage",
        "00c1d0b8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd00c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0051b828"
      ]
    ]
  ],
  "added": [
    [
      "00c59a54",
      "READ",
      [
        "storage",
        "00c9cae8",
        null,
        "pointer"
      ]
    ],
    [
      "00c59a5c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0051b828"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd000.md#insn-00bdd000) · [`00bdd004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd000.md#insn-00bdd004) · [`00bdd008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd000.md#insn-00bdd008)

~~~diff
- 00bdd000 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd000 bytes 10020090
- 00bdd004 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b8:8"]]
- 00bdd004 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd004 bytes 115e40f9
- 00bdd008 ["COPY", "tmp:0:8", ["const:b8:8"]]
- 00bdd008 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd008 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd008 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd008 bytes 10e20291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b86f37fa584793753a47de28cf08697f"></a>

### [`00bdd030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd030.md) → [`00c59a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a80.md) _ZNK5Botan11X509_Object10BER_encodeEv

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`004fc5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc5bc.md) [`0050168c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/0050168c.md) [`0050645c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/0050645c.md) [`00506ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506ee0.md) · 呼出先 1件 [`004fc4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc4b0.md)
- 新版 呼出元 4件 [`0051f454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f454.md) [`00524524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/00524524.md) [`005292f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/005292f4.md) [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) · 呼出先 1件 [`0051f348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f348.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd034",
      "READ",
      [
        "storage",
        "00c1d0d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd03c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0051f348"
      ]
    ]
  ],
  "added": [
    [
      "00c59a84",
      "READ",
      [
        "storage",
        "00c9cb00",
        null,
        "pointer"
      ]
    ],
    [
      "00c59a8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0051f348"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd030.md#insn-00bdd030) · [`00bdd034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd030.md#insn-00bdd034) · [`00bdd038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd030.md#insn-00bdd038)

~~~diff
- 00bdd030 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd030 bytes 10020090
- 00bdd034 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:d0:8"]]
- 00bdd034 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd034 bytes 116a40f9
- 00bdd038 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 00bdd038 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd038 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd038 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd038 bytes 10420391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-943cf3bd27fa00e7b82a6b4ebb68f8dc"></a>

### [`00bdd090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd090.md) → [`00c59ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ae0.md) _ZN5Botan4PKIX11check_chainERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEENS1_6chrono10time_pointINSC_

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00508860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508860.md) · 呼出先 1件 [`00503af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503af8.md)
- 新版 呼出元 1件 [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) · 呼出先 1件 [`00526990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526990.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd094",
      "READ",
      [
        "storage",
        "00c1d100",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd09c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00526990"
      ]
    ]
  ],
  "added": [
    [
      "00c59ae4",
      "READ",
      [
        "storage",
        "00c9cb30",
        null,
        "pointer"
      ]
    ],
    [
      "00c59aec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00526990"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd090.md#insn-00bdd090) · [`00bdd094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd090.md#insn-00bdd094) · [`00bdd098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd090.md#insn-00bdd098)

~~~diff
- 00bdd090 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd090 bytes 10020090
- 00bdd094 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:100:8"]]
- 00bdd094 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd094 bytes 118240f9
- 00bdd098 ["COPY", "tmp:0:8", ["const:100:8"]]
- 00bdd098 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd098 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd098 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd098 bytes 10020491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5e17756edfa209e63338931652558f1"></a>

### [`00bdd0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0b0.md) → [`00c59b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b00.md) _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_8X509_CRLEEENS7

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005060a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/005060a8.md) · 呼出先 1件 [`005054cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00505/005054cc.md)
- 新版 呼出元 1件 [`00528f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528f40.md) · 呼出先 1件 [`00528364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528364.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd0b4",
      "READ",
      [
        "storage",
        "00c1d110",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd0bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00528364"
      ]
    ]
  ],
  "added": [
    [
      "00c59b04",
      "READ",
      [
        "storage",
        "00c9cb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c59b0c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00528364"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0b0.md#insn-00bdd0b0) · [`00bdd0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0b0.md#insn-00bdd0b4) · [`00bdd0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0b0.md#insn-00bdd0b8)

~~~diff
- 00bdd0b0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd0b0 bytes 10020090
- 00bdd0b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:110:8"]]
- 00bdd0b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd0b4 bytes 118a40f9
- 00bdd0b8 ["COPY", "tmp:0:8", ["const:110:8"]]
- 00bdd0b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd0b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd0b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd0b8 bytes 10420491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34687c77a3f681a35c083ca564898855"></a>

### [`00bdd270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd270.md) → [`00c59cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cc0.md) _ZNSt6__ndk115recursive_mutexC1Ev

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0054841c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/0054841c.md) · 呼出先 1件 [`00b7d334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d334.md)
- 新版 呼出元 1件 [`0056b2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b2b4.md) · 呼出先 1件 [`00bf9d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d7c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd274",
      "READ",
      [
        "storage",
        "00c1d1f0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd27c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf9d7c"
      ]
    ]
  ],
  "added": [
    [
      "00c59cc4",
      "READ",
      [
        "storage",
        "00c9cc20",
        null,
        "pointer"
      ]
    ],
    [
      "00c59ccc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf9d7c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd270.md#insn-00bdd270) · [`00bdd274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd270.md#insn-00bdd274) · [`00bdd278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd270.md#insn-00bdd278)

~~~diff
- 00bdd270 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd270 bytes 10020090
- 00bdd274 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1f0:8"]]
- 00bdd274 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd274 bytes 11fa40f9
- 00bdd278 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 00bdd278 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd278 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd278 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd278 bytes 10c20791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ccee084ed2564c316c0eb6988c741c0"></a>

### [`00bdd290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd290.md) → [`00c59ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ce0.md) _ZNSt6__ndk115recursive_mutex4lockEv

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`005487f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005487f8.md) [`005488c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005488c4.md) [`00548a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548a34.md) [`00548b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548b4c.md) [`00549364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549364.md) · 呼出先 1件 [`00b7d3f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3f8.md)
- 新版 呼出元 6件 [`0056b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md) [`0056b75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b75c.md) [`0056b8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md) [`0056b9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md) [`0056c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c1fc.md) · 呼出先 1件 [`00bf9e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e40.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd294",
      "READ",
      [
        "storage",
        "00c1d200",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd29c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf9e40"
      ]
    ]
  ],
  "added": [
    [
      "00c59ce4",
      "READ",
      [
        "storage",
        "00c9cc30",
        null,
        "pointer"
      ]
    ],
    [
      "00c59cec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf9e40"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd290.md#insn-00bdd290) · [`00bdd294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd290.md#insn-00bdd294) · [`00bdd298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd290.md#insn-00bdd298)

~~~diff
- 00bdd290 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd290 bytes 10020090
- 00bdd294 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:200:8"]]
- 00bdd294 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd294 bytes 110241f9
- 00bdd298 ["COPY", "tmp:0:8", ["const:200:8"]]
- 00bdd298 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd298 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd298 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd298 bytes 10020891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1a9497664c41f29503dbf46491f7369"></a>

### [`00bdd2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2a0.md) → [`00c59cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cf0.md) _ZNSt6__ndk115recursive_mutex6unlockEv

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`005487f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005487f8.md) [`005488c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005488c4.md) [`00548a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548a34.md) [`00548b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548b4c.md) [`00549364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549364.md) · 呼出先 1件 [`00b7d424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d424.md)
- 新版 呼出元 6件 [`0056b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b690.md) [`0056b75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b75c.md) [`0056b8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b8cc.md) [`0056b9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b9e4.md) [`0056c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c1fc.md) · 呼出先 1件 [`00bf9e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e6c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd2a4",
      "READ",
      [
        "storage",
        "00c1d208",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd2ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf9e6c"
      ]
    ]
  ],
  "added": [
    [
      "00c59cf4",
      "READ",
      [
        "storage",
        "00c9cc38",
        null,
        "pointer"
      ]
    ],
    [
      "00c59cfc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf9e6c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2a0.md#insn-00bdd2a0) · [`00bdd2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2a0.md#insn-00bdd2a4) · [`00bdd2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2a0.md#insn-00bdd2a8)

~~~diff
- 00bdd2a0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd2a0 bytes 10020090
- 00bdd2a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:208:8"]]
- 00bdd2a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd2a4 bytes 110641f9
- 00bdd2a8 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00bdd2a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd2a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd2a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd2a8 bytes 10220891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36a6d6dac9f110619c3c292ae616bbf7"></a>

### [`00bdd2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2d0.md) → [`00c59d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d20.md) &lt;EXTERNAL&gt;::sincos

採用 · 移動量 `+0x7ca50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0054cec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054cec8.md) [`00a17d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a17/00a17d24.md) · 呼出先 1件 [`010a5248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5248.md)
- 新版 呼出元 2件 [`0056fd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fd60.md) [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · 呼出先 1件 [`0112a248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a248.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd2d4",
      "READ",
      [
        "storage",
        "00c1d220",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd2dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a248"
      ]
    ]
  ],
  "added": [
    [
      "00c59d24",
      "READ",
      [
        "storage",
        "00c9cc50",
        null,
        "pointer"
      ]
    ],
    [
      "00c59d2c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a248"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2d0.md#insn-00bdd2d0) · [`00bdd2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2d0.md#insn-00bdd2d4) · [`00bdd2d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2d0.md#insn-00bdd2d8)

~~~diff
- 00bdd2d0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd2d0 bytes 10020090
- 00bdd2d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:220:8"]]
- 00bdd2d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd2d4 bytes 111241f9
- 00bdd2d8 ["COPY", "tmp:0:8", ["const:220:8"]]
- 00bdd2d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd2d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd2d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd2d8 bytes 10820891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-907d368f92b7fc9695200e7b5fb16943"></a>

### [`00bdd320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd320.md) → [`00c59d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d70.md) &lt;EXTERNAL&gt;::AAsset_getRemainingLength

採用 · 移動量 `+0x7ca50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00559f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559f90.md) [`0055a254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a254.md) · 呼出先 1件 [`010a5270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5270.md)
- 新版 呼出元 2件 [`0057ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057ce28.md) [`0057d0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d0ec.md) · 呼出先 1件 [`0112a270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a270.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd324",
      "READ",
      [
        "storage",
        "00c1d248",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd32c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a270"
      ]
    ]
  ],
  "added": [
    [
      "00c59d74",
      "READ",
      [
        "storage",
        "00c9cc78",
        null,
        "pointer"
      ]
    ],
    [
      "00c59d7c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a270"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd320.md#insn-00bdd320) · [`00bdd324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd320.md#insn-00bdd324) · [`00bdd328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd320.md#insn-00bdd328)

~~~diff
- 00bdd320 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd320 bytes 10020090
- 00bdd324 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:248:8"]]
- 00bdd324 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd324 bytes 112641f9
- 00bdd328 ["COPY", "tmp:0:8", ["const:248:8"]]
- 00bdd328 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd328 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd328 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd328 bytes 10220991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a4f0ace95a6598f59a63b1ce6e90c1a"></a>

### [`00bdd470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd470.md) → [`00c59ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ec0.md) &lt;EXTERNAL&gt;::AndroidBitmap_lockPixels

採用 · 移動量 `+0x7ca50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0055c994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c994.md) [`0055d5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d5cc.md) · 呼出先 1件 [`010a5310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5310.md)
- 新版 呼出元 2件 [`0057f82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f82c.md) [`00580464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580464.md) · 呼出先 1件 [`0112a310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a310.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd474",
      "READ",
      [
        "storage",
        "00c1d2f0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd47c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a310"
      ]
    ]
  ],
  "added": [
    [
      "00c59ec4",
      "READ",
      [
        "storage",
        "00c9cd20",
        null,
        "pointer"
      ]
    ],
    [
      "00c59ecc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a310"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd470.md#insn-00bdd470) · [`00bdd474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd470.md#insn-00bdd474) · [`00bdd478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd470.md#insn-00bdd478)

~~~diff
- 00bdd470 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd470 bytes 10020090
- 00bdd474 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2f0:8"]]
- 00bdd474 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd474 bytes 117a41f9
- 00bdd478 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 00bdd478 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd478 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd478 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd478 bytes 10c20b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32f3c694098c93613ffad0121cf43cc6"></a>

### [`00bdd500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd500.md) → [`00c59f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f50.md) &lt;EXTERNAL&gt;::__android_log_write

採用 · 移動量 `+0x7ca50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0056c3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c3ac.md) · 呼出先 1件 [`010a5350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5350.md)
- 新版 呼出元 1件 [`0058f244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f244.md) · 呼出先 1件 [`0112a350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a350.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd504",
      "READ",
      [
        "storage",
        "00c1d338",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd50c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a350"
      ]
    ]
  ],
  "added": [
    [
      "00c59f54",
      "READ",
      [
        "storage",
        "00c9cd68",
        null,
        "pointer"
      ]
    ],
    [
      "00c59f5c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a350"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd500.md#insn-00bdd500) · [`00bdd504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd500.md#insn-00bdd504) · [`00bdd508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd500.md#insn-00bdd508)

~~~diff
- 00bdd500 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd500 bytes 10020090
- 00bdd504 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:338:8"]]
- 00bdd504 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd504 bytes 119e41f9
- 00bdd508 ["COPY", "tmp:0:8", ["const:338:8"]]
- 00bdd508 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd508 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd508 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd508 bytes 10e20c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daabd6c9d252dade20f3309c35ef3358"></a>

### [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md) → [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_

採用 · 移動量 `+0x7ca80` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 44件 [`00af7cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7cd0.md) [`00afa474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa474.md) [`00afd108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd108.md) [`00b01950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01950.md) [`00b0abe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0abe8.md) · 呼出先 1件 [`00af7b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7b0c.md)
- 新版 呼出元 50件 [`00b57a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57a54.md) [`00b5a1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a1f8.md) [`00b5ce8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5ce8c.md) [`00b61584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61584.md) [`00b6abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6abd0.md) · 呼出先 1件 [`00b57890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57890.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde734",
      "READ",
      [
        "storage",
        "00c1dc50",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde73c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b57890"
      ]
    ]
  ],
  "added": [
    [
      "00c5b1b4",
      "READ",
      [
        "storage",
        "00c9d698",
        null,
        "pointer"
      ]
    ],
    [
      "00c5b1bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b57890"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md#insn-00bde730) · [`00bde734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md#insn-00bde734) · [`00bde738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md#insn-00bde738)

~~~diff
- 00bde730 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde730 bytes f00100f0
- 00bde734 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c50:8"]]
- 00bde734 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde734 bytes 112a46f9
- 00bde738 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 00bde738 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde738 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde738 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde738 bytes 10423191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9710b93356cee83c0f692ab99dd5c95c"></a>

### [`00bde7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7a0.md) → [`00c5b220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b220.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE21__push_back_slow_pathIS2_EEvOT_

採用 · 移動量 `+0x7ca80` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00af38a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af38a8.md) [`00af52d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af52d8.md) · 呼出先 1件 [`00af7f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7f80.md)
- 新版 呼出元 2件 [`00b5362c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b5362c.md) [`00b5505c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b5505c.md) · 呼出先 1件 [`00b57d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57d04.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde7a4",
      "READ",
      [
        "storage",
        "00c1dc88",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde7ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b57d04"
      ]
    ]
  ],
  "added": [
    [
      "00c5b224",
      "READ",
      [
        "storage",
        "00c9d6d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c5b22c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b57d04"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7a0.md#insn-00bde7a0) · [`00bde7a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7a0.md#insn-00bde7a4) · [`00bde7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7a0.md#insn-00bde7a8)

~~~diff
- 00bde7a0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde7a0 bytes f00100f0
- 00bde7a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c88:8"]]
- 00bde7a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde7a4 bytes 114646f9
- 00bde7a8 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00bde7a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde7a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde7a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde7a8 bytes 10223291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5550c3605c9afc67c015f835db043b4"></a>

### [`00bde7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7d0.md) → [`00c5b250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b250.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIS6_EEvOT_

採用 · 移動量 `+0x7ca80` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`00af32bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af32bc.md) [`00af35a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af35a4.md) [`00afd888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd888.md) [`00b02544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02544.md) [`00b0e73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e73c.md) · 呼出先 1件 [`00af7e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7e20.md)
- 新版 呼出元 15件 [`00b53040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53040.md) [`00b53328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53328.md) [`00b5d60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d60c.md) [`00b62178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62178.md) [`00b6f690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f690.md) · 呼出先 1件 [`00b57ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57ba4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde7d4",
      "READ",
      [
        "storage",
        "00c1dca0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde7dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b57ba4"
      ]
    ]
  ],
  "added": [
    [
      "00c5b254",
      "READ",
      [
        "storage",
        "00c9d6e8",
        null,
        "pointer"
      ]
    ],
    [
      "00c5b25c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b57ba4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7d0.md#insn-00bde7d0) · [`00bde7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7d0.md#insn-00bde7d4) · [`00bde7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7d0.md#insn-00bde7d8)

~~~diff
- 00bde7d0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde7d0 bytes f00100f0
- 00bde7d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ca0:8"]]
- 00bde7d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde7d4 bytes 115246f9
- 00bde7d8 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00bde7d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde7d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde7d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde7d8 bytes 10823291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-610b048c4d326ec9b7f4e51e78953a07"></a>

### [`00bde810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde810.md) → [`00c5b290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b290.md) &lt;EXTERNAL&gt;::pthread_mutex_destroy

採用 · 移動量 `+0x7ca80` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00af0c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0c38.md) [`00b05490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05490.md) [`00b4ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4ced4.md) [`00b7d2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2a0.md) [`00b7d334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d334.md) · 呼出先 1件 [`010a5598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5598.md)
- 新版 呼出元 6件 [`00b509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b509bc.md) [`00b650e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b650e8.md) [`00bbac30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbac30.md) [`00bf9ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ce8.md) [`00bf9d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d7c.md) · 呼出先 1件 [`0112a598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a598.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde814",
      "READ",
      [
        "storage",
        "00c1dcc0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde81c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a598"
      ]
    ]
  ],
  "added": [
    [
      "00c5b294",
      "READ",
      [
        "storage",
        "00c9d708",
        null,
        "pointer"
      ]
    ],
    [
      "00c5b29c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a598"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde810.md#insn-00bde810) · [`00bde814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde810.md#insn-00bde814) · [`00bde818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde810.md#insn-00bde818)

~~~diff
- 00bde810 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde810 bytes f00100f0
- 00bde814 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:cc0:8"]]
- 00bde814 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde814 bytes 116246f9
- 00bde818 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 00bde818 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde818 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde818 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde818 bytes 10023391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c92be308d2f37e004ca1ba868179f414"></a>

### [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) → [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) &lt;EXTERNAL&gt;::pthread_mutex_lock

採用 · 移動量 `+0x7ca80` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 22件 [`00af0c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0c38.md) [`00af1364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1364.md) [`00af5cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5cf8.md) [`00af5f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5f00.md) [`00b054b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b054b8.md) · 呼出先 1件 [`010a55a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a55a0.md)
- 新版 呼出元 22件 [`00b509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b509bc.md) [`00b510e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b510e8.md) [`00b55a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55a7c.md) [`00b55c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55c84.md) [`00b65110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65110.md) · 呼出先 1件 [`0112a5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a5a0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde824",
      "READ",
      [
        "storage",
        "00c1dcc8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde82c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a5a0"
      ]
    ]
  ],
  "added": [
    [
      "00c5b2a4",
      "READ",
      [
        "storage",
        "00c9d710",
        null,
        "pointer"
      ]
    ],
    [
      "00c5b2ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a5a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md#insn-00bde820) · [`00bde824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md#insn-00bde824) · [`00bde828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md#insn-00bde828)

~~~diff
- 00bde820 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde820 bytes f00100f0
- 00bde824 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:cc8:8"]]
- 00bde824 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde824 bytes 116646f9
- 00bde828 ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 00bde828 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde828 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde828 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde828 bytes 10223391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a805fd5dad047b27747485130d061510"></a>

### [`00bde8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8b0.md) → [`00c5b330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b330.md) _ZN8firebase10app_common16IsDefaultAppNameEPKc

採用 · 移動量 `+0x7ca80` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b06d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md) · 呼出先 1件 [`00af9340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9340.md)
- 新版 呼出元 1件 [`00b6697c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6697c.md) · 呼出先 1件 [`00b590c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b590c4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde8b4",
      "READ",
      [
        "storage",
        "00c1dd10",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde8bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b590c4"
      ]
    ]
  ],
  "added": [
    [
      "00c5b334",
      "READ",
      [
        "storage",
        "00c9d758",
        null,
        "pointer"
      ]
    ],
    [
      "00c5b33c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b590c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8b0.md#insn-00bde8b0) · [`00bde8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8b0.md#insn-00bde8b4) · [`00bde8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8b0.md#insn-00bde8b8)

~~~diff
- 00bde8b0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde8b0 bytes f00100f0
- 00bde8b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:d10:8"]]
- 00bde8b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde8b4 bytes 118a46f9
- 00bde8b8 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 00bde8b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde8b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde8b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde8b8 bytes 10423491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84dccc6e21437e56c9a13adc704af748"></a>

### [`00bde8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8c0.md) → [`00c5b340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b340.md) _ZN8firebase10app_common16RegisterSdkUsageEPv

採用 · 移動量 `+0x7ca80` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b06d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md) · 呼出先 1件 [`00afa2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa2e4.md)
- 新版 呼出元 1件 [`00b6697c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6697c.md) · 呼出先 1件 [`00b5a068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a068.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde8c4",
      "READ",
      [
        "storage",
        "00c1dd18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde8cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b5a068"
      ]
    ]
  ],
  "added": [
    [
      "00c5b344",
      "READ",
      [
        "storage",
        "00c9d760",
        null,
        "pointer"
      ]
    ],
    [
      "00c5b34c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b5a068"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8c0.md#insn-00bde8c0) · [`00bde8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8c0.md#insn-00bde8c4) · [`00bde8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8c0.md#insn-00bde8c8)

~~~diff
- 00bde8c0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde8c0 bytes f00100f0
- 00bde8c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:d18:8"]]
- 00bde8c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde8c4 bytes 118e46f9
- 00bde8c8 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 00bde8c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde8c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde8c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde8c8 bytes 10623491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b45fa4e64929e027fa409fb140620cd"></a>

### [`00bde980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde980.md) → [`00c5b400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b400.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x7ca80` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00af8e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8e94.md) · 呼出先 1件 [`00afabb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afabb0.md)
- 新版 呼出元 1件 [`00b58c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58c18.md) · 呼出先 1件 [`00b5a934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a934.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde984",
      "READ",
      [
        "storage",
        "00c1dd78",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde98c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b5a934"
      ]
    ]
  ],
  "added": [
    [
      "00c5b404",
      "READ",
      [
        "storage",
        "00c9d7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00c5b40c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b5a934"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde980.md#insn-00bde980) · [`00bde984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde980.md#insn-00bde984) · [`00bde988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde980.md#insn-00bde988)

~~~diff
- 00bde980 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde980 bytes f00100f0
- 00bde984 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:d78:8"]]
- 00bde984 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde984 bytes 11be46f9
- 00bde988 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00bde988 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde988 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde988 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde988 bytes 10e23591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27bbd82491eac5db563ccfaccffab8df"></a>

### [`00bde9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9a0.md) → [`00c5b420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b420.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x7ca80` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00af9594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9594.md) · 呼出先 1件 [`00afaecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaecc.md)
- 新版 呼出元 1件 [`00b59318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59318.md) · 呼出先 1件 [`00b5ac50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ac50.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde9a4",
      "READ",
      [
        "storage",
        "00c1dd88",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde9ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b5ac50"
      ]
    ]
  ],
  "added": [
    [
      "00c5b424",
      "READ",
      [
        "storage",
        "00c9d7d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c5b42c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b5ac50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9a0.md#insn-00bde9a0) · [`00bde9a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9a0.md#insn-00bde9a4) · [`00bde9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9a0.md#insn-00bde9a8)

~~~diff
- 00bde9a0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde9a0 bytes f00100f0
- 00bde9a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:d88:8"]]
- 00bde9a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde9a4 bytes 11c646f9
- 00bde9a8 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 00bde9a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde9a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde9a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde9a8 bytes 10223691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dc4d3dad5a5a7bf984946a01a5a09be"></a>

### [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md) → [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md) &lt;EXTERNAL&gt;::strcmp

採用 · 移動量 `+0x7ca80` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 28件 [`00af8e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8e94.md) [`00af9340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9340.md) [`00b0376c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b0376c.md) [`00b03ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03ce8.md) [`00b12820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12820.md) · 呼出先 1件 [`010a55b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a55b8.md)
- 新版 呼出元 28件 [`00b58c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58c18.md) [`00b590c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b590c4.md) [`00b633c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b63/00b633c4.md) [`00b63940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b63/00b63940.md) [`00b72b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b72b34.md) · 呼出先 1件 [`0112a5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a5b8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde9d4",
      "READ",
      [
        "storage",
        "00c1dda0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde9dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a5b8"
      ]
    ]
  ],
  "added": [
    [
      "00c5b454",
      "READ",
      [
        "storage",
        "00c9d7e8",
        null,
        "pointer"
      ]
    ],
    [
      "00c5b45c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a5b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md#insn-00bde9d0) · [`00bde9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md#insn-00bde9d4) · [`00bde9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md#insn-00bde9d8)

~~~diff
- 00bde9d0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde9d0 bytes f00100f0
- 00bde9d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:da0:8"]]
- 00bde9d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde9d4 bytes 11d246f9
- 00bde9d8 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00bde9d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde9d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde9d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde9d8 bytes 10823691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da4838b8e8979b15f707426d08f8edb0"></a>

### [`00bdee10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee10.md) → [`00c5b8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b8c0.md) _ZN8firebase26ReferenceCountedFutureImpl18ForceReleaseFutureERKNS_12FutureHandleE

採用 · 移動量 `+0x7cab0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00afe7a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe7a4.md) · 呼出先 1件 [`00b00bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00bb4.md)
- 新版 呼出元 1件 [`00b5e528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e528.md) · 呼出先 1件 [`00b60938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60938.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdee14",
      "READ",
      [
        "storage",
        "00c1dfc0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdee1c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b60938"
      ]
    ]
  ],
  "added": [
    [
      "00c5b8c4",
      "READ",
      [
        "storage",
        "00c9da20",
        null,
        "pointer"
      ]
    ],
    [
      "00c5b8cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b60938"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdee10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee10.md#insn-00bdee10) · [`00bdee14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee10.md#insn-00bdee14) · [`00bdee18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee10.md#insn-00bdee18)

~~~diff
- 00bdee10 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdee10 bytes f00100f0
- 00bdee14 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fc0:8"]]
- 00bdee14 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdee14 bytes 11e247f9
- 00bdee18 ["COPY", "tmp:0:8", ["const:fc0:8"]]
- 00bdee18 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdee18 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdee18 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdee18 bytes 10023f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb8f12fcf585068d1326d966c85f1920"></a>

### [`00bdee80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee80.md) → [`00c5b930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b930.md) _ZN8firebase16StaticFutureData22GetFutureDataForModuleEPKvi

採用 · 移動量 `+0x7cab0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b5c88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c88c.md) · 呼出先 1件 [`00b02374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02374.md)
- 新版 呼出元 1件 [`00bcbd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbd8c.md) · 呼出先 1件 [`00b61fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61fa8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdee84",
      "READ",
      [
        "storage",
        "00c1dff8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdee8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b61fa8"
      ]
    ]
  ],
  "added": [
    [
      "00c5b934",
      "READ",
      [
        "storage",
        "00c9da58",
        null,
        "pointer"
      ]
    ],
    [
      "00c5b93c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b61fa8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdee80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee80.md#insn-00bdee80) · [`00bdee84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee80.md#insn-00bdee84) · [`00bdee88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee80.md#insn-00bdee88)

~~~diff
- 00bdee80 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdee80 bytes f00100f0
- 00bdee84 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ff8:8"]]
- 00bdee84 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdee84 bytes 11fe47f9
- 00bdee88 ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 00bdee88 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdee88 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdee88 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdee88 bytes 10e23f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-575975bf1c86df25bf604f732bf2d1fb"></a>

### [`00bdef80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef80.md) → [`00c5ba30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba30.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE6assignIPS2_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constru

採用 · 移動量 `+0x7cab0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b02ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ec0.md) · 呼出先 1件 [`00b04dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04dc0.md)
- 新版 呼出元 1件 [`00b62b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62b18.md) · 呼出先 1件 [`00b64a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64a18.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdef84",
      "READ",
      [
        "storage",
        "00c1e078",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdef8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b64a18"
      ]
    ]
  ],
  "added": [
    [
      "00c5ba34",
      "READ",
      [
        "storage",
        "00c9dad8",
        null,
        "pointer"
      ]
    ],
    [
      "00c5ba3c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b64a18"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdef80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef80.md#insn-00bdef80) · [`00bdef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef80.md#insn-00bdef84) · [`00bdef88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef80.md#insn-00bdef88)

~~~diff
- 00bdef80 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdef80 bytes 10020090
- 00bdef84 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:78:8"]]
- 00bdef84 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdef84 bytes 113e40f9
- 00bdef88 ["COPY", "tmp:0:8", ["const:78:8"]]
- 00bdef88 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdef88 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdef88 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdef88 bytes 10e20191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-455f064b1eec743ebf10119f8dc46485"></a>

### [`00bdf250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf250.md) → [`00c5bc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc90.md) _ZN11flatbuffers11SymbolTableINS_7RPCCallEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x7ca40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b22458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22458.md) [`00b2bb3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2bb3c.md) · 呼出先 1件 [`00b22e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22e74.md)
- 新版 呼出元 2件 [`00b85fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85fbc.md) [`00b91cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91cb4.md) · 呼出先 1件 [`00b86bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86bd4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf254",
      "READ",
      [
        "storage",
        "00c1e1e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf25c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b86bd4"
      ]
    ]
  ],
  "added": [
    [
      "00c5bc94",
      "READ",
      [
        "storage",
        "00c9dc08",
        null,
        "pointer"
      ]
    ],
    [
      "00c5bc9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b86bd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf250.md#insn-00bdf250) · [`00bdf254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf250.md#insn-00bdf254) · [`00bdf258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf250.md#insn-00bdf258)

~~~diff
- 00bdf250 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf250 bytes f00100f0
- 00bdf254 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1e0:8"]]
- 00bdf254 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf254 bytes 11f240f9
- 00bdf258 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 00bdf258 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf258 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf258 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf258 bytes 10820791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9355bc402060ec185eb8efb6861bacc7"></a>

### [`00bdf2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2f0.md) → [`00c5bd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bd00.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE3EaEENS_12CheckedErrorEPli

採用 · 移動量 `+0x7ca10` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2efb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2efb4.md) · 呼出先 1件 [`00b2f5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f5b8.md)
- 新版 呼出元 1件 [`00b96330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96330.md) · 呼出先 1件 [`00b96934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b96934.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf2f4",
      "READ",
      [
        "storage",
        "00c1e230",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf2fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b96934"
      ]
    ]
  ],
  "added": [
    [
      "00c5bd04",
      "READ",
      [
        "storage",
        "00c9dc40",
        null,
        "pointer"
      ]
    ],
    [
      "00c5bd0c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b96934"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2f0.md#insn-00bdf2f0) · [`00bdf2f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2f0.md#insn-00bdf2f4) · [`00bdf2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2f0.md#insn-00bdf2f8)

~~~diff
- 00bdf2f0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf2f0 bytes f00100f0
- 00bdf2f4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:230:8"]]
- 00bdf2f4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf2f4 bytes 111a41f9
- 00bdf2f8 ["COPY", "tmp:0:8", ["const:230:8"]]
- 00bdf2f8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf2f8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf2f8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf2f8 bytes 10c20891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb0a334c9ca58f5af8edaf79ac55391a"></a>

### [`00bdf5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5f0.md) → [`00c5bdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bdc0.md) _ZN11flatbuffers19StringToIntegerImplImEEbPT_PKcib

採用 · 移動量 `+0x7c7d0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b14ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b14/00b14ed4.md) [`00b1bd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1bd6c.md) [`00b20bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b20bf8.md) · 呼出先 1件 [`00b2e280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2e280.md)
- 新版 呼出元 4件 [`00b76614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b76614.md) [`00b7e52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e52c.md) [`00b8420c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b8420c.md) [`00baaae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baa/00baaae4.md) · 呼出先 1件 [`00b957ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b957ec.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf5f4",
      "READ",
      [
        "storage",
        "00c1e3b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf5fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b957ec"
      ]
    ]
  ],
  "added": [
    [
      "00c5bdc4",
      "READ",
      [
        "storage",
        "00c9dca0",
        null,
        "pointer"
      ]
    ],
    [
      "00c5bdcc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b957ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5f0.md#insn-00bdf5f0) · [`00bdf5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5f0.md#insn-00bdf5f4) · [`00bdf5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5f0.md#insn-00bdf5f8)

~~~diff
- 00bdf5f0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf5f0 bytes f00100f0
- 00bdf5f4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:3b0:8"]]
- 00bdf5f4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf5f4 bytes 11da41f9
- 00bdf5f8 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 00bdf5f8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5f8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5f8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf5f8 bytes 10c20e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16dfb017e84171829d90d85ec7a3fc75"></a>

### [`00bdfe30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfe30.md) → [`00c5c9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9c0.md) _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEbT0_SA_T_

採用 · 移動量 `+0x7cb90` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b44a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44a44.md) · 呼出先 1件 [`00b45344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45344.md)
- 新版 呼出元 1件 [`00bb0668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0668.md) · 呼出先 1件 [`00bb0f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0f68.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfe34",
      "READ",
      [
        "storage",
        "00c1e7d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdfe3c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb0f68"
      ]
    ]
  ],
  "added": [
    [
      "00c5c9c4",
      "READ",
      [
        "storage",
        "00c9e2a0",
        null,
        "pointer"
      ]
    ],
    [
      "00c5c9cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb0f68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfe30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfe30.md#insn-00bdfe30) · [`00bdfe34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfe30.md#insn-00bdfe34) · [`00bdfe38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfe30.md#insn-00bdfe38)

~~~diff
- 00bdfe30 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdfe30 bytes f00100f0
- 00bdfe34 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:7d0:8"]]
- 00bdfe34 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdfe34 bytes 11ea43f9
- 00bdfe38 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 00bdfe38 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfe38 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfe38 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdfe38 bytes 10421f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eebb3c62dd7ba953db8b5bfa81f1656"></a>

### [`00bdfeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfeb0.md) → [`00c5c9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9f0.md) _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x7cb40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b218b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b21/00b218b0.md) [`00b430c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b430c0.md) · 呼出先 1件 [`00b430c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b430c0.md)
- 新版 呼出元 2件 [`00b85014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b85/00b85014.md) [`00baea00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00baea00.md) · 呼出先 1件 [`00baea00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00baea00.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfeb4",
      "READ",
      [
        "storage",
        "00c1e810",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdfebc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00baea00"
      ]
    ]
  ],
  "added": [
    [
      "00c5c9f4",
      "READ",
      [
        "storage",
        "00c9e2b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c5c9fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00baea00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfeb0.md#insn-00bdfeb0) · [`00bdfeb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfeb0.md#insn-00bdfeb4) · [`00bdfeb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfeb0.md#insn-00bdfeb8)

~~~diff
- 00bdfeb0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdfeb0 bytes f00100f0
- 00bdfeb4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:810:8"]]
- 00bdfeb4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdfeb4 bytes 110a44f9
- 00bdfeb8 ["COPY", "tmp:0:8", ["const:810:8"]]
- 00bdfeb8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfeb8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfeb8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdfeb8 bytes 10422091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eec06a8b87871c8cc16e5be076e05f35"></a>

### [`00be00d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00d0.md) → [`00c5cc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc70.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertENS_11__wrap_iterIPKhEEmRS5_

採用 · 移動量 `+0x7cba0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b262d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b262d0.md) [`00b32148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b32/00b32148.md) [`00b33c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33c60.md) · 呼出先 1件 [`00b333a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b333a0.md)
- 新版 呼出元 3件 [`00b8af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8af50.md) [`00b995cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b995cc.md) [`00b9b2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9b2d4.md) · 呼出先 1件 [`00b9a9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9a9e4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be00d4",
      "READ",
      [
        "storage",
        "00c1e920",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be00dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b9a9e4"
      ]
    ]
  ],
  "added": [
    [
      "00c5cc74",
      "READ",
      [
        "storage",
        "00c9e3f8",
        null,
        "pointer"
      ]
    ],
    [
      "00c5cc7c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b9a9e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be00d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00d0.md#insn-00be00d0) · [`00be00d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00d0.md#insn-00be00d4) · [`00be00d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00d0.md#insn-00be00d8)

~~~diff
- 00be00d0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be00d0 bytes f00100d0
- 00be00d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:920:8"]]
- 00be00d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be00d4 bytes 119244f9
- 00be00d8 ["COPY", "tmp:0:8", ["const:920:8"]]
- 00be00d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be00d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be00d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be00d8 bytes 10822491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57df9fc17765cc53ab682339aed752f2"></a>

### [`00be0200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0200.md) → [`00c5cd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd00.md) &lt;EXTERNAL&gt;::acos

採用 · 移動量 `+0x7cb00` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e3d8.md) · 呼出先 1件 [`010a5630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5630.md)
- 新版 呼出元 1件 [`00b81344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b81/00b81344.md) · 呼出先 1件 [`0112a630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a630.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0204",
      "READ",
      [
        "storage",
        "00c1e9b8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be020c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a630"
      ]
    ]
  ],
  "added": [
    [
      "00c5cd04",
      "READ",
      [
        "storage",
        "00c9e440",
        null,
        "pointer"
      ]
    ],
    [
      "00c5cd0c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a630"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0200.md#insn-00be0200) · [`00be0204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0200.md#insn-00be0204) · [`00be0208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0200.md#insn-00be0208)

~~~diff
- 00be0200 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0200 bytes f00100d0
- 00be0204 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9b8:8"]]
- 00be0204 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0204 bytes 11de44f9
- 00be0208 ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 00be0208 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0208 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0208 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0208 bytes 10e22691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da9146796e1a80df3dfcf2cdf1a894d7"></a>

### [`00be0230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0230.md) → [`00c5cd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd30.md) &lt;EXTERNAL&gt;::strncmp

採用 · 移動量 `+0x7cb00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`00b2c808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c808.md) [`00b2c8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c8fc.md) [`00b2c9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c9a0.md) [`00b33b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33b08.md) [`00b33e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33e84.md) · 呼出先 1件 [`010a5648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5648.md)
- 新版 呼出元 9件 [`00b6f690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6f/00b6f690.md) [`00b93410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b93410.md) [`00b93520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b93520.md) [`00b935bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b93/00b935bc.md) [`00bb2d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2d04.md) · 呼出先 1件 [`0112a648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a648.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0234",
      "READ",
      [
        "storage",
        "00c1e9d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be023c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a648"
      ]
    ]
  ],
  "added": [
    [
      "00c5cd34",
      "READ",
      [
        "storage",
        "00c9e458",
        null,
        "pointer"
      ]
    ],
    [
      "00c5cd3c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a648"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0230.md#insn-00be0230) · [`00be0234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0230.md#insn-00be0234) · [`00be0238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0230.md#insn-00be0238)

~~~diff
- 00be0230 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0230 bytes f00100d0
- 00be0234 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9d0:8"]]
- 00be0234 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0234 bytes 11ea44f9
- 00be0238 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00be0238 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0238 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0238 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0238 bytes 10422791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bba789df4799998441f308b08382ffcc"></a>

### [`00be0270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0270.md) → [`00c5cd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd80.md) _ZNKSt6__ndk16locale9has_facetERNS0_2idE

採用 · 移動量 `+0x7cb10` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b48950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48950.md) [`00b8881c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b8881c.md) · 呼出先 1件 [`00ba8740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8740.md)
- 新版 呼出元 2件 [`00bb50c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb50c0.md) [`00c05264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05264.md) · 呼出先 1件 [`00c25188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25188.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0274",
      "READ",
      [
        "storage",
        "00c1e9f0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be027c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00c25188"
      ]
    ]
  ],
  "added": [
    [
      "00c5cd84",
      "READ",
      [
        "storage",
        "00c9e480",
        null,
        "pointer"
      ]
    ],
    [
      "00c5cd8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00c25188"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0270.md#insn-00be0270) · [`00be0274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0270.md#insn-00be0274) · [`00be0278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0270.md#insn-00be0278)

~~~diff
- 00be0270 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0270 bytes f00100d0
- 00be0274 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9f0:8"]]
- 00be0274 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0274 bytes 11fa44f9
- 00be0278 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 00be0278 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0278 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0278 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0278 bytes 10c22791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-059950b90db5af5e25c5bc3b2dad6315"></a>

### [`00be0280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0280.md) → [`00c5cd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd90.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4syncEv

採用 · 移動量 `+0x7cb10` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b47b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47b9c.md) [`00b88ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ad4.md) · 呼出先 1件 [`00b47f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f74.md)
- 新版 呼出元 2件 [`00bb53e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb53e8.md) [`00c0551c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0551c.md) · 呼出先 1件 [`00bb57c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb57c0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0284",
      "READ",
      [
        "storage",
        "00c1e9f8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be028c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb57c0"
      ]
    ]
  ],
  "added": [
    [
      "00c5cd94",
      "READ",
      [
        "storage",
        "00c9e488",
        null,
        "pointer"
      ]
    ],
    [
      "00c5cd9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb57c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0280.md#insn-00be0280) · [`00be0284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0280.md#insn-00be0284) · [`00be0288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0280.md#insn-00be0288)

~~~diff
- 00be0280 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0280 bytes f00100d0
- 00be0284 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9f8:8"]]
- 00be0284 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0284 bytes 11fe44f9
- 00be0288 ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 00be0288 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0288 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0288 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0288 bytes 10e22791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e60d747d3356a427c50411a0f99c555"></a>

### [`00be0290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0290.md) → [`00c5cda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cda0.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC2Ev

採用 · 移動量 `+0x7cb10` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b465dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b465dc.md) [`00b4675c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b4675c.md) [`00b46f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46f24.md) · 呼出先 1件 [`00b48950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48950.md)
- 新版 呼出元 3件 [`00bb22e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb22e4.md) [`00bb270c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb270c.md) [`00bb2850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2850.md) · 呼出先 1件 [`00bb50c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb50c0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0294",
      "READ",
      [
        "storage",
        "00c1ea00",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be029c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb50c0"
      ]
    ]
  ],
  "added": [
    [
      "00c5cda4",
      "READ",
      [
        "storage",
        "00c9e490",
        null,
        "pointer"
      ]
    ],
    [
      "00c5cdac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb50c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0290.md#insn-00be0290) · [`00be0294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0290.md#insn-00be0294) · [`00be0298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0290.md#insn-00be0298)

~~~diff
- 00be0290 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0290 bytes f00100d0
- 00be0294 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a00:8"]]
- 00be0294 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0294 bytes 110245f9
- 00be0298 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00be0298 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0298 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0298 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0298 bytes 10022891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6fefe121507d794812aadaa8936540e"></a>

### [`00be02d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02d0.md) → [`00c5cdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdf0.md) &lt;EXTERNAL&gt;::ftello

採用 · 移動量 `+0x7cb20` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00b47e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47e44.md) · 呼出先 1件 [`010a5670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5670.md)
- 新版 呼出元 1件 [`00bb5690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5690.md) · 呼出先 1件 [`0112a678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a678.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be02d4",
      "READ",
      [
        "storage",
        "00c1ea20",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be02dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a678"
      ]
    ]
  ],
  "added": [
    [
      "00c5cdf4",
      "READ",
      [
        "storage",
        "00c9e4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c5cdfc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a678"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be02d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02d0.md#insn-00be02d0) · [`00be02d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02d0.md#insn-00be02d4) · [`00be02d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02d0.md#insn-00be02d8)

~~~diff
- 00be02d0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be02d0 bytes f00100d0
- 00be02d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a20:8"]]
- 00be02d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be02d4 bytes 111245f9
- 00be02d8 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00be02d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be02d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be02d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be02d8 bytes 10822891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07b1d3e44f2d00b69ba47e9ac03b006a"></a>

### [`00be0350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0350.md) → [`00c5cec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cec0.md) _ZN8firebase9messaging12NotificationC2ERKS1_

採用 · 移動量 `+0x7cb70` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b49b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49b10.md) · 呼出先 1件 [`00b49d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49d40.md)
- 新版 呼出元 1件 [`00bb7828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7828.md) · 呼出先 1件 [`00bb7a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7a58.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0354",
      "READ",
      [
        "storage",
        "00c1ea60",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be035c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb7a58"
      ]
    ]
  ],
  "added": [
    [
      "00c5cec4",
      "READ",
      [
        "storage",
        "00c9e520",
        null,
        "pointer"
      ]
    ],
    [
      "00c5cecc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb7a58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0350.md#insn-00be0350) · [`00be0354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0350.md#insn-00be0354) · [`00be0358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0350.md#insn-00be0358)

~~~diff
- 00be0350 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0350 bytes f00100d0
- 00be0354 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a60:8"]]
- 00be0354 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0354 bytes 113245f9
- 00be0358 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 00be0358 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0358 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0358 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0358 bytes 10822991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-731354de813bc1344a2ddc09d118425e"></a>

### [`00be0390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0390.md) → [`00c5cef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cef0.md) _ZN8firebase9messaging17NotifyListenerSetEPNS0_8ListenerE

採用 · 移動量 `+0x7cb60` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b48c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c88.md) · 呼出先 1件 [`00b4b5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b5e0.md)
- 新版 呼出元 1件 [`00bb6370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6370.md) · 呼出先 1件 [`00bb9304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9304.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0394",
      "READ",
      [
        "storage",
        "00c1ea80",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be039c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb9304"
      ]
    ]
  ],
  "added": [
    [
      "00c5cef4",
      "READ",
      [
        "storage",
        "00c9e538",
        null,
        "pointer"
      ]
    ],
    [
      "00c5cefc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb9304"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0390.md#insn-00be0390) · [`00be0394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0390.md#insn-00be0394) · [`00be0398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0390.md#insn-00be0398)

~~~diff
- 00be0390 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0390 bytes f00100d0
- 00be0394 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a80:8"]]
- 00be0394 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0394 bytes 114245f9
- 00be0398 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 00be0398 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0398 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0398 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0398 bytes 10022a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be76484822c8bee549dc8c90077a6c65"></a>

### [`00be03e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03e0.md) → [`00c5cf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf90.md) _ZN8firebase9messaging20SetListenerIfNotNullEPNS0_8ListenerE

採用 · 移動量 `+0x7cbb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4c4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4c4c4.md) · 呼出先 1件 [`00b48dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48dd0.md)
- 新版 呼出元 1件 [`00bba200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba200.md) · 呼出先 1件 [`00bb657c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb657c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be03e4",
      "READ",
      [
        "storage",
        "00c1eaa8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be03ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb657c"
      ]
    ]
  ],
  "added": [
    [
      "00c5cf94",
      "READ",
      [
        "storage",
        "00c9e588",
        null,
        "pointer"
      ]
    ],
    [
      "00c5cf9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb657c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be03e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03e0.md#insn-00be03e0) · [`00be03e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03e0.md#insn-00be03e4) · [`00be03e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03e0.md#insn-00be03e8)

~~~diff
- 00be03e0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be03e0 bytes f00100d0
- 00be03e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:aa8:8"]]
- 00be03e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be03e4 bytes 115645f9
- 00be03e8 ["COPY", "tmp:0:8", ["const:aa8:8"]]
- 00be03e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be03e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be03e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be03e8 bytes 10a22a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b0a6f1948ba0680df9a6d65ae59000e"></a>

### [`00be0400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0400.md) → [`00c5cfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cfb0.md) _ZN8firebase9messaging29NotifyListenerOnTokenReceivedEPKc

採用 · 移動量 `+0x7cbb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b4e8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e8e0.md) [`00b4ea90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ea90.md) · 呼出先 1件 [`00b48e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48e54.md)
- 新版 呼出元 2件 [`00bbcd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd30.md) [`00bbcf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcf70.md) · 呼出先 1件 [`00bb6600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6600.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0404",
      "READ",
      [
        "storage",
        "00c1eab8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be040c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb6600"
      ]
    ]
  ],
  "added": [
    [
      "00c5cfb4",
      "READ",
      [
        "storage",
        "00c9e598",
        null,
        "pointer"
      ]
    ],
    [
      "00c5cfbc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb6600"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0400.md#insn-00be0400) · [`00be0404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0400.md#insn-00be0404) · [`00be0408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0400.md#insn-00be0408)

~~~diff
- 00be0400 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0400 bytes f00100d0
- 00be0404 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ab8:8"]]
- 00be0404 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0404 bytes 115e45f9
- 00be0408 ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 00be0408 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0408 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0408 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0408 bytes 10e22a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dc71154466296245e5bbc67ecdb26cb"></a>

### [`00be0420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0420.md) → [`00c5cff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cff0.md) _ZN8firebase9messaging7MessageD2Ev

採用 · 移動量 `+0x7cbd0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00b490e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b490e4.md) [`00b4926c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4926c.md) [`00b49538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49538.md) [`00b4b8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b8c8.md) [`00b4f0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4f0f8.md) · 呼出先 1件 [`00b49650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49650.md)
- 新版 呼出元 5件 [`00bb6aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6aec.md) [`00bb6d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6d5c.md) [`00bb7250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7250.md) [`00bb95ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb95ec.md) [`00bbd624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd624.md) · 呼出先 1件 [`00bb7368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7368.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0424",
      "READ",
      [
        "storage",
        "00c1eac8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be042c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb7368"
      ]
    ]
  ],
  "added": [
    [
      "00c5cff4",
      "READ",
      [
        "storage",
        "00c9e5b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c5cffc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb7368"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0420.md#insn-00be0420) · [`00be0424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0420.md#insn-00be0424) · [`00be0428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0420.md#insn-00be0428)

~~~diff
- 00be0420 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0420 bytes f00100d0
- 00be0424 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ac8:8"]]
- 00be0424 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0424 bytes 116645f9
- 00be0428 ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 00be0428 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0428 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0428 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0428 bytes 10222b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0fc3526da3bf0515a38537ccdb813b4"></a>

### [`00be0470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0470.md) → [`00c5d040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d040.md) _ZN8firebase9messaging9TerminateEv

採用 · 移動量 `+0x7cbd0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b48bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48bd4.md) [`00b4950c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4950c.md) · 呼出先 1件 [`00b4ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4ced4.md)
- 新版 呼出元 2件 [`00bb62bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb62bc.md) [`00bb7224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7224.md) · 呼出先 1件 [`00bbac30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbac30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0474",
      "READ",
      [
        "storage",
        "00c1eaf0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be047c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bbac30"
      ]
    ]
  ],
  "added": [
    [
      "00c5d044",
      "READ",
      [
        "storage",
        "00c9e5e0",
        null,
        "pointer"
      ]
    ],
    [
      "00c5d04c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bbac30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0470.md#insn-00be0470) · [`00be0474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0470.md#insn-00be0474) · [`00be0478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0470.md#insn-00be0478)

~~~diff
- 00be0470 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0470 bytes f00100d0
- 00be0474 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:af0:8"]]
- 00be0474 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0474 bytes 117a45f9
- 00be0478 ["COPY", "tmp:0:8", ["const:af0:8"]]
- 00be0478 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0478 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0478 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0478 bytes 10c22b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48a4647e9d00da1f3485e1015dd8807d"></a>

### [`00be0480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0480.md) → [`00c5d050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d050.md) _ZNKSt6__ndk121__basic_string_commonILb1EE20__throw_out_of_rangeEv

採用 · 移動量 `+0x7cbd0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b48e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48e54.md) [`00b648d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b648d0.md) · 呼出先 1件 [`00b77d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77d18.md)
- 新版 呼出元 3件 [`00bb6600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6600.md) [`00bb67f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb67f0.md) [`00bd3dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3dd0.md) · 呼出先 1件 [`00bf4760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4760.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0484",
      "READ",
      [
        "storage",
        "00c1eaf8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be048c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf4760"
      ]
    ]
  ],
  "added": [
    [
      "00c5d054",
      "READ",
      [
        "storage",
        "00c9e5e8",
        null,
        "pointer"
      ]
    ],
    [
      "00c5d05c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf4760"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0480.md#insn-00be0480) · [`00be0484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0480.md#insn-00be0484) · [`00be0488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0480.md#insn-00be0488)

~~~diff
- 00be0480 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0480 bytes f00100d0
- 00be0484 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:af8:8"]]
- 00be0484 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0484 bytes 117e45f9
- 00be0488 ["COPY", "tmp:0:8", ["const:af8:8"]]
- 00be0488 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0488 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0488 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0488 bytes 10e22b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b0659dcc9585330d592538de7516a92"></a>

### [`00be04a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04a0.md) → [`00c5d070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d070.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageENS_9allocatorIS4_EEE10push_frontEOS4_

採用 · 移動量 `+0x7cbd0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md) · 呼出先 1件 [`00b4a6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a6dc.md)
- 新版 呼出元 1件 [`00bb7f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7f60.md) · 呼出先 1件 [`00bb83f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb83f4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be04a4",
      "READ",
      [
        "storage",
        "00c1eb08",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be04ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb83f4"
      ]
    ]
  ],
  "added": [
    [
      "00c5d074",
      "READ",
      [
        "storage",
        "00c9e5f8",
        null,
        "pointer"
      ]
    ],
    [
      "00c5d07c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb83f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be04a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04a0.md#insn-00be04a0) · [`00be04a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04a0.md#insn-00be04a4) · [`00be04a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04a0.md#insn-00be04a8)

~~~diff
- 00be04a0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be04a0 bytes f00100d0
- 00be04a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b08:8"]]
- 00be04a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be04a4 bytes 118645f9
- 00be04a8 ["COPY", "tmp:0:8", ["const:b08:8"]]
- 00be04a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be04a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be04a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be04a8 bytes 10222c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8db88190e3e48833f6b4db1b1d37bae3"></a>

### [`00be04d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04d0.md) → [`00c5d0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d0a0.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageERNS_9allocatorIS4_EEE9push_backEOS4_

採用 · 移動量 `+0x7cbd0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md) · 呼出先 1件 [`00b4a81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a81c.md)
- 新版 呼出元 1件 [`00bb7f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7f60.md) · 呼出先 1件 [`00bb8534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8534.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be04d4",
      "READ",
      [
        "storage",
        "00c1eb20",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be04dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb8534"
      ]
    ]
  ],
  "added": [
    [
      "00c5d0a4",
      "READ",
      [
        "storage",
        "00c9e610",
        null,
        "pointer"
      ]
    ],
    [
      "00c5d0ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb8534"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be04d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04d0.md#insn-00be04d0) · [`00be04d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04d0.md#insn-00be04d4) · [`00be04d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04d0.md#insn-00be04d8)

~~~diff
- 00be04d0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be04d0 bytes f00100d0
- 00be04d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b20:8"]]
- 00be04d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be04d4 bytes 119245f9
- 00be04d8 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00be04d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be04d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be04d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be04d8 bytes 10822c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7e4b046b9af1160855b860d8cdbb85b"></a>

### [`00be04e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04e0.md) → [`00c5d0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d0b0.md) _ZNSt6__ndk15dequeIN8firebase9messaging7MessageENS_9allocatorIS3_EEE19__add_back_capacityEv

採用 · 移動量 `+0x7cbd0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b490e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b490e4.md) · 呼出先 1件 [`00b4a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md)
- 新版 呼出元 1件 [`00bb6aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6aec.md) · 呼出先 1件 [`00bb7f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be04e4",
      "READ",
      [
        "storage",
        "00c1eb28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be04ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb7f60"
      ]
    ]
  ],
  "added": [
    [
      "00c5d0b4",
      "READ",
      [
        "storage",
        "00c9e618",
        null,
        "pointer"
      ]
    ],
    [
      "00c5d0bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb7f60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be04e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04e0.md#insn-00be04e0) · [`00be04e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04e0.md#insn-00be04e4) · [`00be04e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04e0.md#insn-00be04e8)

~~~diff
- 00be04e0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be04e0 bytes f00100d0
- 00be04e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b28:8"]]
- 00be04e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be04e4 bytes 119645f9
- 00be04e8 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00be04e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be04e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be04e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be04e8 bytes 10a22c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d55174cc7c7170062d6416243989f46"></a>

### [`00be04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04f0.md) → [`00c5d0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d0c0.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIPhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_

採用 · 移動量 `+0x7cbd0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b49b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49b10.md) · 呼出先 1件 [`00b49f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49f30.md)
- 新版 呼出元 1件 [`00bb7828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7828.md) · 呼出先 1件 [`00bb7c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7c48.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be04f4",
      "READ",
      [
        "storage",
        "00c1eb30",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be04fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb7c48"
      ]
    ]
  ],
  "added": [
    [
      "00c5d0c4",
      "READ",
      [
        "storage",
        "00c9e620",
        null,
        "pointer"
      ]
    ],
    [
      "00c5d0cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bb7c48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04f0.md#insn-00be04f0) · [`00be04f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04f0.md#insn-00be04f4) · [`00be04f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04f0.md#insn-00be04f8)

~~~diff
- 00be04f0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be04f0 bytes f00100d0
- 00be04f4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b30:8"]]
- 00be04f4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be04f4 bytes 119a45f9
- 00be04f8 ["COPY", "tmp:0:8", ["const:b30:8"]]
- 00be04f8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be04f8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be04f8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be04f8 bytes 10c22c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

