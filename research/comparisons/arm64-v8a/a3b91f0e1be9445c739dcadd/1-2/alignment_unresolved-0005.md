# v15.7.3 → v15.7.4 · 命令位置の検査未完了 (5)

[一覧の目次](README.md)

<a id="compare-4d78c3d2580d602897c4b6a5de4a8152"></a>

### [`00bdc660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc660.md) → [`00bdc6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6b0.md) _ZN5Botan17EMSA_PKCS1v15_RawC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004c3c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3c00.md) [`005104e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/005104e0.md) · 呼出先 1件 [`0049e24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e24c.md)
- 新版 呼出元 2件 [`004c3c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3c00.md) [`005104e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005104e0.md) · 呼出先 1件 [`0049e24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e24c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

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
        "00c1cbc0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc66c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0049e24c"
      ]
    ]
  ],
  "added": [
    [
      "00bdc6b4",
      "READ",
      [
        "storage",
        "00c1cc10",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc6bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0049e24c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc660.md#insn-00bdc660) · [`00bdc664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc660.md#insn-00bdc664) · [`00bdc668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc660.md#insn-00bdc668)

~~~diff
- 00bdc660 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc660 bytes 10020090
- 00bdc664 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:bc0:8"]]
- 00bdc664 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc664 bytes 11e245f9
- 00bdc668 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00bdc668 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc668 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc668 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc668 bytes 10022f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d08b8695990e864f7715926ab9cd9c8d"></a>

### [`00bdc670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc670.md) → [`00bdc6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6c0.md) _ZN5Botan13EMSA_PKCS1v15C1EPNS_12HashFunctionE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004c3c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3c00.md) [`0051038c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/0051038c.md) · 呼出先 1件 [`0049dbe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dbe4.md)
- 新版 呼出元 2件 [`004c3c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3c00.md) [`0051038c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/0051038c.md) · 呼出先 1件 [`0049dbe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dbe4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc674",
      "READ",
      [
        "storage",
        "00c1cbc8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc67c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0049dbe4"
      ]
    ]
  ],
  "added": [
    [
      "00bdc6c4",
      "READ",
      [
        "storage",
        "00c1cc18",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc6cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0049dbe4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc670.md#insn-00bdc670) · [`00bdc674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc670.md#insn-00bdc674) · [`00bdc678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc670.md#insn-00bdc678)

~~~diff
- 00bdc670 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc670 bytes 10020090
- 00bdc674 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:bc8:8"]]
- 00bdc674 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc674 bytes 11e645f9
- 00bdc678 ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 00bdc678 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc678 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc678 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc678 bytes 10222f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7ec2098f79724991dfbbba08857dd95"></a>

### [`00bdc680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc680.md) → [`00bdc6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6d0.md) _ZN5Botan4PSSRC2EPNS_12HashFunctionEm

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004c3c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3c00.md) [`005106e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/005106e0.md) · 呼出先 1件 [`0049e9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e9b0.md)
- 新版 呼出元 2件 [`004c3c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3c00.md) [`005106e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005106e0.md) · 呼出先 1件 [`0049e9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e9b0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc684",
      "READ",
      [
        "storage",
        "00c1cbd0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc68c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0049e9b0"
      ]
    ]
  ],
  "added": [
    [
      "00bdc6d4",
      "READ",
      [
        "storage",
        "00c1cc20",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc6dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0049e9b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc680.md#insn-00bdc680) · [`00bdc684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc680.md#insn-00bdc684) · [`00bdc688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc680.md#insn-00bdc688)

~~~diff
- 00bdc680 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc680 bytes 10020090
- 00bdc684 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:bd0:8"]]
- 00bdc684 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc684 bytes 11ea45f9
- 00bdc688 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 00bdc688 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc688 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc688 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc688 bytes 10422f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04c7967a461cc0ecf4ebf7d3f589bf9a"></a>

### [`00bdc690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc690.md) → [`00bdc6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6e0.md) _ZN5Botan8PSSR_RawC2EPNS_12HashFunctionEm

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004c3c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3c00.md) [`00510820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510820.md) · 呼出先 1件 [`0049fe48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049fe48.md)
- 新版 呼出元 2件 [`004c3c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3c00.md) [`00510820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510820.md) · 呼出先 1件 [`0049fe48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049fe48.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc694",
      "READ",
      [
        "storage",
        "00c1cbd8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc69c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0049fe48"
      ]
    ]
  ],
  "added": [
    [
      "00bdc6e4",
      "READ",
      [
        "storage",
        "00c1cc28",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc6ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0049fe48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc690.md#insn-00bdc690) · [`00bdc694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc690.md#insn-00bdc694) · [`00bdc698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc690.md#insn-00bdc698)

~~~diff
- 00bdc690 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc690 bytes 10020090
- 00bdc694 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:bd8:8"]]
- 00bdc694 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc694 bytes 11ee45f9
- 00bdc698 ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 00bdc698 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc698 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc698 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc698 bytes 10622f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e6cfbe70c01d198c07cfb9a312e4a9d"></a>

### [`00bdc6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6d0.md) → [`00bdc720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc720.md) _ZN5Botan15load_public_keyERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS3_9allocatorIhEEEE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004ce004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce004.md) · 呼出先 1件 [`004c52e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c52e0.md)
- 新版 呼出元 1件 [`004ce004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce004.md) · 呼出先 1件 [`004c52e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c52e0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc6d4",
      "READ",
      [
        "storage",
        "00c1cbf8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc6dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c52e0"
      ]
    ]
  ],
  "added": [
    [
      "00bdc724",
      "READ",
      [
        "storage",
        "00c1cc48",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc72c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c52e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6d0.md#insn-00bdc6d0) · [`00bdc6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6d0.md#insn-00bdc6d4) · [`00bdc6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6d0.md#insn-00bdc6d8)

~~~diff
- 00bdc6d0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc6d0 bytes 10020090
- 00bdc6d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:bf8:8"]]
- 00bdc6d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc6d4 bytes 11fe45f9
- 00bdc6d8 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00bdc6d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc6d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc6d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc6d8 bytes 10e22f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8374f9758f0718245dc503656dcc45c"></a>

### [`00bdc6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6e0.md) → [`00bdc730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc730.md) _ZN5Botan13RSA_PublicKeyC1ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004c52e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c52e0.md) · 呼出先 1件 [`004c56b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c56b0.md)
- 新版 呼出元 1件 [`004c52e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c52e0.md) · 呼出先 1件 [`004c56b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c56b0.md)

変更の種類 comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdc734",
      "READ",
      [
        "storage",
        "00c1cc00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bdc734",
      "READ",
      [
        "storage",
        "00c1cc50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6e0.md#insn-00bdc6e4) · [`00bdc6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6e0.md#insn-00bdc6e8)
- 新版 [`00bdc734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc730.md#insn-00bdc734) · [`00bdc738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc730.md#insn-00bdc738)

~~~diff
- 00bdc6e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c00:8"]]
- 00bdc6e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdc734 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c50:8"]]
+ 00bdc734 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc6e4 bytes 110246f9
+ 00bdc734 bytes 112a46f9
- 00bdc6e8 ["COPY", "tmp:0:8", ["const:c00:8"]]
- 00bdc6e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc6e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc6e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc6e8 bytes 10023091
+ 00bdc738 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 00bdc738 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
+ 00bdc738 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
+ 00bdc738 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
+ 00bdc738 bytes 10423191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55629c4525ad92162eb3e98dafdb300b"></a>

### [`00bdc6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6f0.md) → [`00bdc740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc740.md) _ZN5Botan16load_private_keyERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) · 呼出先 1件 [`004c585c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c585c.md)
- 新版 呼出元 1件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) · 呼出先 1件 [`004c585c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c585c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc6f4",
      "READ",
      [
        "storage",
        "00c1cc08",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc6fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c585c"
      ]
    ]
  ],
  "added": [
    [
      "00bdc744",
      "READ",
      [
        "storage",
        "00c1cc58",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc74c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c585c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6f0.md#insn-00bdc6f0) · [`00bdc6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6f0.md#insn-00bdc6f4) · [`00bdc6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6f0.md#insn-00bdc6f8)

~~~diff
- 00bdc6f0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc6f0 bytes 10020090
- 00bdc6f4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c08:8"]]
- 00bdc6f4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc6f4 bytes 110646f9
- 00bdc6f8 ["COPY", "tmp:0:8", ["const:c08:8"]]
- 00bdc6f8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc6f8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc6f8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc6f8 bytes 10223091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6254bed3eb2e92bd03465dc114cba564"></a>

### [`00bdc830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc830.md) → [`00bdc880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc880.md) _ZN5Botan4X5098load_keyERNS_10DataSourceE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`004ce670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce670.md) [`004ce6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce6fc.md) [`004ce7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce7d8.md) [`004ec0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec0b4.md) [`0055ddc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055ddc8.md) · 呼出先 1件 [`004ce004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce004.md)
- 新版 呼出元 5件 [`004ce670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce670.md) [`004ce6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce6fc.md) [`004ce7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce7d8.md) [`004ec0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec0b4.md) [`0055ddc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055ddc8.md) · 呼出先 1件 [`004ce004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce004.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc834",
      "READ",
      [
        "storage",
        "00c1cca8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc83c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ce004"
      ]
    ]
  ],
  "added": [
    [
      "00bdc884",
      "READ",
      [
        "storage",
        "00c1ccf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc88c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ce004"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc830.md#insn-00bdc834) · [`00bdc838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc830.md#insn-00bdc838) · [`00bdc83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc830.md#insn-00bdc83c)

~~~diff
- 00bdc834 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ca8:8"]]
- 00bdc834 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc834 bytes 115646f9
- 00bdc838 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 00bdc838 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc838 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc838 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc838 bytes 10a23291
- 00bdc83c ["COPY", "register:0:8", ["register:4088:8"]]
- 00bdc83c ["BRANCHIND", null, ["register:0:8"]]
- 00bdc83c bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9407f853b31f1fed7599bb1a250c4d1f"></a>

### [`00bdc840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc840.md) → [`00bdc890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc890.md) _ZN5Botan11BER_DecoderC2ERNS_10DataSourceE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`004ce004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce004.md) [`004ea660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004ea660.md) [`00513c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513c60.md) · 呼出先 1件 [`0048d668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d668.md)
- 新版 呼出元 3件 [`004ce004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce004.md) [`004ea660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea660.md) [`00513c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513c60.md) · 呼出先 1件 [`0048d668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d668.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc844",
      "READ",
      [
        "storage",
        "00c1ccb0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc84c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048d668"
      ]
    ]
  ],
  "added": [
    [
      "00bdc894",
      "READ",
      [
        "storage",
        "00c1cd00",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc89c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048d668"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc840.md#insn-00bdc840) · [`00bdc844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc840.md#insn-00bdc844) · [`00bdc848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc840.md#insn-00bdc848)

~~~diff
- 00bdc840 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc840 bytes 10020090
- 00bdc844 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:cb0:8"]]
- 00bdc844 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc844 bytes 115a46f9
- 00bdc848 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00bdc848 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc848 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc848 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc848 bytes 10c23291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4390e5c2bb739d5543e3589249cb60a"></a>

### [`00bdc850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc850.md) → [`00bdc8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8a0.md) _ZN5Botan4X5098load_keyERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004fdfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdfd8.md) [`00500f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00500/00500f10.md) · 呼出先 1件 [`004ce6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce6fc.md)
- 新版 呼出元 2件 [`004fdfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdfd8.md) [`00500f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/00500f10.md) · 呼出先 1件 [`004ce6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce6fc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc854",
      "READ",
      [
        "storage",
        "00c1ccb8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc85c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ce6fc"
      ]
    ]
  ],
  "added": [
    [
      "00bdc8a4",
      "READ",
      [
        "storage",
        "00c1cd08",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc8ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ce6fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc850.md#insn-00bdc850) · [`00bdc854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc850.md#insn-00bdc854) · [`00bdc858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc850.md#insn-00bdc858)

~~~diff
- 00bdc850 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc850 bytes 10020090
- 00bdc854 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:cb8:8"]]
- 00bdc854 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc854 bytes 115e46f9
- 00bdc858 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 00bdc858 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc858 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc858 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc858 bytes 10e23291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-858f32347226e510e6f9ec3574733f65"></a>

### [`00bdcc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc80.md) → [`00bdccd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccd0.md) _ZN5Botan25key_constraints_to_stringENS_15Key_ConstraintsE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004e3024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3024.md) · 呼出先 1件 [`004e242c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e2/004e242c.md)
- 新版 呼出元 1件 [`004e3024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3024.md) · 呼出先 1件 [`004e242c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e242c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcc84",
      "READ",
      [
        "storage",
        "00c1ced0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcc8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e242c"
      ]
    ]
  ],
  "added": [
    [
      "00bdccd4",
      "READ",
      [
        "storage",
        "00c1cf20",
        null,
        "pointer"
      ]
    ],
    [
      "00bdccdc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e242c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc80.md#insn-00bdcc80) · [`00bdcc84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc80.md#insn-00bdcc84) · [`00bdcc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc80.md#insn-00bdcc88)

~~~diff
- 00bdcc80 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcc80 bytes 10020090
- 00bdcc84 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ed0:8"]]
- 00bdcc84 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcc84 bytes 116a47f9
- 00bdcc88 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 00bdcc88 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcc88 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcc88 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcc88 bytes 10423b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-058215dce1cc81ebc5f63b8ac68fba9d"></a>

### [`00bdcc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc90.md) → [`00bdcce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcce0.md) _ZN5Botan42verify_cert_constraints_valid_for_key_typeERKNS_10Public_KeyENS_15Key_ConstraintsE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`004ede80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ede80.md) [`0050a638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md) · 呼出先 1件 [`004e3024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3024.md)
- 新版 呼出元 3件 [`004ede80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md) [`0050a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) · 呼出先 1件 [`004e3024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3024.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcc94",
      "READ",
      [
        "storage",
        "00c1ced8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcc9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e3024"
      ]
    ]
  ],
  "added": [
    [
      "00bdcce4",
      "READ",
      [
        "storage",
        "00c1cf28",
        null,
        "pointer"
      ]
    ],
    [
      "00bdccec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e3024"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc90.md#insn-00bdcc90) · [`00bdcc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc90.md#insn-00bdcc94) · [`00bdcc98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc90.md#insn-00bdcc98)

~~~diff
- 00bdcc90 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcc90 bytes 10020090
- 00bdcc94 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ed8:8"]]
- 00bdcc94 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcc94 bytes 116e47f9
- 00bdcc98 ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 00bdcc98 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcc98 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcc98 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcc98 bytes 10623b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7db75e031c4b0e3ba3522d948ec33fc5"></a>

### [`00bdcd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd50.md) → [`00bdcda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcda0.md) _ZN5Botan11BER_Decoder15decode_optionalINS_10ExtensionsEEERS0_RT_NS_8ASN1_TagES6_RKS4_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004e6d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6d3c.md) [`004e9fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e9/004e9fdc.md) · 呼出先 1件 [`004e82ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e82ac.md)
- 新版 呼出元 2件 [`004e6d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6d3c.md) [`004e9fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9fdc.md) · 呼出先 1件 [`004e82ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e82ac.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcd54",
      "READ",
      [
        "storage",
        "00c1cf38",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcd5c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e82ac"
      ]
    ]
  ],
  "added": [
    [
      "00bdcda4",
      "READ",
      [
        "storage",
        "00c1cf88",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcdac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e82ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd50.md#insn-00bdcd50) · [`00bdcd54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd50.md#insn-00bdcd54) · [`00bdcd58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd50.md#insn-00bdcd58)

~~~diff
- 00bdcd50 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcd50 bytes 10020090
- 00bdcd54 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f38:8"]]
- 00bdcd54 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcd54 bytes 119e47f9
- 00bdcd58 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 00bdcd58 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcd58 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcd58 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcd58 bytes 10e23c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65a2f67c31b1f8192fed2791220ff90b"></a>

### [`00bdcd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd60.md) → [`00bdcdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcdb0.md) _ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004e8a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8a14.md) · 呼出先 1件 [`004e85ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e85ec.md)
- 新版 呼出元 1件 [`004e8a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8a14.md) · 呼出先 1件 [`004e85ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e85ec.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcd64",
      "READ",
      [
        "storage",
        "00c1cf40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcd6c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e85ec"
      ]
    ]
  ],
  "added": [
    [
      "00bdcdb4",
      "READ",
      [
        "storage",
        "00c1cf90",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcdbc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e85ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd60.md#insn-00bdcd60) · [`00bdcd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd60.md#insn-00bdcd64) · [`00bdcd68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd60.md#insn-00bdcd68)

~~~diff
- 00bdcd60 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcd60 bytes 10020090
- 00bdcd64 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f40:8"]]
- 00bdcd64 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcd64 bytes 11a247f9
- 00bdcd68 ["COPY", "tmp:0:8", ["const:f40:8"]]
- 00bdcd68 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcd68 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcd68 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcd68 bytes 10023d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f139f03ae0baabd11a4eb6565adcd79c"></a>

### [`00bdcd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd70.md) → [`00bdcdc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcdc0.md) _ZNK5Botan16X509_Certificate23load_subject_public_keyEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`004e85ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e85ec.md) [`00501b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00501/00501b08.md) [`00503af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503af8.md) [`005054cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00505/005054cc.md) · 呼出先 1件 [`00500f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00500/00500f10.md)
- 新版 呼出元 4件 [`004e85ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e85ec.md) [`00501b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501b08.md) [`00503af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503af8.md) [`005054cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00505/005054cc.md) · 呼出先 1件 [`00500f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/00500f10.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcd74",
      "READ",
      [
        "storage",
        "00c1cf48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcd7c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00500f10"
      ]
    ]
  ],
  "added": [
    [
      "00bdcdc4",
      "READ",
      [
        "storage",
        "00c1cf98",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcdcc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00500f10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd70.md#insn-00bdcd70) · [`00bdcd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd70.md#insn-00bdcd74) · [`00bdcd78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd70.md#insn-00bdcd78)

~~~diff
- 00bdcd70 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcd70 bytes 10020090
- 00bdcd74 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f48:8"]]
- 00bdcd74 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcd74 bytes 11a647f9
- 00bdcd78 ["COPY", "tmp:0:8", ["const:f48:8"]]
- 00bdcd78 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcd78 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcd78 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcd78 bytes 10223d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-604e0b4996447f3ffbdacae2a6928a3a"></a>

### [`00bdcd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd80.md) → [`00bdcdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcdd0.md) _ZNK5Botan4OCSP8Response15check_signatureERKNSt6__ndk16vectorIPNS_17Certificate_StoreENS2_9allocatorIS5_EEEERKNS3_INS2_10shared_ptrIKNS_16X5

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00504f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00504/00504f50.md) · 呼出先 1件 [`004e8a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8a14.md)
- 新版 呼出元 1件 [`00504f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504f50.md) · 呼出先 1件 [`004e8a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8a14.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcd84",
      "READ",
      [
        "storage",
        "00c1cf50",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcd8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e8a14"
      ]
    ]
  ],
  "added": [
    [
      "00bdcdd4",
      "READ",
      [
        "storage",
        "00c1cfa0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcddc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e8a14"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd80.md#insn-00bdcd80) · [`00bdcd84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd80.md#insn-00bdcd84) · [`00bdcd88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd80.md#insn-00bdcd88)

~~~diff
- 00bdcd80 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcd80 bytes 10020090
- 00bdcd84 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f50:8"]]
- 00bdcd84 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcd84 bytes 11aa47f9
- 00bdcd88 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 00bdcd88 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcd88 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcd88 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcd88 bytes 10423d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e280f79ba33b3d9f4a4e3232e7814100"></a>

### [`00bdce80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce80.md) → [`00bdced0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdced0.md) _ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004ec8c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec8c8.md) [`004fdfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdfd8.md) · 呼出先 1件 [`004eca70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004eca70.md)
- 新版 呼出元 2件 [`004ec8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec8c8.md) [`004fdfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdfd8.md) · 呼出先 1件 [`004eca70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004eca70.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdce84",
      "READ",
      [
        "storage",
        "00c1cfd0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdce8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004eca70"
      ]
    ]
  ],
  "added": [
    [
      "00bdced4",
      "READ",
      [
        "storage",
        "00c1d020",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcedc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004eca70"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdce80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce80.md#insn-00bdce80) · [`00bdce84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce80.md#insn-00bdce84) · [`00bdce88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce80.md#insn-00bdce88)

~~~diff
- 00bdce80 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdce80 bytes 10020090
- 00bdce84 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fd0:8"]]
- 00bdce84 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdce84 bytes 11ea47f9
- 00bdce88 ["COPY", "tmp:0:8", ["const:fd0:8"]]
- 00bdce88 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdce88 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdce88 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdce88 bytes 10423f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11fc0947163b3256e7a9bb9f9031a5ed"></a>

### [`00bdce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce90.md) → [`00bdcee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcee0.md) _ZN5Botan10Extensions7replaceEPNS_21Certificate_ExtensionEb

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004ede80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ede80.md) · 呼出先 1件 [`004ee4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee4f4.md)
- 新版 呼出元 1件 [`004ede80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md) · 呼出先 1件 [`004ee4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee4f4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdce94",
      "READ",
      [
        "storage",
        "00c1cfd8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdce9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ee4f4"
      ]
    ]
  ],
  "added": [
    [
      "00bdcee4",
      "READ",
      [
        "storage",
        "00c1d028",
        null,
        "pointer"
      ]
    ],
    [
      "00bdceec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ee4f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce90.md#insn-00bdce90) · [`00bdce94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce90.md#insn-00bdce94) · [`00bdce98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce90.md#insn-00bdce98)

~~~diff
- 00bdce90 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdce90 bytes 10020090
- 00bdce94 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fd8:8"]]
- 00bdce94 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdce94 bytes 11ee47f9
- 00bdce98 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00bdce98 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdce98 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdce98 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdce98 bytes 10623f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0274388667c9e1c2ec084264e4759284"></a>

### [`00bdcea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcea0.md) → [`00bdcef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcef0.md) _ZN5Botan14Cert_Extension14Subject_Key_IDC2ERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEERKNS2_12basic_stringIcNS2_11char_traitsIcEENS4_IcEEEE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004ede80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ede80.md) [`0050a638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md) · 呼出先 1件 [`004f61e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f6/004f61e8.md)
- 新版 呼出元 2件 [`004ede80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md) [`0050a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) · 呼出先 1件 [`004f61e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f61e8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcea4",
      "READ",
      [
        "storage",
        "00c1cfe0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdceac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004f61e8"
      ]
    ]
  ],
  "added": [
    [
      "00bdcef4",
      "READ",
      [
        "storage",
        "00c1d030",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcefc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004f61e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcea0.md#insn-00bdcea0) · [`00bdcea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcea0.md#insn-00bdcea4) · [`00bdcea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcea0.md#insn-00bdcea8)

~~~diff
- 00bdcea0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcea0 bytes 10020090
- 00bdcea4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fe0:8"]]
- 00bdcea4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcea4 bytes 11f247f9
- 00bdcea8 ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 00bdcea8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcea8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcea8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcea8 bytes 10823f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cc3a93bdd4ef17a865a11632cc7e1f3"></a>

### [`00bdcef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcef0.md) → [`00bdcf40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf40.md) _ZN5Botan8X509_CRLC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004ef204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004ef204.md) · 呼出先 1件 [`004efb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efb8c.md)
- 新版 呼出元 1件 [`004ef204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef204.md) · 呼出先 1件 [`004efb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efb8c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcef4",
      "READ",
      [
        "storage",
        "00c1d008",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcefc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004efb8c"
      ]
    ]
  ],
  "added": [
    [
      "00bdcf44",
      "READ",
      [
        "storage",
        "00c1d058",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcf4c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004efb8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcef0.md#insn-00bdcef0) · [`00bdcef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcef0.md#insn-00bdcef4) · [`00bdcef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcef0.md#insn-00bdcef8)

~~~diff
- 00bdcef0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdcef0 bytes 100200b0
- 00bdcef4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8:8"]]
- 00bdcef4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcef4 bytes 110640f9
- 00bdcef8 ["COPY", "tmp:0:8", ["const:8:8"]]
- 00bdcef8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcef8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcef8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcef8 bytes 10220091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cd9922d5eb8c66f988c911d04bb79d4"></a>

### [`00bdcf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf00.md) → [`00bdcf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf50.md) _ZNK5Botan8X509_CRL10is_revokedERKNS_16X509_CertificateE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005054cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00505/005054cc.md) · 呼出先 1件 [`004f00b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f00b0.md)
- 新版 呼出元 1件 [`005054cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00505/005054cc.md) · 呼出先 1件 [`004f00b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f00b0.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcf04",
      "READ",
      [
        "storage",
        "00c1d010",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcf0c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004f00b0"
      ]
    ]
  ],
  "added": [
    [
      "00bdcf54",
      "READ",
      [
        "storage",
        "00c1d060",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcf5c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004f00b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcf04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf00.md#insn-00bdcf04) · [`00bdcf08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf00.md#insn-00bdcf08) · [`00bdcf0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf00.md#insn-00bdcf0c)

~~~diff
- 00bdcf04 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:10:8"]]
- 00bdcf04 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcf04 bytes 110a40f9
- 00bdcf08 ["COPY", "tmp:0:8", ["const:10:8"]]
- 00bdcf08 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf08 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf08 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcf08 bytes 10420091
- 00bdcf0c ["COPY", "register:0:8", ["register:4088:8"]]
- 00bdcf0c ["BRANCHIND", null, ["register:0:8"]]
- 00bdcf0c bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca6ccb67a54bc963e81550cb656c99bd"></a>

### [`00bdcfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfc0.md) → [`00bdd010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd010.md) _ZN5Botan11BER_Decoder11decode_listINS_14Cert_Extension23CRL_Distribution_Points18Distribution_PointEEERS0_RNSt6__ndk16vectorIT_NS6_9allocat

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004fb0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb0d8.md) · 呼出先 1件 [`004fb4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb4c0.md)
- 新版 呼出元 1件 [`004fb0d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fb/004fb0d8.md) · 呼出先 1件 [`004fb4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fb/004fb4c0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcfc4",
      "READ",
      [
        "storage",
        "00c1d070",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcfcc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fb4c0"
      ]
    ]
  ],
  "added": [
    [
      "00bdd014",
      "READ",
      [
        "storage",
        "00c1d0c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd01c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fb4c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfc0.md#insn-00bdcfc0) · [`00bdcfc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfc0.md#insn-00bdcfc4) · [`00bdcfc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfc0.md#insn-00bdcfc8)

~~~diff
- 00bdcfc0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdcfc0 bytes 100200b0
- 00bdcfc4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:70:8"]]
- 00bdcfc4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcfc4 bytes 113a40f9
- 00bdcfc8 ["COPY", "tmp:0:8", ["const:70:8"]]
- 00bdcfc8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcfc8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcfc8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcfc8 bytes 10c20191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7822efca84125e2b617c1c31d3e438a2"></a>

### [`00bdcfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfe0.md) → [`00bdd030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd030.md) _ZNK5Botan11X509_Object10BER_encodeEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`004fc5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc5bc.md) [`0050168c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00501/0050168c.md) [`0050645c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/0050645c.md) [`00506ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/00506ee0.md) · 呼出先 1件 [`004fc4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc4b0.md)
- 新版 呼出元 4件 [`004fc5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc5bc.md) [`0050168c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/0050168c.md) [`0050645c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/0050645c.md) [`00506ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506ee0.md) · 呼出先 1件 [`004fc4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc4b0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcfe4",
      "READ",
      [
        "storage",
        "00c1d080",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcfec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fc4b0"
      ]
    ]
  ],
  "added": [
    [
      "00bdd034",
      "READ",
      [
        "storage",
        "00c1d0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd03c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fc4b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfe0.md#insn-00bdcfe0) · [`00bdcfe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfe0.md#insn-00bdcfe4) · [`00bdcfe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfe0.md#insn-00bdcfe8)

~~~diff
- 00bdcfe0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdcfe0 bytes 100200b0
- 00bdcfe4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:80:8"]]
- 00bdcfe4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcfe4 bytes 114240f9
- 00bdcfe8 ["COPY", "tmp:0:8", ["const:80:8"]]
- 00bdcfe8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcfe8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcfe8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcfe8 bytes 10020291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b42c51df8102265c06879614b8534e3d"></a>

### [`00bdcff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcff0.md) → [`00bdd040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd040.md) _ZNK5Botan11X509_Object23hash_used_for_signatureEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00503af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503af8.md) [`0050a3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a3ac.md) · 呼出先 1件 [`004fc6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc6ac.md)
- 新版 呼出元 2件 [`00503af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503af8.md) [`0050a3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a3ac.md) · 呼出先 1件 [`004fc6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc6ac.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcff4",
      "READ",
      [
        "storage",
        "00c1d088",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcffc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fc6ac"
      ]
    ]
  ],
  "added": [
    [
      "00bdd044",
      "READ",
      [
        "storage",
        "00c1d0d8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd04c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fc6ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcff0.md#insn-00bdcff0) · [`00bdcff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcff0.md#insn-00bdcff4) · [`00bdcff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcff0.md#insn-00bdcff8)

~~~diff
- 00bdcff0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdcff0 bytes 100200b0
- 00bdcff4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:88:8"]]
- 00bdcff4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcff4 bytes 114640f9
- 00bdcff8 ["COPY", "tmp:0:8", ["const:88:8"]]
- 00bdcff8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcff8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcff8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcff8 bytes 10220291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdef56b6ce812c8ebd6769820c54fae5"></a>

### [`00bdd040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd040.md) → [`00bdd090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd090.md) _ZN5Botan4PKIX11check_chainERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEENS1_6chrono10time_pointINSC_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00508860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508860.md) · 呼出先 1件 [`00503af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503af8.md)
- 新版 呼出元 1件 [`00508860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508860.md) · 呼出先 1件 [`00503af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503af8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd044",
      "READ",
      [
        "storage",
        "00c1d0b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd04c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00503af8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd094",
      "READ",
      [
        "storage",
        "00c1d100",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd09c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00503af8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd040.md#insn-00bdd040) · [`00bdd044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd040.md#insn-00bdd044) · [`00bdd048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd040.md#insn-00bdd048)

~~~diff
- 00bdd040 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd040 bytes 10020090
- 00bdd044 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b0:8"]]
- 00bdd044 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd044 bytes 115a40f9
- 00bdd048 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 00bdd048 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd048 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd048 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd048 bytes 10c20291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c050865ee31b43aeb81d64dca76866c4"></a>

### [`00bdd060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd060.md) → [`00bdd0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0b0.md) _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_8X509_CRLEEENS7

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005060a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/005060a8.md) · 呼出先 1件 [`005054cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00505/005054cc.md)
- 新版 呼出元 1件 [`005060a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/005060a8.md) · 呼出先 1件 [`005054cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00505/005054cc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd064",
      "READ",
      [
        "storage",
        "00c1d0c0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd06c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "005054cc"
      ]
    ]
  ],
  "added": [
    [
      "00bdd0b4",
      "READ",
      [
        "storage",
        "00c1d110",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd0bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "005054cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd060.md#insn-00bdd060) · [`00bdd064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd060.md#insn-00bdd064) · [`00bdd068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd060.md#insn-00bdd068)

~~~diff
- 00bdd060 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd060 bytes 10020090
- 00bdd064 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c0:8"]]
- 00bdd064 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd064 bytes 116240f9
- 00bdd068 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 00bdd068 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd068 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd068 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd068 bytes 10020391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a3e7426a7eb7072c2af4c6e5b54e2a9"></a>

### [`00bdd070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd070.md) → [`00bdd0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0c0.md) _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_IPNS_17Certificate_StoreE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00508860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508860.md) · 呼出先 1件 [`005060a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/005060a8.md)
- 新版 呼出元 1件 [`00508860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508860.md) · 呼出先 1件 [`005060a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/005060a8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd074",
      "READ",
      [
        "storage",
        "00c1d0c8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd07c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "005060a8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd0c4",
      "READ",
      [
        "storage",
        "00c1d118",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd0cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "005060a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd070.md#insn-00bdd070) · [`00bdd074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd070.md#insn-00bdd074) · [`00bdd078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd070.md#insn-00bdd078)

~~~diff
- 00bdd070 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd070 bytes 10020090
- 00bdd074 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c8:8"]]
- 00bdd074 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd074 bytes 116640f9
- 00bdd078 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 00bdd078 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd078 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd078 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd078 bytes 10220391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60ad4a005fa16999db193ce066520785"></a>

### [`00bdd220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd220.md) → [`00bdd270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd270.md) _ZNSt6__ndk115recursive_mutexC1Ev

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0054841c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/0054841c.md) · 呼出先 1件 [`00b7d2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d2f0.md)
- 新版 呼出元 1件 [`0054841c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/0054841c.md) · 呼出先 1件 [`00b7d334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d334.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd224",
      "READ",
      [
        "storage",
        "00c1d1a0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd22c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d334"
      ]
    ]
  ],
  "added": [
    [
      "00bdd274",
      "READ",
      [
        "storage",
        "00c1d1f0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd27c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d334"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd220.md#insn-00bdd220) · [`00bdd224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd220.md#insn-00bdd224) · [`00bdd228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd220.md#insn-00bdd228)

~~~diff
- 00bdd220 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd220 bytes 10020090
- 00bdd224 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1a0:8"]]
- 00bdd224 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd224 bytes 11d240f9
- 00bdd228 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 00bdd228 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd228 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd228 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd228 bytes 10820691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b665bf97b96c9a2df269feab01de6b4"></a>

### [`00bdd230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd230.md) → [`00bdd280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd280.md) _ZNSt6__ndk115recursive_mutexD1Ev

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005488c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/005488c4.md) · 呼出先 1件 [`00b7d394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d394.md)
- 新版 呼出元 1件 [`005488c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005488c4.md) · 呼出先 1件 [`00b7d3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3d8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd234",
      "READ",
      [
        "storage",
        "00c1d1a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd23c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d3d8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd284",
      "READ",
      [
        "storage",
        "00c1d1f8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd28c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d3d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd230.md#insn-00bdd230) · [`00bdd234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd230.md#insn-00bdd234) · [`00bdd238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd230.md#insn-00bdd238)

~~~diff
- 00bdd230 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd230 bytes 10020090
- 00bdd234 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1a8:8"]]
- 00bdd234 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd234 bytes 11d640f9
- 00bdd238 ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 00bdd238 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd238 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd238 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd238 bytes 10a20691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d6d66064e2f72d5a651fc86178adf8d"></a>

### [`00bdd240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd240.md) → [`00bdd290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd290.md) _ZNSt6__ndk115recursive_mutex4lockEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`005487f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/005487f8.md) [`005488c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/005488c4.md) [`00548a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/00548a34.md) [`00548b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/00548b4c.md) [`00549364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549364.md) · 呼出先 1件 [`00b7d3b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d3b4.md)
- 新版 呼出元 6件 [`005487f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005487f8.md) [`005488c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005488c4.md) [`00548a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548a34.md) [`00548b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548b4c.md) [`00549364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549364.md) · 呼出先 1件 [`00b7d3f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3f8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd244",
      "READ",
      [
        "storage",
        "00c1d1b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd24c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d3f8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd294",
      "READ",
      [
        "storage",
        "00c1d200",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd29c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d3f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd240.md#insn-00bdd240) · [`00bdd244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd240.md#insn-00bdd244) · [`00bdd248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd240.md#insn-00bdd248)

~~~diff
- 00bdd240 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd240 bytes 10020090
- 00bdd244 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1b0:8"]]
- 00bdd244 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd244 bytes 11da40f9
- 00bdd248 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 00bdd248 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd248 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd248 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd248 bytes 10c20691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82fdab937215459006278efde7dcef3c"></a>

### [`00bdd250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd250.md) → [`00bdd2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2a0.md) _ZNSt6__ndk115recursive_mutex6unlockEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`005487f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/005487f8.md) [`005488c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/005488c4.md) [`00548a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/00548a34.md) [`00548b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/00548b4c.md) [`00549364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549364.md) · 呼出先 1件 [`00b7d3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d3e0.md)
- 新版 呼出元 6件 [`005487f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005487f8.md) [`005488c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005488c4.md) [`00548a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548a34.md) [`00548b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548b4c.md) [`00549364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549364.md) · 呼出先 1件 [`00b7d424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d424.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd254",
      "READ",
      [
        "storage",
        "00c1d1b8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd25c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d424"
      ]
    ]
  ],
  "added": [
    [
      "00bdd2a4",
      "READ",
      [
        "storage",
        "00c1d208",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd2ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d424"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd250.md#insn-00bdd254) · [`00bdd258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd250.md#insn-00bdd258) · [`00bdd25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd250.md#insn-00bdd25c)

~~~diff
- 00bdd254 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1b8:8"]]
- 00bdd254 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd254 bytes 11de40f9
- 00bdd258 ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 00bdd258 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd258 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd258 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd258 bytes 10e20691
- 00bdd25c ["COPY", "register:0:8", ["register:4088:8"]]
- 00bdd25c ["BRANCHIND", null, ["register:0:8"]]
- 00bdd25c bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b9d55cff57dfdc2414ef55609d44dd5"></a>

### [`00bdd260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd260.md) → [`00bdd2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2b0.md) &lt;EXTERNAL&gt;::log10f

採用 · 移動量 `+0x50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00549504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549504.md) · 呼出先 1件 [`010a5238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5238.md)
- 新版 呼出元 1件 [`00549504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549504.md) · 呼出先 1件 [`010a5238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5238.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd264",
      "READ",
      [
        "storage",
        "00c1d1c0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd26c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5238"
      ]
    ]
  ],
  "added": [
    [
      "00bdd2b4",
      "READ",
      [
        "storage",
        "00c1d210",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd2bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5238"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd260.md#insn-00bdd260) · [`00bdd264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd260.md#insn-00bdd264) · [`00bdd268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd260.md#insn-00bdd268)

~~~diff
- 00bdd260 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd260 bytes 10020090
- 00bdd264 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1c0:8"]]
- 00bdd264 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd264 bytes 11e240f9
- 00bdd268 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 00bdd268 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd268 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd268 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd268 bytes 10020791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ec1ed5ca2e68dde9a9043f519850ad9"></a>

### [`00bdd280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd280.md) → [`00bdd2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2d0.md) &lt;EXTERNAL&gt;::sincos

採用 · 移動量 `+0x50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0054cec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054c/0054cec8.md) [`00a17ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a17/00a17ce0.md) · 呼出先 1件 [`010a5248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5248.md)
- 新版 呼出元 2件 [`0054cec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054cec8.md) [`00a17d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a17/00a17d24.md) · 呼出先 1件 [`010a5248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5248.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd284",
      "READ",
      [
        "storage",
        "00c1d1d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd28c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5248"
      ]
    ]
  ],
  "added": [
    [
      "00bdd2d4",
      "READ",
      [
        "storage",
        "00c1d220",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd2dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5248"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd280.md#insn-00bdd280) · [`00bdd284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd280.md#insn-00bdd284) · [`00bdd288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd280.md#insn-00bdd288)

~~~diff
- 00bdd280 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd280 bytes 10020090
- 00bdd284 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1d0:8"]]
- 00bdd284 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd284 bytes 11ea40f9
- 00bdd288 ["COPY", "tmp:0:8", ["const:1d0:8"]]
- 00bdd288 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd288 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd288 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd288 bytes 10420791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bf5121987c8a97c3ebb48fdc213bc00"></a>

### [`00bdd290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd290.md) → [`00bdd2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2e0.md) &lt;EXTERNAL&gt;::__fread_chk

採用 · 移動量 `+0x50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0054da70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054d/0054da70.md) · 呼出先 1件 [`010a5250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5250.md)
- 新版 呼出元 1件 [`0054da70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054d/0054da70.md) · 呼出先 1件 [`010a5250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5250.md)

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
        "00c1d1d8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd29c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5250"
      ]
    ]
  ],
  "added": [
    [
      "00bdd2e4",
      "READ",
      [
        "storage",
        "00c1d228",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd2ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5250"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd290.md#insn-00bdd290) · [`00bdd294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd290.md#insn-00bdd294) · [`00bdd298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd290.md#insn-00bdd298)

~~~diff
- 00bdd290 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd290 bytes 10020090
- 00bdd294 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1d8:8"]]
- 00bdd294 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd294 bytes 11ee40f9
- 00bdd298 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 00bdd298 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd298 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd298 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd298 bytes 10620791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e41fe8afce4384bbb5c5a7d1b67f0045"></a>

### [`00bdd2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2d0.md) → [`00bdd320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd320.md) &lt;EXTERNAL&gt;::AAsset_getRemainingLength

採用 · 移動量 `+0x50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00559f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559f90.md) [`0055a254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055a254.md) · 呼出先 1件 [`010a5270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5270.md)
- 新版 呼出元 2件 [`00559f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559f90.md) [`0055a254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a254.md) · 呼出先 1件 [`010a5270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5270.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

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
        "00c1d1f8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd2dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5270"
      ]
    ]
  ],
  "added": [
    [
      "00bdd324",
      "READ",
      [
        "storage",
        "00c1d248",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd32c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5270"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2d0.md#insn-00bdd2d0) · [`00bdd2d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2d0.md#insn-00bdd2d4) · [`00bdd2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2d0.md#insn-00bdd2d8)

~~~diff
- 00bdd2d0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd2d0 bytes 10020090
- 00bdd2d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1f8:8"]]
- 00bdd2d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd2d4 bytes 11fe40f9
- 00bdd2d8 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 00bdd2d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd2d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd2d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd2d8 bytes 10e20791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec4ceb9ea582e8316f07ee5d8fe60c2a"></a>

### [`00bdd2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2e0.md) → [`00bdd330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd330.md) &lt;EXTERNAL&gt;::AAsset_read

採用 · 移動量 `+0x50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00559fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559fe0.md) [`0055af38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055af38.md) · 呼出先 1件 [`010a5278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5278.md)
- 新版 呼出元 2件 [`00559fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559fe0.md) [`0055af38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055af38.md) · 呼出先 1件 [`010a5278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5278.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd2e4",
      "READ",
      [
        "storage",
        "00c1d200",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd2ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5278"
      ]
    ]
  ],
  "added": [
    [
      "00bdd334",
      "READ",
      [
        "storage",
        "00c1d250",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd33c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5278"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2e0.md#insn-00bdd2e0) · [`00bdd2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2e0.md#insn-00bdd2e4) · [`00bdd2e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2e0.md#insn-00bdd2e8)

~~~diff
- 00bdd2e0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd2e0 bytes 10020090
- 00bdd2e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:200:8"]]
- 00bdd2e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd2e4 bytes 110241f9
- 00bdd2e8 ["COPY", "tmp:0:8", ["const:200:8"]]
- 00bdd2e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd2e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd2e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd2e8 bytes 10020891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaf9b255f96ea2d46db8394994fee285"></a>

### [`00bdd420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd420.md) → [`00bdd470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd470.md) &lt;EXTERNAL&gt;::AndroidBitmap_lockPixels

採用 · 移動量 `+0x50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0055c994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c994.md) [`0055d5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d5cc.md) · 呼出先 1件 [`010a5310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5310.md)
- 新版 呼出元 2件 [`0055c994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c994.md) [`0055d5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d5cc.md) · 呼出先 1件 [`010a5310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5310.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd424",
      "READ",
      [
        "storage",
        "00c1d2a0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd42c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5310"
      ]
    ]
  ],
  "added": [
    [
      "00bdd474",
      "READ",
      [
        "storage",
        "00c1d2f0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd47c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5310"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd420.md#insn-00bdd420) · [`00bdd424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd420.md#insn-00bdd424) · [`00bdd428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd420.md#insn-00bdd428)

~~~diff
- 00bdd420 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd420 bytes 10020090
- 00bdd424 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2a0:8"]]
- 00bdd424 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd424 bytes 115241f9
- 00bdd428 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 00bdd428 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd428 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd428 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd428 bytes 10820a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a65c1c03cae6293d4624c4d555a96940"></a>

### [`00bdd430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd430.md) → [`00bdd480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd480.md) &lt;EXTERNAL&gt;::AndroidBitmap_unlockPixels

採用 · 移動量 `+0x50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0055c994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c994.md) [`0055d5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d5cc.md) · 呼出先 1件 [`010a5318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5318.md)
- 新版 呼出元 2件 [`0055c994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c994.md) [`0055d5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d5cc.md) · 呼出先 1件 [`010a5318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5318.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd434",
      "READ",
      [
        "storage",
        "00c1d2a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd43c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5318"
      ]
    ]
  ],
  "added": [
    [
      "00bdd484",
      "READ",
      [
        "storage",
        "00c1d2f8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd48c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5318"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd430.md#insn-00bdd430) · [`00bdd434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd430.md#insn-00bdd434) · [`00bdd438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd430.md#insn-00bdd438)

~~~diff
- 00bdd430 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd430 bytes 10020090
- 00bdd434 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2a8:8"]]
- 00bdd434 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd434 bytes 115641f9
- 00bdd438 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00bdd438 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd438 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd438 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd438 bytes 10a20a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e901e6563924fb1fc4e702984544fbc7"></a>

### [`00bdd4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd4b0.md) → [`00bdd500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd500.md) &lt;EXTERNAL&gt;::__android_log_write

採用 · 移動量 `+0x50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0056c3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c3ac.md) · 呼出先 1件 [`010a5350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5350.md)
- 新版 呼出元 1件 [`0056c3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c3ac.md) · 呼出先 1件 [`010a5350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5350.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd4b4",
      "READ",
      [
        "storage",
        "00c1d2e8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd4bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5350"
      ]
    ]
  ],
  "added": [
    [
      "00bdd504",
      "READ",
      [
        "storage",
        "00c1d338",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd50c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5350"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd4b0.md#insn-00bdd4b0) · [`00bdd4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd4b0.md#insn-00bdd4b4) · [`00bdd4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd4b0.md#insn-00bdd4b8)

~~~diff
- 00bdd4b0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd4b0 bytes 10020090
- 00bdd4b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2e8:8"]]
- 00bdd4b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd4b4 bytes 117641f9
- 00bdd4b8 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 00bdd4b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd4b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd4b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd4b8 bytes 10a20b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-975db1a5bc56286e11eafdd45be417eb"></a>

### [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md) → [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 44件 [`00af7c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7c8c.md) [`00afa430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa430.md) [`00afd0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd0c4.md) [`00b0190c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0190c.md) [`00b0aba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0aba4.md) · 呼出先 1件 [`00af7ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7ac8.md)
- 新版 呼出元 44件 [`00af7cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7cd0.md) [`00afa474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa474.md) [`00afd108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd108.md) [`00b01950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01950.md) [`00b0abe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0abe8.md) · 呼出先 1件 [`00af7b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7b0c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde6e4",
      "READ",
      [
        "storage",
        "00c1dc00",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde6ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af7b0c"
      ]
    ]
  ],
  "added": [
    [
      "00bde734",
      "READ",
      [
        "storage",
        "00c1dc50",
        null,
        "pointer"
      ]
    ],
    [
      "00bde73c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af7b0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md#insn-00bde6e0) · [`00bde6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md#insn-00bde6e4) · [`00bde6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md#insn-00bde6e8)

~~~diff
- 00bde6e0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde6e0 bytes f00100f0
- 00bde6e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c00:8"]]
- 00bde6e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde6e4 bytes 110246f9
- 00bde6e8 ["COPY", "tmp:0:8", ["const:c00:8"]]
- 00bde6e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde6e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde6e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde6e8 bytes 10023091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d028b9ff5bb5e1f32981d0542c17c6b1"></a>

### [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md) → [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 32件 [`00af23a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af23a4.md) [`00af37b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af37b4.md) [`00af5884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5884.md) [`00af7258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7258.md) [`00b0347c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b0347c.md) · 呼出先 1件 [`00af3b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3b3c.md)
- 新版 呼出元 32件 [`00af23e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af23e8.md) [`00af37f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af37f8.md) [`00af58c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af58c8.md) [`00af729c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af729c.md) [`00b034c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b034c0.md) · 呼出先 1件 [`00af3b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3b80.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde6f4",
      "READ",
      [
        "storage",
        "00c1dc08",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde6fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af3b80"
      ]
    ]
  ],
  "added": [
    [
      "00bde744",
      "READ",
      [
        "storage",
        "00c1dc58",
        null,
        "pointer"
      ]
    ],
    [
      "00bde74c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af3b80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md#insn-00bde6f0) · [`00bde6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md#insn-00bde6f4) · [`00bde6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md#insn-00bde6f8)

~~~diff
- 00bde6f0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde6f0 bytes f00100f0
- 00bde6f4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c08:8"]]
- 00bde6f4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde6f4 bytes 110646f9
- 00bde6f8 ["COPY", "tmp:0:8", ["const:c08:8"]]
- 00bde6f8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde6f8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde6f8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde6f8 bytes 10223091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c319633fea8bbe7d0667f686029618dd"></a>

### [`00bde750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde750.md) → [`00bde7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7a0.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE21__push_back_slow_pathIS2_EEvOT_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00af3864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3864.md) [`00af5294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5294.md) · 呼出先 1件 [`00af7f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7f3c.md)
- 新版 呼出元 2件 [`00af38a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af38a8.md) [`00af52d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af52d8.md) · 呼出先 1件 [`00af7f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7f80.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde754",
      "READ",
      [
        "storage",
        "00c1dc38",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde75c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af7f80"
      ]
    ]
  ],
  "added": [
    [
      "00bde7a4",
      "READ",
      [
        "storage",
        "00c1dc88",
        null,
        "pointer"
      ]
    ],
    [
      "00bde7ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af7f80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde750.md#insn-00bde750) · [`00bde754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde750.md#insn-00bde754) · [`00bde758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde750.md#insn-00bde758)

~~~diff
- 00bde750 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde750 bytes f00100f0
- 00bde754 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c38:8"]]
- 00bde754 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde754 bytes 111e46f9
- 00bde758 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 00bde758 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde758 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde758 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde758 bytes 10e23091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5f920f5ab3e0636dd89b7bc558460b4"></a>

### [`00bde760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde760.md) → [`00bde7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7b0.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE7reserveEm

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00af3864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3864.md) [`00af5294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5294.md) · 呼出先 1件 [`00af3a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3a20.md)
- 新版 呼出元 2件 [`00af38a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af38a8.md) [`00af52d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af52d8.md) · 呼出先 1件 [`00af3a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3a64.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde764",
      "READ",
      [
        "storage",
        "00c1dc40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde76c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af3a64"
      ]
    ]
  ],
  "added": [
    [
      "00bde7b4",
      "READ",
      [
        "storage",
        "00c1dc90",
        null,
        "pointer"
      ]
    ],
    [
      "00bde7bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af3a64"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde760.md#insn-00bde760) · [`00bde764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde760.md#insn-00bde764) · [`00bde768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde760.md#insn-00bde768)

~~~diff
- 00bde760 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde760 bytes f00100f0
- 00bde764 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c40:8"]]
- 00bde764 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde764 bytes 112246f9
- 00bde768 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 00bde768 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde768 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde768 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde768 bytes 10023191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c365a3c4e3d69da2d9f5d653d8433d99"></a>

### [`00bde780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde780.md) → [`00bde7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7d0.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIS6_EEvOT_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`00af3278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3278.md) [`00af3560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3560.md) [`00afd844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd844.md) [`00b02500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02500.md) [`00b0e6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e6f8.md) · 呼出先 1件 [`00af7ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7ddc.md)
- 新版 呼出元 10件 [`00af32bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af32bc.md) [`00af35a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af35a4.md) [`00afd888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd888.md) [`00b02544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02544.md) [`00b0e73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e73c.md) · 呼出先 1件 [`00af7e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7e20.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde784",
      "READ",
      [
        "storage",
        "00c1dc50",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde78c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af7e20"
      ]
    ]
  ],
  "added": [
    [
      "00bde7d4",
      "READ",
      [
        "storage",
        "00c1dca0",
        null,
        "pointer"
      ]
    ],
    [
      "00bde7dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af7e20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde780.md#insn-00bde780) · [`00bde784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde780.md#insn-00bde784) · [`00bde788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde780.md#insn-00bde788)

~~~diff
- 00bde780 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde780 bytes f00100f0
- 00bde784 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c50:8"]]
- 00bde784 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde784 bytes 112a46f9
- 00bde788 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 00bde788 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde788 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde788 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde788 bytes 10423191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a5e19f6d49ea0aa60c53382fbd3cd82"></a>

### [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) → [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md) &lt;EXTERNAL&gt;::pthread_mutex_unlock

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 25件 [`00af0bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md) [`00af1320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1320.md) [`00af5cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5cb4.md) [`00af5ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ebc.md) [`00b054a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b054a4.md) · 呼出先 1件 [`010a55a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a55a8.md)
- 新版 呼出元 25件 [`00af0c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af0/00af0c38.md) [`00af1364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1364.md) [`00af5cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5cf8.md) [`00af5f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5f00.md) [`00b054e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b054e8.md) · 呼出先 1件 [`010a55a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a55a8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde7e4",
      "READ",
      [
        "storage",
        "00c1dc80",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde7ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a55a8"
      ]
    ]
  ],
  "added": [
    [
      "00bde834",
      "READ",
      [
        "storage",
        "00c1dcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00bde83c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a55a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md#insn-00bde7e0) · [`00bde7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md#insn-00bde7e4) · [`00bde7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md#insn-00bde7e8)

~~~diff
- 00bde7e0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde7e0 bytes f00100f0
- 00bde7e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c80:8"]]
- 00bde7e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde7e4 bytes 114246f9
- 00bde7e8 ["COPY", "tmp:0:8", ["const:c80:8"]]
- 00bde7e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde7e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde7e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde7e8 bytes 10023291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6b2d9f7299386d7c7bdbf517f70fc9c"></a>

### [`00bde860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde860.md) → [`00bde8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8b0.md) _ZN8firebase10app_common16IsDefaultAppNameEPKc

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b06ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md) · 呼出先 1件 [`00af92fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af92fc.md)
- 新版 呼出元 1件 [`00b06d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md) · 呼出先 1件 [`00af9340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9340.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde864",
      "READ",
      [
        "storage",
        "00c1dcc0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde86c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af9340"
      ]
    ]
  ],
  "added": [
    [
      "00bde8b4",
      "READ",
      [
        "storage",
        "00c1dd10",
        null,
        "pointer"
      ]
    ],
    [
      "00bde8bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af9340"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde860.md#insn-00bde860) · [`00bde864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde860.md#insn-00bde864) · [`00bde868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde860.md#insn-00bde868)

~~~diff
- 00bde860 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde860 bytes f00100f0
- 00bde864 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:cc0:8"]]
- 00bde864 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde864 bytes 116246f9
- 00bde868 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 00bde868 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde868 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde868 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde868 bytes 10023391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6023ddb784a73a978100747d64951cca"></a>

### [`00bde880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde880.md) → [`00bde8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8d0.md) _ZN8firebase10app_common6AddAppEPNS_3AppEPNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS_10InitResultENS3_4l

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b06ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md) · 呼出先 1件 [`00af8e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8e50.md)
- 新版 呼出元 1件 [`00b06d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md) · 呼出先 1件 [`00af8e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8e94.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde884",
      "READ",
      [
        "storage",
        "00c1dcd0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde88c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af8e94"
      ]
    ]
  ],
  "added": [
    [
      "00bde8d4",
      "READ",
      [
        "storage",
        "00c1dd20",
        null,
        "pointer"
      ]
    ],
    [
      "00bde8dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af8e94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde880.md#insn-00bde880) · [`00bde884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde880.md#insn-00bde884) · [`00bde888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde880.md#insn-00bde888)

~~~diff
- 00bde880 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde880 bytes f00100f0
- 00bde884 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:cd0:8"]]
- 00bde884 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde884 bytes 116a46f9
- 00bde888 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00bde888 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde888 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde888 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde888 bytes 10423391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f03e8dc660310d4eda5668b8e0395fa"></a>

### [`00bde930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde930.md) → [`00bde980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde980.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00af8e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8e50.md) · 呼出先 1件 [`00afab6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afab6c.md)
- 新版 呼出元 1件 [`00af8e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8e94.md) · 呼出先 1件 [`00afabb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afabb0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde934",
      "READ",
      [
        "storage",
        "00c1dd28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde93c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afabb0"
      ]
    ]
  ],
  "added": [
    [
      "00bde984",
      "READ",
      [
        "storage",
        "00c1dd78",
        null,
        "pointer"
      ]
    ],
    [
      "00bde98c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afabb0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde930.md#insn-00bde930) · [`00bde934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde930.md#insn-00bde934) · [`00bde938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde930.md#insn-00bde938)

~~~diff
- 00bde930 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde930 bytes f00100f0
- 00bde934 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:d28:8"]]
- 00bde934 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde934 bytes 119646f9
- 00bde938 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00bde938 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde938 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde938 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde938 bytes 10a23491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8febcf0c58713f9eed5971c9a19011b"></a>

### [`00bde940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde940.md) → [`00bde990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde990.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00af91c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af91c4.md) [`00af9550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9550.md) [`00afa88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa88c.md) · 呼出先 1件 [`00afac8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afac8c.md)
- 新版 呼出元 3件 [`00af9208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9208.md) [`00af9594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9594.md) [`00afa8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa8d0.md) · 呼出先 1件 [`00afacd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afacd0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde944",
      "READ",
      [
        "storage",
        "00c1dd30",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde94c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afacd0"
      ]
    ]
  ],
  "added": [
    [
      "00bde994",
      "READ",
      [
        "storage",
        "00c1dd80",
        null,
        "pointer"
      ]
    ],
    [
      "00bde99c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afacd0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde940.md#insn-00bde940) · [`00bde944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde940.md#insn-00bde944) · [`00bde948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde940.md#insn-00bde948)

~~~diff
- 00bde940 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde940 bytes f00100f0
- 00bde944 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:d30:8"]]
- 00bde944 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde944 bytes 119a46f9
- 00bde948 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 00bde948 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde948 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde948 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde948 bytes 10c23491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8294a4da615ca77cc9a86dd9da5b17e"></a>

### [`00bde950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde950.md) → [`00bde9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9a0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00af9550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9550.md) · 呼出先 1件 [`00afae88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afae88.md)
- 新版 呼出元 1件 [`00af9594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9594.md) · 呼出先 1件 [`00afaecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaecc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde954",
      "READ",
      [
        "storage",
        "00c1dd38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bde9a4",
      "READ",
      [
        "storage",
        "00c1dd88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde950.md#insn-00bde950) · [`00bde954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde950.md#insn-00bde954) · [`00bde958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde950.md#insn-00bde958)

~~~diff
- 00bde950 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde950 bytes f00100f0
- 00bde954 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:d38:8"]]
- 00bde954 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde954 bytes 119e46f9
- 00bde958 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00bde958 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde958 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde958 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde958 bytes 10e23491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbd852b305b8b7b355af280943bcd0e8"></a>

### [`00bde960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde960.md) → [`00bde9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9b0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00af9550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9550.md) [`00afaf58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaf58.md) · 呼出先 1件 [`00afaf58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaf58.md)
- 新版 呼出元 2件 [`00af9594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9594.md) [`00afaf9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaf9c.md) · 呼出先 1件 [`00afaf9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaf9c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde964",
      "READ",
      [
        "storage",
        "00c1dd40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde96c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afaf9c"
      ]
    ]
  ],
  "added": [
    [
      "00bde9b4",
      "READ",
      [
        "storage",
        "00c1dd90",
        null,
        "pointer"
      ]
    ],
    [
      "00bde9bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afaf9c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde960.md#insn-00bde960) · [`00bde964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde960.md#insn-00bde964) · [`00bde968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde960.md#insn-00bde968)

~~~diff
- 00bde960 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde960 bytes f00100f0
- 00bde964 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:d40:8"]]
- 00bde964 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde964 bytes 11a246f9
- 00bde968 ["COPY", "tmp:0:8", ["const:d40:8"]]
- 00bde968 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde968 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde968 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde968 bytes 10023591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c20c305ee5bf1b67163481497f84554"></a>

### [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md) → [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md) &lt;EXTERNAL&gt;::strcmp

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 28件 [`00af8e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8e50.md) [`00af92fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af92fc.md) [`00b03728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03728.md) [`00b03ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03ca4.md) [`00b127dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b127dc.md) · 呼出先 1件 [`010a55b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a55b8.md)
- 新版 呼出元 28件 [`00af8e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8e94.md) [`00af9340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9340.md) [`00b0376c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b0376c.md) [`00b03ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03ce8.md) [`00b12820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12820.md) · 呼出先 1件 [`010a55b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a55b8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

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
        "00c1dd50",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde98c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a55b8"
      ]
    ]
  ],
  "added": [
    [
      "00bde9d4",
      "READ",
      [
        "storage",
        "00c1dda0",
        null,
        "pointer"
      ]
    ],
    [
      "00bde9dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a55b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md#insn-00bde980) · [`00bde984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md#insn-00bde984) · [`00bde988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md#insn-00bde988)

~~~diff
- 00bde980 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde980 bytes f00100f0
- 00bde984 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:d50:8"]]
- 00bde984 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde984 bytes 11aa46f9
- 00bde988 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 00bde988 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde988 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde988 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde988 bytes 10423591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abf8b3342584493f8e0f1735fbe6f3a1"></a>

### [`00bded20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded20.md) → [`00bded70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded70.md) &lt;EXTERNAL&gt;::__strchr_chk

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00afced4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afced4.md) [`00afd844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd844.md) · 呼出先 1件 [`010a55f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a55f0.md)
- 新版 呼出元 2件 [`00afcf18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcf18.md) [`00afd888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd888.md) · 呼出先 1件 [`010a55f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a55f0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bded24",
      "READ",
      [
        "storage",
        "00c1df20",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bded2c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a55f0"
      ]
    ]
  ],
  "added": [
    [
      "00bded74",
      "READ",
      [
        "storage",
        "00c1df70",
        null,
        "pointer"
      ]
    ],
    [
      "00bded7c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a55f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bded20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded20.md#insn-00bded20) · [`00bded24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded20.md#insn-00bded24) · [`00bded28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded20.md#insn-00bded28)

~~~diff
- 00bded20 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bded20 bytes f00100f0
- 00bded24 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f20:8"]]
- 00bded24 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bded24 bytes 119247f9
- 00bded28 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00bded28 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bded28 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bded28 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bded28 bytes 10823c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5a541be745ca022979f786196a8de7e"></a>

### [`00bdedc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedc0.md) → [`00bdee10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee10.md) _ZN8firebase26ReferenceCountedFutureImpl18ForceReleaseFutureERKNS_12FutureHandleE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00afe760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe760.md) · 呼出先 1件 [`00b00b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00b70.md)
- 新版 呼出元 1件 [`00afe7a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe7a4.md) · 呼出先 1件 [`00b00bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00bb4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdedc4",
      "READ",
      [
        "storage",
        "00c1df70",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdedcc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b00bb4"
      ]
    ]
  ],
  "added": [
    [
      "00bdee14",
      "READ",
      [
        "storage",
        "00c1dfc0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdee1c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b00bb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdedc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedc0.md#insn-00bdedc0) · [`00bdedc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedc0.md#insn-00bdedc4) · [`00bdedc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedc0.md#insn-00bdedc8)

~~~diff
- 00bdedc0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdedc0 bytes f00100f0
- 00bdedc4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f70:8"]]
- 00bdedc4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdedc4 bytes 11ba47f9
- 00bdedc8 ["COPY", "tmp:0:8", ["const:f70:8"]]
- 00bdedc8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdedc8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdedc8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdedc8 bytes 10c23d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7f2d4c96989a5ec0ae427b0bd715c51"></a>

### [`00bdedd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedd0.md) → [`00bdee20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee20.md) _ZN8firebase26ReferenceCountedFutureImplD1Ev

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00afecd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afecd8.md) · 呼出先 1件 [`00afeae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afeae0.md)
- 新版 呼出元 1件 [`00afed1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afed1c.md) · 呼出先 1件 [`00afeb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afeb24.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdedd4",
      "READ",
      [
        "storage",
        "00c1df78",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdeddc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afeb24"
      ]
    ]
  ],
  "added": [
    [
      "00bdee24",
      "READ",
      [
        "storage",
        "00c1dfc8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdee2c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afeb24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdedd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedd0.md#insn-00bdedd0) · [`00bdedd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedd0.md#insn-00bdedd4) · [`00bdedd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedd0.md#insn-00bdedd8)

~~~diff
- 00bdedd0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdedd0 bytes f00100f0
- 00bdedd4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f78:8"]]
- 00bdedd4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdedd4 bytes 11be47f9
- 00bdedd8 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00bdedd8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdedd8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdedd8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdedd8 bytes 10e23d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5514361f8894208c0d2526c25252c28"></a>

### [`00bdee30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee30.md) → [`00bdee80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee80.md) _ZN8firebase16StaticFutureData22GetFutureDataForModuleEPKvi

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b5c848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c848.md) · 呼出先 1件 [`00b02330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02330.md)
- 新版 呼出元 1件 [`00b5c88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c88c.md) · 呼出先 1件 [`00b02374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02374.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdee34",
      "READ",
      [
        "storage",
        "00c1dfa8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdee3c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b02374"
      ]
    ]
  ],
  "added": [
    [
      "00bdee84",
      "READ",
      [
        "storage",
        "00c1dff8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdee8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b02374"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdee30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee30.md#insn-00bdee30) · [`00bdee34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee30.md#insn-00bdee34) · [`00bdee38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee30.md#insn-00bdee38)

~~~diff
- 00bdee30 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdee30 bytes f00100f0
- 00bdee34 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fa8:8"]]
- 00bdee34 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdee34 bytes 11d647f9
- 00bdee38 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 00bdee38 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdee38 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdee38 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdee38 bytes 10a23e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f8be8515d5e5f55e672cb681b808127"></a>

### [`00bdee40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee40.md) → [`00bdee90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee90.md) _ZN8firebase16StaticFutureData26CleanupFutureDataForModuleEPKv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b5c858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c858.md) · 呼出先 1件 [`00b0221c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b0221c.md)
- 新版 呼出元 1件 [`00b5c89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c89c.md) · 呼出先 1件 [`00b02260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02260.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdee44",
      "READ",
      [
        "storage",
        "00c1dfb0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdee4c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b02260"
      ]
    ]
  ],
  "added": [
    [
      "00bdee94",
      "READ",
      [
        "storage",
        "00c1e000",
        null,
        "pointer"
      ]
    ],
    [
      "00bdee9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b02260"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdee40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee40.md#insn-00bdee40) · [`00bdee44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee40.md#insn-00bdee44) · [`00bdee48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee40.md#insn-00bdee48)

~~~diff
- 00bdee40 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdee40 bytes f00100f0
- 00bdee44 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fb0:8"]]
- 00bdee44 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdee44 bytes 11da47f9
- 00bdee48 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 00bdee48 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdee48 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdee48 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdee48 bytes 10c23e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b64040f8b87f6dd46d3a0810d05ef599"></a>

### [`00bdef30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef30.md) → [`00bdef80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef80.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE6assignIPS2_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constru

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b02e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02e7c.md) · 呼出先 1件 [`00b04d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04d7c.md)
- 新版 呼出元 1件 [`00b02ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ec0.md) · 呼出先 1件 [`00b04dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04dc0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdef34",
      "READ",
      [
        "storage",
        "00c1e028",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdef3c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b04dc0"
      ]
    ]
  ],
  "added": [
    [
      "00bdef84",
      "READ",
      [
        "storage",
        "00c1e078",
        null,
        "pointer"
      ]
    ],
    [
      "00bdef8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b04dc0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdef30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef30.md#insn-00bdef30) · [`00bdef34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef30.md#insn-00bdef34) · [`00bdef38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef30.md#insn-00bdef38)

~~~diff
- 00bdef30 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdef30 bytes 10020090
- 00bdef34 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:28:8"]]
- 00bdef34 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdef34 bytes 111640f9
- 00bdef38 ["COPY", "tmp:0:8", ["const:28:8"]]
- 00bdef38 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdef38 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdef38 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdef38 bytes 10a20091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32ac508fe0f9e8917db28449673ba71c"></a>

### [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md) → [`00bdef90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef90.md) _ZdaPv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 16件 [`00b031c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b031c0.md) [`00b0cefc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cefc.md) [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) [`00b2e5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e5f0.md) [`00b47b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47b58.md) · 呼出先 1件 [`00bd4ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4ee4.md)
- 新版 呼出元 16件 [`00b03204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03204.md) [`00b0cf40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0c/00b0cf40.md) [`00b195a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b195a8.md) [`00b2e634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2e634.md) [`00b47b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47b9c.md) · 呼出先 1件 [`00bd4f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4f28.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdef44",
      "READ",
      [
        "storage",
        "00c1e030",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdef4c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bd4f28"
      ]
    ]
  ],
  "added": [
    [
      "00bdef94",
      "READ",
      [
        "storage",
        "00c1e080",
        null,
        "pointer"
      ]
    ],
    [
      "00bdef9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bd4f28"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md#insn-00bdef40) · [`00bdef44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md#insn-00bdef44) · [`00bdef48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md#insn-00bdef48)

~~~diff
- 00bdef40 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdef40 bytes 10020090
- 00bdef44 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:30:8"]]
- 00bdef44 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdef44 bytes 111a40f9
- 00bdef48 ["COPY", "tmp:0:8", ["const:30:8"]]
- 00bdef48 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdef48 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdef48 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdef48 bytes 10c20091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0e3f399de4e52519ee55bd1fb31c049"></a>

### [`00bdf030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf030.md) → [`00bdf080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf080.md) _ZN20google_play_services23MakeAvailableLastResultEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b0df30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0df30.md) · 呼出先 1件 [`00b0e154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e154.md)
- 新版 呼出元 1件 [`00b0df74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0df74.md) · 呼出先 1件 [`00b0e198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e198.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf034",
      "READ",
      [
        "storage",
        "00c1e0a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf03c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b0e198"
      ]
    ]
  ],
  "added": [
    [
      "00bdf084",
      "READ",
      [
        "storage",
        "00c1e0f8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf08c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b0e198"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf030.md#insn-00bdf030) · [`00bdf034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf030.md#insn-00bdf034) · [`00bdf038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf030.md#insn-00bdf038)

~~~diff
- 00bdf030 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf030 bytes f00100f0
- 00bdf034 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a8:8"]]
- 00bdf034 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf034 bytes 115640f9
- 00bdf038 ["COPY", "tmp:0:8", ["const:a8:8"]]
- 00bdf038 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf038 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf038 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf038 bytes 10a20291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9b23d010ba425c84f74d673a68f2a89"></a>

### [`00bdf0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0c0.md) → [`00bdf110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf110.md) _ZN10reflection12FieldBuilder14add_deprecatedEb

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2b0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b0a8.md) · 呼出先 1件 [`00b34ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34ccc.md)
- 新版 呼出元 1件 [`00b2b0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2b0ec.md) · 呼出先 1件 [`00b34d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b34/00b34d10.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf0c4",
      "READ",
      [
        "storage",
        "00c1e0f0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf0cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b34d10"
      ]
    ]
  ],
  "added": [
    [
      "00bdf114",
      "READ",
      [
        "storage",
        "00c1e140",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf11c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b34d10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0c0.md#insn-00bdf0c0) · [`00bdf0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0c0.md#insn-00bdf0c4) · [`00bdf0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0c0.md#insn-00bdf0c8)

~~~diff
- 00bdf0c0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf0c0 bytes f00100f0
- 00bdf0c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f0:8"]]
- 00bdf0c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf0c4 bytes 117a40f9
- 00bdf0c8 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00bdf0c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf0c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf0c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf0c8 bytes 10c20391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9a81f92935b4efd76405948d33e6ca5"></a>

### [`00bdf200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf200.md) → [`00bdf250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf250.md) _ZN11flatbuffers11SymbolTableINS_7RPCCallEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b22414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22414.md) [`00b2baf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2baf8.md) · 呼出先 1件 [`00b22e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22e30.md)
- 新版 呼出元 2件 [`00b22458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22458.md) [`00b2bb3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2bb3c.md) · 呼出先 1件 [`00b22e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22e74.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf204",
      "READ",
      [
        "storage",
        "00c1e190",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf20c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b22e74"
      ]
    ]
  ],
  "added": [
    [
      "00bdf254",
      "READ",
      [
        "storage",
        "00c1e1e0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf25c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b22e74"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf200.md#insn-00bdf200) · [`00bdf204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf200.md#insn-00bdf204) · [`00bdf208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf200.md#insn-00bdf208)

~~~diff
- 00bdf200 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf200 bytes f00100f0
- 00bdf204 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:190:8"]]
- 00bdf204 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf204 bytes 11ca40f9
- 00bdf208 ["COPY", "tmp:0:8", ["const:190:8"]]
- 00bdf208 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf208 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf208 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf208 bytes 10420691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6651b5802171a90ce13f39915269e68e"></a>

### [`00bdf2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf2a0.md) → [`00bdf2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2f0.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE3EaEENS_12CheckedErrorEPli

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2ef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ef70.md) · 呼出先 1件 [`00b2f574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f574.md)
- 新版 呼出元 1件 [`00b2efb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2efb4.md) · 呼出先 1件 [`00b2f5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f5b8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf2a4",
      "READ",
      [
        "storage",
        "00c1e1e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf2ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2f5b8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf2f4",
      "READ",
      [
        "storage",
        "00c1e230",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf2fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2f5b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf2a0.md#insn-00bdf2a0) · [`00bdf2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf2a0.md#insn-00bdf2a4) · [`00bdf2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf2a0.md#insn-00bdf2a8)

~~~diff
- 00bdf2a0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf2a0 bytes f00100f0
- 00bdf2a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1e0:8"]]
- 00bdf2a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf2a4 bytes 11f240f9
- 00bdf2a8 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 00bdf2a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf2a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf2a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf2a8 bytes 10820791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-434b087a253c25fd2ef421f663109779"></a>

### [`00bdf2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf2b0.md) → [`00bdf300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf300.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE4EhEENS_12CheckedErrorEPli

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2ef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ef70.md) · 呼出先 1件 [`00b2f7ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f7ac.md)
- 新版 呼出元 1件 [`00b2efb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2efb4.md) · 呼出先 1件 [`00b2f7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f7f0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf2b4",
      "READ",
      [
        "storage",
        "00c1e1e8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf2bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2f7f0"
      ]
    ]
  ],
  "added": [
    [
      "00bdf304",
      "READ",
      [
        "storage",
        "00c1e238",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf30c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2f7f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf2b0.md#insn-00bdf2b0) · [`00bdf2b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf2b0.md#insn-00bdf2b4) · [`00bdf2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf2b0.md#insn-00bdf2b8)

~~~diff
- 00bdf2b0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf2b0 bytes f00100f0
- 00bdf2b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1e8:8"]]
- 00bdf2b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf2b4 bytes 11f640f9
- 00bdf2b8 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00bdf2b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf2b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf2b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf2b8 bytes 10a20791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9f373d8f41a72c015afa2238859e1c8"></a>

### [`00bdf380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf380.md) → [`00bdf3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf3d0.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection4EnumEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b28904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28904.md) · 呼出先 1件 [`00b3d674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d674.md)
- 新版 呼出元 1件 [`00b28948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b28948.md) · 呼出先 1件 [`00b3d6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3d6b8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf384",
      "READ",
      [
        "storage",
        "00c1e250",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf38c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3d6b8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf3d4",
      "READ",
      [
        "storage",
        "00c1e2a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf3dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3d6b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf380.md#insn-00bdf380) · [`00bdf384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf380.md#insn-00bdf384) · [`00bdf388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf380.md#insn-00bdf388)

~~~diff
- 00bdf380 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf380 bytes f00100f0
- 00bdf384 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:250:8"]]
- 00bdf384 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf384 bytes 112a41f9
- 00bdf388 ["COPY", "tmp:0:8", ["const:250:8"]]
- 00bdf388 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf388 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf388 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf388 bytes 10420991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5ff0b7ed5ab48b06de5b42468419e5f"></a>

### [`00bdf3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3e0.md) → [`00bdf430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf430.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection8KeyValueEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b29c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b29c10.md) · 呼出先 1件 [`00b39cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39cfc.md)
- 新版 呼出元 1件 [`00b29c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b29/00b29c54.md) · 呼出先 1件 [`00b39d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b39/00b39d40.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf3e4",
      "READ",
      [
        "storage",
        "00c1e280",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf3ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b39d40"
      ]
    ]
  ],
  "added": [
    [
      "00bdf434",
      "READ",
      [
        "storage",
        "00c1e2d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf43c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b39d40"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3e0.md#insn-00bdf3e0) · [`00bdf3e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3e0.md#insn-00bdf3e4) · [`00bdf3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3e0.md#insn-00bdf3e8)

~~~diff
- 00bdf3e0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf3e0 bytes f00100f0
- 00bdf3e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:280:8"]]
- 00bdf3e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf3e4 bytes 114241f9
- 00bdf3e8 ["COPY", "tmp:0:8", ["const:280:8"]]
- 00bdf3e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf3e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf3e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf3e8 bytes 10020a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ad82cda150901854299578ab500a995"></a>

### [`00bdf420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf420.md) → [`00bdf470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf470.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIiEEjT_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00b1711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md) [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) [`00b1c92c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c92c.md) [`00b2a064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2a064.md) · 呼出先 1件 [`00b1b684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b684.md)
- 新版 呼出元 6件 [`00b17160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17160.md) [`00b18d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md) [`00b195a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b195a8.md) [`00b1c970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c970.md) [`00b2a0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2a0a8.md) · 呼出先 1件 [`00b1b6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1b6c8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf424",
      "READ",
      [
        "storage",
        "00c1e2a0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf42c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1b6c8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf474",
      "READ",
      [
        "storage",
        "00c1e2f0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf47c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1b6c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf420.md#insn-00bdf420) · [`00bdf424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf420.md#insn-00bdf424) · [`00bdf428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf420.md#insn-00bdf428)

~~~diff
- 00bdf420 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf420 bytes f00100f0
- 00bdf424 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2a0:8"]]
- 00bdf424 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf424 bytes 115241f9
- 00bdf428 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 00bdf428 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf428 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf428 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf428 bytes 10820a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1acbee9ae9cdf4edb72bae74bd823dd7"></a>

### [`00bdf440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf440.md) → [`00bdf490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf490.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIlEEjT_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00b1711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md) [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) [`00b2b0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b0a8.md) [`00b2c564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c564.md) · 呼出先 1件 [`00b1bc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bc3c.md)
- 新版 呼出元 5件 [`00b17160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17160.md) [`00b18d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md) [`00b195a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b195a8.md) [`00b2b0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2b0ec.md) [`00b2c5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c5a8.md) · 呼出先 1件 [`00b1bc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1bc80.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf444",
      "READ",
      [
        "storage",
        "00c1e2b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf44c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1bc80"
      ]
    ]
  ],
  "added": [
    [
      "00bdf494",
      "READ",
      [
        "storage",
        "00c1e300",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf49c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1bc80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf440.md#insn-00bdf440) · [`00bdf444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf440.md#insn-00bdf444) · [`00bdf448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf440.md#insn-00bdf448)

~~~diff
- 00bdf440 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf440 bytes f00100f0
- 00bdf444 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2b0:8"]]
- 00bdf444 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf444 bytes 115a41f9
- 00bdf448 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 00bdf448 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf448 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf448 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf448 bytes 10c20a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a33069d839f633b4fbd29db800aa49b1"></a>

### [`00bdf450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf450.md) → [`00bdf4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf4a0.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementImEEjT_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b1711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md) [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) · 呼出先 1件 [`00b1c158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c158.md)
- 新版 呼出元 3件 [`00b17160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17160.md) [`00b18d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md) [`00b195a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b195a8.md) · 呼出先 1件 [`00b1c19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c19c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf454",
      "READ",
      [
        "storage",
        "00c1e2b8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf45c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1c19c"
      ]
    ]
  ],
  "added": [
    [
      "00bdf4a4",
      "READ",
      [
        "storage",
        "00c1e308",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf4ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1c19c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf450.md#insn-00bdf450) · [`00bdf454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf450.md#insn-00bdf454) · [`00bdf458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf450.md#insn-00bdf458)

~~~diff
- 00bdf450 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf450 bytes f00100f0
- 00bdf454 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2b8:8"]]
- 00bdf454 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf454 bytes 115e41f9
- 00bdf458 ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 00bdf458 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf458 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf458 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf458 bytes 10e20a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e692f9e8dcde725d7c225e9c2c9c5f3"></a>

### [`00bdf460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf460.md) → [`00bdf4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf4b0.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIvEEjNS_6OffsetIT_EE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) · 呼出先 1件 [`00b1cc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cc40.md)
- 新版 呼出元 2件 [`00b18d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md) [`00b195a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b195a8.md) · 呼出先 1件 [`00b1cc84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cc84.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf464",
      "READ",
      [
        "storage",
        "00c1e2c0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf46c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1cc84"
      ]
    ]
  ],
  "added": [
    [
      "00bdf4b4",
      "READ",
      [
        "storage",
        "00c1e310",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf4bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1cc84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf460.md#insn-00bdf460) · [`00bdf464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf460.md#insn-00bdf464) · [`00bdf468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf460.md#insn-00bdf468)

~~~diff
- 00bdf460 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf460 bytes f00100f0
- 00bdf464 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2c0:8"]]
- 00bdf464 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf464 bytes 116241f9
- 00bdf468 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 00bdf468 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf468 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf468 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf468 bytes 10020b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f93865a95d3f103128c94742974fc92"></a>

### [`00bdf480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf480.md) → [`00bdf4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf4d0.md) _ZN11flatbuffers17FlatBufferBuilder12CreateStringEPKcm

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`00b154d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b154d4.md) [`00b28904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28904.md) [`00b291bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b291bc.md) [`00b29458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b29458.md) [`00b2976c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b2976c.md) · 呼出先 1件 [`00b2e4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e4b4.md)
- 新版 呼出元 10件 [`00b15518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b15518.md) [`00b28948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b28948.md) [`00b29200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b29/00b29200.md) [`00b2949c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b29/00b2949c.md) [`00b297b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b29/00b297b0.md) · 呼出先 1件 [`00b2e4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2e4f8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf484",
      "READ",
      [
        "storage",
        "00c1e2d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf48c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2e4f8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf4d4",
      "READ",
      [
        "storage",
        "00c1e320",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf4dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2e4f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf480.md#insn-00bdf480) · [`00bdf484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf480.md#insn-00bdf484) · [`00bdf488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf480.md#insn-00bdf488)

~~~diff
- 00bdf480 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf480 bytes f00100f0
- 00bdf484 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2d0:8"]]
- 00bdf484 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf484 bytes 116a41f9
- 00bdf488 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 00bdf488 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf488 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf488 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf488 bytes 10420b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7700dfc7699e213f8dc8e2e5397039b8"></a>

### [`00bdf490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf490.md) → [`00bdf4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf4e0.md) _ZN11flatbuffers17FlatBufferBuilder12CreateVectorIhEENS_6OffsetINS_6VectorIT_EEEERKNSt6__ndk16vectorIS4_NS7_9allocatorIS4_EEEE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b3fc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3fc88.md) · 呼出先 1件 [`00b40328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40328.md)
- 新版 呼出元 1件 [`00b3fccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3fccc.md) · 呼出先 1件 [`00b4036c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b4036c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf494",
      "READ",
      [
        "storage",
        "00c1e2d8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf49c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4036c"
      ]
    ]
  ],
  "added": [
    [
      "00bdf4e4",
      "READ",
      [
        "storage",
        "00c1e328",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf4ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4036c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf490.md#insn-00bdf490) · [`00bdf494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf490.md#insn-00bdf494) · [`00bdf498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf490.md#insn-00bdf498)

~~~diff
- 00bdf490 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf490 bytes f00100f0
- 00bdf494 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2d8:8"]]
- 00bdf494 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf494 bytes 116e41f9
- 00bdf498 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 00bdf498 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf498 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf498 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf498 bytes 10620b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86e06eff11c127c0874667fafad75dcd"></a>

### [`00bdf550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf550.md) → [`00bdf5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5a0.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6VectorINS_6OffsetIN10reflection7ServiceEEEEEEEvtNS3_IT_EE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b28904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28904.md) · 呼出先 1件 [`00b33f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33f84.md)
- 新版 呼出元 1件 [`00b28948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b28948.md) · 呼出先 1件 [`00b33fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33fc8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf554",
      "READ",
      [
        "storage",
        "00c1e338",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf55c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b33fc8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf5a4",
      "READ",
      [
        "storage",
        "00c1e388",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf5ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b33fc8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf550.md#insn-00bdf550) · [`00bdf554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf550.md#insn-00bdf554) · [`00bdf558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf550.md#insn-00bdf558)

~~~diff
- 00bdf550 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf550 bytes f00100f0
- 00bdf554 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:338:8"]]
- 00bdf554 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf554 bytes 119e41f9
- 00bdf558 ["COPY", "tmp:0:8", ["const:338:8"]]
- 00bdf558 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf558 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf558 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf558 bytes 10e20c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09ed15ab5e8935332859f0ff0036cae1"></a>

### [`00bdf5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5a0.md) → [`00bdf5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf5f0.md) _ZN11flatbuffers19StringToIntegerImplImEEbPT_PKcib

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b14e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b14/00b14e90.md) [`00b1bd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bd28.md) [`00b20bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20bb4.md) · 呼出先 1件 [`00b2e23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e23c.md)
- 新版 呼出元 3件 [`00b14ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b14/00b14ed4.md) [`00b1bd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1bd6c.md) [`00b20bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b20bf8.md) · 呼出先 1件 [`00b2e280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2e280.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf5a4",
      "READ",
      [
        "storage",
        "00c1e360",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf5ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2e280"
      ]
    ]
  ],
  "added": [
    [
      "00bdf5f4",
      "READ",
      [
        "storage",
        "00c1e3b0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf5fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2e280"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5a0.md#insn-00bdf5a0) · [`00bdf5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5a0.md#insn-00bdf5a4) · [`00bdf5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5a0.md#insn-00bdf5a8)

~~~diff
- 00bdf5a0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf5a0 bytes f00100f0
- 00bdf5a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:360:8"]]
- 00bdf5a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf5a4 bytes 11b241f9
- 00bdf5a8 ["COPY", "tmp:0:8", ["const:360:8"]]
- 00bdf5a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf5a8 bytes 10820d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae358cd17f0c4407c2dca0261f739d4d"></a>

### [`00bdf5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5b0.md) → [`00bdf600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf600.md) _ZN11flatbuffers20TypeToIntervalStringIaEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b1a2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a2f8.md) [`00b2f574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f574.md) · 呼出先 1件 [`00b308b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b308b8.md)
- 新版 呼出元 2件 [`00b1a33c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1a33c.md) [`00b2f5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f5b8.md) · 呼出先 1件 [`00b308fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b308fc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf5b4",
      "READ",
      [
        "storage",
        "00c1e368",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf5bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b308fc"
      ]
    ]
  ],
  "added": [
    [
      "00bdf604",
      "READ",
      [
        "storage",
        "00c1e3b8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf60c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b308fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5b0.md#insn-00bdf5b0) · [`00bdf5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5b0.md#insn-00bdf5b4) · [`00bdf5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5b0.md#insn-00bdf5b8)

~~~diff
- 00bdf5b0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf5b0 bytes f00100f0
- 00bdf5b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:368:8"]]
- 00bdf5b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf5b4 bytes 11b641f9
- 00bdf5b8 ["COPY", "tmp:0:8", ["const:368:8"]]
- 00bdf5b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf5b8 bytes 10a20d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06c98f72aca5b125b11bd248e2f4fcc3"></a>

### [`00bdf5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5c0.md) → [`00bdf610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf610.md) _ZN11flatbuffers20TypeToIntervalStringIhEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00b16c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16c88.md) [`00b2f10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f10c.md) [`00b2f340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f340.md) [`00b2f7ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f7ac.md) · 呼出先 1件 [`00b30718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30718.md)
- 新版 呼出元 4件 [`00b16ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16ccc.md) [`00b2f150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f150.md) [`00b2f384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f384.md) [`00b2f7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f7f0.md) · 呼出先 1件 [`00b3075c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b3075c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf5c4",
      "READ",
      [
        "storage",
        "00c1e370",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf5cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3075c"
      ]
    ]
  ],
  "added": [
    [
      "00bdf614",
      "READ",
      [
        "storage",
        "00c1e3c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf61c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3075c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5c0.md#insn-00bdf5c0) · [`00bdf5c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5c0.md#insn-00bdf5c4) · [`00bdf5c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5c0.md#insn-00bdf5c8)

~~~diff
- 00bdf5c0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf5c0 bytes f00100f0
- 00bdf5c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:370:8"]]
- 00bdf5c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf5c4 bytes 11ba41f9
- 00bdf5c8 ["COPY", "tmp:0:8", ["const:370:8"]]
- 00bdf5c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf5c8 bytes 10c20d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3304402bfadcf9bc826ae94c08c47fc3"></a>

### [`00bdf5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5d0.md) → [`00bdf620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf620.md) _ZN11flatbuffers20TypeToIntervalStringIiEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b1b220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b220.md) [`00b2fe4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2fe4c.md) · 呼出先 1件 [`00b30d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30d98.md)
- 新版 呼出元 2件 [`00b1b264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1b264.md) [`00b2fe90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2fe90.md) · 呼出先 1件 [`00b30ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30ddc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf5d4",
      "READ",
      [
        "storage",
        "00c1e378",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf5dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b30ddc"
      ]
    ]
  ],
  "added": [
    [
      "00bdf624",
      "READ",
      [
        "storage",
        "00c1e3c8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf62c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b30ddc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5d0.md#insn-00bdf5d0) · [`00bdf5d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5d0.md#insn-00bdf5d4) · [`00bdf5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5d0.md#insn-00bdf5d8)

~~~diff
- 00bdf5d0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf5d0 bytes f00100f0
- 00bdf5d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:378:8"]]
- 00bdf5d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf5d4 bytes 11be41f9
- 00bdf5d8 ["COPY", "tmp:0:8", ["const:378:8"]]
- 00bdf5d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf5d8 bytes 10e20d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a585ac8c1dfed86b65410d9bf3d41cf6"></a>

### [`00bdf5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5e0.md) → [`00bdf630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf630.md) _ZN11flatbuffers20TypeToIntervalStringIjEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b163f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b163f0.md) [`00b30088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30088.md) · 呼出先 1件 [`00b30f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30f38.md)
- 新版 呼出元 2件 [`00b16434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16434.md) [`00b300cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b300cc.md) · 呼出先 1件 [`00b30f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30f7c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf5e4",
      "READ",
      [
        "storage",
        "00c1e380",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf5ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b30f7c"
      ]
    ]
  ],
  "added": [
    [
      "00bdf634",
      "READ",
      [
        "storage",
        "00c1e3d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf63c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b30f7c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5e0.md#insn-00bdf5e0) · [`00bdf5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5e0.md#insn-00bdf5e4) · [`00bdf5e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5e0.md#insn-00bdf5e8)

~~~diff
- 00bdf5e0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf5e0 bytes f00100f0
- 00bdf5e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:380:8"]]
- 00bdf5e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf5e4 bytes 11c241f9
- 00bdf5e8 ["COPY", "tmp:0:8", ["const:380:8"]]
- 00bdf5e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf5e8 bytes 10020e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b916a4d75f76c72fa17889f7886c1049"></a>

### [`00bdf5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5f0.md) → [`00bdf640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf640.md) _ZN11flatbuffers20TypeToIntervalStringIlEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b1b85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b85c.md) [`00b302bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b302bc.md) · 呼出先 1件 [`00b310d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b310d8.md)
- 新版 呼出元 2件 [`00b1b8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1b8a0.md) [`00b30300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30300.md) · 呼出先 1件 [`00b3111c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3111c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

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
        "00c1e388",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf5fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3111c"
      ]
    ]
  ],
  "added": [
    [
      "00bdf644",
      "READ",
      [
        "storage",
        "00c1e3d8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf64c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3111c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5f0.md#insn-00bdf5f0) · [`00bdf5f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5f0.md#insn-00bdf5f4) · [`00bdf5f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5f0.md#insn-00bdf5f8)

~~~diff
- 00bdf5f0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf5f0 bytes f00100f0
- 00bdf5f4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:388:8"]]
- 00bdf5f4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf5f4 bytes 11c641f9
- 00bdf5f8 ["COPY", "tmp:0:8", ["const:388:8"]]
- 00bdf5f8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5f8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5f8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf5f8 bytes 10220e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a99ae88ba43dab935ec51e62bc8b8d8b"></a>

### [`00bdf600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf600.md) → [`00bdf650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf650.md) _ZN11flatbuffers20TypeToIntervalStringImEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b1bd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bd28.md) [`00b304ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b304ec.md) · 呼出先 1件 [`00b31278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31278.md)
- 新版 呼出元 2件 [`00b1bd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1bd6c.md) [`00b30530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30530.md) · 呼出先 1件 [`00b312bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b312bc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf604",
      "READ",
      [
        "storage",
        "00c1e390",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf60c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b312bc"
      ]
    ]
  ],
  "added": [
    [
      "00bdf654",
      "READ",
      [
        "storage",
        "00c1e3e0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf65c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b312bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf600.md#insn-00bdf600) · [`00bdf604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf600.md#insn-00bdf604) · [`00bdf608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf600.md#insn-00bdf608)

~~~diff
- 00bdf600 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf600 bytes f00100f0
- 00bdf604 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:390:8"]]
- 00bdf604 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf604 bytes 11ca41f9
- 00bdf608 ["COPY", "tmp:0:8", ["const:390:8"]]
- 00bdf608 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf608 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf608 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf608 bytes 10420e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-171428d22b780c5ded4f7fcbeb1c1cb9"></a>

### [`00bdf630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf630.md) → [`00bdf680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf680.md) _ZN11flatbuffers4Type11DeserializeERKNS_6ParserEPKN10reflection4TypeE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b2ab04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2ab04.md) [`00b2beac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2beac.md) [`00b2c204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c204.md) · 呼出先 1件 [`00b2b2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b2e4.md)
- 新版 呼出元 3件 [`00b2ab48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2ab48.md) [`00b2bef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2bef0.md) [`00b2c248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c248.md) · 呼出先 1件 [`00b2b328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2b328.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf634",
      "READ",
      [
        "storage",
        "00c1e3a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf63c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2b328"
      ]
    ]
  ],
  "added": [
    [
      "00bdf684",
      "READ",
      [
        "storage",
        "00c1e3f8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf68c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2b328"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf630.md#insn-00bdf630) · [`00bdf634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf630.md#insn-00bdf634) · [`00bdf638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf630.md#insn-00bdf638)

~~~diff
- 00bdf630 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf630 bytes f00100f0
- 00bdf634 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:3a8:8"]]
- 00bdf634 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf634 bytes 11d641f9
- 00bdf638 ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 00bdf638 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf638 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf638 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf638 bytes 10a20e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42f4f516ae8282b86f6285865f2b3380"></a>

### [`00bdf640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf640.md) → [`00bdf690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf690.md) _ZN11flatbuffers4atotIaEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00b13df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b13/00b13df8.md) [`00b1711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md) [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) · 呼出先 1件 [`00b1a2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a2f8.md)
- 新版 呼出元 4件 [`00b13e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e3c.md) [`00b17160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17160.md) [`00b18d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md) [`00b195a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b195a8.md) · 呼出先 1件 [`00b1a33c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1a33c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf644",
      "READ",
      [
        "storage",
        "00c1e3b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf64c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1a33c"
      ]
    ]
  ],
  "added": [
    [
      "00bdf694",
      "READ",
      [
        "storage",
        "00c1e400",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf69c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1a33c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf640.md#insn-00bdf640) · [`00bdf644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf640.md#insn-00bdf644) · [`00bdf648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf640.md#insn-00bdf648)

~~~diff
- 00bdf640 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf640 bytes f00100f0
- 00bdf644 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:3b0:8"]]
- 00bdf644 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf644 bytes 11da41f9
- 00bdf648 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 00bdf648 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf648 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf648 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf648 bytes 10c20e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9c47f78ae7388c3d8be33d71355d4fa"></a>

### [`00bdf650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf650.md) → [`00bdf6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf6a0.md) _ZN11flatbuffers4atotIdEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00b13df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b13/00b13df8.md) [`00b1711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md) [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) [`00b1e394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e394.md) · 呼出先 1件 [`00b1c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c518.md)
- 新版 呼出元 5件 [`00b13e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e3c.md) [`00b17160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17160.md) [`00b18d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md) [`00b195a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b195a8.md) [`00b1e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e3d8.md) · 呼出先 1件 [`00b1c55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c55c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf654",
      "READ",
      [
        "storage",
        "00c1e3b8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf65c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1c55c"
      ]
    ]
  ],
  "added": [
    [
      "00bdf6a4",
      "READ",
      [
        "storage",
        "00c1e408",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf6ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1c55c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf650.md#insn-00bdf650) · [`00bdf654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf650.md#insn-00bdf654) · [`00bdf658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf650.md#insn-00bdf658)

~~~diff
- 00bdf650 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf650 bytes f00100f0
- 00bdf654 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:3b8:8"]]
- 00bdf654 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf654 bytes 11de41f9
- 00bdf658 ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 00bdf658 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf658 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf658 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf658 bytes 10e20e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09b76e79e1b95f953d0f102f6e7e8cd7"></a>

### [`00bdf660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf660.md) → [`00bdf6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf6b0.md) _ZN11flatbuffers4atotIfEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00b13df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b13/00b13df8.md) [`00b1711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md) [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) · 呼出先 1件 [`00b1c244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c244.md)
- 新版 呼出元 4件 [`00b13e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e3c.md) [`00b17160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17160.md) [`00b18d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md) [`00b195a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b195a8.md) · 呼出先 1件 [`00b1c288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c288.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf664",
      "READ",
      [
        "storage",
        "00c1e3c0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf66c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1c288"
      ]
    ]
  ],
  "added": [
    [
      "00bdf6b4",
      "READ",
      [
        "storage",
        "00c1e410",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf6bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1c288"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf660.md#insn-00bdf664) · [`00bdf668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf660.md#insn-00bdf668) · [`00bdf66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf660.md#insn-00bdf66c)

~~~diff
- 00bdf664 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:3c0:8"]]
- 00bdf664 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf664 bytes 11e241f9
- 00bdf668 ["COPY", "tmp:0:8", ["const:3c0:8"]]
- 00bdf668 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf668 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf668 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf668 bytes 10020f91
- 00bdf66c ["COPY", "register:0:8", ["register:4088:8"]]
- 00bdf66c ["BRANCHIND", null, ["register:0:8"]]
- 00bdf66c bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8637e4c08573b8292ecaed0d0641b691"></a>

### [`00bdfc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc90.md) → [`00bdfce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfce0.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbEENS_19__map_value_compareIS7_S8_NS_4lessI

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b29c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b29c10.md) · 呼出先 1件 [`00b46434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46434.md)
- 新版 呼出元 1件 [`00b29c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b29/00b29c54.md) · 呼出先 1件 [`00b46478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46478.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfc94",
      "READ",
      [
        "storage",
        "00c1e6d8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdfc9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b46478"
      ]
    ]
  ],
  "added": [
    [
      "00bdfce4",
      "READ",
      [
        "storage",
        "00c1e728",
        null,
        "pointer"
      ]
    ],
    [
      "00bdfcec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b46478"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc90.md#insn-00bdfc90) · [`00bdfc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc90.md#insn-00bdfc94) · [`00bdfc98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc90.md#insn-00bdfc98)

~~~diff
- 00bdfc90 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdfc90 bytes f00100f0
- 00bdfc94 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:6d8:8"]]
- 00bdfc94 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdfc94 bytes 116e43f9
- 00bdfc98 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 00bdfc98 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfc98 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfc98 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdfc98 bytes 10621b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c94d6808938b4d70558b2d5b5b28135f"></a>

### [`00bdfde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfde0.md) → [`00bdfe30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfe30.md) _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEbT0_SA_T_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b44a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44a00.md) · 呼出先 1件 [`00b45300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45300.md)
- 新版 呼出元 1件 [`00b44a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44a44.md) · 呼出先 1件 [`00b45344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45344.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfde4",
      "READ",
      [
        "storage",
        "00c1e780",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdfdec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b45344"
      ]
    ]
  ],
  "added": [
    [
      "00bdfe34",
      "READ",
      [
        "storage",
        "00c1e7d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdfe3c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b45344"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfde0.md#insn-00bdfde0) · [`00bdfde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfde0.md#insn-00bdfde4) · [`00bdfde8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfde0.md#insn-00bdfde8)

~~~diff
- 00bdfde0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdfde0 bytes f00100f0
- 00bdfde4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:780:8"]]
- 00bdfde4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdfde4 bytes 11c243f9
- 00bdfde8 ["COPY", "tmp:0:8", ["const:780:8"]]
- 00bdfde8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfde8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfde8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdfde8 bytes 10021e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-325b9bcacb2550ef181ef13bdd1ea156"></a>

### [`00bdfe60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe60.md) → [`00bdfeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfeb0.md) _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b2186c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b2186c.md) [`00b4307c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b4307c.md) · 呼出先 1件 [`00b4307c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b4307c.md)
- 新版 呼出元 2件 [`00b218b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b21/00b218b0.md) [`00b430c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b430c0.md) · 呼出先 1件 [`00b430c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b430c0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfe64",
      "READ",
      [
        "storage",
        "00c1e7c0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdfe6c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b430c0"
      ]
    ]
  ],
  "added": [
    [
      "00bdfeb4",
      "READ",
      [
        "storage",
        "00c1e810",
        null,
        "pointer"
      ]
    ],
    [
      "00bdfebc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b430c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfe60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe60.md#insn-00bdfe60) · [`00bdfe64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe60.md#insn-00bdfe64) · [`00bdfe68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe60.md#insn-00bdfe68)

~~~diff
- 00bdfe60 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdfe60 bytes f00100f0
- 00bdfe64 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:7c0:8"]]
- 00bdfe64 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdfe64 bytes 11e243f9
- 00bdfe68 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 00bdfe68 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfe68 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfe68 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdfe68 bytes 10021f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc70ac9771e23fd8611c3671c0d94b81"></a>

### [`00bdfe70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe70.md) → [`00bdfec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfec0.md) _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b28f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28f64.md) [`00b44a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44a00.md) · 呼出先 1件 [`00b44a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44a00.md)
- 新版 呼出元 2件 [`00b28fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b28fa8.md) [`00b44a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44a44.md) · 呼出先 1件 [`00b44a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44a44.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfe74",
      "READ",
      [
        "storage",
        "00c1e7c8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdfe7c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b44a44"
      ]
    ]
  ],
  "added": [
    [
      "00bdfec4",
      "READ",
      [
        "storage",
        "00c1e818",
        null,
        "pointer"
      ]
    ],
    [
      "00bdfecc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b44a44"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfe70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe70.md#insn-00bdfe70) · [`00bdfe74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe70.md#insn-00bdfe74) · [`00bdfe78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe70.md#insn-00bdfe78)

~~~diff
- 00bdfe70 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdfe70 bytes f00100f0
- 00bdfe74 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:7c8:8"]]
- 00bdfe74 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdfe74 bytes 11e643f9
- 00bdfe78 ["COPY", "tmp:0:8", ["const:7c8:8"]]
- 00bdfe78 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfe78 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfe78 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdfe78 bytes 10221f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7730838927e55c25164e19006e6077e6"></a>

### [`00bdff50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff50.md) → [`00bdffa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdffa0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2c3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c3ac.md) · 呼出先 1件 [`00b42bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42bd4.md)
- 新版 呼出元 1件 [`00b2c3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c3f0.md) · 呼出先 1件 [`00b42c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42c18.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdff54",
      "READ",
      [
        "storage",
        "00c1e838",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdff5c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b42c18"
      ]
    ]
  ],
  "added": [
    [
      "00bdffa4",
      "READ",
      [
        "storage",
        "00c1e888",
        null,
        "pointer"
      ]
    ],
    [
      "00bdffac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b42c18"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdff50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff50.md#insn-00bdff50) · [`00bdff54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff50.md#insn-00bdff54) · [`00bdff58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff50.md#insn-00bdff58)

~~~diff
- 00bdff50 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdff50 bytes f00100f0
- 00bdff54 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:838:8"]]
- 00bdff54 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdff54 bytes 111e44f9
- 00bdff58 ["COPY", "tmp:0:8", ["const:838:8"]]
- 00bdff58 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdff58 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdff58 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdff58 bytes 10e22091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a356892a27e6797b64e665db502adee3"></a>

### [`00be0080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0080.md) → [`00be00d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00d0.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertENS_11__wrap_iterIPKhEEmRS5_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b2628c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b2628c.md) [`00b32104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32104.md) [`00b33c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33c1c.md) · 呼出先 1件 [`00b3335c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b3335c.md)
- 新版 呼出元 3件 [`00b262d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b262d0.md) [`00b32148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b32/00b32148.md) [`00b33c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33c60.md) · 呼出先 1件 [`00b333a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b333a0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0084",
      "READ",
      [
        "storage",
        "00c1e8d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be008c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b333a0"
      ]
    ]
  ],
  "added": [
    [
      "00be00d4",
      "READ",
      [
        "storage",
        "00c1e920",
        null,
        "pointer"
      ]
    ],
    [
      "00be00dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b333a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0080.md#insn-00be0080) · [`00be0084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0080.md#insn-00be0084) · [`00be0088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0080.md#insn-00be0088)

~~~diff
- 00be0080 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0080 bytes f00100d0
- 00be0084 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8d0:8"]]
- 00be0084 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0084 bytes 116a44f9
- 00be0088 ["COPY", "tmp:0:8", ["const:8d0:8"]]
- 00be0088 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0088 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0088 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0088 bytes 10422391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06924305f8c598499c65973e8ff0b9fb"></a>

### [`00be0090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0090.md) → [`00be00e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00e0.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00b2628c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b2628c.md) [`00b32104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32104.md) [`00b33278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33278.md) [`00b33c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33c1c.md) [`00b442c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b442c8.md) · 呼出先 1件 [`00b336c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b336c8.md)
- 新版 呼出元 5件 [`00b262d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b262d0.md) [`00b32148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b32/00b32148.md) [`00b332bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b332bc.md) [`00b33c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33c60.md) [`00b4430c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4430c.md) · 呼出先 1件 [`00b3370c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b3370c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0094",
      "READ",
      [
        "storage",
        "00c1e8d8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be009c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3370c"
      ]
    ]
  ],
  "added": [
    [
      "00be00e4",
      "READ",
      [
        "storage",
        "00c1e928",
        null,
        "pointer"
      ]
    ],
    [
      "00be00ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3370c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0090.md#insn-00be0090) · [`00be0094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0090.md#insn-00be0094) · [`00be0098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0090.md#insn-00be0098)

~~~diff
- 00be0090 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0090 bytes f00100d0
- 00be0094 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8d8:8"]]
- 00be0094 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0094 bytes 116e44f9
- 00be0098 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 00be0098 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0098 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0098 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0098 bytes 10622391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d584a53c23e8dc243d3983dfb6c3104"></a>

### [`00be00a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00a0.md) → [`00be00f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00f0.md) _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00b3c41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3c41c.md) [`00b3cdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cdac.md) [`00b3d208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d208.md) [`00b3d3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d3a4.md) · 呼出先 1件 [`00b3cb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cb60.md)
- 新版 呼出元 4件 [`00b3c460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3c/00b3c460.md) [`00b3cdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3c/00b3cdf0.md) [`00b3d24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3d24c.md) [`00b3d3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3d/00b3d3e8.md) · 呼出先 1件 [`00b3cba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3c/00b3cba4.md)

変更の種類 comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00be00f4",
      "READ",
      [
        "storage",
        "00c1e8e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00be00f4",
      "READ",
      [
        "storage",
        "00c1e930",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be00a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00a0.md#insn-00be00a4) · [`00be00a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00a0.md#insn-00be00a8)
- 新版 [`00be00f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00f0.md#insn-00be00f4) · [`00be00f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00f0.md#insn-00be00f8)

~~~diff
- 00be00a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8e0:8"]]
- 00be00a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
+ 00be00f4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:930:8"]]
+ 00be00f4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be00a4 bytes 117244f9
+ 00be00f4 bytes 119a44f9
- 00be00a8 ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 00be00a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be00a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be00a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be00a8 bytes 10822391
+ 00be00f8 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 00be00f8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
+ 00be00f8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
+ 00be00f8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
+ 00be00f8 bytes 10c22491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d6c6bc2493395808f6c963281506c53"></a>

### [`00be00b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00b0.md) → [`00be0100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0100.md) _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00b39dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39dcc.md) [`00b3a75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a75c.md) [`00b3abb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3abb8.md) [`00b3ad54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3ad54.md) · 呼出先 1件 [`00b3a510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a510.md)
- 新版 呼出元 4件 [`00b39e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b39/00b39e10.md) [`00b3a7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3a/00b3a7a0.md) [`00b3abfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3a/00b3abfc.md) [`00b3ad98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3a/00b3ad98.md) · 呼出先 1件 [`00b3a554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3a/00b3a554.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be00b4",
      "READ",
      [
        "storage",
        "00c1e8e8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be00bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3a554"
      ]
    ]
  ],
  "added": [
    [
      "00be0104",
      "READ",
      [
        "storage",
        "00c1e938",
        null,
        "pointer"
      ]
    ],
    [
      "00be010c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3a554"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be00b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00b0.md#insn-00be00b0) · [`00be00b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00b0.md#insn-00be00b4) · [`00be00b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00b0.md#insn-00be00b8)

~~~diff
- 00be00b0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be00b0 bytes f00100d0
- 00be00b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8e8:8"]]
- 00be00b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be00b4 bytes 117644f9
- 00be00b8 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 00be00b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be00b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be00b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be00b8 bytes 10a22391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74b4d5f0f1ef6c53ada1a3bfb857ccd0"></a>

### [`00be00c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00c0.md) → [`00be0110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0110.md) _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00b3b0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3b0f4.md) [`00b3ba84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3ba84.md) [`00b3bee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3bee0.md) [`00b3c07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3c07c.md) · 呼出先 1件 [`00b3b838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3b838.md)
- 新版 呼出元 4件 [`00b3b138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3b/00b3b138.md) [`00b3bac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3b/00b3bac8.md) [`00b3bf24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3b/00b3bf24.md) [`00b3c0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3c/00b3c0c0.md) · 呼出先 1件 [`00b3b87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3b/00b3b87c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be00c4",
      "READ",
      [
        "storage",
        "00c1e8f0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be00cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3b87c"
      ]
    ]
  ],
  "added": [
    [
      "00be0114",
      "READ",
      [
        "storage",
        "00c1e940",
        null,
        "pointer"
      ]
    ],
    [
      "00be011c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3b87c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be00c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00c0.md#insn-00be00c0) · [`00be00c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00c0.md#insn-00be00c4) · [`00be00c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00c0.md#insn-00be00c8)

~~~diff
- 00be00c0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be00c0 bytes f00100d0
- 00be00c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8f0:8"]]
- 00be00c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be00c4 bytes 117a44f9
- 00be00c8 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00be00c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be00c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be00c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be00c8 bytes 10c22391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-859d62bf04fc4748eaf5ad415a459237"></a>

### [`00be01b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01b0.md) → [`00be0200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0200.md) &lt;EXTERNAL&gt;::acos

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1e394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e394.md) · 呼出先 1件 [`010a5630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5630.md)
- 新版 呼出元 1件 [`00b1e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e3d8.md) · 呼出先 1件 [`010a5630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5630.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be01b4",
      "READ",
      [
        "storage",
        "00c1e968",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be01bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5630"
      ]
    ]
  ],
  "added": [
    [
      "00be0204",
      "READ",
      [
        "storage",
        "00c1e9b8",
        null,
        "pointer"
      ]
    ],
    [
      "00be020c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5630"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be01b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01b0.md#insn-00be01b0) · [`00be01b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01b0.md#insn-00be01b4) · [`00be01b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01b0.md#insn-00be01b8)

~~~diff
- 00be01b0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be01b0 bytes f00100d0
- 00be01b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:968:8"]]
- 00be01b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be01b4 bytes 11b644f9
- 00be01b8 ["COPY", "tmp:0:8", ["const:968:8"]]
- 00be01b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be01b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be01b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be01b8 bytes 10a22591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6b9bac2011a04e472e982bc4fad0ad5"></a>

### [`00be01c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01c0.md) → [`00be0210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0210.md) &lt;EXTERNAL&gt;::asin

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1e394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e394.md) · 呼出先 1件 [`010a5638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5638.md)
- 新版 呼出元 1件 [`00b1e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e3d8.md) · 呼出先 1件 [`010a5638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5638.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be01c4",
      "READ",
      [
        "storage",
        "00c1e970",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be01cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5638"
      ]
    ]
  ],
  "added": [
    [
      "00be0214",
      "READ",
      [
        "storage",
        "00c1e9c0",
        null,
        "pointer"
      ]
    ],
    [
      "00be021c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5638"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be01c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01c0.md#insn-00be01c0) · [`00be01c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01c0.md#insn-00be01c4) · [`00be01c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01c0.md#insn-00be01c8)

~~~diff
- 00be01c0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be01c0 bytes f00100d0
- 00be01c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:970:8"]]
- 00be01c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be01c4 bytes 11ba44f9
- 00be01c8 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00be01c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be01c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be01c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be01c8 bytes 10c22591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2931bda5a1cd16bf54a054b1ef8a447"></a>

### [`00be01e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01e0.md) → [`00be0230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0230.md) &lt;EXTERNAL&gt;::strncmp

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`00b2c7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c7c4.md) [`00b2c8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c8b8.md) [`00b2c95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c95c.md) [`00b33ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33ac4.md) [`00b33e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33e40.md) · 呼出先 1件 [`010a5648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5648.md)
- 新版 呼出元 9件 [`00b2c808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c808.md) [`00b2c8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c8fc.md) [`00b2c9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c9a0.md) [`00b33b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33b08.md) [`00b33e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33e84.md) · 呼出先 1件 [`010a5648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5648.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be01e4",
      "READ",
      [
        "storage",
        "00c1e980",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be01ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5648"
      ]
    ]
  ],
  "added": [
    [
      "00be0234",
      "READ",
      [
        "storage",
        "00c1e9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00be023c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5648"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be01e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01e0.md#insn-00be01e0) · [`00be01e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01e0.md#insn-00be01e4) · [`00be01e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01e0.md#insn-00be01e8)

~~~diff
- 00be01e0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be01e0 bytes f00100d0
- 00be01e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:980:8"]]
- 00be01e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be01e4 bytes 11c244f9
- 00be01e8 ["COPY", "tmp:0:8", ["const:980:8"]]
- 00be01e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be01e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be01e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be01e8 bytes 10022691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2498e1ed34f9daaea3636ad96a267e4b"></a>

### [`00be01f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01f0.md) → [`00be0240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0240.md) &lt;EXTERNAL&gt;::strpbrk

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b23f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b23f78.md) · 呼出先 1件 [`010a5650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5650.md)
- 新版 呼出元 1件 [`00b23fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b23fbc.md) · 呼出先 1件 [`010a5650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5650.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be01f4",
      "READ",
      [
        "storage",
        "00c1e988",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be01fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5650"
      ]
    ]
  ],
  "added": [
    [
      "00be0244",
      "READ",
      [
        "storage",
        "00c1e9d8",
        null,
        "pointer"
      ]
    ],
    [
      "00be024c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5650"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be01f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01f0.md#insn-00be01f0) · [`00be01f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01f0.md#insn-00be01f4) · [`00be01f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01f0.md#insn-00be01f8)

~~~diff
- 00be01f0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be01f0 bytes f00100d0
- 00be01f4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:988:8"]]
- 00be01f4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be01f4 bytes 11c644f9
- 00be01f8 ["COPY", "tmp:0:8", ["const:988:8"]]
- 00be01f8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be01f8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be01f8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be01f8 bytes 10222691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-350b791a20207abeccac7065606358f8"></a>

### [`00be0210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0210.md) → [`00be0260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0260.md) &lt;EXTERNAL&gt;::toupper

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b0e2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e2cc.md) [`00b0e538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e538.md) · 呼出先 1件 [`010a5660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5660.md)
- 新版 呼出元 2件 [`00b0e310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e310.md) [`00b0e57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e57c.md) · 呼出先 1件 [`010a5660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5660.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0214",
      "READ",
      [
        "storage",
        "00c1e998",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be021c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5660"
      ]
    ]
  ],
  "added": [
    [
      "00be0264",
      "READ",
      [
        "storage",
        "00c1e9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00be026c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5660"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0210.md#insn-00be0210) · [`00be0214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0210.md#insn-00be0214) · [`00be0218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0210.md#insn-00be0218)

~~~diff
- 00be0210 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0210 bytes f00100d0
- 00be0214 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:998:8"]]
- 00be0214 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0214 bytes 11ce44f9
- 00be0218 ["COPY", "tmp:0:8", ["const:998:8"]]
- 00be0218 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0218 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0218 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0218 bytes 10622691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ba5eb9d951ff101914c8e7f7d2978a0"></a>

### [`00be0220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0220.md) → [`00be0270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0270.md) _ZNKSt6__ndk16locale9has_facetERNS0_2idE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b4890c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b4890c.md) [`00b887d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b887d8.md) · 呼出先 1件 [`00ba86fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba86fc.md)
- 新版 呼出元 2件 [`00b48950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48950.md) [`00b8881c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b8881c.md) · 呼出先 1件 [`00ba8740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8740.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0224",
      "READ",
      [
        "storage",
        "00c1e9a0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be022c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00ba8740"
      ]
    ]
  ],
  "added": [
    [
      "00be0274",
      "READ",
      [
        "storage",
        "00c1e9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00be027c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00ba8740"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0220.md#insn-00be0220) · [`00be0224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0220.md#insn-00be0224) · [`00be0228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0220.md#insn-00be0228)

~~~diff
- 00be0220 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0220 bytes f00100d0
- 00be0224 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9a0:8"]]
- 00be0224 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0224 bytes 11d244f9
- 00be0228 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00be0228 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0228 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0228 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0228 bytes 10822691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

